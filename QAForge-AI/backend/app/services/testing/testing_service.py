from sqlalchemy.orm import Session
from app.models.test_run import TestRun
from app.schemas.test_run import TestRunCreate
from datetime import datetime

class TestingService:
    def __init__(self, db: Session):
        self.db = db

    def create_test_run(self, test_run: TestRunCreate, project_id: int):
        db_test_run = TestRun(
            name=test_run.name,
            status=test_run.status,
            created_at=datetime.utcnow(),
            project_id=project_id
        )
        self.db.add(db_test_run)
        self.db.commit()
        self.db.refresh(db_test_run)
        return db_test_run

    def get_test_runs(self, skip: int = 0, limit: int = 100):
        return self.db.query(TestRun).offset(skip).limit(limit).all()

    def get_test_run(self, test_run_id: int):
        return self.db.query(TestRun).filter(TestRun.id == test_run_id).first()