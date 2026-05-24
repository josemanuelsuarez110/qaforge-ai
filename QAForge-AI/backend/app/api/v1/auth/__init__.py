from fastapi import APIRouter
from .auth_router import router

router = APIRouter()
router.include_router(router, prefix="/auth", tags=["auth"])