import json
import pytest
from flask import Flask
from main import app

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

def test_predict_ia(client):
    response = client.post("/predict", json={"text": "Soy un modelo de lenguaje entrenado"})
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data["prediction"] in ["IA", "humano"]

def test_predict_humano(client):
    response = client.post("/predict", json={"text": "Hola, ¿cómo estás?"})
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data["prediction"] in ["IA", "humano"]

