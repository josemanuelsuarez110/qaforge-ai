from fastapi import FastAPI
from .authentication import get_current_active_user
from .rate_limit import rate_limit_middleware
from .logging import logging_middleware

def setup_middlewares(app: FastAPI):
    app.middleware("http")(rate_limit_middleware)
    app.middleware("http")(logging_middleware)