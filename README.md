# StarterPython

Production-oriented Python backend starterkit built with FastAPI, PostgreSQL, SQLAlchemy 2, Alembic, Redis, and a pragmatic Modular Monolith / DDD-lite architecture.

## Goals

StarterPython is a reusable baseline for APIs, SaaS backends, internal systems, AI services, trading/data services, and other backend applications that need clear module boundaries without the overhead of full enterprise DDD.

The project optimizes for:

- clear module boundaries;
- pragmatic DDD-lite conventions;
- AI/Codex-friendly documentation;
- production-ready configuration patterns;
- strong typing, linting, and automated tests;
- incremental growth from a small service to a larger modular application.

## Technology

- Python 3.13+
- FastAPI
- Pydantic v2 + pydantic-settings
- SQLAlchemy 2
- PostgreSQL
- Alembic
- Redis
- uv package manager
- pytest + HTTPX
- Ruff
- Pyright
- Docker / Docker Compose

## Architecture

```text
HTTP Request
    |
    v
Presentation / FastAPI Router
    |
    v
Application Use Case
    |
    v
Domain Model
    |
    v
Repository Contract
    |
    v
Infrastructure Adapter
    |
    v
PostgreSQL / External Service
```

Application code is organized by business module rather than technical layer at the project root.

```text
src/starterpython/
├── main.py
├── bootstrap/
├── core/
├── shared/
└── modules/
    └── system/
        ├── application/
        ├── domain/
        ├── infrastructure/
        └── presentation/
```

See [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) and [`docs/MODULE-GUIDE.md`](docs/MODULE-GUIDE.md) before adding a new module.

## Quick start

### 1. Install uv

Follow the official uv installation instructions, then:

```bash
uv sync --all-groups
```

### 2. Configure environment

```bash
cp .env.example .env
```

### 3. Start dependencies

```bash
docker compose up -d postgres redis
```

### 4. Run the API

```bash
uv run fastapi dev src/starterpython/main.py
```

Open:

- API docs: `http://127.0.0.1:8000/docs`
- Health endpoint: `http://127.0.0.1:8000/api/v1/health`

### 5. Run quality checks

```bash
uv run ruff check .
uv run ruff format --check .
uv run pyright
uv run pytest
```

## Commands

```bash
# Development server
uv run fastapi dev src/starterpython/main.py

# Tests
uv run pytest

# Lint
uv run ruff check .

# Format
uv run ruff format .

# Type check
uv run pyright

# Migrations
uv run alembic upgrade head
uv run alembic revision --autogenerate -m "change description"
```

## Development rules

Before implementing a feature, read:

1. [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md)
2. [`docs/MODULE-GUIDE.md`](docs/MODULE-GUIDE.md)
3. [`docs/DOMAIN-COMMUNICATION.md`](docs/DOMAIN-COMMUNICATION.md)
4. [`docs/AI-DEVELOPMENT-GUIDE.md`](docs/AI-DEVELOPMENT-GUIDE.md)

New architectural decisions should be recorded as ADRs under `docs/adr/`.

## Current status

`v0.1-foundation` establishes the project skeleton, configuration, health endpoint, database/Redis infrastructure, testing baseline, CI, Docker environment, and architectural documentation. Authentication, access control, background jobs, module generators, and production observability are intentionally planned as later increments.

## License

No license has been selected yet. Add one before distributing the starterkit as an open-source package.
