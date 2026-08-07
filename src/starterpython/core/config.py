from functools import lru_cache
from typing import Literal

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="",
        extra="ignore",
        case_sensitive=False,
    )

    app_name: str = Field(default="StarterPython", alias="APP_NAME")
    environment: Literal["local", "test", "staging", "production"] = Field(
        default="local", alias="APP_ENV"
    )
    debug: bool = Field(default=False, alias="APP_DEBUG")
    api_prefix: str = Field(default="/api/v1", alias="APP_API_PREFIX")
    log_level: str = Field(default="INFO", alias="APP_LOG_LEVEL")
    database_url: str = Field(alias="DATABASE_URL")
    redis_url: str = Field(alias="REDIS_URL")


@lru_cache
def get_settings() -> Settings:
    return Settings()
