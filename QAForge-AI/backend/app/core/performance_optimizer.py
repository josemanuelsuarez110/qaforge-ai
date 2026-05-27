import time
from functools import wraps
from typing import Callable, Any, TypeVar, ParamSpec, Optional
import logging
import time
from fastapi import Request, Response
from app.core.logging import logger
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware

P = ParamSpec('P')
T = TypeVar('T')

class PerformanceOptimizer:
    def __init__(self):
        self.cache = {}
        self.query_count = 0
        self.query_time = 0
        self.response_time = 0
        self.response_count = 0

    def cache_result(self, max_age: int = 300):
        def decorator(func: Callable[P, T]) -> Callable[P, T]:
            @wraps(func)
            def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
                cache_key = f"{func.__name__}_{args}_{kwargs}"
                if cache_key in self.cache and time.time() - self.cache[cache_key]['timestamp'] < max_age:
                    logger.info(f"Cache hit for {func.__name__}")
                    return self.cache[cache_key]['result']

                result = func(*args, **kwargs)
                self.cache[cache_key] = {
                    'result': result,
                    'timestamp': time.time()
                }
                logger.info(f"Cache miss for {func.__name__}, result cached")
                return result
            return wrapper
        return decorator

    def log_query_performance(self, func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()

            self.query_count += 1
            self.query_time += (end_time - start_time)

            logger.info(f"Query {func.__name__} executed in {end_time - start_time:.4f} seconds")
            return result
        return wrapper

    def log_response_time(self, request: Request, call_next: Callable) -> Response:
        start_time = time.time()
        response = call_next(request)
        end_time = time.time()

        self.response_count += 1
        self.response_time += (end_time - start_time)

        logger.info(f"Request {request.method} {request.url.path} processed in {end_time - start_time:.4f} seconds")
        return response

    def get_performance_metrics(self) -> dict:
        return {
            'query_count': self.query_count,
            'total_query_time': self.query_time,
            'average_query_time': self.query_time / self.query_count if self.query_count > 0 else 0,
            'response_count': self.response_count,
            'total_response_time': self.response_time,
            'average_response_time': self.response_time / self.response_count if self.response_count > 0 else 0
        }

    def add_performance_middleware(self, app):
        """Add performance optimization middleware to the FastAPI app"""
        # Add GZip middleware for response compression
        app.add_middleware(GZipMiddleware, minimum_size=1000)

        # Add HTTPS redirect middleware if not in development
        if not app.debug:
            app.add_middleware(HTTPSRedirectMiddleware)

        # Add trusted host middleware for security
        app.add_middleware(
            TrustedHostMiddleware,
            allowed_hosts=["example.com", "*.example.com"]
        )

        # Add response time logging middleware
        app.middleware("http")(self.log_response_time)

performance_optimizer = PerformanceOptimizer()
