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

## DevOps & Setup
- Docker
- Docker Compose
- Setup Scripts

---

# Design Principles
- Local-first architecture
- Privacy-focused analysis
- Visual repository understanding
- Modular and extensible system design
- Offline-capable workflows
- Contributor-friendly experience

---

# Future Goals
- One-command local setup
- Dockerized development environment
- Cross-platform support
- Advanced repository visualization
- AI-assisted debugging and onboarding
- Plugin and extension system
- Large-scale monorepo support

---

# Setup Philosophy

RepoLens is designed as a local-first platform where all repository analysis, indexing, and visualization happen on the user's machine. No repository data is sent to external servers or cloud-hosted LLMs by default.

Future versions will support:
- Automated setup scripts
- Docker-based installation
- Plug-and-play local development environments

---

# Extra Details

this is my current project overview in obsidian as notes improve this 
**CLI Interface** — Command-line tool to manage repos, analysis, and monitoring.
- **Local Web Dashboard** — Browser-based UI for visualizing repos, issues, graphs, and notifications.
- **GitHub Monitor** — Tracks PRs, issues, mentions, commits, and repository events.
- **Repo Explorer** — Browse repository structure, files, folders, and README easily.
- **AI Codebase Assistant** — Explains files, folders, architecture, and summarizes code/PRs.
- **Trace Flow Engine** — Shows function calls, dependencies, imports, and execution flow visually.
- **Contribution Assistant** — Finds good first issues, setup steps, and related files for contributors.
- **CI/CD Monitor** — Displays GitHub Actions, build status, deployments, and failed pipelines.
- **Notifications System** — Real-time alerts for PRs, mentions, CI failures, and issue updates.
- **Code Analysis Engine** — Uses Tree-sitter, ctags, and graphs for repo intelligence and indexing.
- **Semantic Search** — Search codebase using meaning/context instead of exact keywords.
- **Local Repo Storage** — Stores cloned repos, cache, metadata, logs, and indexed data locally.
- **Git Integration** — Clone, pull, sync, and analyze repositories locally.
- **Offline Support** — Core repo analysis features work locally without internet after indexing.
- **Extensible Architecture** — New modules, integrations, and services can be added easily later.
- Blast Radius Mechanism

### **Tech Stack:**
Frontend:
- Next.js
- Tailwind CSS
- React Flow
- Cytoscape.js

Backend:
- FastAPI
- Python

Analysis:
- Tree-sitter
- GitPython
- NetworkX

Database:
- SQLite

Search:
- sentence-transformers

Integrations:
- GitHub API

---

```