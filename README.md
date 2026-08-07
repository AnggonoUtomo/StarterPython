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
    ├── system/
    └── users/
        ├── application/
        ├── domain/
        ├── infrastructure/
        └── presentation/
```

The `users` module is the reference vertical slice for persistence conventions.

Read these documents before adding modules or persistence behavior:

- `docs/ARCHITECTURE.md`
- `docs/MODULE-GUIDE.md`
- `docs/DOMAIN-COMMUNICATION.md`
- `docs/PERSISTENCE-CONVENTIONS.md`
- `docs/AI-DEVELOPMENT-GUIDE.md`

## Quick start

```bash
uv sync --all-groups
cp .env.example .env
docker compose up -d postgres redis
uv run alembic upgrade head
uv run fastapi dev src/starterpython/main.py
```

Open `http://127.0.0.1:8000/docs` and `http://127.0.0.1:8000/api/v1/health`.

The persistence reference endpoint is:

```http
POST /api/v1/users
Content-Type: application/json

{
  "email": "user@example.com",
  "name": "Example User"
}
```

## Quality checks

```bash
uv run ruff check .
uv run ruff format --check .
uv run pyright
uv run pytest
```

`uv run pytest` runs the default fast test suite without external infrastructure.

To run PostgreSQL integration tests locally:

```bash
docker compose up -d postgres
uv run pytest -o addopts="-q --strict-markers --strict-config" -m integration tests/integration
```

GitHub Actions provisions its own PostgreSQL service for the integration suite.

## Migrations

```bash
uv run alembic upgrade head
uv run alembic revision --autogenerate -m "change description"
```

## Current status

`v0.2.0` establishes the runnable foundation plus the official persistence reference implementation: domain entity, repository contract, SQLAlchemy mapping/adapter, Unit of Work transaction boundary, Alembic migration, thin HTTP endpoint, fake-based unit tests, and PostgreSQL integration tests.

Next planned increment: `v0.3 Identity`.

## License

No license has been selected yet. Add one before distributing this starterkit as an open-source package.
