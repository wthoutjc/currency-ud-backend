import pytest
from src.create_app import create_app

@pytest.fixture
def client():
    app = create_app()
    with app.test_client() as client:
        yield client
