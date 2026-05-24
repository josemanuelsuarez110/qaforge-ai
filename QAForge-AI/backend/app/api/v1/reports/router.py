from fastapi import APIRouter, Depends, HTTPException, status
from ...core.security import get_current_user
from ...core.database import get_db
from ...models.report import Report
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/")
async def create_report(test_run_id: int, content: str, current_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    report = Report(test_run_id=test_run_id, content=content, user_id=current_user["sub"])
    db.add(report)
    db.commit()
    db.refresh(report)
    return report

@router.get("/")
async def read_reports(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    reports = db.query(Report).offset(skip).limit(limit).all()
    return reports

@router.get("/{report_id}")
async def read_report(report_id: int, db: Session = Depends(get_db)):
    report = db.query(Report).filter(Report.id == report_id).first()
    if not report:
        raise HTTPException(status_code=404, detail="Report not found")
    return report

@router.put("/{report_id}")
async def update_report(report_id: int, content: str, db: Session = Depends(get_db)):
    report = db.query(Report).filter(Report.id == report_id).first()
    if not report:
        raise HTTPException(status_code=404, detail="Report not found")
    report.content = content
    db.commit()
    db.refresh(report)
    return report

@router.delete("/{report_id}")
async def delete_report(report_id: int, db: Session = Depends(get_db)):
    report = db.query(Report).filter(Report.id == report_id).first()
    if not report:
        raise HTTPException(status_code=404, detail="Report not found")
    db.delete(report)
    db.commit()
    return {"message": "Report deleted successfully"}