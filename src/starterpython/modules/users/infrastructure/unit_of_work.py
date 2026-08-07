from sqlalchemy.ext.asyncio import AsyncSession

from starterpython.modules.users.infrastructure.repositories import SQLAlchemyUserRepository


class SQLAlchemyUserUnitOfWork:
    def __init__(self, session: AsyncSession) -> None:
        self._session = session
        self.users = SQLAlchemyUserRepository(session)

    async def commit(self) -> None:
        await self._session.commit()

    async def rollback(self) -> None:
        await self._session.rollback()
