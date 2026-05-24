from fastapi import FastAPI
from app.api.v1.router import router as api_router
from app.core.database import engine
from app.models import Base

app = FastAPI(title="QAForge AI")

# Create tables
Base.metadata.create_all(bind=engine)

# Include API router
app.include_router(api_router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"message": "Welcome to QAForge AI"}