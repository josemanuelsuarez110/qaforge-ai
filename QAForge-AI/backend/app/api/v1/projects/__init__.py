from fastapi import APIRouter
from .projects_router import router

router = APIRouter()
router.include_router(router, prefix="/projects", tags=["projects"])