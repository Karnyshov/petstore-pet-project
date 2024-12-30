import pytest
from src.services.store import StoreService
from src.services.pet import PetService


@pytest.fixture
def store_service():
    yield StoreService()


@pytest.fixture
def pet_service():
    yield PetService()
