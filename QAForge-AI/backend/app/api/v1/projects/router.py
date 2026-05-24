from fastapi import APIRouter, Depends, HTTPException, status
from ...core.security import get_current_user
from ...core.database import get_db
from ...models.project import Project
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/")
async def create_project(name: str, description: str, current_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    project = Project(name=name, description=description, owner_id=current_user["sub"])
    db.add(project)
    db.commit()
    db.refresh(project)
    return project

@router.get("/")
async def read_projects(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    projects = db.query(Project).offset(skip).limit(limit).all()
    return projects

@router.get("/{project_id}")
async def read_project(project_id: int, db: Session = Depends(get_db)):
    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project

@router.put("/{project_id}")
async def update_project(project_id: int, name: str, description: str, db: Session = Depends(get_db)):
    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    project.name = name
    project.description = description
    db.commit()
    db.refresh(project)
    return project

@router.delete("/{project_id}")
async def delete_project(project_id: int, db: Session = Depends(get_db)):
    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    db.delete(project)
    db.commit()
    return {"message": "Project deleted successfully"}