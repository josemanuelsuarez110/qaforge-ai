import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to QAForge AI"}

def test_rate_limiting():
    # Make multiple requests to test rate limiting
    for _ in range(5):
        response = client.get("/")
        assert response.status_code == 200

    # The 6th request should be rate limited
    response = client.get("/")
    assert response.status_code == 429