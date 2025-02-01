import pytest
from conftest import pet_service, valid_pet, create_valid_pet, parsed_pet
from src.test_data.test_data import PetData

class TestPet:
    # TODO: add generation & parametrization
    def test_create_pet(self, pet_service, valid_pet):
        response = pet_service.create_pet(valid_pet.to_json())
        assert 200 == response.status_code

    @pytest.mark.parametrize('status', PetData.status)
    def test_find_by_status_available(self, pet_service, status):
        response = pet_service.find_by_status(status)
        assert 200 == response.status_code

    # returns 200 and empty array instead of 400
    @pytest.mark.parametrize('status', PetData.invalid_status)
    @pytest.mark.xfail
    def test_find_by_invalid_status(self, pet_service, status):
        response = pet_service.find_by_status(status)
        assert 400 == response.status_code

    def test_get_pet_by_id(self, pet_service, parsed_pet):
        created_pet_id = parsed_pet.get("id")
        response = pet_service.get_pet(created_pet_id)
        assert 200 == response.status_code
        assert created_pet_id == response.json().get("id")

    # TODO: add generation & parametrization
    # TODO: add more assertions
    def test_update_pet(self, pet_service, create_valid_pet, valid_pet):
        updated_pet = pet_service.update_valid_pet(valid_pet)
        response = pet_service.update_pet(updated_pet.to_json())
        assert 200 == response.status_code

    # TODO: add generation & parametrization
    def test_update_pet_form(self, pet_service, create_valid_pet, valid_pet):
        response = pet_service.update_pet_form(valid_pet.pet_id, pet_service.form_data())
        assert 200 == response.status_code

    # TODO: add generation & parametrization
    @pytest.mark.xfail
    # returns 500 instead of 400
    def test_update_pet_invalid_id(self, pet_service, create_valid_pet):
        response = pet_service.update_pet(pet_service.update_pet_invalid_id().to_json())
        assert 400 == response.status_code

    # TODO: add generation & parametrization
    @pytest.mark.xfail
    # returns 500 instead of 400
    def test_update_pet_invalid_body(self, pet_service, create_valid_pet, valid_pet):
        updated_pet = pet_service.update_pet_invalid_body(valid_pet)
        response = pet_service.update_pet(updated_pet.to_json())
        assert 400 == response.status_code

    # TODO: add generation
    def test_delete_pet(self, pet_service, parsed_pet):
        created_pet_id = parsed_pet.get("id")
        response = pet_service.delete_pet(created_pet_id)
        assert 200 == response.status_code

    # TODO: add generation
    def test_delete_deleted_pet(self, pet_service, parsed_pet):
        created_pet_id = parsed_pet.get("id")
        pet_service.delete_pet(created_pet_id)
        response = pet_service.delete_pet(created_pet_id)
        assert 404 == response.status_code

    # TODO: add generation
    def test_get_deleted_pet(self, pet_service, parsed_pet):
        created_pet_id = parsed_pet.get("id")
        pet_service.delete_pet(created_pet_id)
        response = pet_service.get_pet(created_pet_id)
        assert 404 == response.status_code
