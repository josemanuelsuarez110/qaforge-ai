from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime
from app.core.database import get_db
from app.schemas.test_run import TestRun, TestRunCreate
from app.models.test_run import TestRun as TestRunModel
from app.core.security import get_current_user

router = APIRouter()

@router.post("/", response_model=TestRun)
def create_test_run(test_run: TestRunCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_test_run = TestRunModel(**test_run.dict(), created_at=datetime.utcnow())
    db.add(db_test_run)
    db.commit()
    db.refresh(db_test_run)
    return db_test_run

@router.get("/", response_model=List[TestRun])
def read_test_runs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    test_runs = db.query(TestRunModel).offset(skip).limit(limit).all()
    return test_runs

@router.get("/{test_run_id}", response_model=TestRun)
def read_test_run(test_run_id: int, db: Session = Depends(get_db)):
    test_run = db.query(TestRunModel).filter(TestRunModel.id == test_run_id).first()
    if test_run is None:
        raise HTTPException(status_code=404, detail="Test run not found")
    return test_run