import pytest
from src.services.store import StoreService
from src.services.pet import PetService
from src.services.user import UserService


@pytest.fixture(scope="function")
def store_service():
    yield StoreService()


@pytest.fixture(scope="function")
def pet_service():
    yield PetService()

    
@pytest.fixture(scope="function")
def user_service():
    yield UserService()
