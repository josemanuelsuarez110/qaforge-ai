from fastapi import APIRouter, Depends, HTTPException, status
from ...core.security import get_current_user
from ...core.database import get_db
from ...models.test_run import TestRun
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/")
async def create_test_run(project_id: int, status: str, results: str, current_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    test_run = TestRun(project_id=project_id, status=status, results=results, user_id=current_user["sub"])
    db.add(test_run)
    db.commit()
    db.refresh(test_run)
    return test_run

@router.get("/")
async def read_test_runs(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    test_runs = db.query(TestRun).offset(skip).limit(limit).all()
    return test_runs

@router.get("/{test_run_id}")
async def read_test_run(test_run_id: int, db: Session = Depends(get_db)):
    test_run = db.query(TestRun).filter(TestRun.id == test_run_id).first()
    if not test_run:
        raise HTTPException(status_code=404, detail="Test run not found")
    return test_run

@router.put("/{test_run_id}")
async def update_test_run(test_run_id: int, status: str, results: str, db: Session = Depends(get_db)):
    test_run = db.query(TestRun).filter(TestRun.id == test_run_id).first()
    if not test_run:
        raise HTTPException(status_code=404, detail="Test run not found")
    test_run.status = status
    test_run.results = results
    db.commit()
    db.refresh(test_run)
    return test_run

@router.delete("/{test_run_id}")
async def delete_test_run(test_run_id: int, db: Session = Depends(get_db)):
    test_run = db.query(TestRun).filter(TestRun.id == test_run_id).first()
    if not test_run:
        raise HTTPException(status_code=404, detail="Test run not found")
    db.delete(test_run)
    db.commit()
    return {"message": "Test run deleted successfully"}