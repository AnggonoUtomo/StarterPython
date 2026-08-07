# Arsitektur

## Keputusan

StarterPython menggunakan **Modular Monolith dengan batas DDD-lite yang pragmatis**. FastAPI adalah mekanisme delivery HTTP utama, bukan pusat arsitektur aplikasi.

## Arah Dependency

```text
Presentation -> Application -> Domain
Infrastructure -> kontrak Domain/Application
Bootstrap -> seluruh composition root
```

Layer Domain tidak boleh mengimpor FastAPI, model ORM SQLAlchemy, client Redis, atau framework delivery/infrastructure lainnya.

## Tanggung Jawab Level Atas

### `core/`
Primitive teknis yang digunakan bersama oleh aplikasi: konfigurasi, logging, database engine/session, cache client, dan pemetaan exception. Business rule tidak boleh ditempatkan di sini.

### `bootstrap/`
Composition root. Bagian ini menghubungkan router, lifecycle hook, implementasi dependency, dan proses inisialisasi aplikasi.

### `modules/`
Kapabilitas bisnis. Perilaku bisnis baru pada umumnya harus ditempatkan di dalam sebuah modul.

### `shared/`
Shared kernel yang sengaja dijaga tetap kecil untuk primitive stabil yang benar-benar digunakan beberapa modul. Jangan menjadikannya tempat penampungan kode umum.

## Struktur Modul

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

Folder dibuat ketika memang memiliki isi dan tanggung jawab nyata. Tidak perlu membuat struktur kosong hanya demi mengikuti template.

## Alur Request

Request yang mengubah state pada umumnya mengikuti alur:

```text
HTTP schema -> route -> application command/use case -> domain -> repository contract -> adapter
```

Operasi baca sederhana boleh menggunakan query service/read model tanpa membangun aggregate lengkap jika tidak ada invariant domain yang perlu dijalankan.

## Aturan

1. Jangan pernah mengimpor model infrastructure milik modul lain secara langsung.
2. Akses sinkron lintas modul harus melalui application contract/facade.
3. Reaksi lintas modul yang tidak membutuhkan hasil langsung menggunakan event.
4. Transaction boundary berada pada layer application/use case, bukan pada HTTP route.
5. Object domain mengekspresikan invariant; Pydantic request schema bukan domain entity.
6. Utamakan kode eksplisit dibanding abstraction repository/service generik yang tidak memberi nilai bisnis.
7. Gunakan pola CQRS hanya ketika pemisahan command/query benar-benar meningkatkan kejelasan atau skalabilitas.
8. Perubahan arsitektur yang signifikan harus dicatat sebagai ADR.
9. Seluruh dokumentasi arsitektur dan dokumentasi proyek wajib ditulis dalam Bahasa Indonesia.
