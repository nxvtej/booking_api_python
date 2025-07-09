import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi.testclient import TestClient
from server import app

client = TestClient(app)

def test_classes_endpoint():
    response = client.get("/classes")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    print("Class test case passed")

def test_invalid_booking():
    response = client.post("/book", json={
        "id":1,
        "class_id": 999,
        "client_name": "Test",
        "client_email": "test@example.com"
    })
    assert response.status_code == 404
    print("Booking test case passed")

if __name__ == "__main__":
    test_classes_endpoint()
    test_invalid_booking()
