# Roadmap

## v0.1 — Foundation

- [x] FastAPI application factory
- [x] environment configuration
- [x] structured logging baseline
- [x] SQLAlchemy async session
- [x] Redis client
- [x] health endpoint
- [x] Docker Compose PostgreSQL + Redis
- [x] pytest, Ruff, Pyright
- [x] CI workflow
- [x] architectural documentation

## v0.2 — Persistence conventions

- [x] example `users` aggregate and SQLAlchemy mapping
- [x] Unit of Work transaction boundary
- [x] repository contract + SQLAlchemy adapter example
- [x] first Alembic migration
- [x] unit tests with fake repository/UoW
- [x] PostgreSQL integration-test fixtures
- [x] documented persistence conventions

Reference implementation: `src/starterpython/modules/users/`.

## v0.3 — Identity

- [ ] registration/login
- [ ] Argon2 password hashing
- [ ] access + refresh tokens
- [ ] token rotation/revocation
- [ ] email verification/password reset boundaries

## v0.4 — Access Control

- [ ] roles and permissions
- [ ] policy/authorization layer
- [ ] reusable FastAPI authorization dependency

## v0.5 — Application messaging

- [ ] in-process event bus
- [ ] transactional event dispatch convention
- [ ] background job adapter
- [ ] retry/idempotency conventions

## v0.6 — Developer Experience

- [ ] CLI command `starterpython new`
- [ ] module generator
- [ ] feature generator
- [ ] migration/test scaffolding

## v1.0 — Production baseline

- [ ] OpenTelemetry
- [ ] metrics/tracing
- [ ] production Docker hardening
- [ ] security checklist
- [ ] deployment guide
- [x] example reference module (`users`)
