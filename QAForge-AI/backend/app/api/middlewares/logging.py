from fastapi import Request, Response
from fastapi.middleware import Middleware
from app.core.logging import audit_logger

async def logging_middleware(request: Request, call_next):
    audit_logger.info(f"Request: {request.method} {request.url}")
    response = await call_next(request)
    audit_logger.info(f"Response: {response.status_code}")
    return response