from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    LOGGING_FORMAT: str
    DISCINFO_NAME: str
    WIITDB_NAME: str
    ASSETS_DIR: str


settings = Settings()
