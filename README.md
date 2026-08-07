# StarterPython

Production-oriented Python backend starterkit built with FastAPI, PostgreSQL, SQLAlchemy 2, Alembic, Redis, and a pragmatic Modular Monolith / DDD-lite architecture.

## Goals

StarterPython is a reusable baseline for APIs, SaaS backends, internal systems, AI services, trading/data services, and other backend applications that need clear module boundaries without the overhead of full enterprise DDD.

The project optimizes for clear module boundaries, pragmatic DDD-lite conventions, AI/Codex-friendly documentation, production-ready configuration patterns, strong typing, and incremental growth.

## Stack

- Python 3.13+
- FastAPI
- Pydantic v2 + pydantic-settings
- SQLAlchemy 2 + PostgreSQL
- Alembic
- Redis
- uv
- pytest + HTTPX
- Ruff + Pyright
- Docker / Docker Compose

## Architecture

```text
HTTP Request
    -> Presentation / FastAPI Router
    -> Application Use Case
    -> Domain Model
    -> Repository Contract
    -> Infrastructure Adapter
    -> PostgreSQL / External Service
```

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

Read `docs/ARCHITECTURE.md`, `docs/MODULE-GUIDE.md`, and `docs/AI-DEVELOPMENT-GUIDE.md` before adding modules.

## Quick start

```bash
uv sync --all-groups
cp .env.example .env
docker compose up -d postgres redis
uv run fastapi dev src/starterpython/main.py
```

Open `http://127.0.0.1:8000/docs` and `http://127.0.0.1:8000/api/v1/health`.

## Quality checks

```bash
uv run ruff check .
uv run ruff format --check .
uv run pyright
uv run pytest
```

## Migrations

```bash
uv run alembic upgrade head
uv run alembic revision --autogenerate -m "change description"
```

## Current status

`v0.1-foundation` establishes the runnable skeleton, configuration, health endpoint, persistence/cache infrastructure, testing baseline, CI, Docker environment, and architectural documentation. Identity, access control, jobs, generators, and observability are planned increments.

## License

No license has been selected yet. Add one before distributing this starterkit as an open-source package.
