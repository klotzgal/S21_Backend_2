from datetime import tzinfo
from zoneinfo import ZoneInfo

from pydantic import field_validator
from pydantic_core.core_schema import ValidationInfo
from pydantic_settings import BaseSettings
from sqlalchemy import URL


class Settings(BaseSettings):
    LOG_LEVEL: str = "INFO"
    APP_NAME: str = "shop-service"
    LOG_PATH: str = "/tmp/logs/log.log"

    # database setup
    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: int | str = 5433
    POSTGRES_USER: str = "123"
    POSTGRES_PASSWORD: str = "123"
    POSTGRES_DB: str = "shop-service-test"
    POSTGRES_SCHEMA: str = "public"
    SQLALCHEMY_DATABASE_URI: URL | None = None

    DEFAULT_TIMEZONE: tzinfo | str = "Europe/Moscow"
    DEFAULT_ENCODING: str = "utf-8"

    @field_validator("DEFAULT_TIMEZONE")
    @classmethod
    def assemble_timezone(cls, v: str, _) -> ZoneInfo:
        return ZoneInfo(v)

    @field_validator("SQLALCHEMY_DATABASE_URI")
    @classmethod
    def assemble_db_connection(cls, v: str | None, values: ValidationInfo) -> URL:
        if isinstance(v, str):
            return v
        return URL.create(
            drivername="postgresql+asyncpg",
            username=values.data.get("POSTGRES_USER"),
            password=values.data.get("POSTGRES_PASSWORD"),
            host=values.data.get("POSTGRES_HOST"),
            port=values.data.get("POSTGRES_PORT"),
            database=values.data.get("POSTGRES_DB"),
        )


settings = Settings()  # type: ignore
