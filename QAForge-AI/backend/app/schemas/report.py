from pydantic import BaseModel
from datetime import datetime

class ReportBase(BaseModel):
    title: str
    content: str

class ReportCreate(ReportBase):
    pass

class Report(ReportBase):
    id: int
    created_at: datetime
    test_run_id: int

    class Config:
        orm_mode = True