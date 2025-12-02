import sys
from pathlib import Path

# Garante que a pasta raiz do projeto (onde está a pasta "app") entre no sys.path
ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT_DIR))

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health_check():
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.json()["status"] == "ok"


def test_ask_question():
    payload = {
        "subject": "Cloud Computing",
        "question": "O que é escalabilidade horizontal?"
    }
    resp = client.post("/ask", json=payload)
    assert resp.status_code == 200
    data = resp.json()
    assert "answer" in data
    assert "model_used" in data