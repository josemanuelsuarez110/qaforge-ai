from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class QueueBase(BaseModel):
    name: str
    description: str
    status: str

class QueueCreate(QueueBase):
    pass

class Queue(QueueBase):
    id: int
    user_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
