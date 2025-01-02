import pytest
from conftest import pet_service

class TestPet:
    def test_create_pet(self, pet_service):
        response = pet_service.create_pet(pet_service.pet_json)
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

    # TODO: reduce number of lines
    def test_get_pet_by_id(self, pet_service):
        created_pet = pet_service.create_pet(pet_service.pet_json)
        parsed_created_pet = created_pet.json()
        created_pet_id = parsed_created_pet.get("id")
        response = pet_service.get_pet(created_pet_id)
        assert 200 == response.status_code
        assert created_pet_id == response.json().get("id")

    # TODO: optimize usage of created and updated pet
    # TODO: add more assertions
    def test_update_pet(self, pet_service):
        pet_service.create_pet(pet_service.pet_json)
        response = pet_service.update_pet(pet_service.pet_updated_json)
        assert 200 == response.status_code

    # TODO: optimize usage of created and updated pet
    @pytest.mark.xfail
    # returns 500 instead of 400
    def test_update_pet_invalid_id(self, pet_service):
        response = pet_service.update_pet(pet_service.pet_invalid_id_json)
        assert 400 == response.status_code

    # TODO: optimize usage of created and updated pet
    @pytest.mark.xfail
    # returns 500 instead of 400
    def test_update_pet_invalid_body(self, pet_service):
        response = pet_service.update_pet(pet_service.pet_invalid_body_json)
        assert 400 == response.status_code

    # TODO: add more invalid cases
    # returns 404 instead of 400
    @pytest.mark.xfail
    def test_get_order_by_invalid_id(self, store_service):
        response = store_service.get_order("qwe")
        assert 400 == response.status_code


    # TODO: add more cases for 404
    def test_get_absent_order(self, store_service):
        response = store_service.get_order(0)
        assert 404 == response.status_code


    # TODO: reduce number of lines
    def test_delete_order(self, pet_service):
        created_pet = pet_service.create_pet(pet_service.pet_json)
        parsed_created_pet = created_pet.json()
        created_pet_id = parsed_created_pet.get("id")
        response = pet_service.delete_pet(created_pet_id)
        assert 200 == response.status_code


    # TODO: reduce number of lines
    def test_delete_deleted_order(self, pet_service):
        created_pet = pet_service.create_pet(pet_service.pet_json)
        parsed_created_pet = created_pet.json()
        created_pet_id = parsed_created_pet.get("id")
        pet_service.delete_pet(created_pet_id)
        response = pet_service.delete_pet(created_pet_id)
        assert 404 == response.status_code


    # TODO: reduce number of lines
    def test_get_deleted_order(self, pet_service):
        created_pet = pet_service.create_pet(pet_service.pet_json)
        parsed_created_pet = created_pet.json()
        created_pet_id = parsed_created_pet.get("id")
        pet_service.delete_pet(created_pet_id)
        response = pet_service.get_pet(created_pet_id)
        assert 404 == response.status_code
