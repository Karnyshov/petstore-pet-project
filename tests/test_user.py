import allure
import pytest
from conftest import user_service, create_valid_user, valid_user, invalid_user
from pytest_check import check_functions as cf
from src.test_data.test_data_user import random_username, generated_users, generated_updated_users, \
    generated_invalid_users, generated_updated_invalid_users, generated_invalid_username, generated_username


class TestUser:
    @allure.title("Create random user")
    def test_create_user(self, user_service, valid_user):
        response = user_service.create_user(valid_user.to_json())
        assert 200 == response.status_code
        parsed_response = response.json()
        assert valid_user.user_id == int(parsed_response.get("message"))
        parsed_created_user_response = user_service.get_user(valid_user.username).json()
        cf.equal(valid_user.user_id, parsed_created_user_response.get("id"))
        cf.equal(valid_user.username, parsed_created_user_response.get("username"))
        cf.equal(valid_user.firstName, parsed_created_user_response.get("firstName"))
        cf.equal(valid_user.lastName, parsed_created_user_response.get("lastName"))
        cf.equal(valid_user.email, parsed_created_user_response.get("email"))
        cf.equal(valid_user.password, parsed_created_user_response.get("password"))
        cf.equal(valid_user.phone, parsed_created_user_response.get("phone"))
        cf.equal(valid_user.userStatus, parsed_created_user_response.get("userStatus"))

    @pytest.mark.parametrize("user", generated_users)
    def test_create_param_user(self, user_service, user):
        response = user_service.create_user(user.to_json())
        assert 200 == response.status_code
        parsed_created_user_response = response.json()
        cf.equal(user.user_id, parsed_created_user_response.get("id"))
        cf.equal(user.username, parsed_created_user_response.get("username"))
        cf.equal(user.firstName, parsed_created_user_response.get("firstName"))
        cf.equal(user.lastName, parsed_created_user_response.get("lastName"))
        cf.equal(user.email, parsed_created_user_response.get("email"))
        cf.equal(user.password, parsed_created_user_response.get("password"))
        cf.equal(user.phone, parsed_created_user_response.get("phone"))
        cf.equal(user.userStatus, parsed_created_user_response.get("userStatus"))

    @pytest.mark.xfail
    # returns 500 instead of 400
    def test_create_invalid_user(self, user_service, invalid_user):
        response = user_service.create_user(invalid_user.to_json())
        assert 400 == response.status_code

    @pytest.mark.xfail
    @pytest.mark.parametrize("user", generated_invalid_users)
    # returns 500 instead of 400
    def test_create_param_invalid_user(self, user_service, user):
        response = user_service.create_user(user.to_json())
        assert 400 == response.status_code

    # TODO: Fix
    def test_update_user(self, user_service, create_valid_user, valid_user):
        parsed_created_user_response = user_service.get_user(valid_user.username).json()
        updated_user = user_service.updating_user(valid_user.username)
        response = user_service.update_user(valid_user.username, updated_user.to_json())
        assert 200 == response.status_code
        parsed_response = response.json()
        assert parsed_response.get("message") == str(valid_user.user_id)
        parsed_updated_user_response = user_service.get_user(valid_user.username).json()
        cf.equal(parsed_created_user_response.get("id"), parsed_updated_user_response.get("id"))
        # cf.equal(parsed_created_user_response.get("username"), parsed_updated_user_response.get("username"))
        # cf.equal(parsed_created_user_response.get("firstName"), parsed_updated_user_response.get("firstName"))
        # cf.not_equal(parsed_created_user_response.get("lastName"), parsed_updated_user_response.get("lastName"))
        # cf.not_equal(parsed_created_user_response.get("email"), parsed_updated_user_response.get("email"))
        # cf.not_equal(parsed_created_user_response.get("password"), parsed_updated_user_response.get("password"))
        # cf.not_equal(parsed_created_user_response.get("phone"), parsed_updated_user_response.get("phone"))
        # cf.not_equal(parsed_created_user_response.get("userStatus"), parsed_updated_user_response.get("userStatus"))

    # TODO: add more assertions
    @pytest.mark.parametrize("users", generated_updated_users)
    def test_update_param_user(self, user_service, create_valid_user, valid_user, users):
        updated_users = user_service.updating_users(valid_user.username, users)
        response = user_service.update_user(valid_user.username, updated_users.to_json())
        assert 200 == response.status_code
        parsed_response = response.json()

    @pytest.mark.xfail
    # return 500 instead of 400
    def test_update_invalid_user(self, user_service, create_valid_user, valid_user, invalid_user):
        updated_user = user_service.invalid_update_user(valid_user, invalid_user)
        response = user_service.update_user(valid_user.username, updated_user.to_json())
        assert 400 == response.status_code

    @pytest.mark.xfail
    @pytest.mark.parametrize("users", generated_updated_invalid_users)
    # return 500 instead of 400
    def test_update_param_invalid_user(self, user_service, create_valid_user, valid_user, users):
        updated_users = user_service.updating_users(valid_user.username, users)
        response = user_service.update_user(valid_user.username, updated_users.to_json())
        assert 400 == response.status_code

    @pytest.mark.xfail
    # return 200 instead of 404
    def test_update_absent_user(self, user_service, valid_user):
        response = user_service.update_user(random_username(), valid_user.to_json())
        assert 404 == response.status_code

    def test_get_user_by_username(self, user_service, create_valid_user, valid_user):
        response = user_service.get_user(valid_user.username)
        assert 200 == response.status_code

    @pytest.mark.xfail
    # return 404 instead of 400
    def test_get_user_invalid_username(self, user_service):
        response = user_service.get_user(generated_invalid_username)
        assert 400 == response.status_code

    # Flaky. May return 200 instead of 404. Duplicates test_get_deleted_user
    def test_get_absent_user(self, user_service):
        response = user_service.get_user(generated_username)
        assert 404 == response.status_code

    def test_delete_user(self, user_service, create_valid_user, valid_user):
        response = user_service.delete_user(valid_user.username)
        assert 200 == response.status_code
        parsed_response = response.json()
        assert parsed_response.get("message") == valid_user.username

    @pytest.mark.xfail
    # Flaky. May return 200 instead of 404
    def test_get_deleted_user(self, user_service, create_valid_user, valid_user):
        user_service.delete_user(valid_user.username)
        response = user_service.get_user(valid_user.username)
        assert 404 == response.status_code

    @pytest.mark.xfail
    # Flaky. May return 200 instead of 404
    def test_delete_deleted_user(self, user_service, create_valid_user, valid_user):
        user_service.delete_user(valid_user.username)
        response = user_service.delete_user(valid_user.username)
        assert 404 == response.status_code
