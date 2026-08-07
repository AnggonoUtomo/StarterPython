from fastapi import APIRouter

from starterpython.core.config import get_settings
from starterpython.modules.system.presentation.schemas import HealthResponse

router = APIRouter(tags=["system"])


@router.get("/health", response_model=HealthResponse)
async def health() -> HealthResponse:
    settings = get_settings()
    return HealthResponse(service=settings.app_name)
