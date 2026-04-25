"""
Unit tests for DSA Master — quiz fix, routes, code execution, progress tracking.
Run with: python test_app.py
"""
import unittest
import json
import os
import tempfile
from app import app, init_db
from modules_data import MODULES


class TestQuizTemplate(unittest.TestCase):
    """Verify the quiz HTML renders correct name/value attributes after the bug fix."""

    def setUp(self):
        app.config['TESTING'] = True
        app.config['SECRET_KEY'] = 'test-secret'
        self.client = app.test_client()

    def _quiz_html(self, module_id=1, level='beginner'):
        resp = self.client.get(f'/quiz/{module_id}?level={level}')
        return resp.data.decode()

    def _quiz(self, module_id=1, level='beginner'):
        module = next(m for m in MODULES if m['id'] == module_id)
        return module['levels'][level]['quiz']

    def test_each_question_has_unique_radio_group(self):
        """All 4 options within a question must share the same name (q0, q1, ...)."""
        html = self._quiz_html(1)
        quiz = self._quiz(1)
        for q_idx in range(len(quiz)):
            # Every option for question q_idx should have name="q{q_idx}"
            count = html.count(f'name="q{q_idx}"')
            self.assertEqual(
                count, len(quiz[q_idx]['options']),
                f"Question {q_idx}: expected {len(quiz[q_idx]['options'])} "
                f"radio inputs with name='q{q_idx}', found {count}"
            )

    def test_option_values_are_sequential_per_question(self):
        """Options within each question must have values 0, 1, 2, 3 (not mixed up)."""
        html = self._quiz_html(1)
        quiz = self._quiz(1)
        for q_idx in range(len(quiz)):
            for opt_idx in range(len(quiz[q_idx]['options'])):
                self.assertIn(
                    f'name="q{q_idx}" value="{opt_idx}"', html,
                    f"Missing: name='q{q_idx}' value='{opt_idx}'"
                )

    def test_selectOption_args_match_question_and_option_index(self):
        """onchange must call selectOption(q_idx, opt_idx) — not (opt_idx-1, opt_idx)."""
        html = self._quiz_html(1)
        quiz = self._quiz(1)
        for q_idx in range(len(quiz)):
            for opt_idx in range(len(quiz[q_idx]['options'])):
                expected = f'selectOption({q_idx}, {opt_idx})'
                self.assertIn(
                    expected, html,
                    f"Missing correct selectOption call: {expected}"
                )

    def test_option_a_is_selectable_not_minus_one(self):
        """The old bug: option A called selectOption(-1, 0). Must now be selectOption(q, 0)."""
        html = self._quiz_html(1)
        self.assertNotIn(
            'selectOption(-1,', html,
            "Bug still present: option A calls selectOption(-1, ...) making it unclickable"
        )

    def test_all_modules_quiz_pages_render(self):
        """Every module's quiz page must return HTTP 200."""
        for m in MODULES:
            resp = self.client.get(f'/quiz/{m["id"]}?level=beginner')
            self.assertEqual(resp.status_code, 200, f"Module {m['id']} quiz page failed")

    def test_level_tabs_present_in_quiz(self):
        """Quiz page must contain beginner/intermediate/advanced level tabs."""
        html = self._quiz_html(1)
        self.assertIn('Beginner', html)
        self.assertIn('Intermediate', html)
        self.assertIn('Advanced', html)

    def test_intermediate_quiz_renders(self):
        """Intermediate quiz page must return HTTP 200 for all modules."""
        for m in MODULES:
            resp = self.client.get(f'/quiz/{m["id"]}?level=intermediate')
            self.assertEqual(resp.status_code, 200,
                             f"Module {m['id']} intermediate quiz page failed")

    def test_advanced_quiz_renders(self):
        """Advanced quiz page must return HTTP 200 for all modules."""
        for m in MODULES:
            resp = self.client.get(f'/quiz/{m["id"]}?level=advanced')
            self.assertEqual(resp.status_code, 200,
                             f"Module {m['id']} advanced quiz page failed")


