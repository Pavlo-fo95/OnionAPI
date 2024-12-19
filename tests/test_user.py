import sys
import os

# Добавляем корень проекта в sys.path, чтобы Python мог найти app.main
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_user():
    response = client.post("/users/", json={"username": "John", "email": "john@example.com"})
    print("Response JSON:", response.json())
    assert response.status_code == 200
    assert response.json()["username"] == "John"

def test_get_user():
    response = client.get("/users/1")
    print("Response JSON:", response.json())
    assert response.status_code == 200
    assert response.json()["user_id"] == 1

def test_get_all_users():
    response = client.get("/users/")
    print("Response JSON:", response.json())
    assert response.status_code == 200
    assert len(response.json()) > 0