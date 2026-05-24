from sqlalchemy.orm import Session
from app.models.notification import Notification
from app.schemas.notification import NotificationCreate
from datetime import datetime

class NotificationService:
    def __init__(self, db: Session):
        self.db = db

    def create_notification(self, notification: NotificationCreate, user_id: int):
        db_notification = Notification(
            message=notification.message,
            created_at=datetime.utcnow(),
            user_id=user_id
        )
        self.db.add(db_notification)
        self.db.commit()
        self.db.refresh(db_notification)
        return db_notification

    def get_notifications(self, skip: int = 0, limit: int = 100):
        return self.db.query(Notification).offset(skip).limit(limit).all()

    def get_notification(self, notification_id: int):
        return self.db.query(Notification).filter(Notification.id == notification_id).first()