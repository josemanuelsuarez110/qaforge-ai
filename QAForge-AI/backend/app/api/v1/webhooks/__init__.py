from fastapi import APIRouter
from .webhooks_router import router

router = APIRouter()
router.include_router(router, prefix="/webhooks", tags=["webhooks"])