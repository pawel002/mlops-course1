# settings.py
from pydantic_settings import BaseSettings
from pydantic import field_validator


class Settings(BaseSettings):
    ENVIRONMENT: str
    APP_NAME: str
    API_KEY: str

    @field_validator("ENVIRONMENT", mode="before")
    @classmethod
    def validate_environment(cls, value):
        if value is None:
            raise ValueError("ENVIRONMENT must be set")

        allowed = {"dev", "test", "prod"}
        if value not in allowed:
            raise ValueError(f"ENVIRONMENT must be one of: ({', '.join(allowed)}).")

        return value
