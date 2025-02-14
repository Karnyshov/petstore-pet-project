import pytest
from src.services.store import StoreService
from src.services.pet import PetService
from src.services.user import UserService
from src.core.objects.order import Order
from src.core.objects.pet import Pet
from src.core.objects.user import User


@pytest.fixture(scope="function")
def store_service():
    yield StoreService()

@pytest.fixture(scope="function")
def pet_service():
    yield PetService()

@pytest.fixture(scope="function")
def user_service():
    yield UserService()

@pytest.fixture(scope="function")
def valid_order():
    order = Order.generate_order()
    yield order

@pytest.fixture(scope="function")
def invalid_order():
    invalid_order = Order.generate_invalid_order()
    yield invalid_order

@pytest.fixture(scope="function")
def create_valid_order(store_service, valid_order):
    created_order = store_service.create_order(valid_order.to_json())
    yield created_order

@pytest.fixture(scope="function")
def parsed_order(create_valid_order):
    parsed_order = create_valid_order.json()
    yield parsed_order

@pytest.fixture(scope="function")
def valid_pet():
    pet = Pet.generate_pet()
    yield pet

@pytest.fixture(scope="function")
def create_valid_pet(pet_service, valid_pet):
    created_pet = pet_service.create_pet(valid_pet.to_json())
    yield created_pet

@pytest.fixture(scope="function")
def parsed_pet(create_valid_pet):
    parsed_pet = create_valid_pet.json()
    yield parsed_pet

@pytest.fixture(scope="function")
def valid_user():
    user = User.generate_user()
    yield user

@pytest.fixture(scope="function")
def invalid_user():
    invalid_user = User.generate_invalid_user()
    yield invalid_user

@pytest.fixture(scope="function")
def create_valid_user(user_service, valid_user):
    created_user = user_service.create_user(valid_user.to_json())
    yield created_user