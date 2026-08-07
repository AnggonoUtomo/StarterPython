from __future__ import annotations

from typing import Protocol

from starterpython.modules.users.domain.entities import User


class UserRepository(Protocol):
    async def add(self, user: User) -> None: ...

    async def get_by_email(self, email: str) -> User | None: ...
