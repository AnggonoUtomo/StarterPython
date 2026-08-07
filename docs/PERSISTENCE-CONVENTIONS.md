# Konvensi Persistence

## Tujuan

Dokumen ini mendefinisikan pola persistence default untuk StarterPython. Modul `users` merupakan implementasi referensinya.

## Alur Referensi

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

Arah dependency tetap bergerak ke dalam: domain dan application contract tidak mengimpor SQLAlchemy.

## Domain Entity

Domain entity adalah object Python yang independen dari framework. Domain entity memiliki business invariant dan normalisasi yang memang bermakna bagi domain.

Referensi: `src/starterpython/modules/users/domain/entities.py`.

Jangan menggunakan model SQLAlchemy atau Pydantic request model sebagai domain entity.

## Repository Contract

Repository contract berada di sisi domain/application dan hanya mendeskripsikan operasi yang benar-benar dibutuhkan use case.

Utamakan contract kecil yang berorientasi bisnis dibanding generic CRUD repository.

```python
class UserRepository(Protocol):
    async def add(self, user: User) -> None: ...
    async def get_by_email(self, email: str) -> User | None: ...
```

Jangan mengekspos SQLAlchemy `Session`, query, ORM model, atau tipe khusus database melalui contract.

## Model SQLAlchemy

ORM model ditempatkan di bawah `infrastructure/persistence/`. Model ini mendeskripsikan storage, index, constraint, dan detail mapping.

Model SQLAlchemy dapat terlihat mirip dengan domain entity, tetapi keduanya bukan object yang sama.

Adapter harus melakukan mapping secara eksplisit antara ORM model dan domain object.

## Repository Adapter

Infrastructure repository mengimplementasikan repository contract menggunakan `AsyncSession`.

Aturan:

1. konstruksi query berada di adapter;
2. object yang melewati repository boundary adalah domain object, bukan ORM model;
3. repository tidak melakukan commit transaction;
4. repository boleh memanggil `flush()` jika membutuhkan nilai yang dihasilkan database secara langsung, tetapi penyelesaian transaction tetap berada di luar repository.

## Unit of Work

Application use-case boundary mengelola penyelesaian transaction melalui contract Unit of Work.

```text
Application Handler
    -> operasi repository
    -> commit jika berhasil
    -> rollback jika gagal
```

HTTP route tidak boleh berisi transaction choreography.

Untuk modul sederhana, gunakan UoW spesifik modul daripada memperkenalkan abstraction global generik terlalu dini.

## Application Use Case

Application handler mengoordinasikan use case. Ia dapat:

- melakukan query melalui repository;
- membuat atau memanggil domain object;
- mengoordinasikan beberapa operasi repository;
- melakukan commit atau rollback Unit of Work;
- mengembalikan application DTO/result object.

Application handler tidak boleh mengetahui FastAPI request object, HTTP status code, atau SQLAlchemy ORM model.

## HTTP Presentation

Route menerjemahkan kebutuhan transport menjadi application command serta menerjemahkan kegagalan application/domain yang dikenali menjadi HTTP response.

Route sengaja dibuat tipis:

```text
validasi request -> bangun dependency -> panggil handler -> mapping result/error
```

## Migrasi Database

Alembic merupakan source of truth untuk evolusi schema.

- Setiap perubahan persistent schema wajib memiliki migration.
- ORM metadata yang digunakan autogenerate harus diimpor dari `migrations/env.py` atau melalui model registry terpusat pada masa mendatang.
- Jangan mengandalkan `Base.metadata.create_all()` untuk deployment schema produksi.
- Integration test boleh menggunakan `create_all()` untuk adapter test terisolasi jika behavior migration bukan hal yang sedang diuji.

## Testing Pyramid

### Unit Test

Test application/domain menggunakan fake repository dan fake Unit of Work. Test ini cepat dan tidak membutuhkan infrastructure eksternal.

Jalankan:

```bash
uv run pytest
```

### Integration Test

Test repository/mapping menggunakan PostgreSQL nyata dan diberi marker `integration`.

Jalankan secara lokal setelah PostgreSQL aktif:

```bash
docker compose up -d postgres
uv run pytest -o addopts="-q --strict-markers --strict-config" -m integration tests/integration
```

GitHub Actions menyediakan PostgreSQL secara otomatis untuk kelompok test ini.

## Menambahkan Modul Persistent Baru

Gunakan urutan berikut:

1. definisikan domain entity/value object;
2. definisikan repository contract minimum yang dibutuhkan use case;
3. definisikan application command/query dan handler;
4. tambahkan ORM model pada infrastructure;
5. implementasikan repository adapter;
6. implementasikan atau perluas Unit of Work modul;
7. tambahkan migration;
8. daftarkan ORM metadata untuk Alembic;
9. ekspos use case melalui presentation;
10. tambahkan unit test;
11. tambahkan repository integration test jika behavior persistence penting.

## Anti-pattern

Jangan memperkenalkan pola berikut tanpa keputusan arsitektur eksplisit:

- satu global `GenericRepository[T]` untuk seluruh domain;
- commit di dalam method repository;
- model SQLAlchemy diimpor oleh kode domain/application;
- business rule di dalam FastAPI route;
- direct cross-module ORM relationship yang melewati contract modul;
- `Base.metadata.create_all()` sebagai mekanisme migration saat startup aplikasi;
- shared `utils.py` sebagai tempat penampungan behavior persistence.

Seluruh dokumentasi persistence, migration note, dan keputusan terkait data wajib ditulis dalam Bahasa Indonesia.
