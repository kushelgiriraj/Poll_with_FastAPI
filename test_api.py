from fastapi.testclient import TestClient
from main import app  # Ensure 'main' is the name of your FastAPI script

# Create a TestClient instance for testing FastAPI
client = TestClient(app)

# Basic test for a simple endpoint
def test_root():
    response = client.get("/")
    assert response.status_code == 200  # Ensure the status code is correct
    assert response.json() == {"message": "Hello World"}  # Ensure the response content is correct

# Test for an endpoint with query parameters
def test_users():
    response = client.get("/users/?skip=0&limit=10")
    assert response.status_code == 200
    # Optionally, add more specific assertions for response data

def test_create_user():
    response = client.post(
        "/users/",
        json={"username": "test", "email": "kushel@example.com"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "kushel@example.com"
    assert data["username"] == "test"
    # assert "id" in data
    # user_id = data["id"]
    # response = client.get(f"/users/{user_id}")
    # assert response.status_code == 200
    # data = response.json()
    # assert data["email"] == "sani@example.com"
    # assert data["username"] == "test"
    # assert data["id"] == user_id

def test_create_poll():
    response = client.post(
        "/polls/",
        json={
            "title": "test",
            "type": "single",
            "is_add_choices_active": True,
            "is_voting_active": True,
            "created_by": 1,
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "test"
    assert data["type"] == "single"
    assert data["is_add_choices_active"] == True
    assert data["is_voting_active"] == True
    assert data["created_by"] == 1
    # assert "id" in data
    # poll_id = data["id"]
    # response = client.get(f"/polls/{poll_id}")
    # assert response.status_code == 200
    # data = response.json()
    # assert data["title"] == "test"
    # assert data["type"] == "single"
    # assert data["is_add_choices_active"] == True
    # assert data["is_voting_active"] == True
    # assert data["created_by"] == 1
    # assert data["id"] == poll_id


