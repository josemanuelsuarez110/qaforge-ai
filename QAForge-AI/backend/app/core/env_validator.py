import os
from typing import Dict, Any
from pydantic import BaseSettings, PostgresDsn, AnyHttpUrl, validator

class Settings(BaseSettings):
    DATABASE_URL: PostgresDsn
    SQLALCHEMY_DATABASE_URL: PostgresDsn
    SUPABASE_URL: AnyHttpUrl
    SUPABASE_KEY: str

    class Config:
        env_file = ".env"

    @validator("SUPABASE_KEY")
    def validate_supabase_key(cls, v: str) -> str:
        if len(v) < 32:
            raise ValueError("Supabase key must be at least 32 characters long")
        return v

def validate_environment_variables() -> Dict[str, Any]:
    try:
        settings = Settings()
        return {
            "status": "success",
            "message": "All environment variables are valid",
            "variables": {
                "DATABASE_URL": str(settings.DATABASE_URL),
                "SQLALCHEMY_DATABASE_URL": str(settings.SQLALCHEMY_DATABASE_URL),
                "SUPABASE_URL": str(settings.SUPABASE_URL),
                "SUPABASE_KEY": "*****"  # Mask the key for security
            }
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Environment validation failed: {str(e)}",
            "variables": {}
        }