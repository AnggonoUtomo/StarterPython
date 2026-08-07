from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from starterpython.core.database import get_db_session
from starterpython.modules.users.application.create_user import (
    CreateUserCommand,
    CreateUserHandler,
    UserAlreadyExists,
)
from starterpython.modules.users.domain.entities import InvalidUser
from starterpython.modules.users.infrastructure.unit_of_work import SQLAlchemyUserUnitOfWork
from starterpython.modules.users.presentation.schemas import CreateUserRequest, UserResponse

router = APIRouter(prefix="/users", tags=["users"])


@router.post("", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(
    payload: CreateUserRequest,
    session: Annotated[AsyncSession, Depends(get_db_session)],
) -> UserResponse:
    handler = CreateUserHandler(SQLAlchemyUserUnitOfWork(session))

    try:
        result = await handler(CreateUserCommand(email=payload.email, name=payload.name))
    except UserAlreadyExists as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc)) from exc
    except InvalidUser as exc:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
            detail=str(exc),
        ) from exc

    return UserResponse(id=result.id, email=result.email, name=result.name)
