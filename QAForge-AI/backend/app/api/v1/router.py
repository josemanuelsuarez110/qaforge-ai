from fastapi import APIRouter
from app.api.v1.users import users_router
from app.api.v1.projects import projects_router
from app.api.v1.test_runs import test_runs_router
from app.api.v1.reports import reports_router
from app.api.v1.webhooks import webhooks_router
from app.api.v1.ai import ai_router

router = APIRouter()

router.include_router(users_router.router, prefix="/users", tags=["users"])
router.include_router(projects_router.router, prefix="/projects", tags=["projects"])
router.include_router(test_runs_router.router, prefix="/test-runs", tags=["test-runs"])
router.include_router(reports_router.router, prefix="/reports", tags=["reports"])
router.include_router(webhooks_router.router, prefix="/webhooks", tags=["webhooks"])
router.include_router(ai_router.router, prefix="/ai", tags=["ai"])