import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_user():
    response = client.post(
        "/api/v1/users/",
        json={"email": "testuser@example.com", "password": "testpassword"}
    )
    assert response.status_code == 200
    assert response.json()["email"] == "testuser@example.com"

def test_get_users():
    # First create a test user
    client.post(
        "/api/v1/users/",
        json={"email": "testuser2@example.com", "password": "testpassword"}
    )

    # Then get all users
    response = client.get("/api/v1/users/")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_get_user_me():
    # First create and login a test user
    client.post(
        "/api/v1/users/",
        json={"email": "testuser3@example.com", "password": "testpassword"}
    )
    login_response = client.post(
        "/api/v1/auth/token",
        data={"username": "testuser3@example.com", "password": "testpassword"}
    )
    token = login_response.json()["access_token"]

    # Then get the current user
    response = client.get(
        "/api/v1/users/me",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    assert response.json()["email"] == "testuser3@example.com"