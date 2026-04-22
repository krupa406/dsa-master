import sys
import subprocess
import json
from flask import Flask, render_template, request, jsonify, session
from modules_data import MODULES

app = Flask(__name__)
app.secret_key = 'dsa-platform-secret-2024'


@app.context_processor
def inject_nav():
    return {'modules_nav': MODULES, 'active_module': 0}


def get_progress():
    if 'progress' not in session:
        session['progress'] = {
            'modules_visited': [],
            'labs_completed': {},
            'quiz_scores': {},
        }
    return session['progress']


def save_progress(progress):
    session['progress'] = progress
    session.modified = True


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


@app.route('/')
def index():
    progress = get_progress()
    modules_with_status = []
    for m in MODULES:
        mid = str(m['id'])
        labs_done = sum(
            1 for lab in m['labs']
            if f"{mid}_{lab['id']}" in progress['labs_completed']
        )
        quiz_score = progress['quiz_scores'].get(mid)
        modules_with_status.append({
            **m,
            'visited': m['id'] in progress['modules_visited'],
            'labs_done': labs_done,
            'total_labs': len(m['labs']),
            'quiz_score': quiz_score,
            'content': None,  # Don't send full content to index
        })
    total_labs = sum(len(m['labs']) for m in MODULES)
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
    progress = get_progress()
    if module_id not in progress['modules_visited']:
        progress['modules_visited'].append(module_id)
        save_progress(progress)
    mid = str(module_id)
    labs_status = {
        lab['id']: f"{mid}_{lab['id']}" in progress['labs_completed']
        for lab in m['labs']
    }
    quiz_score = progress['quiz_scores'].get(mid)
    prev_module = get_module(module_id - 1)
    next_module = get_module(module_id + 1)
    return render_template(
        'module.html',
        module=m,
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
    lab = next((l for l in m['labs'] if l['id'] == lab_id), None)
    if not lab:
        return 'Lab not found', 404
    progress = get_progress()
    lab_key = f"{module_id}_{lab_id}"
    is_completed = lab_key in progress['labs_completed']
    lab_idx = next(i for i, l in enumerate(m['labs']) if l['id'] == lab_id)
    prev_lab = m['labs'][lab_idx - 1] if lab_idx > 0 else None
    next_lab = m['labs'][lab_idx + 1] if lab_idx < len(m['labs']) - 1 else None
    return render_template(
        'lab.html',
        module=m,
        lab=lab,
        lab_number=lab_idx + 1,
        total_labs=len(m['labs']),
        is_completed=is_completed,
        prev_lab=prev_lab,
        next_lab=next_lab,
    )


@app.route('/quiz/<int:module_id>')
def quiz_page(module_id):
    m = get_module(module_id)
    if not m:
        return 'Module not found', 404
    progress = get_progress()
    quiz_score = progress['quiz_scores'].get(str(module_id))
    prev_module = get_module(module_id - 1)
    next_module = get_module(module_id + 1)
    return render_template(
        'quiz.html',
        module=m,
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
    if not module_id or not lab_id:
        return jsonify({'error': 'Missing module_id or lab_id'}), 400
    progress = get_progress()
    lab_key = f"{module_id}_{lab_id}"
    progress['labs_completed'][lab_key] = True
    save_progress(progress)
    return jsonify({'success': True})


@app.route('/submit_quiz', methods=['POST'])
def submit_quiz():
    data = request.get_json()
    module_id = data.get('module_id')
    answers = data.get('answers', {})
    m = get_module(int(module_id))
    if not m:
        return jsonify({'error': 'Module not found'}), 404
    quiz = m['quiz']
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
    progress = get_progress()
    mid = str(module_id)
    if mid not in progress['quiz_scores'] or score > progress['quiz_scores'][mid]:
        progress['quiz_scores'][mid] = score
        save_progress(progress)
    return jsonify({
        'score': score,
        'correct': correct,
        'total': len(quiz),
        'results': results,
    })


@app.route('/reset_progress', methods=['POST'])
def reset_progress():
    session['progress'] = {
        'modules_visited': [],
        'labs_completed': {},
        'quiz_scores': {},
    }
    session.modified = True
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
