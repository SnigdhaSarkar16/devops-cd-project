import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from app import app, add


def test_add_function():
    assert add(2, 3) == 5


def test_home():
    client = app.test_client()

    res = client.get("/")

    assert res.status_code == 200
    assert b"Automated CI/CD Pipeline" in res.data


def test_health():
    client = app.test_client()

    res = client.get("/health")

    assert res.status_code == 200
    assert res.get_json() == {"status": "ok"}


def test_status():
    client = app.test_client()

    res = client.get("/api/status")

    assert res.status_code == 200
    assert res.get_json()["status"] == "running"


def test_add_route():
    client = app.test_client()

    res = client.get("/add/4/6")

    assert res.status_code == 200
    assert res.get_json()["result"] == 10
