from sqlalchemy.orm import Session
from app.models.supabase_models import User, Project, TestRun
from datetime import datetime

def seed_database(db: Session):
    # Create sample users
    user1 = User(
        email="user1@example.com",
        hashed_password="hashed_password1",
        is_active=True,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    user2 = User(
        email="user2@example.com",
        hashed_password="hashed_password2",
        is_active=True,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    db.add(user1)
    db.add(user2)
    db.commit()

    # Create sample projects
    project1 = Project(
        name="Project 1",
        description="Description for Project 1",
        owner_id=user1.id,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    project2 = Project(
        name="Project 2",
        description="Description for Project 2",
        owner_id=user2.id,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    db.add(project1)
    db.add(project2)
    db.commit()

    # Create sample test runs
    test_run1 = TestRun(
        project_id=project1.id,
        status="completed",
        started_at=datetime.utcnow(),
        completed_at=datetime.utcnow(),
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    test_run2 = TestRun(
        project_id=project2.id,
        status="in_progress",
        started_at=datetime.utcnow(),
        completed_at=None,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    db.add(test_run1)
    db.add(test_run2)
    db.commit()