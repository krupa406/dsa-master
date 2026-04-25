import sys
import subprocess
import json
import sqlite3
import uuid
from datetime import timedelta
from flask import Flask, render_template, request, jsonify, session, current_app
from modules_data import MODULES

app = Flask(__name__)
app.secret_key = 'dsa-platform-secret-2024'
app.config['SESSION_PERMANENT'] = True
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=365)
app.config['DB_PATH'] = 'progress.db'


@app.context_processor
def inject_nav():
    return {'modules_nav': MODULES, 'active_module': 0}


def get_db_path():
    return current_app.config.get('DB_PATH', 'progress.db')


def init_db():
    with sqlite3.connect(get_db_path()) as conn:
        conn.executescript('''
            CREATE TABLE IF NOT EXISTS modules_visited (
                user_id TEXT NOT NULL,
                module_id INTEGER NOT NULL,
                PRIMARY KEY (user_id, module_id)
            );
            CREATE TABLE IF NOT EXISTS labs_completed (
                user_id TEXT NOT NULL,
                lab_key TEXT NOT NULL,
                PRIMARY KEY (user_id, lab_key)
            );
            CREATE TABLE IF NOT EXISTS quiz_scores (
                user_id TEXT NOT NULL,
                module_id TEXT NOT NULL,
                score INTEGER NOT NULL,
                PRIMARY KEY (user_id, module_id)
            );
        ''')


@app.before_request
def ensure_db():
    if not getattr(app, '_db_ready', False):
        init_db()
        app._db_ready = True


def get_user_id():
    if 'user_id' not in session:
        session['user_id'] = str(uuid.uuid4())
    return session['user_id']


def get_progress():
    user_id = get_user_id()
    db = get_db_path()
    with sqlite3.connect(db) as conn:
        visited = [row[0] for row in conn.execute(
            'SELECT module_id FROM modules_visited WHERE user_id = ?', (user_id,)
        )]
        labs = {row[0]: True for row in conn.execute(
            'SELECT lab_key FROM labs_completed WHERE user_id = ?', (user_id,)
        )}
        scores = {row[0]: row[1] for row in conn.execute(
            'SELECT module_id, score FROM quiz_scores WHERE user_id = ?', (user_id,)
        )}
    return {
        'modules_visited': visited,
        'labs_completed': labs,
        'quiz_scores': scores,
    }


def execute_code(code, timeout=10):
    try:
        result = subprocess.run(
            [sys.executable, '-c', code],
            capture_output=True,
            text=True,
            timeout=timeout
        )
        return {
            'stdout': result.stdout,
            'stderr': result.stderr,
            'success': result.returncode == 0,
        }
    except subprocess.TimeoutExpired:
        return {
            'stdout': '',
            'stderr': f'Error: Code timed out after {timeout} seconds. Check for infinite loops.',
            'success': False,
        }
    except Exception as e:
        return {
            'stdout': '',
            'stderr': str(e),
            'success': False,
        }


def get_module(module_id):
    for m in MODULES:
        if m['id'] == module_id:
            return m
    return None


VALID_LEVELS = ('beginner', 'intermediate', 'advanced')


def get_level():
    """Read ?level= query param, defaulting to 'beginner'."""
    level = request.args.get('level', 'beginner').lower()
    return level if level in VALID_LEVELS else 'beginner'


@app.route('/')
def index():
    progress = get_progress()
    modules_with_status = []
    for m in MODULES:
        mid = str(m['id'])
        # Count completed labs across ALL levels for the dashboard summary
        labs_done = sum(
            1 for key in progress['labs_completed']
            if key.startswith(f"{mid}_")
        )
        # Best quiz score across all levels
        best_score = None
        for lvl in VALID_LEVELS:
            s = progress['quiz_scores'].get(f"{mid}_{lvl}")
            if s is not None:
                best_score = max(best_score, s) if best_score is not None else s
        total_labs = sum(len(m['levels'][lvl]['labs']) for lvl in VALID_LEVELS)
        modules_with_status.append({
            **m,
            'visited': m['id'] in progress['modules_visited'],
            'labs_done': labs_done,
            'total_labs': total_labs,
            'quiz_score': best_score,
            'content': None,
        })
    total_labs = sum(
        len(m['levels'][lvl]['labs'])
        for m in MODULES for lvl in VALID_LEVELS
    )
    completed_labs = len(progress['labs_completed'])
    completed_quizzes = len(progress['quiz_scores'])
    return render_template(
        'index.html',
        modules=modules_with_status,
        total_labs=total_labs,
        completed_labs=completed_labs,
        completed_quizzes=completed_quizzes,
        total_modules=len(MODULES),
    )


@app.route('/module/<int:module_id>')
def module_page(module_id):
    m = get_module(module_id)
    if not m:
        return 'Module not found', 404
    level = get_level()
    progress = get_progress()
    if module_id not in progress['modules_visited']:
        user_id = get_user_id()
        with sqlite3.connect(get_db_path()) as conn:
            conn.execute(
                'INSERT OR IGNORE INTO modules_visited (user_id, module_id) VALUES (?, ?)',
                (user_id, module_id)
            )
    mid = str(module_id)
    level_data = m['levels'][level]
    labs_status = {
        lab['id']: f"{mid}_{level}_{lab['id']}" in progress['labs_completed']
        for lab in level_data['labs']
    }
    quiz_score = progress['quiz_scores'].get(f"{mid}_{level}")
    prev_module = get_module(module_id - 1)
    next_module = get_module(module_id + 1)
    return render_template(
        'module.html',
        module=m,
        level=level,
        level_data=level_data,
        labs_status=labs_status,
        quiz_score=quiz_score,
        prev_module=prev_module,
        next_module=next_module,
    )