class TestQuizSubmission(unittest.TestCase):
    """Test the /submit_quiz endpoint scoring logic."""

    def setUp(self):
        app.config['TESTING'] = True
        app.config['SECRET_KEY'] = 'test-secret'
        self.client = app.test_client()

    def _submit(self, module_id, answers, level='beginner'):
        return self.client.post(
            '/submit_quiz',
            data=json.dumps({'module_id': module_id, 'level': level, 'answers': answers}),
            content_type='application/json'
        )

    def _quiz(self, module_id=1, level='beginner'):
        module = next(m for m in MODULES if m['id'] == module_id)
        return module['levels'][level]['quiz']

    def test_all_correct_gives_100(self):
        quiz = self._quiz(1)
        correct = {str(i): q['answer'] for i, q in enumerate(quiz)}
        resp = self._submit(1, correct)
        data = json.loads(resp.data)
        self.assertEqual(data['score'], 100)
        self.assertEqual(data['correct'], len(quiz))

    def test_all_wrong_gives_0(self):
        quiz = self._quiz(1)
        wrong = {str(i): (q['answer'] + 1) % 4 for i, q in enumerate(quiz)}
        resp = self._submit(1, wrong)
        data = json.loads(resp.data)
        self.assertEqual(data['score'], 0)
        self.assertEqual(data['correct'], 0)

    def test_partial_score_rounds_correctly(self):
        quiz = self._quiz(1)  # 5 questions
        # Answer only first 2 correctly
        answers = {str(i): q['answer'] if i < 2 else (q['answer'] + 1) % 4
                   for i, q in enumerate(quiz)}
        resp = self._submit(1, answers)
        data = json.loads(resp.data)
        self.assertEqual(data['correct'], 2)
        self.assertEqual(data['score'], 40)  # 2/5 = 40%

    def test_response_has_per_question_results(self):
        quiz = self._quiz(1)
        answers = {str(i): q['answer'] for i, q in enumerate(quiz)}
        resp = self._submit(1, answers)
        data = json.loads(resp.data)
        self.assertIn('results', data)
        self.assertEqual(len(data['results']), len(quiz))
        for r in data['results']:
            self.assertIn('correct', r)
            self.assertIn('explanation', r)
            self.assertIn('correct_answer', r)

    def test_correct_flag_per_question(self):
        quiz = self._quiz(1)
        # Answer all correctly
        answers = {str(i): q['answer'] for i, q in enumerate(quiz)}
        resp = self._submit(1, answers)
        data = json.loads(resp.data)
        self.assertTrue(all(r['correct'] for r in data['results']))

    def test_all_modules_scoreable(self):
        """Submit all-correct answers for every module at beginner level; each must score 100."""
        for module in MODULES:
            quiz = module['levels']['beginner']['quiz']
            correct = {str(i): q['answer'] for i, q in enumerate(quiz)}
            resp = self._submit(module['id'], correct, level='beginner')
            data = json.loads(resp.data)
            self.assertEqual(
                data['score'], 100,
                f"Module {module['id']} ({module['title']}) failed all-correct test"
            )

    def test_intermediate_quiz_scoreable(self):
        """Submit all-correct answers for every module at intermediate level."""
        for module in MODULES:
            quiz = module['levels']['intermediate']['quiz']
            correct = {str(i): q['answer'] for i, q in enumerate(quiz)}
            resp = self._submit(module['id'], correct, level='intermediate')
            data = json.loads(resp.data)
            self.assertEqual(
                data['score'], 100,
                f"Module {module['id']} intermediate quiz failed"
            )

    def test_advanced_quiz_scoreable(self):
        """Submit all-correct answers for every module at advanced level."""
        for module in MODULES:
            quiz = module['levels']['advanced']['quiz']
            correct = {str(i): q['answer'] for i, q in enumerate(quiz)}
            resp = self._submit(module['id'], correct, level='advanced')
            data = json.loads(resp.data)
            self.assertEqual(
                data['score'], 100,
                f"Module {module['id']} advanced quiz failed"
            )


