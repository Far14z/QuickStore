from pydantic.v1 import BaseSettings

"""
This class is responsible for loading the application settings from the .env file.
"""
class Settings(BaseSettings):

    APP_HOST: str
    APP_PORT: int
    DATABASE_URL: str
    DATABASE_NAME: str

    class Config:
        env_file = "app/.env"
        env_file_encoding = "utf-8"

# Create an instance of the Settings class
settings = Settings()