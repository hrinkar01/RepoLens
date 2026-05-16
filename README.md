# RepoLens

RepoLens is a local-first visual repository intelligence and open-source contribution platform designed to help developers understand large codebases faster through interactive visualization, repository analysis, semantic search, and contribution-focused workflows.

---

# Core Features

## Repository & GitHub Management
- GitHub repository monitoring
- PR, issue, commit, and mention tracking
- Local repository cloning and synchronization
- CI/CD and GitHub Actions monitoring
- Real-time notification system

## Repository Understanding
- Interactive repository explorer
- Visual trace flow and dependency mapping
- Function call and import analysis
- Codebase architecture visualization
- Semantic code search
- Blast Radius Analysis — identifies files, functions, modules, and dependencies affected by code changes.

## Contributor Assistance
- Good first issue discovery
- Related file suggestions
- Contribution workflow guidance
- Repository onboarding assistance
- AI-assisted codebase explanations and summaries

## Analysis Engine
- Static code analysis
- Repository indexing
- Dependency graph generation
- Symbol and reference tracking
- Local-first offline analysis support

---

# Tech Stack

## Frontend
- Next.js
- Tailwind CSS
- React Flow
- Cytoscape.js

## Backend
- Python
- FastAPI

## Analysis Engine
- Tree-sitter
- GitPython
- NetworkX
- Universal Ctags

## Database
- SQLite

## Search & AI
- sentence-transformers
- Ollama *(future optional local AI support)*

## Integrations
- GitHub API

---

# Design Principles
- Local-first architecture
- Privacy-focused analysis
- Visual repository understanding
- Modular and extensible system design
- Offline-capable workflows
- Contributor-friendly experience