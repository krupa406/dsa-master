# DevLearn — Interactive DevOps Learning Platform

An interactive, self-hosted web application for learning **Ansible**, **Terraform**, and **Kubernetes** through structured modules, hands-on in-browser labs, and auto-graded quizzes with official-documentation citations.

---

## Overview

| Technology | Version (N-1) | Levels | Modules | Labs | Quiz Questions |
|------------|--------------|--------|---------|------|----------------|
| Ansible    | ansible-core 2.19 | Beginner · Intermediate · Expert | 9 | 9 | 90 |
| Terraform  | 1.13 | Beginner · Intermediate · Expert | 9 | 9 | 90 |
| Kubernetes | 1.35 ("Timbernetes") | Beginner · Intermediate · Expert | 9 | 9 | 90 |

**27 modules · 27 interactive labs · 270 quiz questions** — all content targets the current N-1 release of each tool.

---

## Features

### Learning Experience
- **Structured curriculum** — 3 technologies × 3 difficulty levels × 3 modules per level
- **Theory panels** — rich HTML content with typography optimised for reading
- **Architecture diagrams** — every module includes a Mermaid.js flowchart or sequence diagram illustrating the key concept (based on Mayer's Multimedia Learning / dual-coding theory)
- **Syntax-highlighted code** — all code examples rendered with highlight.js (GitHub Dark theme)
- **Copy buttons** — one-click copy on every code block
- **Sticky outline sidebar** — auto-generated table of contents with IntersectionObserver active-heading tracking
- **Collapsible learning objectives** — visible on demand without cluttering the reading view
- **In-browser code labs** — Monaco Editor (VS Code engine) with language-specific starter code, hints, and simulated output
- **Auto-graded quizzes** — per-question feedback: correct/wrong highlighted instantly, animated explanation, and clickable official-docs citation links
- **Progress tracking** — localStorage persistence; level unlock gates (complete all modules to unlock the quiz)

### Technical Highlights
- **Agentless quiz grading** — `correctOptionId` is never sent to the client; answers are verified server-side
- **Per-question answer endpoint** — `/quiz/answer` returns `correct`, `correctOption`, `explanation`, and `citations` immediately after each answer, enabling real-time feedback without revealing answers upfront
- **Tech-specific accent colours** — Ansible red, Terraform purple, Kubernetes blue throughout the UI
- **Animated transitions** — `animate-fadeIn` / `animate-slideUp` on question cards and explanations
- **Version-specific content** — each introductory module covers new features and deprecations in the exact N-1 release

---

## Tech Stack

### Frontend (`client/`)
| Library | Version | Purpose |
|---------|---------|---------|
| React | 18 | UI framework |
| Vite | 5 | Dev server + bundler |
| Tailwind CSS | 3 | Utility-first styling |
| React Router | v6 | Client-side routing |
| @monaco-editor/react | latest | In-browser code editor |
| Mermaid.js | 11 | Architecture diagrams |
| highlight.js | 11 | Syntax highlighting |
| lucide-react | latest | Icons |

### Backend (`server/`)
| Library | Version | Purpose |
|---------|---------|---------|
| Express | 4 | REST API server |
| cors | latest | Cross-origin for Vite dev proxy |
| js-yaml | latest | YAML lab validation |
| nodemon | latest | Dev hot-reload |

---

## Project Structure

```
.
├── package.json              # Monorepo root — concurrently scripts
├── client/                   # React + Vite frontend
│   ├── src/
│   │   ├── App.jsx
│   │   ├── main.jsx
│   │   ├── index.css         # Tailwind + highlight.js + custom component classes
│   │   ├── routes/           # Page-level components
│   │   │   ├── HomePage.jsx
│   │   │   ├── TechnologyPage.jsx
│   │   │   ├── LevelPage.jsx
│   │   │   ├── ModulePage.jsx
│   │   │   └── QuizPage.jsx
│   │   ├── components/
│   │   │   ├── layout/       # AppShell, Navbar
│   │   │   ├── module/       # TheoryPanel, LabPanel, CodeEditor, ModuleOutline
│   │   │   ├── quiz/         # QuizContainer, QuestionCard, QuizProgress, QuizIntro, QuizResults
│   │   │   └── shared/       # Badge, ProgressRing, LoadingSpinner, ErrorMessage
│   │   ├── context/          # ProgressContext (React context + localStorage)
│   │   ├── hooks/            # useApi, useProgress
│   │   ├── services/         # api.js (fetch helpers)
│   │   └── utils/            # progressStorage.js
│   └── vite.config.js        # /api proxy → localhost:3001
│
└── server/                   # Express REST API
    └── src/
        ├── index.js           # Starts server on port 3001
        ├── app.js             # Mounts routers + CORS
        ├── routes/            # technologies, levels, modules, labs, quizzes
        ├── services/
        │   ├── contentService.js    # JSON file loading, strips correctOptionId/solutionCode
        │   └── labValidatorService.js # contains/regex/yamlParse validation rules
        ├── middleware/        # errorHandler, requestLogger
        └── data/              # All course content as JSON
            ├── ansible/
            │   ├── meta.json
            │   ├── beginner/  intermediate/  expert/
            │   │   ├── level-meta.json
            │   │   └── module-0N-*/
            │   │       ├── module.json   # theory HTML + learning objectives
            │   │       ├── lab.json      # starter/solution code, validation rules
            │   │       └── quiz.json     # 10 questions with citations
            ├── terraform/     # same structure
            └── kubernetes/    # same structure
```

---

## Getting Started

### Prerequisites
- **Node.js** ≥ 20
- **npm** ≥ 9

### 1. Clone the repository

```bash
git clone https://github.com/krupa406/Course-Terraform-Ansible-Kubernetes.git
cd Course-Terraform-Ansible-Kubernetes
```

### 2. Install all dependencies (one command)

```bash
npm run install:all
```

This installs the monorepo root, server, and client dependencies in one shot.

### 3. Start the development servers

```bash
npm run dev
```

This starts both servers concurrently:
- **API server** → http://localhost:3001
- **Vite dev server** → http://localhost:5173

Open [http://localhost:5173](http://localhost:5173) in your browser.

### 4. Production build (optional)

```bash
npm run build
```

Outputs to `client/dist/`. Serve with any static host or via the Express server by adding a static-files middleware.

---

## API Endpoints

All endpoints are prefixed with `/api`.

| Method | Path | Description |
|--------|------|-------------|
| GET | `/technologies` | List all 3 technologies |
| GET | `/technologies/:tech` | Technology metadata |
| GET | `/technologies/:tech/levels` | All levels for a technology |
| GET | `/technologies/:tech/levels/:level` | Level metadata |
| GET | `/technologies/:tech/levels/:level/modules` | Module list (no theory content) |
| GET | `/technologies/:tech/levels/:level/modules/:id` | Full module with theory HTML |
| GET | `/technologies/:tech/levels/:level/modules/:id/lab` | Lab (solutionCode stripped) |
| POST | `/technologies/:tech/levels/:level/modules/:id/lab/run` | Run lab validation |
| GET | `/technologies/:tech/levels/:level/quiz` | Quiz questions (correctOptionId stripped) |
| POST | `/technologies/:tech/levels/:level/quiz/answer` | Grade single question → returns explanation + citations |
| POST | `/technologies/:tech/levels/:level/quiz/submit` | Submit all answers → final score |

---

## Content Structure

### Technologies and Versions

| Technology | N-1 Version | Codename / Notes |
|------------|------------|------------------|
| Ansible | ansible-core **2.19** | Data Tagging, Windows Server 2025 support |
| Terraform | **1.13** | Stacks GA, rpcapi GA |
| Kubernetes | **1.35** | "Timbernetes" — Image Volumes GA, IPVS deprecated |

### Curriculum Map

```
Beginner     → Core concepts, installation, first commands/configs
Intermediate → Advanced patterns, multi-environment, error handling, roles/modules
Expert       → Production patterns, performance, security, CI/CD, GitOps, operators
```

Each module contains:
- **Theory** — HTML with embedded Mermaid diagrams, tables, and code examples
- **Lab** — Monaco Editor with starter code, hints, and auto-validation
- **Quiz** — 10 questions, server-graded, with explanation + official-docs citation per question

---

## Quiz Security

The `correctOptionId` is **never sent to the client** in GET responses. Answers are graded server-side:

- `GET /quiz` — returns questions with options but without correct answers
- `POST /quiz/answer` — you send `{ questionId, answer }`; server returns `{ correct, correctOption, explanation, citations }`
- `POST /quiz/submit` — final bulk submission for score calculation and progress saving

---

## Progress Tracking

Progress is persisted in **localStorage** under the key `devlearn_progress`. It tracks:
- Module started/completed status
- Lab best score per module
- Quiz score per level
- Level unlock status (complete all modules in a level to unlock the quiz)

No backend database is required — the app works fully offline after initial load.

---

## Official Documentation References

Every quiz question cites one or more official documentation pages:

- **Ansible** — https://docs.ansible.com/ansible/latest/
- **Terraform** — https://developer.hashicorp.com/terraform/docs
- **Kubernetes** — https://kubernetes.io/docs/

---

## Scripts Reference

| Command | Description |
|---------|-------------|
| `npm run dev` | Start both API server and Vite dev server concurrently |
| `npm run dev:server` | Start Express API server only (port 3001) |
| `npm run dev:client` | Start Vite dev server only (port 5173) |
| `npm run build` | Build client for production |
| `npm run install:all` | Install all dependencies (root + server + client) |

---

## License

MIT
