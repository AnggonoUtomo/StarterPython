from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from starterpython.core.cache import redis_client
from starterpython.core.database import engine


@asynccontextmanager
async def lifespan(_app: FastAPI) -> AsyncIterator[None]:
    yield
    await redis_client.aclose()
    await engine.dispose()
