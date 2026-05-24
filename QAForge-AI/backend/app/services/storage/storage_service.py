from sqlalchemy.orm import Session
from app.models.storage import Storage
from app.schemas.storage import StorageCreate
from datetime import datetime

class StorageService:
    def __init__(self, db: Session):
        self.db = db

    def create_storage_item(self, storage_item: StorageCreate, user_id: int):
        db_storage_item = Storage(
            file_name=storage_item.file_name,
            file_path=storage_item.file_path,
            created_at=datetime.utcnow(),
            user_id=user_id
        )
        self.db.add(db_storage_item)
        self.db.commit()
        self.db.refresh(db_storage_item)
        return db_storage_item

    def get_storage_items(self, skip: int = 0, limit: int = 100):
        return self.db.query(Storage).offset(skip).limit(limit).all()

    def get_storage_item(self, storage_id: int):
        return self.db.query(Storage).filter(Storage.id == storage_id).first()