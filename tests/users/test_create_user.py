from __future__ import annotations

from uuid import uuid4

import pytest

from starterpython.modules.users.application.create_user import (
    CreateUserCommand,
    CreateUserHandler,
    UserAlreadyExists,
)
from starterpython.modules.users.domain.entities import User


class FakeUserRepository:
    def __init__(self) -> None:
        self.items: dict[str, User] = {}

    async def add(self, user: User) -> None:
        self.items[user.email] = user

    async def get_by_email(self, email: str) -> User | None:
        return self.items.get(email)


class FakeUserUnitOfWork:
    def __init__(self) -> None:
        self.users = FakeUserRepository()
        self.committed = False
        self.rolled_back = False

    async def commit(self) -> None:
        self.committed = True

    async def rollback(self) -> None:
        self.rolled_back = True


async def test_create_user_normalizes_and_commits() -> None:
    uow = FakeUserUnitOfWork()
    handler = CreateUserHandler(uow)

    result = await handler(CreateUserCommand(email=" USER@Example.COM ", name=" Ino "))

    assert result.email == "user@example.com"
    assert result.name == "Ino"
    assert uow.committed is True
    assert uow.rolled_back is False
    assert await uow.users.get_by_email("user@example.com") is not None


async def test_create_user_rejects_duplicate_email() -> None:
    uow = FakeUserUnitOfWork()
    existing = User.create(email="user@example.com", name="Existing", user_id=uuid4())
    await uow.users.add(existing)
    handler = CreateUserHandler(uow)

    with pytest.raises(UserAlreadyExists):
        await handler(CreateUserCommand(email="USER@example.com", name="Another"))

    assert uow.committed is False
