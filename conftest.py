import pytest
from src.services.store import StoreService
from src.services.pet import PetService
from src.services.user import UserService


@pytest.fixture
def store_service():
    yield StoreService()


@pytest.fixture
def pet_service():
    yield PetService()

    
@pytest.fixture
def user_service():
    yield UserService()
