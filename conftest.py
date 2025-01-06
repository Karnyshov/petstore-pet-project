import copy

import pytest
from src.services.store import StoreService
from src.services.pet import PetService
from src.services.user import UserService
from src.core.objects.order import Order
from src.core.objects.pet import Pet


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
def updated_pet(pet_service, valid_pet):
    original_pet = copy.deepcopy(valid_pet)
    pet_updated = Pet.update_pet(valid_pet)
    yield pet_updated

@pytest.fixture(scope="function")
def updated_pet_invalid_id(pet_service, valid_pet):
    original_pet = copy.deepcopy(valid_pet)
    pet_updated_invalid_id = Pet.update_pet_invalid_id(valid_pet)
    yield pet_updated_invalid_id

@pytest.fixture(scope="function")
def updated_pet_invalid_body(pet_service, valid_pet):
    original_pet = copy.deepcopy(valid_pet)
    pet_updated_invalid_body = Pet.update_pet_invalid_body(valid_pet)
    yield pet_updated_invalid_body