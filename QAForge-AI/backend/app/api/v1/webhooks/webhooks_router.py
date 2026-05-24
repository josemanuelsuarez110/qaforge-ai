from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.core.database import get_db
from app.schemas.webhook import Webhook, WebhookCreate
from app.models.webhook import Webhook as WebhookModel
from app.core.security import get_current_user

router = APIRouter()

@router.post("/", response_model=Webhook)
def create_webhook(webhook: WebhookCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_webhook = WebhookModel(**webhook.dict(), owner_id=current_user.id)
    db.add(db_webhook)
    db.commit()
    db.refresh(db_webhook)
    return db_webhook

@router.get("/", response_model=List[Webhook])
def read_webhooks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    webhooks = db.query(WebhookModel).offset(skip).limit(limit).all()
    return webhooks

@router.get("/{webhook_id}", response_model=Webhook)
def read_webhook(webhook_id: int, db: Session = Depends(get_db)):
    webhook = db.query(WebhookModel).filter(WebhookModel.id == webhook_id).first()
    if webhook is None:
        raise HTTPException(status_code=404, detail="Webhook not found")
    return webhook