class TestRoutes(unittest.TestCase):
    """Smoke-test all major routes."""

    def setUp(self):
        app.config['TESTING'] = True
        app.config['SECRET_KEY'] = 'test-secret'
        self.client = app.test_client()

    def test_dashboard(self):
        self.assertEqual(self.client.get('/').status_code, 200)

    def test_all_module_pages(self):
        for m in MODULES:
            resp = self.client.get(f'/module/{m["id"]}')
            self.assertEqual(resp.status_code, 200, f"Module {m['id']} page failed")

    def test_all_lab_pages(self):
        for m in MODULES:
            for lab in m['levels']['beginner']['labs']:
                resp = self.client.get(f'/lab/{m["id"]}/{lab["id"]}?level=beginner')
                self.assertEqual(
                    resp.status_code, 200,
                    f"Lab {m['id']}/{lab['id']} (beginner) page failed"
                )

    def test_all_intermediate_lab_pages(self):
        for m in MODULES:
            for lab in m['levels']['intermediate']['labs']:
                resp = self.client.get(f'/lab/{m["id"]}/{lab["id"]}?level=intermediate')
                self.assertEqual(
                    resp.status_code, 200,
                    f"Lab {m['id']}/{lab['id']} (intermediate) page failed"
                )

    def test_all_advanced_lab_pages(self):
        for m in MODULES:
            for lab in m['levels']['advanced']['labs']:
                resp = self.client.get(f'/lab/{m["id"]}/{lab["id"]}?level=advanced')
                self.assertEqual(
                    resp.status_code, 200,
                    f"Lab {m['id']}/{lab['id']} (advanced) page failed"
                )

    def test_invalid_module_returns_404(self):
        self.assertEqual(self.client.get('/module/999').status_code, 404)

    def test_invalid_lab_returns_404(self):
        self.assertEqual(self.client.get('/lab/1/999').status_code, 404)

    def test_progress_api(self):
        resp = self.client.get('/api/progress')
        self.assertEqual(resp.status_code, 200)
        data = json.loads(resp.data)
        self.assertIn('modules_visited', data)
        self.assertIn('labs_completed', data)
        self.assertIn('quiz_scores', data)

    def test_invalid_level_defaults_to_beginner(self):
        """An unknown ?level= value should silently fall back to beginner."""
        resp = self.client.get('/module/1?level=expert')
        self.assertEqual(resp.status_code, 200)
        html = resp.data.decode()
        # The active tab should be beginner
        self.assertIn('Beginner', html)

    def test_level_tabs_present_in_module(self):
        """Module page must contain level tabs for all 3 levels."""
        html = self.client.get('/module/1?level=beginner').data.decode()
        self.assertIn('Beginner', html)
        self.assertIn('Intermediate', html)
        self.assertIn('Advanced', html)

    def test_level_tabs_present_in_lab(self):
        """Lab page must contain level tabs for all 3 levels."""
        lab_id = MODULES[0]['levels']['beginner']['labs'][0]['id']
        html = self.client.get(f'/lab/1/{lab_id}?level=beginner').data.decode()
        self.assertIn('Beginner', html)
        self.assertIn('Intermediate', html)
        self.assertIn('Advanced', html)


