import pytest
from conftest import user_service, create_valid_user, valid_user, invalid_user
from src.test_data.test_data_generation import auto_generate_users
from src.test_data.test_data_user import random_username, generated_users, generated_updated_users, \
    generated_invalid_users, generated_updated_invalid_users, generated_invalid_username, generated_username, user_data


class TestUser:
    def test_create_user(self, user_service, valid_user):
        response = user_service.create_user(valid_user.to_json())
        assert 200 == response.status_code

    @pytest.mark.parametrize("user", generated_users)
    def test_create_param_user(self, user_service, user):
        response = user_service.create_user(user.to_json())
        assert 200 == response.status_code

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

    def test_update_user(self, user_service, create_valid_user, valid_user):
        updated_user = user_service.updating_user(valid_user)
        response = user_service.update_user(valid_user.username, updated_user.to_json())
        assert 200 == response.status_code

    @pytest.mark.parametrize("users", generated_updated_users)
    def test_update_param_user(self, user_service, create_valid_user, valid_user, users):
        updated_users = user_service.updating_users(valid_user.username, users)
        response = user_service.update_user(valid_user.username, updated_users.to_json())
        assert 200 == response.status_code

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

    # may return 200 instead of 404
    def test_get_absent_user(self, user_service):
        response = user_service.get_user(generated_username)
        assert 404 == response.status_code

    def test_delete_user(self, user_service, create_valid_user, valid_user):
        response = user_service.delete_user(valid_user.username)
        assert 200 == response.status_code

    @pytest.mark.xfail
    # returns 200 instead of 404
    def test_get_deleted_user(self, user_service, create_valid_user, valid_user):
        user_service.delete_user(valid_user.username)
        response = user_service.get_user(valid_user.username)
        assert 404 == response.status_code

    @pytest.mark.xfail
    # returns 200 instead of 404
    def test_deleted_user(self, user_service, create_valid_user, valid_user):
        user_service.delete_user(valid_user.username)
        response = user_service.delete_user(valid_user.username)
        assert 404 == response.status_code
