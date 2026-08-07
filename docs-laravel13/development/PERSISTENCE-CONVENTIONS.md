# Konvensi Persistence Laravel 13

## Tujuan

Dokumen ini menetapkan pola persistence default untuk Modular Monolith + DDD-lite pada Laravel 13.

## Prinsip Utama

Eloquent adalah detail Infrastructure, bukan domain model secara otomatis. Untuk use case yang memiliki invariant atau business rule penting, gunakan boundary yang eksplisit.

```text
Application Action
    -> Domain
    -> Repository Contract
    -> Eloquent Repository
    -> Eloquent Model
    -> Database
```

## Kapan Repository Digunakan

Repository digunakan ketika ia melindungi domain/use-case boundary atau ownership persistence. Repository tidak wajib untuk setiap query CRUD sederhana.

Hindari interface generik yang hanya menyalin Eloquent:

```php
interface UserRepository
{
    public function all();
    public function find();
    public function create();
    public function update();
    public function delete();
}
```

Contract sebaiknya mencerminkan kebutuhan use case/domain.

## Query Sederhana

Read-only query yang tidak memiliki invariant kompleks boleh menggunakan dedicated query service/read model berbasis Eloquent secara pragmatis, selama ownership module tetap terjaga.

## Transaction Boundary

Transaction ditempatkan pada Application Layer/use case boundary.

```php
return DB::transaction(function () use ($data) {
    // orkestrasi use case
});
```

Controller tidak boleh mengelola `beginTransaction`, `commit`, dan `rollback` untuk business workflow.

## Ownership Data

- satu module memiliki tabel/data yang menjadi tanggung jawabnya;
- module lain tidak menulis tabel tersebut secara langsung;
- relasi lintas module/boundary tidak boleh membuat ownership kabur;
- komunikasi dilakukan melalui contract, query interface, atau event.

## Migration

Migration berada dekat dengan module pemiliknya bila project loader mendukung pola tersebut. Setiap perubahan schema persistent wajib memiliki migration.

## Eloquent Model

Eloquent Model dapat menyimpan mapping, cast, relation persistence, scope query yang relevan, dan detail ORM. Business invariant penting tidak boleh hanya hidup sebagai side effect tersembunyi pada model ORM.

## Anti-pattern

- semua business logic di Eloquent Model;
- repository generik untuk seluruh domain;
- commit/transaction tersebar pada controller;
- query langsung ke tabel module lain;
- model Infrastructure menjadi public contract lintas module;
- `DB::table()` lintas boundary tanpa ownership yang jelas.