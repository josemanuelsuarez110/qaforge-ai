from fastapi import APIRouter
from .users_router import router

router = APIRouter()
router.include_router(router, prefix="/users", tags=["users"])