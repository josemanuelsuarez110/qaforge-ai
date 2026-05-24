from sqlalchemy.orm import Session
from app.models.project import Project
from app.schemas.project import ProjectCreate

class ProjectService:
    def __init__(self, db: Session):
        self.db = db

    def create_project(self, project: ProjectCreate, owner_id: int):
        db_project = Project(**project.dict(), owner_id=owner_id)
        self.db.add(db_project)
        self.db.commit()
        self.db.refresh(db_project)
        return db_project

    def get_projects(self, skip: int = 0, limit: int = 100):
        return self.db.query(Project).offset(skip).limit(limit).all()

    def get_project(self, project_id: int):
        return self.db.query(Project).filter(Project.id == project_id).first()