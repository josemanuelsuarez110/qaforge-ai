from sqlalchemy.orm import Session
from app.models.report import Report
from app.schemas.report import ReportCreate
from datetime import datetime

class ReportService:
    def __init__(self, db: Session):
        self.db = db

    def create_report(self, report: ReportCreate, test_run_id: int):
        db_report = Report(
            title=report.title,
            content=report.content,
            created_at=datetime.utcnow(),
            test_run_id=test_run_id
        )
        self.db.add(db_report)
        self.db.commit()
        self.db.refresh(db_report)
        return db_report

    def get_reports(self, skip: int = 0, limit: int = 100):
        return self.db.query(Report).offset(skip).limit(limit).all()

    def get_report(self, report_id: int):
        return self.db.query(Report).filter(Report.id == report_id).first()