import pytest
import requests
from app.core.config import settings

@pytest.fixture
def base_url():
    return "https://your-production-url.vercel.app"

def test_frontend_health(base_url):
    response = requests.get(f"{base_url}/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_backend_health(base_url):
    response = requests.get(f"{base_url}/api/v1/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_authentication(base_url):
    # Test authentication flow
    login_data = {
        "username": "testuser",
        "password": "testpassword"
    }
    response = requests.post(f"{base_url}/api/v1/auth/login", json=login_data)
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_test_execution(base_url):
    # Test test execution flow
    test_data = {
        "test_scripts": ["test_script1", "test_script2"],
        "parallel": True
    }
    response = requests.post(f"{base_url}/api/v1/test-runs/execute", json=test_data)
    assert response.status_code == 200
    assert "test_results" in response.json()

def test_report_generation(base_url):
    # Test report generation flow
    response = requests.get(f"{base_url}/api/v1/reports/generate")
    assert response.status_code == 200
    assert "report_data" in response.json()

def test_database_connection(base_url):
    # Test database connection
    response = requests.get(f"{base_url}/api/v1/database/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_supabase_integration(base_url):
    # Test Supabase integration
    response = requests.get(f"{base_url}/api/v1/supabase/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"