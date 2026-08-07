from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID

from starterpython.modules.users.application.ports import UserUnitOfWork
from starterpython.modules.users.domain.entities import User


class UserAlreadyExists(RuntimeError):
    """Raised when creating a user with an existing email."""


@dataclass(frozen=True, slots=True)
class CreateUserCommand:
    email: str
    name: str


@dataclass(frozen=True, slots=True)
class CreateUserResult:
    id: UUID
    email: str
    name: str


class CreateUserHandler:
    def __init__(self, uow: UserUnitOfWork) -> None:
        self._uow = uow

    async def __call__(self, command: CreateUserCommand) -> CreateUserResult:
        normalized_email = command.email.strip().lower()
        if await self._uow.users.get_by_email(normalized_email) is not None:
            raise UserAlreadyExists(f"User with email {normalized_email!r} already exists.")

        user = User.create(email=normalized_email, name=command.name)

        try:
            await self._uow.users.add(user)
            await self._uow.commit()
        except Exception:
            await self._uow.rollback()
            raise

        return CreateUserResult(id=user.id, email=user.email, name=user.name)
