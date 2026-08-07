# Persistence Conventions

## Purpose

This document defines the default persistence pattern for StarterPython. The `users` module is the reference implementation.

## Reference flow

```text
HTTP Request
    -> presentation schema
    -> application command
    -> application handler
    -> domain entity
    -> repository contract
    -> SQLAlchemy repository adapter
    -> Unit of Work
    -> PostgreSQL
```

The dependency direction remains inward: domain and application contracts do not import SQLAlchemy.

## Domain entity

Domain entities are framework-independent Python objects. They own business invariants and normalization that are meaningful to the domain.

Reference: `src/starterpython/modules/users/domain/entities.py`.

Do not use SQLAlchemy models or Pydantic request models as domain entities.

## Repository contract

Repository contracts live on the domain/application side and describe only operations required by use cases.

Prefer small business-oriented contracts over generic CRUD repositories.

```python
class UserRepository(Protocol):
    async def add(self, user: User) -> None: ...
    async def get_by_email(self, email: str) -> User | None: ...
```

Do not expose SQLAlchemy `Session`, queries, ORM models, or database-specific types through the contract.

## SQLAlchemy model

ORM models belong under `infrastructure/persistence/`. They describe storage, indexes, constraints, and mapping details.

A SQLAlchemy model may resemble a domain entity but is not the domain entity.

Adapters explicitly map between ORM models and domain objects.

## Repository adapter

The infrastructure repository implements the repository contract using `AsyncSession`.

Rules:

1. query construction belongs in the adapter;
2. domain objects cross the repository boundary, not ORM models;
3. repositories do not commit transactions;
4. repositories may call `flush()` when an immediate database-generated value is required, but transaction completion remains outside the repository.

## Unit of Work

The application use-case boundary owns transaction completion through a Unit of Work contract.

```text
Application Handler
    -> repository operations
    -> commit on success
    -> rollback on failure
```

HTTP routes must not contain transaction choreography.

For simple modules a module-specific UoW is preferred over introducing a global generic abstraction prematurely.

## Application use case

Application handlers coordinate the use case. They may:

- query repositories;
- create or invoke domain objects;
- coordinate multiple repository operations;
- commit or roll back the Unit of Work;
- return application DTO/result objects.

They should not know FastAPI request objects, HTTP status codes, or SQLAlchemy ORM models.

## HTTP presentation

Routes translate transport concerns into application commands and translate known application/domain failures into HTTP responses.

The route is intentionally thin:

```text
validate request -> construct dependency -> call handler -> map result/error
```

## Migrations

Alembic is the source of truth for schema evolution.

- Every persistent schema change requires a migration.
- ORM metadata used by autogenerate must be imported from `migrations/env.py` or from a future centralized model registry.
- Never rely on `Base.metadata.create_all()` for production schema deployment.
- Integration tests may use `create_all()` for isolated adapter tests when migration behavior is not the subject of that test.

## Testing pyramid

### Unit tests

Application/domain tests use fake repositories and fake Unit of Work implementations. They are fast and require no external infrastructure.

Run:

```bash
uv run pytest
```

### Integration tests

Repository/mapping tests use a real PostgreSQL instance and are marked `integration`.

Run locally after starting PostgreSQL:

```bash
docker compose up -d postgres
uv run pytest -o addopts="-q --strict-markers --strict-config" -m integration tests/integration
```

GitHub Actions provisions PostgreSQL automatically for this test group.

## Adding a new persistent module

Use this sequence:

1. define domain entity/value objects;
2. define the minimum repository contract required by the use case;
3. define application command/query and handler;
4. add ORM model under infrastructure;
5. implement repository adapter;
6. implement or extend the module Unit of Work;
7. add migration;
8. register ORM metadata for Alembic;
9. expose the use case through presentation;
10. add unit tests;
11. add repository integration tests where persistence behavior matters.

## Anti-patterns

Do not introduce these patterns without an explicit architectural decision:

- one global `GenericRepository[T]` for every domain;
- commits inside repository methods;
- SQLAlchemy models imported by domain/application code;
- business rules inside FastAPI routes;
- direct cross-module ORM relationships that bypass module contracts;
- `Base.metadata.create_all()` as an application startup migration mechanism;
- a shared `utils.py` dumping ground for persistence behavior.
