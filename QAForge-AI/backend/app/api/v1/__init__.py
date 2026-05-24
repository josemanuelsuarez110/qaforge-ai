from fastapi import APIRouter
from .users import users_router
from .projects import projects_router
from .test_runs import test_runs_router
from .reports import reports_router
from .webhooks import webhooks_router
from .ai import ai_router

router = APIRouter()

router.include_router(users_router.router, prefix="/users", tags=["users"])
router.include_router(projects_router.router, prefix="/projects", tags=["projects"])
router.include_router(test_runs_router.router, prefix="/test-runs", tags=["test-runs"])
router.include_router(reports_router.router, prefix="/reports", tags=["reports"])
router.include_router(webhooks_router.router, prefix="/webhooks", tags=["webhooks"])
router.include_router(ai_router.router, prefix="/ai", tags=["ai"])