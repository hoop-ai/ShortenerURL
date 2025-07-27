from fastapi.testclient import TestClient
from app.main import app
from app import database, models

client = TestClient(app)


def test_shorten_url_and_redirect():
    # Paso 1: enviar una URL original
    response = client.post(
        "/shorten", json={"original_url": "https://www.google.com"})
    assert response.status_code == 200
    data = response.json()
    assert "short_url" in data

    # Paso 2: extraer el código
    short_url = data["short_url"]
    code = short_url.split("/")[-1]

    # Paso 3: simular acceso al enlace corto
    redirect_response = client.get(f"/{code}", follow_redirects=False)
    assert redirect_response.status_code == 307
    assert redirect_response.headers["location"].rstrip(
        "/") == "https://www.google.com"
