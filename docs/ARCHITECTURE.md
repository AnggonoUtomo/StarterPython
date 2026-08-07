# Architecture

## Decision

StarterPython uses a **Modular Monolith with pragmatic DDD-lite boundaries**. FastAPI is the primary HTTP delivery mechanism, not the center of the architecture.

## Dependency direction

```text
Presentation -> Application -> Domain
Infrastructure -> Domain/Application contracts
Bootstrap -> all composition roots
```

The Domain layer must not import FastAPI, SQLAlchemy ORM models, Redis clients, or other delivery/infrastructure frameworks.

## Top-level responsibilities

### `core/`
Technical primitives shared by the application: configuration, logging, database engine/session, cache client, exception mapping. Business rules do not belong here.

### `bootstrap/`
Composition root. It connects routers, lifecycle hooks, dependency implementations, and application initialization.

### `modules/`
Business capabilities. New business behavior should normally live in a module.

### `shared/`
A deliberately small shared kernel for stable primitives used by multiple modules. Do not use it as a dumping ground.

## Module structure

```text
modules/<module>/
├── domain/
│   ├── entities/
│   ├── value_objects/
│   ├── events/
│   └── repositories.py
├── application/
│   ├── commands/
│   ├── queries/
│   ├── dto/
│   └── services/
├── infrastructure/
│   ├── persistence/
│   ├── repositories/
│   └── integrations/
└── presentation/
    ├── routes.py
    └── schemas.py
```

Folders are created when they have real content; empty ceremony is not required.

## Request flow

A mutating request should generally flow as:

```text
HTTP schema -> route -> application command/use case -> domain -> repository contract -> adapter
```

A simple read may use a query service/read model without reconstructing a rich aggregate when no domain invariant is involved.

## Rules

1. Never import another module's infrastructure models directly.
2. Cross-module synchronous access goes through an application contract/facade.
3. Cross-module reactions that need no immediate response use events.
4. Transactions belong to the application/use-case boundary, not HTTP routes.
5. Domain objects express invariants; Pydantic request schemas are not domain entities.
6. Prefer explicit code over generic repository/service abstractions with no business value.
7. Add CQRS patterns only where command/query separation improves clarity or scaling.
8. Record significant architectural changes as ADRs.
