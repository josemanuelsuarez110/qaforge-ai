from fastapi import APIRouter
from .test_runs_router import router

router = APIRouter()
router.include_router(router, prefix="/test-runs", tags=["test-runs"])