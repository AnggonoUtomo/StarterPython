from __future__ import annotations

import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from starterpython.core.database import Base, engine
from starterpython.modules.users.domain.entities import User
from starterpython.modules.users.infrastructure.persistence.models import UserModel  # noqa: F401
from starterpython.modules.users.infrastructure.repositories import SQLAlchemyUserRepository

pytestmark = pytest.mark.integration


@pytest.fixture
async def db_session() -> AsyncSession:
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.drop_all)
        await connection.run_sync(Base.metadata.create_all)

    async with AsyncSession(engine, expire_on_commit=False) as session:
        yield session

    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.drop_all)


async def test_repository_round_trip(db_session: AsyncSession) -> None:
    repository = SQLAlchemyUserRepository(db_session)
    user = User.create(email="repo@example.com", name="Repository Test")

    await repository.add(user)
    await db_session.commit()

    loaded = await repository.get_by_email("repo@example.com")

    assert loaded == user
