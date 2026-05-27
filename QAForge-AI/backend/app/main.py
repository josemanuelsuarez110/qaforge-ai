from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.api.v1.router import router as api_router
from app.core.database import engine
from app.models import Base
from app.core.health_monitor import health_monitor

app = FastAPI(title="QAForge AI")

# Create tables
Base.metadata.create_all(bind=engine)

# Include API router
app.include_router(api_router, prefix="/api/v1")

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    status = await health_monitor.check_database_health()
    if status["status"] == "healthy":
        return JSONResponse(
            status_code=200,
            content={"status": "healthy", "database": "healthy"}
        )
    else:
        return JSONResponse(
            status_code=503,
            content={"status": "unhealthy", "database": "unhealthy", "error": status["error"]}
        )

@app.get("/ready")
async def readiness_check():
    """Readiness check endpoint"""
    return JSONResponse(
        status_code=200,
        content={"status": "ready"}
    )

@app.get("/")
def read_root():
    return {"message": "Welcome to QAForge AI"}