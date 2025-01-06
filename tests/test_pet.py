import pytest
from conftest import pet_service, valid_pet, create_valid_pet, parsed_pet, updated_pet, updated_pet_invalid_id, updated_pet_invalid_body

class TestPet:
    def test_create_pet(self, pet_service, valid_pet):
        response = pet_service.create_pet(valid_pet.to_json())
        assert 200 == response.status_code

    # TODO: Add tests for other valid options
    def test_find_by_status_available(self, pet_service):
        response = pet_service.find_by_status("available")
        assert 200 == response.status_code

    # TODO: Add more invalid cases
    # returns 200 and empty array instead of 400
    @pytest.mark.xfail
    def test_find_by_invalid_status(self, pet_service):
        response = pet_service.find_by_status("123")
        assert 400 == response.status_code

    def test_get_pet_by_id(self, pet_service, parsed_pet):
        created_pet_id = parsed_pet.get("id")
        response = pet_service.get_pet(created_pet_id)
        assert 200 == response.status_code
        assert created_pet_id == response.json().get("id")

    # TODO: add more assertions
    def test_update_pet(self, pet_service, create_valid_pet, updated_pet):
        response = pet_service.update_pet(updated_pet.to_json())
        assert 200 == response.status_code

    # TODO: optimize usage of created and updated pet
    @pytest.mark.xfail
    # returns 500 instead of 400
    def test_update_pet_invalid_id(self, pet_service, updated_pet_invalid_id):
        response = pet_service.update_pet(updated_pet_invalid_id.to_json())
        assert 400 == response.status_code

    # TODO: optimize usage of created and updated pet
    @pytest.mark.xfail
    # returns 500 instead of 400
    def test_update_pet_invalid_body(self, pet_service, updated_pet_invalid_body):
        response = pet_service.update_pet(updated_pet_invalid_body.to_json())
        assert 400 == response.status_code

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