class TestCodeExecution(unittest.TestCase):
    """Test the /run_free and /run_code endpoints."""

    def setUp(self):
        app.config['TESTING'] = True
        app.config['SECRET_KEY'] = 'test-secret'
        self.client = app.test_client()

    def _run_free(self, code):
        resp = self.client.post(
            '/run_free',
            data=json.dumps({'code': code}),
            content_type='application/json'
        )
        return json.loads(resp.data)

    def _run_code(self, code, test_code):
        resp = self.client.post(
            '/run_code',
            data=json.dumps({'code': code, 'test_code': test_code}),
            content_type='application/json'
        )
        return json.loads(resp.data)

    def test_simple_print(self):
        data = self._run_free("print('hello')")
        self.assertTrue(data['success'])
        self.assertEqual(data['stdout'].strip(), 'hello')

    def test_syntax_error_caught(self):
        data = self._run_free("def bad(: pass")
        self.assertFalse(data['success'])
        self.assertIn('SyntaxError', data['stderr'])

    def test_runtime_error_caught(self):
        data = self._run_free("x = 1/0")
        self.assertFalse(data['success'])
        self.assertIn('ZeroDivisionError', data['stderr'])

    def test_passing_tests_detected(self):
        code = "def add(a, b): return a + b"
        test = "assert add(2,3)==5\nprint('All tests passed!')"
        data = self._run_code(code, test)
        self.assertTrue(data['success'])
        self.assertIn('All tests passed', data['stdout'])

    def test_failing_assertion_detected(self):
        code = "def add(a, b): return 0"
        test = "assert add(2,3)==5, 'Wrong!'"
        data = self._run_code(code, test)
        self.assertFalse(data['success'])

    def test_empty_code_rejected(self):
        data = self._run_free("   ")
        self.assertFalse(data['success'])


