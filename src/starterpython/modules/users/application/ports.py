from __future__ import annotations

from typing import Protocol

from starterpython.modules.users.domain.repositories import UserRepository


class UserUnitOfWork(Protocol):
    users: UserRepository

    async def commit(self) -> None: ...

    async def rollback(self) -> None: ...
