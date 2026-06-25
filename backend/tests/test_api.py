from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_generate_testcases():
    response = client.post(
        "/generate-testcases",
        json={
            "requirement": "As a user, I want to login using email and password."
        }
    )

    assert response.status_code == 200
    assert "requirement" in response.json()


def test_history():
    response = client.get("/history")

    assert response.status_code == 200


def test_export():
    response = client.get("/export")

    assert response.status_code == 200


def test_search():
    response = client.get(
        "/history/search",
        params={"keyword": "login"}
    )

    assert response.status_code == 200


def test_delete_invalid_record():
    response = client.delete("/history/99999")

    assert response.status_code == 200