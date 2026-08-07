# StarterPython

Starterkit backend Python berorientasi produksi yang dibangun dengan FastAPI, PostgreSQL, SQLAlchemy 2, Alembic, Redis, serta arsitektur Modular Monolith / DDD-lite yang pragmatis.

## Tujuan

StarterPython adalah baseline reusable untuk API, backend SaaS, sistem internal, layanan AI, layanan trading/data, dan aplikasi backend lain yang membutuhkan batas modul yang jelas tanpa overhead DDD enterprise penuh.

Proyek ini mengutamakan batas modul yang tegas, konvensi DDD-lite yang pragmatis, dokumentasi yang ramah AI/Codex, pola konfigurasi siap produksi, strong typing, serta pertumbuhan aplikasi secara incremental.

## Kebijakan Bahasa Dokumentasi

**Seluruh dokumentasi StarterPython wajib dibuat dalam Bahasa Indonesia.** Aturan ini berlaku untuk README, dokumentasi arsitektur, ADR, spesifikasi fitur, change record, roadmap, panduan modul, dokumentasi persistence, dan dokumentasi baru yang dibuat pada masa mendatang.

Nama class, function, variable, module, endpoint, command, serta identifier teknis dalam source code tetap menggunakan Bahasa Inggris mengikuti konvensi ekosistem Python. Istilah teknis yang lebih jelas dalam bentuk aslinya seperti `Unit of Work`, `repository`, `domain event`, dan `dependency` boleh dipertahankan dengan penjelasan Bahasa Indonesia.

## Stack Teknologi

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

## Arsitektur

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

Modul `users` merupakan vertical slice referensi untuk konvensi persistence.

Baca dokumentasi berikut sebelum menambahkan modul atau perilaku persistence:

- `docs/ARCHITECTURE.md`
- `docs/MODULE-GUIDE.md`
- `docs/DOMAIN-COMMUNICATION.md`
- `docs/PERSISTENCE-CONVENTIONS.md`
- `docs/AI-DEVELOPMENT-GUIDE.md`

## Memulai dengan Cepat

```bash
uv sync --all-groups
cp .env.example .env
docker compose up -d postgres redis
uv run alembic upgrade head
uv run fastapi dev src/starterpython/main.py
```

Buka `http://127.0.0.1:8000/docs` dan `http://127.0.0.1:8000/api/v1/health`.

Endpoint referensi persistence:

```http
POST /api/v1/users
Content-Type: application/json

{
  "email": "user@example.com",
  "name": "Example User"
}
```

## Pemeriksaan Kualitas

```bash
uv run ruff check .
uv run ruff format --check .
uv run pyright
uv run pytest
```

`uv run pytest` menjalankan test suite cepat secara default tanpa infrastruktur eksternal.

Untuk menjalankan integration test PostgreSQL secara lokal:

```bash
docker compose up -d postgres
uv run pytest -o addopts="-q --strict-markers --strict-config" -m integration tests/integration
```

GitHub Actions menyediakan service PostgreSQL sendiri untuk integration test.

## Migrasi Database

```bash
uv run alembic upgrade head
uv run alembic revision --autogenerate -m "deskripsi perubahan"
```

## Status Saat Ini

`v0.2.0` menyediakan fondasi runnable sekaligus implementasi referensi persistence resmi: domain entity, repository contract, mapping/adapter SQLAlchemy, transaction boundary melalui Unit of Work, migrasi Alembic, HTTP endpoint yang tipis, unit test berbasis fake, dan integration test PostgreSQL.

Increment berikutnya yang direncanakan: `v0.3 Identity`.

## Lisensi

Belum ada lisensi yang dipilih. Tambahkan lisensi sebelum mendistribusikan starterkit ini sebagai paket open-source.
