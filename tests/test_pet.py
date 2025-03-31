import pytest
from conftest import pet_service, valid_pet, create_valid_pet, parsed_pet, invalid_pet
from src.test_data.test_data_pet import invalid_pet_status, pet_status, pet_form_data, invalid_pet_form_data, generated_pets, generated_invalid_pets, generated_updated_pets, generated_pet_form_data, generated_invalid_pet_form_data

class TestPet:
    def test_create_pet(self, pet_service, valid_pet):
        response = pet_service.create_pet(valid_pet.to_json())
        assert 200 == response.status_code

    @pytest.mark.parametrize("pets", generated_pets)
    def test_create_param_pet(self, pet_service, pets):
        response = pet_service.create_pet(pets.to_json())
        assert 200 == response.status_code

    @pytest.mark.xfail
    # returns 500 instead of 400
    def test_create_invalid_pet(self, pet_service, invalid_pet):
        response = pet_service.create_pet(invalid_pet.to_json())
        assert 400 == response.status_code

    @pytest.mark.parametrize("pets", generated_invalid_pets)
    @pytest.mark.xfail
    # returns 500 instead of 400
    def test_create_param_invalid_pet(self, pet_service, pets):
        response = pet_service.create_pet(pets.to_json())
        assert 400 == response.status_code

    @pytest.mark.parametrize('status', pet_status)
    def test_find_by_status_available(self, pet_service, status):
        response = pet_service.find_by_status(status)
        assert 200 == response.status_code

    @pytest.mark.parametrize('status', invalid_pet_status)
    @pytest.mark.xfail
    # returns 200 and empty array instead of 400
    def test_find_by_invalid_status(self, pet_service, status):
        response = pet_service.find_by_status(status)
        assert 400 == response.status_code

    def test_get_pet_by_id(self, pet_service, parsed_pet):
        created_pet_id = parsed_pet.get("id")
        response = pet_service.get_pet(created_pet_id)
        assert 200 == response.status_code
        assert created_pet_id == response.json().get("id")

    # TODO: add more assertions
    def test_update_pet(self, pet_service, create_valid_pet, valid_pet):
        updated_pet = pet_service.update_single_pet(valid_pet)
        response = pet_service.update_pet(updated_pet.to_json())
        assert 200 == response.status_code

    @pytest.mark.xfail
    # returns 500 instead of 400
    def test_update_invalid_pet(self, pet_service, create_valid_pet, valid_pet, invalid_pet):
        updated_pet = pet_service.update_pets(valid_pet.pet_id, invalid_pet)
        response = pet_service.update_pet(updated_pet.to_json())
        assert 400 == response.status_code

    @pytest.mark.parametrize("pets", generated_updated_pets)
    def test_update_param_pet(self, pet_service, create_valid_pet, valid_pet, pets):
        updated_pet = pet_service.update_pets(valid_pet.pet_id, pets)
        response = pet_service.update_pet(updated_pet.to_json())
        assert 200 == response.status_code

    @pytest.mark.parametrize("pets", generated_invalid_pets)
    @pytest.mark.xfail
    # returns 500 instead of 400
    def test_update_param_invalid_pets(self, pet_service, create_valid_pet, valid_pet, pets):
        updated_pet = pet_service.update_pets(valid_pet.pet_id, pets)
        response = pet_service.update_pet(updated_pet.to_json())
        assert 400 == response.status_code

    #random
    def test_update_pet_form(self, pet_service, create_valid_pet, valid_pet):
        response = pet_service.update_pet_form(valid_pet.pet_id, generated_pet_form_data)
        assert 200 == response.status_code

    #random, invalid data doesn't change the object
    def test_update_invalid_pet_form(self, pet_service, create_valid_pet, valid_pet):
        response = pet_service.update_pet_form(valid_pet.pet_id, generated_invalid_pet_form_data)
        assert 200 == response.status_code

    @pytest.mark.parametrize("form_data", pet_form_data)
    def test_update_param_pet_form(self, pet_service, create_valid_pet, valid_pet, form_data):
        response = pet_service.update_pet_form(valid_pet.pet_id, form_data)
        assert 200 == response.status_code

    #invalid data doesn't change the object
    @pytest.mark.parametrize("form_data", invalid_pet_form_data)
    def test_update_param_invalid_pet_form(self, pet_service, create_valid_pet, valid_pet, form_data):
        response = pet_service.update_pet_form(valid_pet.pet_id, form_data)
        assert 200 == response.status_code

    def test_delete_pet(self, pet_service, parsed_pet):
        created_pet_id = parsed_pet.get("id")
        response = pet_service.delete_pet(created_pet_id)
        assert 200 == response.status_code

    def test_delete_deleted_pet(self, pet_service, parsed_pet):
        created_pet_id = parsed_pet.get("id")
        pet_service.delete_pet(created_pet_id)
        response = pet_service.delete_pet(created_pet_id)
        assert 404 == response.status_code

    def test_get_deleted_pet(self, pet_service, parsed_pet):
        created_pet_id = parsed_pet.get("id")
        pet_service.delete_pet(created_pet_id)
        response = pet_service.get_pet(created_pet_id)
        assert 404 == response.status_code
