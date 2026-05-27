import logging
import sys
from typing import Optional
from pydantic import BaseSettings
from app.core.config import settings

class LoggingSettings(BaseSettings):
    LOG_LEVEL: str = "INFO"
    LOG_FORMAT: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    LOG_FILE: Optional[str] = None

    class Config:
        env_prefix = "LOG_"

logging_settings = LoggingSettings()

def setup_logging():
    """Configure application logging"""
    log_level = getattr(logging, logging_settings.LOG_LEVEL.upper(), logging.INFO)

    logging.basicConfig(
        level=log_level,
        format=logging_settings.LOG_FORMAT,
        handlers=[
            logging.StreamHandler(sys.stdout),
        ]
    )

    if logging_settings.LOG_FILE:
        file_handler = logging.FileHandler(logging_settings.LOG_FILE)
        file_handler.setFormatter(logging.Formatter(logging_settings.LOG_FORMAT))
        logging.getLogger().addHandler(file_handler)

    # Suppress logs from specific libraries
    logging.getLogger("uvicorn").setLevel(logging.WARNING)
    logging.getLogger("uvicorn.error").setLevel(logging.ERROR)
    logging.getLogger("sqlalchemy").setLevel(logging.WARNING)

    logger = logging.getLogger(__name__)
    logger.info("Logging configured successfully")
    return logger

logger = setup_logging()