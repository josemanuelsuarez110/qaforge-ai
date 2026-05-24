from sqlalchemy.orm import Session
from app.models.queue import Queue
from app.schemas.queue import QueueCreate
from datetime import datetime

class QueueService:
    def __init__(self, db: Session):
        self.db = db

    def create_queue_item(self, queue_item: QueueCreate, user_id: int):
        db_queue_item = Queue(
            task=queue_item.task,
            status=queue_item.status,
            created_at=datetime.utcnow(),
            user_id=user_id
        )
        self.db.add(db_queue_item)
        self.db.commit()
        self.db.refresh(db_queue_item)
        return db_queue_item

    def get_queue_items(self, skip: int = 0, limit: int = 100):
        return self.db.query(Queue).offset(skip).limit(limit).all()

    def get_queue_item(self, queue_id: int):
        return self.db.query(Queue).filter(Queue.id == queue_id).first()