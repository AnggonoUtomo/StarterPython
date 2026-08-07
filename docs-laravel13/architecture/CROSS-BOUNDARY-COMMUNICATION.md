# Komunikasi Lintas Module Boundary

Komunikasi lintas boundary memiliki aturan lebih ketat daripada komunikasi antar module di dalam boundary yang sama.

## Prinsip

Boundary lain hanya boleh mengetahui public surface dari owning boundary. Ia tidak boleh bergantung pada internal module, Eloquent model, repository implementation, atau detail persistence boundary tersebut.

Contoh:

```text
Finance
    -> AccessControl Public Contract
        -> internal module AccessControl
            -> Role
            -> Permission
            -> Policy
```

Finance tidak perlu mengetahui bagaimana AccessControl menyusun Role dan Permission.

## Public Contract Boundary

Contoh:

```php
interface AccessControlGateway
{
    public function can(UserId $userId, PermissionCode $permission): bool;
}
```

Contract ditempatkan pada surface yang memang dimaksudkan sebagai API internal lintas boundary.

## Pilihan Mekanisme

1. **Synchronous Public Contract** — ketika hasil diperlukan saat itu juga.
2. **Published Event** — ketika boundary lain hanya bereaksi terhadap fakta bisnis.
3. **Read Model / Query Contract** — untuk projection lintas boundary yang read-only.
4. **External Integration Adapter** — ketika boundary berkomunikasi dengan sistem di luar monolith.

## Larangan

- `Finance` mengimpor `AccessControl/Role/Infrastructure/...`;
- membuat foreign write langsung ke tabel boundary lain;
- membuat relasi Eloquent lintas boundary yang menyebabkan ownership kabur;
- mengekspos seluruh internal service hanya demi kemudahan;
- menjadikan shared kernel sebagai jalan pintas untuk menghindari public contract.

## Perubahan Contract

Perubahan public contract lintas boundary harus diperlakukan sebagai perubahan arsitektur yang berdampak luas. Update dokumentasi boundary terkait dan buat ADR bila perubahan bersifat durable/signifikan.