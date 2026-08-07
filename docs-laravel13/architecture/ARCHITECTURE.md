# Arsitektur Laravel 13

## Keputusan Utama

Project menggunakan **Modular Monolith + DDD-lite** dengan Laravel 13 sebagai application framework. Laravel menangani HTTP, container, provider, event dispatcher, queue, console, cache, database, dan fasilitas framework lainnya. Business capability tetap dipisahkan dalam Module Boundary dan Module.

## Struktur Utama

```text
app/
├── Http/
├── Console/
├── Providers/
├── Shared/
└── Module/
    └── {ModuleBoundary}/
        └── {Module}/
```

Pola resmi:

```text
app/Module/{ModuleBoundary}/{Module}
```

## Arah Dependency

```text
Presentation -> Application -> Domain
Infrastructure -> Domain/Application Contracts
Provider/Bootstrap -> Composition Root
```

Domain tidak boleh bergantung pada HTTP, Controller, FormRequest, Eloquent Model, Redis client, Queue driver, Mail facade, SDK eksternal, atau detail framework lainnya.

## Layer

### Domain
Berisi business rule, entity, value object, domain service, domain event, contract, dan exception domain.

### Application
Mengorkestrasi use case. Dapat berisi Action, Command, Query, DTO, application service, dan contract untuk dependency yang dibutuhkan use case.

### Infrastructure
Mengimplementasikan contract ke database, Eloquent, cache, filesystem, external API, message broker, dan detail teknis lainnya.

### Presentation
Mengubah input transport menjadi input application dan hasil application menjadi response HTTP/console/resource.

## Flow Mutation

```text
HTTP Request
    -> FormRequest
    -> Controller
    -> Application Action/Command
    -> Domain
    -> Repository Contract
    -> Eloquent Repository
    -> Database
```

Controller harus tipis dan tidak menjadi tempat business logic atau transaction choreography.

## Prinsip

1. Boundary bisnis lebih penting daripada folder teknis global.
2. Jangan membuat abstraction hanya karena pola DDD menyediakannya.
3. Folder dibuat ketika ada responsibility nyata.
4. Query sederhana boleh lebih pragmatis daripada mutation yang menjaga invariant.
5. Perubahan arsitektur jangka panjang wajib direkam dalam ADR.
6. Semua dokumentasi wajib menggunakan Bahasa Indonesia.