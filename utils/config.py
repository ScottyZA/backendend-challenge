from pydantic import BaseSettings


class Settings(BaseSettings):
    database_url: str = "postgresql://tier:tier@db:5432/url_api"
    base_short_url: str = "https://tier.app/"


def get_settings() -> Settings:
    return Settings()
