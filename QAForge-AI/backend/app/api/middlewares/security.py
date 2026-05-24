from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

security = HTTPBearer()

async def verify_token(request: Request, credentials: HTTPAuthorizationCredentials):
    token = credentials.credentials
    if not token:
        raise HTTPException(status_code=401, detail="Invalid token")
    # Add token verification logic here