from pydantic import BaseModel

class WebhookBase(BaseModel):
    url: str
    secret: str

class WebhookCreate(WebhookBase):
    pass

class Webhook(WebhookBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True