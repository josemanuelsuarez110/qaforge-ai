from fastapi import APIRouter, Depends, HTTPException, status
from ...core.security import get_current_user
from ...core.database import get_db
from ...models.webhook import Webhook
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/")
async def create_webhook(url: str, event_type: str, current_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    webhook = Webhook(url=url, event_type=event_type, user_id=current_user["sub"])
    db.add(webhook)
    db.commit()
    db.refresh(webhook)
    return webhook

@router.get("/")
async def read_webhooks(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    webhooks = db.query(Webhook).offset(skip).limit(limit).all()
    return webhooks

@router.get("/{webhook_id}")
async def read_webhook(webhook_id: int, db: Session = Depends(get_db)):
    webhook = db.query(Webhook).filter(Webhook.id == webhook_id).first()
    if not webhook:
        raise HTTPException(status_code=404, detail="Webhook not found")
    return webhook

@router.put("/{webhook_id}")
async def update_webhook(webhook_id: int, url: str, event_type: str, db: Session = Depends(get_db)):
    webhook = db.query(Webhook).filter(Webhook.id == webhook_id).first()
    if not webhook:
        raise HTTPException(status_code=404, detail="Webhook not found")
    webhook.url = url
    webhook.event_type = event_type
    db.commit()
    db.refresh(webhook)
    return webhook

@router.delete("/{webhook_id}")
async def delete_webhook(webhook_id: int, db: Session = Depends(get_db)):
    webhook = db.query(Webhook).filter(Webhook.id == webhook_id).first()
    if not webhook:
        raise HTTPException(status_code=404, detail="Webhook not found")
    db.delete(webhook)
    db.commit()
    return {"message": "Webhook deleted successfully"}