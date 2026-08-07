# Komunikasi Antar Domain dan Modul

Komunikasi lintas modul harus eksplisit. Pilih mekanisme dengan coupling paling rendah yang tetap menjaga correctness.

## 1. Application Contract / Facade

Gunakan untuk perilaku sinkron ketika pemanggil membutuhkan hasil saat itu juga.

Contoh: Billing menanyakan kepada Identity apakah seorang user aktif melalui public application interface, bukan melalui model ORM milik Identity.

## 2. Domain Event atau Application Event

Gunakan ketika modul lain bereaksi terhadap sesuatu yang sudah terjadi dan transaction asal tidak membutuhkan hasil dari reaksi tersebut.

Contoh: `OrderCreated` dapat memicu handler Notification dan Analytics.

Event adalah fakta, sebaiknya menggunakan nama bentuk lampau, dan tidak boleh mengekspos model infrastructure.

## 3. Query Interface / Read Model

Gunakan untuk pembacaan lintas modul ketika projection khusus lebih jelas dibanding memuat aggregate milik modul lain.

## 4. Shared Kernel

Gunakan hanya untuk primitive stabil yang benar-benar memiliki makna bersama, seperti identifier, primitive uang, base domain event type, atau clock abstraction. Perubahan pada shared kernel memiliki dampak luas.

## Tabel Keputusan

| Kebutuhan | Mekanisme |
|---|---|
| Membutuhkan hasil langsung dari modul lain | Application contract |
| Bereaksi setelah business fact selesai | Event |
| Informasi read-only lintas modul | Query interface/read model |
| Primitive universal yang stabil | Shared kernel |

## Shortcut yang Dilarang

- Mengimpor implementasi repository milik modul lain.
- Mengimpor model SQLAlchemy milik modul lain.
- Menulis langsung ke tabel milik modul lain.
- Menggunakan Redis/pub-sub hanya untuk menghindari pembuatan in-process contract.
- Membuat direktori global `services/` yang melewati ownership modul.

Seluruh penjelasan, keputusan, dan dokumentasi komunikasi antar modul wajib ditulis dalam Bahasa Indonesia.
