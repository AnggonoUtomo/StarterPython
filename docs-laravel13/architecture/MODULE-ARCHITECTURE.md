# Arsitektur Module

## Struktur Referensi

```text
app/Module/{ModuleBoundary}/{Module}/
├── Application/
│   ├── Actions/
│   ├── Commands/
│   ├── Queries/
│   ├── DTO/
│   ├── Contracts/
│   └── Services/
├── Domain/
│   ├── Entities/
│   ├── ValueObjects/
│   ├── Events/
│   ├── Contracts/
│   ├── Services/
│   └── Exceptions/
├── Infrastructure/
│   ├── Models/
│   ├── Repositories/
│   ├── Persistence/
│   └── Integrations/
├── Presentation/
│   ├── Http/
│   │   ├── Controllers/
│   │   ├── Requests/
│   │   └── Resources/
│   └── Console/
├── Database/
│   ├── Migrations/
│   ├── Factories/
│   └── Seeders/
├── Providers/
├── Routes/
├── Tests/
│   ├── Unit/
│   ├── Feature/
│   └── Integration/
└── README.md
```

Struktur tersebut adalah referensi, bukan kewajiban membuat folder kosong. Module kecil boleh dimulai minimal dan tumbuh ketika responsibility muncul.

## Contoh Minimal

```text
Role/
├── Application/
│   └── CreateRole.php
├── Domain/
│   └── Role.php
├── Infrastructure/
│   └── EloquentRoleRepository.php
├── Presentation/
│   └── Http/
│       └── CreateRoleController.php
└── README.md
```

## Namespace

Contoh namespace:

```php
namespace App\Module\AccessControl\Role\Application\Actions;
```

## Service Provider Module

Module dapat memiliki provider sendiri sebagai composition root lokal.

```php
final class RoleServiceProvider extends ServiceProvider
{
    public function register(): void
    {
        $this->app->bind(
            RoleRepository::class,
            EloquentRoleRepository::class,
        );
    }

    public function boot(): void
    {
        // route, migration, policy, event registration bila diperlukan
    }
}
```

`register()` digunakan untuk binding dependency. `boot()` digunakan untuk bootstrap resource framework. Business logic tidak boleh ditempatkan di provider.

## Ownership

Setiap module memiliki business behavior dan persistence yang menjadi tanggung jawabnya. Module lain tidak boleh mengimpor model Infrastructure secara langsung.