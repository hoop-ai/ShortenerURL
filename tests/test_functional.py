from fastapi.testclient import TestClient

from app import database, models


def create_short_url(client: TestClient, url: str) -> str:
    response = client.post("/shorten", json={"original_url": url})
    assert response.status_code == 200
    payload = response.json()
    return payload["short_url"].rsplit("/", maxsplit=1)[-1]


def test_shorten_and_redirect_flow(client: TestClient):
    code = create_short_url(client, "https://www.example.com/docs")
    redirect_response = client.get(f"/r/{code}", follow_redirects=False)
    assert redirect_response.status_code == 307
    assert redirect_response.headers["location"].rstrip("/") == "https://www.example.com/docs"


def test_get_shorten_returns_405(client: TestClient):
    response = client.get("/shorten")
    assert response.status_code == 405
    assert response.json()["detail"] == "Method Not Allowed"


def test_redirect_unknown_code_returns_404(client: TestClient):
    response = client.get("/r/ABC123", follow_redirects=False)
    assert response.status_code == 404
    assert response.json()["detail"] == "Short URL not found"


def test_redirect_increments_click_counter(client: TestClient):
    code = create_short_url(client, "https://fastapi.tiangolo.com")

    # First visit
    client.get(f"/r/{code}", follow_redirects=False)

    session = database.SessionLocal()
    try:
        record = session.query(models.URL).filter_by(short_code=code).first()
        assert record is not None
        assert record.clicks == 1
    finally:
        session.close()
