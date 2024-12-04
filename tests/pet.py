import pytest


def test_create_pet(pet_service):
    response = pet_service.create_pet()
    assert 200 == response.status_code


# TODO: reduce number of lines
def test_get_pet_by_id(pet_service):
    created_pet = pet_service.create_pet()
    parsed_created_pet = created_pet.json()
    created_pet_id = parsed_created_pet.get("id")
    response = pet_service.get_pet(created_pet_id)
    assert 200 == response.status_code
    assert created_pet_id == response.json().get("id")


# TODO: add more invalid cases
# return 404 instead of 400
@pytest.mark.xfail
def test_get_order_by_invalid_id(store_service):
    response = store_service.get_order("qwe")
    assert 400 == response.status_code


# TODO: add more cases for 404
def test_get_absent_order(store_service):
    response = store_service.get_order(0)
    assert 404 == response.status_code


# TODO: reduce number of lines
def test_delete_order(pet_service):
    created_pet = pet_service.create_pet()
    parsed_created_pet = created_pet.json()
    created_pet_id = parsed_created_pet.get("id")
    response = pet_service.delete_pet(created_pet_id)
    assert 200 == response.status_code


# TODO: reduce number of lines
def test_delete_deleted_order(pet_service):
    created_pet = pet_service.create_pet()
    parsed_created_pet = created_pet.json()
    created_pet_id = parsed_created_pet.get("id")
    pet_service.delete_pet(created_pet_id)
    response = pet_service.delete_pet(created_pet_id)
    assert 404 == response.status_code


# TODO: reduce number of lines
def test_get_deleted_order(pet_service):
    created_pet = pet_service.create_pet()
    parsed_created_pet = created_pet.json()
    created_pet_id = parsed_created_pet.get("id")
    pet_service.delete_pet(created_pet_id)
    response = pet_service.get_pet(created_pet_id)
    assert 404 == response.status_code
