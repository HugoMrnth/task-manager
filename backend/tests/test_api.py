from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_read_health():
    """Test health check endpoint"""
    response = client.get("/")
    assert response.status_code == 200


def test_list_tasks():
    """Test list tasks endpoint"""
    response = client.get("/tasks")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
