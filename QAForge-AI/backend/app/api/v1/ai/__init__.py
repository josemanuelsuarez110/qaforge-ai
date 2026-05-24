from fastapi import APIRouter
from .ai_router import router

router = APIRouter()
router.include_router(router, prefix="/ai", tags=["ai"])