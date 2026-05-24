from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class StorageBase(BaseModel):
    name: str
    description: str
    file_path: str
    file_type: str

class StorageCreate(StorageBase):
    pass

class Storage(StorageBase):
    id: int
    user_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
