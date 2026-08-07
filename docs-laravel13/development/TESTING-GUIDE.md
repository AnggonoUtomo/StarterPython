# Panduan Testing Laravel 13

## Tujuan

Testing mengikuti batas arsitektur dan memilih level termurah yang tetap memberi confidence memadai.

## Unit Test

Cocok untuk:

- Entity domain;
- Value Object;
- Domain Service;
- Application logic murni;
- policy/rule yang tidak membutuhkan framework.

Unit test sebisa mungkin tidak membutuhkan bootstrap Laravel lengkap.

## Feature Test

Cocok untuk:

- HTTP endpoint;
- authentication;
- authorization;
- FormRequest validation;
- orchestration use case melalui framework;
- behavior yang dilihat pengguna/API consumer.

## Integration Test

Cocok untuk:

- repository Eloquent;
- mapping database;
- event/queue adapter;
- cache adapter;
- external integration adapter;
- behavior yang membutuhkan dependency nyata.

## Struktur Referensi

```text
app/Module/AccessControl/Role/Tests/
├── Unit/
├── Feature/
└── Integration/
```

## Prinsip

1. Test business invariant sedekat mungkin dengan Domain.
2. Jangan menguji seluruh framework hanya untuk memverifikasi satu aturan kecil.
3. Repository contract/application use case dapat memakai fake pada unit test.
4. Adapter Eloquent diuji dengan database pada integration test.
5. Endpoint penting diuji pada Feature Test.
6. Bug fix harus menambahkan regression test bila memungkinkan.
7. Test lintas boundary harus memvalidasi public contract, bukan internal implementation.

## Definition of Done Testing

Sebuah perubahan belum selesai bila behavior penting belum memiliki test pada level yang sesuai atau perubahan menyebabkan test existing gagal.