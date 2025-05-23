import pytest
import allure
from conftest import pet_service, valid_pet, create_valid_pet, parsed_pet, invalid_pet
from pytest_check import check_functions as cf
from src.test_data.test_data_pet import invalid_pet_status, pet_status, pet_form_data, invalid_pet_form_data, generated_pets, generated_invalid_pets, generated_updated_pets, generated_pet_form_data, generated_invalid_pet_form_data

class TestPet:
    @allure.title("Creating random pet")
    def test_create_pet(self, pet_service, valid_pet):
        response = pet_service.create_pet(valid_pet.to_json())
        assert 200 == response.status_code
        parsed_response = response.json()
        cf.equal(valid_pet.pet_id, parsed_response.get("id"))
        cf.equal(valid_pet.name, parsed_response.get("name"))
        cf.equal(valid_pet.status, parsed_response.get("status"))
        cf.equal(valid_pet.photoUrls, parsed_response.get("photoUrls"))
        cf.equal(valid_pet.tags, parsed_response.get("tags"))
        cf.equal(valid_pet.category, parsed_response.get("category"))

    @pytest.mark.parametrize("pets", generated_pets)
    @allure.title("Creating multiple pets")
    def test_create_param_pet(self, pet_service, pets):
        allure.dynamic.parameter("pets", generated_pets)
        response = pet_service.create_pet(pets.to_json())
        assert 200 == response.status_code
        parsed_response = response.json()
        cf.equal(pets.pet_id, parsed_response.get("id"))
        cf.equal(pets.name, str(parsed_response.get("name")))
        cf.equal(pets.status, parsed_response.get("status"))
        cf.equal(pets.photoUrls, parsed_response.get("photoUrls"))
        cf.equal(pets.tags, parsed_response.get("tags"))
        cf.equal(pets.category, parsed_response.get("category"))


    @pytest.mark.xfail
    @allure.title("Creating pet with random invalid data")
    # returns 500 instead of 400
    def test_create_invalid_pet(self, pet_service, invalid_pet):
        response = pet_service.create_pet(invalid_pet.to_json())
        assert 400 == response.status_code

    @pytest.mark.parametrize("pets", generated_invalid_pets)
    @pytest.mark.xfail
    @allure.title("Creating pet with invalid test data")
    # returns 500 instead of 400
    def test_create_param_invalid_pet(self, pet_service, pets):
        allure.dynamic.parameter("pets", generated_invalid_pets)
        response = pet_service.create_pet(pets.to_json())
        assert 400 == response.status_code

    # TODO: add check
    @pytest.mark.parametrize('status', pet_status)
    @allure.title("Getting pet by status")
    def test_find_by_status_available(self, pet_service, status):
        allure.dynamic.parameter("status", pet_status)
        response = pet_service.find_by_status(status)
        assert 200 == response.status_code

    @pytest.mark.parametrize('status', invalid_pet_status)
    @pytest.mark.xfail
    @allure.title("Getting pet by invalid status")
    # returns 200 and empty array instead of 400
    def test_find_by_invalid_status(self, pet_service, status):
        allure.dynamic.parameter("status", invalid_pet_status)
        response = pet_service.find_by_status(status)
        assert 400 == response.status_code

    @allure.title("Getting pet by ID")
    def test_get_pet_by_id(self, pet_service, parsed_pet):
        created_pet_id = parsed_pet.get("id")
        response = pet_service.get_pet(created_pet_id)
        assert 200 == response.status_code
        assert created_pet_id == response.json().get("id")

    # TODO: add more assertions
    @allure.title("Updating pet with random data")
    def test_update_pet(self, pet_service, create_valid_pet, valid_pet):
        updated_pet = pet_service.update_single_pet(valid_pet)
        response = pet_service.update_pet(updated_pet.to_json())
        assert 200 == response.status_code
        parsed_response = response.json()

    @pytest.mark.xfail
    @allure.title("Updating pet with invalid random data")
    # returns 500 instead of 400
    def test_update_invalid_pet(self, pet_service, create_valid_pet, valid_pet, invalid_pet):
        updated_pet = pet_service.update_pets(valid_pet.pet_id, invalid_pet)
        response = pet_service.update_pet(updated_pet.to_json())
        assert 400 == response.status_code

    # TODO: add more assertions
    @pytest.mark.parametrize("pets", generated_updated_pets)
    @allure.title("Updating pet with test data")
    def test_update_param_pet(self, pet_service, create_valid_pet, valid_pet, pets):
        allure.dynamic.parameter("pets", generated_updated_pets)
        updated_pet = pet_service.update_pets(valid_pet.pet_id, pets)
        response = pet_service.update_pet(updated_pet.to_json())
        assert 200 == response.status_code
        parsed_response = response.json()

    @pytest.mark.parametrize("pets", generated_invalid_pets)
    @pytest.mark.xfail
    @allure.title("Updating pet with invalid test data")
    # returns 500 instead of 400
    def test_update_param_invalid_pets(self, pet_service, create_valid_pet, valid_pet, pets):
        allure.dynamic.parameter("pets", generated_invalid_pets)
        updated_pet = pet_service.update_pets(valid_pet.pet_id, pets)
        response = pet_service.update_pet(updated_pet.to_json())
        assert 400 == response.status_code

    # TODO: add checks (200 message, get pet by id, compare)
    @allure.title("Updating pet with random data via form")
    def test_update_pet_form(self, pet_service, create_valid_pet, valid_pet):
        response = pet_service.update_pet_form(valid_pet.pet_id, generated_pet_form_data)
        assert 200 == response.status_code

    @pytest.mark.xfail
    @allure.title("Updating pet with invalid random data via form")
    def test_update_invalid_pet_form(self, pet_service, create_valid_pet, valid_pet):
        response = pet_service.update_pet_form(valid_pet.pet_id, generated_invalid_pet_form_data)
        assert 405 == response.status_code

    # TODO: add checks (200 message, get pet by id, compare)
    @pytest.mark.parametrize("form_data", pet_form_data)
    @allure.title("Updating pet with test data via form")
    def test_update_param_pet_form(self, pet_service, create_valid_pet, valid_pet, form_data):
        allure.dynamic.parameter("form_data", pet_form_data)
        response = pet_service.update_pet_form(valid_pet.pet_id, form_data)
        assert 200 == response.status_code

    @pytest.mark.xfail
    @pytest.mark.parametrize("form_data", invalid_pet_form_data)
    @allure.title("Updating pet with invalid test data via form")
    def test_update_param_invalid_pet_form(self, pet_service, create_valid_pet, valid_pet, form_data):
        allure.dynamic.parameter("form_data", invalid_pet_form_data)
        response = pet_service.update_pet_form(valid_pet.pet_id, form_data)
        assert 405 == response.status_code

    @allure.title("Deleting pet")
    def test_delete_pet(self, pet_service, create_valid_pet, valid_pet):
        response = pet_service.delete_pet(valid_pet.pet_id)
        assert 200 == response.status_code
        parsed_response = response.json()
        assert parsed_response.get("message") == str(valid_pet.pet_id)

    @pytest.mark.xfail
    @allure.title("Deleting deleted pet")
    # Flaky. May return 200 instead of 404
    def test_delete_deleted_pet(self, pet_service, parsed_pet):
        created_pet_id = parsed_pet.get("id")
        pet_service.delete_pet(created_pet_id)
        response = pet_service.delete_pet(created_pet_id)
        assert 404 == response.status_code

    @pytest.mark.xfail
    @allure.title("Getting deleted pet")
    # Flaky. May return 200 instead of 404
    def test_get_deleted_pet(self, pet_service, parsed_pet):
        created_pet_id = parsed_pet.get("id")
        pet_service.delete_pet(created_pet_id)
        response = pet_service.get_pet(created_pet_id)
        assert 404 == response.status_code
