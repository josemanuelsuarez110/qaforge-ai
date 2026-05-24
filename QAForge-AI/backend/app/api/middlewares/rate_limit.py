from fastapi import Request, HTTPException
from fastapi.middleware import Middleware
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

limiter = Limiter(key_func=get_remote_address)

async def rate_limit_middleware(request: Request, call_next):
    try:
        await limiter.check(request)
        response = await call_next(request)
        return response
    except RateLimitExceeded as e:
        raise HTTPException(status_code=429, detail=str(e))