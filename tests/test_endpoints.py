from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)


def test_root_message():
    r = client.get("/")
    assert r.status_code == 200
    assert r.headers["content-type"].startswith("application/json")
    assert r.json() == {"message": "Welcome to the ML API"}


def test_health_ok():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}
