from fastapi import FastAPI

from starterpython.bootstrap.lifecycle import lifespan
from starterpython.bootstrap.routes import api_router
from starterpython.core.config import get_settings
from starterpython.core.exceptions import register_exception_handlers
from starterpython.core.logging import configure_logging


def create_app() -> FastAPI:
    settings = get_settings()
    configure_logging(settings.log_level)

    application = FastAPI(
        title=settings.app_name,
        debug=settings.debug,
        version="0.1.0",
        lifespan=lifespan,
    )
    application.include_router(api_router, prefix=settings.api_prefix)
    register_exception_handlers(application)
    return application


app = create_app()
