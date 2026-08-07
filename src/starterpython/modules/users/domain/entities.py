from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID, uuid4


class InvalidUser(ValueError):
    """Raised when user domain invariants are violated."""


@dataclass(frozen=True, slots=True)
class User:
    id: UUID
    email: str
    name: str

    @classmethod
    def create(cls, *, email: str, name: str, user_id: UUID | None = None) -> User:
        normalized_email = email.strip().lower()
        normalized_name = name.strip()

        if not normalized_email or "@" not in normalized_email:
            raise InvalidUser("A valid email is required.")
        if not normalized_name:
            raise InvalidUser("Name is required.")

        return cls(id=user_id or uuid4(), email=normalized_email, name=normalized_name)
