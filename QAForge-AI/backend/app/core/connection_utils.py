import os
from sqlalchemy import create_engine, pool
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

class DatabaseConnection:
    def __init__(self):
        self.database_url = os.getenv("DATABASE_URL")
        self.engine = self._create_engine()
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine, expire_on_commit=False)

    def _create_engine(self):
        if not self.database_url:
            raise ValueError("DATABASE_URL must be set in environment variables")
        return create_engine(
            self.database_url,
            pool_size=5,
            max_overflow=10,
            pool_timeout=30,
            pool_recycle=3600,
            pool_pre_ping=True
        )

    def get_session(self):
        return self.SessionLocal()

    def close_session(self, session):
        session.close()

database_connection = DatabaseConnection()