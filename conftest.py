import pytest
from src.services.store import StoreService


@pytest.fixture
def store_service():
    yield StoreService()
