from __future__ import annotations

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from starterpython.modules.users.domain.entities import User
from starterpython.modules.users.infrastructure.persistence.models import UserModel


class SQLAlchemyUserRepository:
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def add(self, user: User) -> None:
        self._session.add(UserModel(id=user.id, email=user.email, name=user.name))

    async def get_by_email(self, email: str) -> User | None:
        statement = select(UserModel).where(UserModel.email == email)
        model = await self._session.scalar(statement)
        if model is None:
            return None
        return User(id=model.id, email=model.email, name=model.name)
