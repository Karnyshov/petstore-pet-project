import pytest


def test_create_user(user_service):
    response = user_service.create_user(user_service.json_user)
    assert 200 == response.status_code


def test_get_user_by_username(user_service):
    user_service.create_user(user_service.user)


