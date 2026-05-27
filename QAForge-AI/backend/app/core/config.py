from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "QAForge AI"
    database_url: str = "postgresql://postgres:AngelitSecure232723@db.rpgzketjnpvstunrcbxv.supabase.co:5432/postgres?sslmode=require"
    sqlalchemy_database_url: str = "postgresql://postgres:AngelitSecure232723@db.rpgzketjnpvstunrcbxv.supabase.co:5432/postgres?sslmode=require"
    secret_key: str = "your-secret-key"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    class Config:
        env_file = ".env"

settings = Settings()
