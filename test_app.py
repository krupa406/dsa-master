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

    def _quiz_html(self, module_id=1):
        resp = self.client.get(f'/quiz/{module_id}')
        return resp.data.decode()

    def test_each_question_has_unique_radio_group(self):
        """All 4 options within a question must share the same name (q0, q1, ...)."""
        html = self._quiz_html(1)
        module = next(m for m in MODULES if m['id'] == 1)
        for q_idx in range(len(module['quiz'])):
            # Every option for question q_idx should have name="q{q_idx}"
            count = html.count(f'name="q{q_idx}"')
            self.assertEqual(
                count, len(module['quiz'][q_idx]['options']),
                f"Question {q_idx}: expected {len(module['quiz'][q_idx]['options'])} "
                f"radio inputs with name='q{q_idx}', found {count}"
            )

    def test_option_values_are_sequential_per_question(self):
        """Options within each question must have values 0, 1, 2, 3 (not mixed up)."""
        html = self._quiz_html(1)
        module = next(m for m in MODULES if m['id'] == 1)
        for q_idx in range(len(module['quiz'])):
            for opt_idx in range(len(module['quiz'][q_idx]['options'])):
                self.assertIn(
                    f'name="q{q_idx}" value="{opt_idx}"', html,
                    f"Missing: name='q{q_idx}' value='{opt_idx}'"
                )

    def test_selectOption_args_match_question_and_option_index(self):
        """onchange must call selectOption(q_idx, opt_idx) — not (opt_idx-1, opt_idx)."""
        html = self._quiz_html(1)
        module = next(m for m in MODULES if m['id'] == 1)
        for q_idx in range(len(module['quiz'])):
            for opt_idx in range(len(module['quiz'][q_idx]['options'])):
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
            resp = self.client.get(f'/quiz/{m["id"]}')
            self.assertEqual(resp.status_code, 200, f"Module {m['id']} quiz page failed")


class TestQuizSubmission(unittest.TestCase):
    """Test the /submit_quiz endpoint scoring logic."""

    def setUp(self):
        app.config['TESTING'] = True
        app.config['SECRET_KEY'] = 'test-secret'
        self.client = app.test_client()

    def _submit(self, module_id, answers):
        return self.client.post(
            '/submit_quiz',
            data=json.dumps({'module_id': module_id, 'answers': answers}),
            content_type='application/json'
        )

    def test_all_correct_gives_100(self):
        module = MODULES[0]
        correct = {str(i): q['answer'] for i, q in enumerate(module['quiz'])}
        resp = self._submit(module['id'], correct)
        data = json.loads(resp.data)
        self.assertEqual(data['score'], 100)
        self.assertEqual(data['correct'], len(module['quiz']))

    def test_all_wrong_gives_0(self):
        module = MODULES[0]
        wrong = {str(i): (q['answer'] + 1) % 4 for i, q in enumerate(module['quiz'])}
        resp = self._submit(module['id'], wrong)
        data = json.loads(resp.data)
        self.assertEqual(data['score'], 0)
        self.assertEqual(data['correct'], 0)

    def test_partial_score_rounds_correctly(self):
        module = MODULES[0]  # 5 questions
        # Answer only first 2 correctly
        answers = {str(i): q['answer'] if i < 2 else (q['answer'] + 1) % 4
                   for i, q in enumerate(module['quiz'])}
        resp = self._submit(module['id'], answers)
        data = json.loads(resp.data)
        self.assertEqual(data['correct'], 2)
        self.assertEqual(data['score'], 40)  # 2/5 = 40%

    def test_response_has_per_question_results(self):
        module = MODULES[0]
        answers = {str(i): q['answer'] for i, q in enumerate(module['quiz'])}
        resp = self._submit(module['id'], answers)
        data = json.loads(resp.data)
        self.assertIn('results', data)
        self.assertEqual(len(data['results']), len(module['quiz']))
        for r in data['results']:
            self.assertIn('correct', r)
            self.assertIn('explanation', r)
            self.assertIn('correct_answer', r)

    def test_correct_flag_per_question(self):
        module = MODULES[0]
        # Answer all correctly
        answers = {str(i): q['answer'] for i, q in enumerate(module['quiz'])}
        resp = self._submit(module['id'], answers)
        data = json.loads(resp.data)
        self.assertTrue(all(r['correct'] for r in data['results']))

    def test_all_modules_scoreable(self):
        """Submit all-correct answers for every module; each must score 100."""
        for module in MODULES:
            correct = {str(i): q['answer'] for i, q in enumerate(module['quiz'])}
            resp = self._submit(module['id'], correct)
            data = json.loads(resp.data)
            self.assertEqual(
                data['score'], 100,
                f"Module {module['id']} ({module['title']}) failed all-correct test"
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
            for lab in m['labs']:
                resp = self.client.get(f'/lab/{m["id"]}/{lab["id"]}')
                self.assertEqual(
                    resp.status_code, 200,
                    f"Lab {m['id']}/{lab['id']} page failed"
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
            data=json.dumps({'module_id': 1, 'lab_id': 1}),
            content_type='application/json'
        )
        resp = self.client.get('/api/progress')
        data = json.loads(resp.data)
        self.assertIn('1_1', data['labs_completed'])

    def test_quiz_score_persists(self):
        module = MODULES[0]
        answers = {str(i): q['answer'] for i, q in enumerate(module['quiz'])}
        self.client.post(
            '/submit_quiz',
            data=json.dumps({'module_id': 1, 'answers': answers}),
            content_type='application/json'
        )
        resp = self.client.get('/api/progress')
        data = json.loads(resp.data)
        self.assertEqual(data['quiz_scores']['1'], 100)

    def test_reset_clears_all_progress(self):
        # Build up some progress first
        self.client.get('/module/1')
        self.client.post(
            '/complete_lab',
            data=json.dumps({'module_id': 1, 'lab_id': 1}),
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
        # Score 100 first
        all_correct = {str(i): q['answer'] for i, q in enumerate(module['quiz'])}
        self.client.post('/submit_quiz',
            data=json.dumps({'module_id': 1, 'answers': all_correct}),
            content_type='application/json')
        # Score 0 next — should NOT overwrite 100
        all_wrong = {str(i): (q['answer']+1) % 4 for i, q in enumerate(module['quiz'])}
        self.client.post('/submit_quiz',
            data=json.dumps({'module_id': 1, 'answers': all_wrong}),
            content_type='application/json')
        resp = self.client.get('/api/progress')
        data = json.loads(resp.data)
        self.assertEqual(data['quiz_scores']['1'], 100)


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
