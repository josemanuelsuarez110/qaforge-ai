from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class TestRunBase(BaseModel):
    name: str
    status: str

class TestRunCreate(TestRunBase):
    pass

class TestRun(TestRunBase):
    id: int
    created_at: datetime
    project_id: int

    class Config:
        orm_mode = True