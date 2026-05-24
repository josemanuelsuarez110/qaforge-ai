from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "QAForge AI"
    database_url: str = "postgresql://postgres:password@localhost:5432/qaforge"
    secret_key: str = "your-secret-key"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    class Config:
        env_file = ".env"

settings = Settings()