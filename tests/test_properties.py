from urllib.parse import urlparse

from fastapi.testclient import TestClient
from hypothesis import assume, given, strategies as st

from app.main import app

client = TestClient(app)


@given(st.text(min_size=1, max_size=64))
def test_shorten_rejects_invalid_urls(random_text):
    """Random strings that are not valid URLs should be rejected."""
    parsed = urlparse(random_text)
    assume(not (parsed.scheme and parsed.netloc))
    response = client.post("/shorten", json={"original_url": random_text})
    assert response.status_code in (400, 422)
