import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_generate_report():
    # First create a test user and project
    user_response = client.post(
        "/api/v1/users/",
        json={"email": "reportuser@example.com", "password": "testpassword"}
    )
    user_id = user_response.json()["id"]

    project_response = client.post(
        "/api/v1/projects/",
        json={"name": "Test Project", "description": "Test Description"},
        headers={"Authorization": f"Bearer {user_id}"}
    )
    project_id = project_response.json()["id"]

    # Create a test run
    test_run_response = client.post(
        "/api/v1/test-runs/",
        json={"name": "Test Run", "status": "completed"},
        headers={"Authorization": f"Bearer {user_id}"}
    )
    test_run_id = test_run_response.json()["id"]

    # Generate a report
    report_response = client.post(
        "/api/v1/reports/",
        json={"title": "Test Report", "content": "Test Report Content"},
        headers={"Authorization": f"Bearer {user_id}"}
    )
    assert report_response.status_code == 200
    assert report_response.json()["title"] == "Test Report"
    assert report_response.json()["content"] == "Test Report Content"

def test_get_reports():
    # First create a test user and report
    user_response = client.post(
        "/api/v1/users/",
        json={"email": "reportuser2@example.com", "password": "testpassword"}
    )
    user_id = user_response.json()["id"]

    report_response = client.post(
        "/api/v1/reports/",
        json={"title": "Test Report 2", "content": "Test Report Content 2"},
        headers={"Authorization": f"Bearer {user_id}"}
    )

    # Get all reports
    reports_response = client.get(
        "/api/v1/reports/",
        headers={"Authorization": f"Bearer {user_id}"}
    )
    assert reports_response.status_code == 200
    assert len(reports_response.json()) > 0