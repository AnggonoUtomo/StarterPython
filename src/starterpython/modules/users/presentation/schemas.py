from uuid import UUID

from pydantic import BaseModel, Field


class CreateUserRequest(BaseModel):
    email: str = Field(min_length=3, max_length=320)
    name: str = Field(min_length=1, max_length=150)


class UserResponse(BaseModel):
    id: UUID
    email: str
    name: str
