from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_user():
    response = client.post("/users/", json={"username": "John", "email": "john@example.com"})
    assert response.status_code == 200
    assert response.json()["username"] == "John"

def test_get_user():
    response = client.get("/users/1")
    assert response.status_code == 200

def test_get_all_users():
    response = client.get("/users/")
    assert response.status_code == 200
