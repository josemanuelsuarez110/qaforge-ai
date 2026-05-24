from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime
from app.core.database import get_db
from app.schemas.report import Report, ReportCreate
from app.models.report import Report as ReportModel
from app.core.security import get_current_user

router = APIRouter()

@router.post("/", response_model=Report)
def create_report(report: ReportCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_report = ReportModel(**report.dict(), created_at=datetime.utcnow())
    db.add(db_report)
    db.commit()
    db.refresh(db_report)
    return db_report

@router.get("/", response_model=List[Report])
def read_reports(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    reports = db.query(ReportModel).offset(skip).limit(limit).all()
    return reports

@router.get("/{report_id}", response_model=Report)
def read_report(report_id: int, db: Session = Depends(get_db)):
    report = db.query(ReportModel).filter(ReportModel.id == report_id).first()
    if report is None:
        raise HTTPException(status_code=404, detail="Report not found")
    return report