@app.route('/lab/<int:module_id>/<int:lab_id>')
def lab_page(module_id, lab_id):
    m = get_module(module_id)
    if not m:
        return 'Module not found', 404
    level = get_level()
    level_data = m['levels'][level]
    lab = next((l for l in level_data['labs'] if l['id'] == lab_id), None)
    if not lab:
        return 'Lab not found', 404
    progress = get_progress()
    lab_key = f"{module_id}_{level}_{lab_id}"
    is_completed = lab_key in progress['labs_completed']
    lab_idx = next(i for i, l in enumerate(level_data['labs']) if l['id'] == lab_id)
    prev_lab = level_data['labs'][lab_idx - 1] if lab_idx > 0 else None
    next_lab = level_data['labs'][lab_idx + 1] if lab_idx < len(level_data['labs']) - 1 else None
    return render_template(
        'lab.html',
        module=m,
        lab=lab,
        level=level,
        lab_number=lab_idx + 1,
        total_labs=len(level_data['labs']),
        is_completed=is_completed,
        prev_lab=prev_lab,
        next_lab=next_lab,
    )


@app.route('/quiz/<int:module_id>')
def quiz_page(module_id):
    m = get_module(module_id)
    if not m:
        return 'Module not found', 404
    level = get_level()
    level_data = m['levels'][level]
    progress = get_progress()
    quiz_score = progress['quiz_scores'].get(f"{module_id}_{level}")
    prev_module = get_module(module_id - 1)
    next_module = get_module(module_id + 1)
    return render_template(
        'quiz.html',
        module=m,
        level=level,
        level_data=level_data,
        quiz_score=quiz_score,
        prev_module=prev_module,
        next_module=next_module,
    )


@app.route('/run_code', methods=['POST'])
def run_code():
    data = request.get_json()
    code = data.get('code', '')
    test_code = data.get('test_code', '')
    if not code.strip():
        return jsonify({'stdout': '', 'stderr': 'No code provided.', 'success': False})
    full_code = code
    if test_code:
        full_code += '\n' + test_code
    result = execute_code(full_code)
    return jsonify(result)


@app.route('/run_free', methods=['POST'])
def run_free():
    data = request.get_json()
    code = data.get('code', '')
    if not code.strip():
        return jsonify({'stdout': '', 'stderr': 'No code provided.', 'success': False})
    result = execute_code(code)
    return jsonify(result)


@app.route('/complete_lab', methods=['POST'])
def complete_lab():
    data = request.get_json()
    module_id = data.get('module_id')
    lab_id = data.get('lab_id')
    level = data.get('level', 'beginner')
    if level not in VALID_LEVELS:
        level = 'beginner'
    if not module_id or not lab_id:
        return jsonify({'error': 'Missing module_id or lab_id'}), 400
    user_id = get_user_id()
    lab_key = f"{module_id}_{level}_{lab_id}"
    with sqlite3.connect(get_db_path()) as conn:
        conn.execute(
            'INSERT OR IGNORE INTO labs_completed (user_id, lab_key) VALUES (?, ?)',
            (user_id, lab_key)
        )
    return jsonify({'success': True})


@app.route('/submit_quiz', methods=['POST'])
def submit_quiz():
    data = request.get_json()
    module_id = data.get('module_id')
    level = data.get('level', 'beginner')
    if level not in VALID_LEVELS:
        level = 'beginner'
    answers = data.get('answers', {})
    m = get_module(int(module_id))
    if not m:
        return jsonify({'error': 'Module not found'}), 404
    quiz = m['levels'][level]['quiz']
    correct = 0
    results = []
    for i, question in enumerate(quiz):
        user_answer = answers.get(str(i))
        is_correct = user_answer == question['answer']
        if is_correct:
            correct += 1
        results.append({
            'correct': is_correct,
            'correct_answer': question['answer'],
            'explanation': question['explanation'],
        })
    score = round((correct / len(quiz)) * 100)
    user_id = get_user_id()
    score_key = f"{module_id}_{level}"
    with sqlite3.connect(get_db_path()) as conn:
        conn.execute(
            'INSERT INTO quiz_scores (user_id, module_id, score) VALUES (?, ?, ?) '
            'ON CONFLICT(user_id, module_id) DO UPDATE SET score = excluded.score '
            'WHERE excluded.score > quiz_scores.score',
            (user_id, score_key, score)
        )
    return jsonify({
        'score': score,
        'correct': correct,
        'total': len(quiz),
        'results': results,
    })


@app.route('/reset_progress', methods=['POST'])
def reset_progress():
    user_id = get_user_id()
    with sqlite3.connect(get_db_path()) as conn:
        conn.execute('DELETE FROM modules_visited WHERE user_id = ?', (user_id,))
        conn.execute('DELETE FROM labs_completed WHERE user_id = ?', (user_id,))
        conn.execute('DELETE FROM quiz_scores WHERE user_id = ?', (user_id,))
    return jsonify({'success': True})


@app.route('/api/progress')
def api_progress():
    return jsonify(get_progress())


if __name__ == '__main__':
    print("\n" + "="*60)
    print("  DSA Learning Platform")
    print("  Open your browser at: http://127.0.0.1:5000")
    print("="*60 + "\n")
    app.run(debug=True, port=5000)
