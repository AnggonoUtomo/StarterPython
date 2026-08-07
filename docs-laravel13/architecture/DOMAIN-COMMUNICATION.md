# Komunikasi Domain dan Antar Module

Komunikasi antar module harus eksplisit dan menggunakan mekanisme dengan coupling paling rendah yang tetap menjaga correctness.

## 1. Application Contract / Facade

Gunakan untuk kebutuhan synchronous ketika pemanggil memerlukan hasil saat itu juga.

Contoh: module Billing membutuhkan status user melalui contract publik, bukan dengan mengakses Eloquent model milik UserManagement.

## 2. Domain/Application Event

Gunakan ketika module lain hanya perlu bereaksi terhadap fakta bisnis yang sudah terjadi dan hasilnya tidak dibutuhkan oleh transaksi asal.

Contoh:

```text
OrderCreated
    -> Notification
    -> Analytics
```

Event menggunakan nama fakta, biasanya bentuk lampau, dan tidak boleh membawa ORM model sebagai kontrak publik.

## 3. Query Contract / Read Model

Gunakan untuk kebutuhan baca lintas module ketika projection khusus lebih tepat daripada mengambil aggregate milik module lain.

## 4. Shared Kernel

Gunakan hanya untuk primitive stabil yang benar-benar memiliki makna bersama, misalnya Identifier, Money, Clock, atau base event abstraction. Shared Kernel bukan tempat membuang helper umum.

## Aturan Dalam Satu Boundary

Module di dalam boundary yang sama boleh berkomunikasi lebih dekat, tetapi tetap tidak boleh mengakses Infrastructure module lain secara langsung.

Dilarang:

```php
use App\Module\AccessControl\Permission\Infrastructure\Models\Permission;
```

Gunakan Application Contract, Query Contract, atau Event.

## Tabel Keputusan

| Kebutuhan | Mekanisme |
|---|---|
| Butuh hasil langsung | Application Contract |
| Reaksi setelah fakta bisnis | Event |
| Baca data lintas module | Query Contract / Read Model |
| Primitive universal yang stabil | Shared Kernel |

## Shortcut yang Dilarang

- mengimpor repository implementation module lain;
- mengimpor Eloquent model module lain;
- menulis tabel milik module lain secara langsung;
- membuat global `Services/` untuk melewati module ownership;
- memakai queue/pub-sub hanya untuk menghindari contract yang seharusnya sederhana dan synchronous.