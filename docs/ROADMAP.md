# Roadmap

## v0.1 — Fondasi

- [x] application factory FastAPI
- [x] konfigurasi environment
- [x] baseline structured logging
- [x] async session SQLAlchemy
- [x] client Redis
- [x] health endpoint
- [x] Docker Compose PostgreSQL + Redis
- [x] pytest, Ruff, Pyright
- [x] workflow CI
- [x] dokumentasi arsitektur

## v0.2 — Konvensi Persistence

- [x] contoh aggregate `users` dan mapping SQLAlchemy
- [x] transaction boundary dengan Unit of Work
- [x] contoh repository contract + SQLAlchemy adapter
- [x] migrasi Alembic pertama
- [x] unit test dengan fake repository/UoW
- [x] fixture integration test PostgreSQL
- [x] dokumentasi konvensi persistence

Implementasi referensi: `src/starterpython/modules/users/`.

## v0.3 — Identity

- [ ] registration/login
- [ ] password hashing Argon2
- [ ] access token + refresh token
- [ ] token rotation/revocation
- [ ] boundary email verification/password reset

## v0.4 — Access Control

- [ ] role dan permission
- [ ] layer policy/authorization
- [ ] reusable FastAPI authorization dependency

## v0.5 — Application Messaging

- [ ] in-process event bus
- [ ] konvensi transactional event dispatch
- [ ] background job adapter
- [ ] konvensi retry/idempotency

## v0.6 — Developer Experience

- [ ] command CLI `starterpython new`
- [ ] generator modul
- [ ] generator fitur
- [ ] scaffolding migration/test

## v1.0 — Baseline Produksi

- [ ] OpenTelemetry
- [ ] metrics/tracing
- [ ] production Docker hardening
- [ ] checklist keamanan
- [ ] panduan deployment
- [x] contoh modul referensi (`users`)

## Kebijakan Dokumentasi

Semua dokumentasi yang dibuat pada setiap fase roadmap wajib menggunakan Bahasa Indonesia, termasuk ADR, Feature Spec, Change Record, panduan implementasi, dokumentasi modul, dan catatan migration.
