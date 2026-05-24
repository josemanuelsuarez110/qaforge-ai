from fastapi import APIRouter
from .reports_router import router

router = APIRouter()
router.include_router(router, prefix="/reports", tags=["reports"])