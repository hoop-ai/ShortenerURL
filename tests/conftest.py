import pytest
from fastapi.testclient import TestClient

from app.main import app
from app import database, models


@pytest.fixture(scope="function", autouse=True)
def db_cleanup():
    """Ensure each test runs with an empty URL table."""
    session = database.SessionLocal()
    try:
        session.query(models.URL).delete()
        session.commit()
        yield
    finally:
        session.close()


@pytest.fixture(scope="function")
def client():
    """Provide a FastAPI TestClient instance."""
    return TestClient(app)
