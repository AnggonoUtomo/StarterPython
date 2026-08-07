# Panduan Modul

Sebuah modul merepresentasikan kapabilitas bisnis dengan boundary, vocabulary, serta kepemilikan model persistence yang eksplisit.

## Kapan Membuat Modul

Buat modul ketika sebuah kapabilitas memiliki business rule yang berarti, lifecycle/data ownership sendiri, atau membutuhkan boundary independen. Jangan membuat modul hanya untuk helper generik.

## Modul Minimal

```text
modules/billing/
├── application/
│   └── create_invoice.py
├── domain/
│   └── invoice.py
├── infrastructure/
│   └── invoice_repository.py
└── presentation/
    ├── routes.py
    └── schemas.py
```

Sebuah modul boleh dimulai lebih kecil. Tambahkan folder karena memang ada tanggung jawab yang perlu ditempatkan, bukan karena template mengharuskan semua folder tersedia.

## Urutan Implementasi Fitur

1. Tulis spesifikasi fitur/modul jika perilakunya tidak trivial.
2. Identifikasi invariant dan ownership.
3. Definisikan konsep domain.
4. Definisikan input/output application yang diperlukan.
5. Definisikan contract untuk persistence atau dependency eksternal.
6. Implementasikan infrastructure adapter.
7. Ekspos melalui presentation layer.
8. Tambahkan unit test, integration test, atau feature test sesuai kebutuhan.
9. Perbarui dokumentasi/ADR jika arsitektur berubah.

## Penamaan

Gunakan bahasa bisnis yang jelas seperti `CreateInvoice`, `Membership`, atau `TradingSignal`. Hindari nama lemah seperti `Manager`, `Helper`, `CommonService`, atau `Utils` jika terdapat nama kapabilitas yang lebih tepat.

Nama identifier di source code tetap menggunakan Bahasa Inggris mengikuti konvensi Python, sedangkan dokumentasi penjelasannya wajib menggunakan Bahasa Indonesia.

## Aturan Boundary

Import berikut dilarang jika dilakukan dari modul lain:

```python
from starterpython.modules.users.infrastructure.models import UserModel
```

Gunakan application-facing contract yang stabil seperti `UserReader`, `UserAccess`, atau event yang dipublikasikan oleh modul pemilik data.
