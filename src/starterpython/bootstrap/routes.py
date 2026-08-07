from fastapi import APIRouter

from starterpython.modules.system.presentation.routes import router as system_router
from starterpython.modules.users.presentation.routes import router as users_router

api_router = APIRouter()
api_router.include_router(system_router)
api_router.include_router(users_router)
