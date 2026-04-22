# DSA Master — Interactive Python Learning Platform

An interactive, browser-based learning platform for mastering **Data Structures & Algorithms in Python** — built for complete beginners. No sign-up, no cloud, runs entirely on your local machine.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-3.0%2B-black?logo=flask)
![License](https://img.shields.io/badge/license-MIT-green)

---

## Features

- **8 complete modules** covering the core DSA curriculum
- **Theory pages** with syntax-highlighted code, visual diagrams, and Big-O complexity tables
- **Interactive labs** — write Python in-browser, run it against hidden test cases, get instant pass/fail feedback
- **Quizzes** — 5-question multiple-choice per module with per-question explanations and a score summary
- **Python Sandbox** on every theory page to freely experiment
- **Progress tracking** — lab completions and quiz scores persist across page reloads (session-based)
- **Collapsible hints** for every lab challenge
- `Ctrl+Enter` keyboard shortcut to run code in any editor
- Fully responsive layout

---

## Modules

| # | Module | Topics |
|---|--------|--------|
| 1 | 📋 Arrays & Lists | Indexing, slicing, common operations, list comprehensions, Big-O |
| 2 | 🔤 Strings | Immutability, methods, f-strings, frequency counting, anagrams |
| 3 | 🔗 Linked Lists | Nodes, singly linked list, append, prepend, search, length |
| 4 | 📚 Stacks & Queues | LIFO/FIFO, bracket matching, deque, real-world use cases |
| 5 | 🌳 Binary Trees | BST insert/search, inorder traversal, height, node count |
| 6 | 🔍 Searching | Linear search O(n), Binary search O(log n), step-by-step traces |
| 7 | 🔢 Sorting | Bubble sort, Insertion sort, complexity comparison table |
| 8 | 🗂️ Hash Tables | Python dicts, Two Sum, first unique character, memoization |

Each module includes:
- **2 coding labs** with auto-graded test cases
- **5-question quiz** with explanations
- **Python sandbox** for free experimentation

---

## Quick Start

### Prerequisites

- Python 3.8 or higher
- pip

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/dsa-master.git
cd dsa-master

# 2. (Recommended) Create a virtual environment
python -m venv venv

# On Windows:
venv\Scripts\activate

# On macOS / Linux:
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
python app.py
```

Then open your browser at **http://127.0.0.1:5000**

---

## Project Structure

```
dsa-master/
├── app.py              # Flask application — routes, code execution, progress API
├── modules_data.py     # All course content (theory HTML, labs, quizzes)
├── requirements.txt    # Python dependencies (just Flask)
│
├── templates/
│   ├── base.html       # Shared layout — top nav, fonts
│   ├── index.html      # Dashboard — module grid, global progress stats
│   ├── module.html     # Theory page — content, sandbox, lab summary
│   ├── lab.html        # Code lab — editor, test runner, hints
│   └── quiz.html       # Quiz — questions, submission, results breakdown
│
└── static/
    ├── css/style.css   # All styles — layout, cards, editor, quiz UI
    └── js/main.js      # Client utilities — syntax highlight, nav state
```

---

## How It Works

### Code Execution

Student code is sent to `/run_code` (with hidden test cases appended) or `/run_free` (sandbox), then executed via Python's `subprocess` module using the same interpreter that runs the Flask server. Execution is sandboxed with a **10-second timeout** to prevent infinite loops.

```
Browser editor → POST /run_code → subprocess.run(python -c "...") → stdout/stderr → Browser output panel
```

### Progress Tracking

Progress is stored in Flask's server-side session (cookie-backed). No database required. Tracked data:

```json
{
  "modules_visited": [1, 2, 3],
  "labs_completed": { "1_1": true, "1_2": true },
  "quiz_scores":    { "1": 100, "2": 80 }
}
```

### Adding Content

To add a new module, append an entry to the `MODULES` list in `modules_data.py`:

```python
{
    'id': 9,
    'title': 'Graphs',
    'icon': '🕸️',
    'description': '...',
    'difficulty': 'Intermediate',
    'estimated_time': '60 min',
    'color': '#0284c7',
    'content': """<h2>...</h2>""",
    'labs': [
        {
            'id': 1,
            'title': 'Lab title',
            'description': 'Instructions...',
            'starter_code': 'def my_func(): pass',
            'test_code': 'assert my_func() == ...',
            'hints': ['Hint 1', 'Hint 2'],
        }
    ],
    'quiz': [
        {
            'question': 'Question text?',
            'options': ['A', 'B', 'C', 'D'],
            'answer': 0,          # index of correct option
            'explanation': '...',
        }
    ]
}
```

No other changes needed — the app picks up new modules automatically.

---

## API Endpoints

| Method | Route | Description |
|--------|-------|-------------|
| GET | `/` | Dashboard |
| GET | `/module/<id>` | Module theory page |
| GET | `/lab/<module_id>/<lab_id>` | Lab page |
| GET | `/quiz/<module_id>` | Quiz page |
| POST | `/run_code` | Execute student code + test cases |
| POST | `/run_free` | Execute free-form sandbox code |
| POST | `/complete_lab` | Mark a lab as completed |
| POST | `/submit_quiz` | Grade a quiz submission |
| POST | `/reset_progress` | Clear all session progress |
| GET | `/api/progress` | Get current progress (JSON) |

---

## Security Notes

This app is designed for **local use only**. Code execution via `subprocess` is intentionally unrestricted — it runs with the same permissions as your Python process. Do **not** deploy this to a public server without adding sandboxing (e.g., Docker, seccomp, or a dedicated code execution service).

---

## License

MIT — free to use, modify, and share.