class TestProgressTracking(unittest.TestCase):
    """Test SQLite-backed progress persistence."""

    def setUp(self):
        self.db_fd, self.db_path = tempfile.mkstemp(suffix='.db')
        os.close(self.db_fd)  # Release fd; SQLite manages the file itself
        app.config['TESTING'] = True
        app.config['SECRET_KEY'] = 'test-secret'
        app.config['DB_PATH'] = self.db_path
        app._db_ready = False
        self.client = app.test_client()

    def tearDown(self):
        import gc
        gc.collect()  # Release SQLite connections before deletion (needed on Windows)
        try:
            os.unlink(self.db_path)
        except (PermissionError, FileNotFoundError):
            pass

    def test_visiting_module_marks_it_visited(self):
        self.client.get('/module/1')
        resp = self.client.get('/api/progress')
        data = json.loads(resp.data)
        self.assertIn(1, data['modules_visited'])

    def test_completing_lab_persists(self):
        self.client.post(
            '/complete_lab',
            data=json.dumps({'module_id': 1, 'lab_id': 1, 'level': 'beginner'}),
            content_type='application/json'
        )
        resp = self.client.get('/api/progress')
        data = json.loads(resp.data)
        self.assertIn('1_beginner_1', data['labs_completed'])

    def test_completing_intermediate_lab_persists(self):
        self.client.post(
            '/complete_lab',
            data=json.dumps({'module_id': 1, 'lab_id': 1, 'level': 'intermediate'}),
            content_type='application/json'
        )
        resp = self.client.get('/api/progress')
        data = json.loads(resp.data)
        self.assertIn('1_intermediate_1', data['labs_completed'])

    def test_completing_advanced_lab_persists(self):
        self.client.post(
            '/complete_lab',
            data=json.dumps({'module_id': 1, 'lab_id': 1, 'level': 'advanced'}),
            content_type='application/json'
        )
        resp = self.client.get('/api/progress')
        data = json.loads(resp.data)
        self.assertIn('1_advanced_1', data['labs_completed'])

    def test_different_levels_tracked_separately(self):
        """Completing a lab at beginner and intermediate stores two separate keys."""
        self.client.post(
            '/complete_lab',
            data=json.dumps({'module_id': 1, 'lab_id': 1, 'level': 'beginner'}),
            content_type='application/json'
        )
        self.client.post(
            '/complete_lab',
            data=json.dumps({'module_id': 1, 'lab_id': 1, 'level': 'intermediate'}),
            content_type='application/json'
        )
        resp = self.client.get('/api/progress')
        data = json.loads(resp.data)
        self.assertIn('1_beginner_1', data['labs_completed'])
        self.assertIn('1_intermediate_1', data['labs_completed'])

    def test_quiz_score_persists(self):
        module = MODULES[0]
        quiz = module['levels']['beginner']['quiz']
        answers = {str(i): q['answer'] for i, q in enumerate(quiz)}
        self.client.post(
            '/submit_quiz',
            data=json.dumps({'module_id': 1, 'level': 'beginner', 'answers': answers}),
            content_type='application/json'
        )
        resp = self.client.get('/api/progress')
        data = json.loads(resp.data)
        self.assertEqual(data['quiz_scores']['1_beginner'], 100)

    def test_intermediate_quiz_score_persists(self):
        module = MODULES[0]
        quiz = module['levels']['intermediate']['quiz']
        answers = {str(i): q['answer'] for i, q in enumerate(quiz)}
        self.client.post(
            '/submit_quiz',
            data=json.dumps({'module_id': 1, 'level': 'intermediate', 'answers': answers}),
            content_type='application/json'
        )
        resp = self.client.get('/api/progress')
        data = json.loads(resp.data)
        self.assertEqual(data['quiz_scores']['1_intermediate'], 100)

    def test_quiz_scores_per_level_independent(self):
        """Beginner and intermediate quiz scores are stored under separate keys."""
        module = MODULES[0]
        bq = module['levels']['beginner']['quiz']
        iq = module['levels']['intermediate']['quiz']
        self.client.post('/submit_quiz',
            data=json.dumps({'module_id': 1, 'level': 'beginner',
                             'answers': {str(i): q['answer'] for i, q in enumerate(bq)}}),
            content_type='application/json')
        self.client.post('/submit_quiz',
            data=json.dumps({'module_id': 1, 'level': 'intermediate',
                             'answers': {str(i): (q['answer']+1)%4 for i, q in enumerate(iq)}}),
            content_type='application/json')
        resp = self.client.get('/api/progress')
        data = json.loads(resp.data)
        self.assertEqual(data['quiz_scores']['1_beginner'], 100)
        self.assertEqual(data['quiz_scores']['1_intermediate'], 0)

    def test_reset_clears_all_progress(self):
        # Build up some progress first
        self.client.get('/module/1')
        self.client.post(
            '/complete_lab',
            data=json.dumps({'module_id': 1, 'lab_id': 1, 'level': 'beginner'}),
            content_type='application/json'
        )
        # Reset
        self.client.post('/reset_progress')
        resp = self.client.get('/api/progress')
        data = json.loads(resp.data)
        self.assertEqual(data['modules_visited'], [])
        self.assertEqual(data['labs_completed'], {})
        self.assertEqual(data['quiz_scores'], {})

    def test_quiz_score_only_updates_if_higher(self):
        module = MODULES[0]
        quiz = module['levels']['beginner']['quiz']
        # Score 100 first
        all_correct = {str(i): q['answer'] for i, q in enumerate(quiz)}
        self.client.post('/submit_quiz',
            data=json.dumps({'module_id': 1, 'level': 'beginner', 'answers': all_correct}),
            content_type='application/json')
        # Score 0 next — should NOT overwrite 100
        all_wrong = {str(i): (q['answer']+1) % 4 for i, q in enumerate(quiz)}
        self.client.post('/submit_quiz',
            data=json.dumps({'module_id': 1, 'level': 'beginner', 'answers': all_wrong}),
            content_type='application/json')
        resp = self.client.get('/api/progress')
        data = json.loads(resp.data)
        self.assertEqual(data['quiz_scores']['1_beginner'], 100)


if __name__ == '__main__':
    loader = unittest.TestLoader()
    suites = [
        loader.loadTestsFromTestCase(TestQuizTemplate),
        loader.loadTestsFromTestCase(TestQuizSubmission),
        loader.loadTestsFromTestCase(TestRoutes),
        loader.loadTestsFromTestCase(TestCodeExecution),
        loader.loadTestsFromTestCase(TestProgressTracking),
    ]
    runner = unittest.TextTestRunner(verbosity=2)
    for suite in suites:
        runner.run(suite)
