from fastapi import APIRouter, Depends, HTTPException, status
from ...core.security import get_current_user
from ...core.database import get_db
from ...models.user import User
from sqlalchemy.orm import Session

router = APIRouter()

@router.get("/me")
async def read_users_me(current_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == current_user["sub"]).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.get("/{username}")
async def read_user(username: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == username).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user