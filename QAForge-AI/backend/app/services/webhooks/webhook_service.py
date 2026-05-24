from sqlalchemy.orm import Session
from datetime import datetime
from typing import List, Optional
from ..models.webhook import Webhook
from ..schemas.webhook import WebhookCreate

class WebhookService:
    def __init__(self, db: Session):
        self.db = db

    def create_webhook(self, webhook: WebhookCreate, user_id: int):
        db_webhook = Webhook(
            name=webhook.name,
            description=webhook.description,
            url=webhook.url,
            method=webhook.method,
            headers=webhook.headers,
            user_id=user_id,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )
        self.db.add(db_webhook)
        self.db.commit()
        self.db.refresh(db_webhook)
        return db_webhook

    def get_webhook(self, webhook_id: int, user_id: int):
        return self.db.query(Webhook).filter(Webhook.id == webhook_id, Webhook.user_id == user_id).first()

    def get_webhooks(self, skip: int = 0, limit: int = 100, user_id: int = None):
        query = self.db.query(Webhook)
        if user_id is not None:
            query = query.filter(Webhook.user_id == user_id)
        return query.offset(skip).limit(limit).all()

    def update_webhook(self, webhook_id: int, webhook: WebhookCreate, user_id: int):
        db_webhook = self.get_webhook(webhook_id, user_id)
        if db_webhook:
            db_webhook.name = webhook.name
            db_webhook.description = webhook.description
            db_webhook.url = webhook.url
            db_webhook.method = webhook.method
            db_webhook.headers = webhook.headers
            db_webhook.updated_at = datetime.utcnow()
            self.db.commit()
            self.db.refresh(db_webhook)
        return db_webhook

    def delete_webhook(self, webhook_id: int, user_id: int):
        db_webhook = self.get_webhook(webhook_id, user_id)
        if db_webhook:
            self.db.delete(db_webhook)
            self.db.commit()
        return db_webhook
