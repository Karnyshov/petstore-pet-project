from dataclasses import dataclass
from typing import Any
from random import randint
import json


@dataclass
class User:
    id: Any
    username: str
    firstName: str
    lastName: str
    email: str
    password: str
    phone: Any
    userStatus: Any

    # TODO: move to fixture
    @staticmethod
    def generate_user():
        user = User(
            randint(0, 10),
            "Bob User",
            "Bob Valid",
            "Balan",
            "test@email.com",
            "p@sw0rd",
            "0991234567",
            randint(0, 2)
        )

        return user


    # TODO: move to fixture
    @staticmethod
    def generate_invalid_user():
        user = User(
            randint(0, 10),
            "Bob User",
            "Bob Invalid",
            "Balan",
            "test@email.com",
            "p@sw0rd",
            [],
            randint(0, 2)

        )

        return user


    # TODO: move to fixture
    @staticmethod
    def update_user(user):
        user.id = randint(0, 10)
        user.username = user.username
        user.firstName = "Bob Updated"
        user.lastName = "Balan Updated"
        user.email = "test_updated@email.com"
        user.password = "p@sw0rd_updated"
        user.phone = "123456789"
        user.userStatus = randint(0, 2)

        return user


    # TODO: move to fixture
    # overrides valid user
    @staticmethod
    def invalid_update_user(user):
        user.id = randint(0, 10)
        user.username = user.username
        user.firstName = "Bob Invalid Updated"
        user.lastName = "Balan Updated"
        user.email = "test_updated@email.com"
        user.password = "p@sw0rd_updated"
        user.phone = "123456789"
        user.userStatus = "qwe"

        return user


    @staticmethod
    def user_to_json(user) -> str:
        user_json = {
            "id": user.id,
            "username": user.username,
            "firstName": user.firstName,
            "lastName": user.lastName,
            "email": user.email,
            "password": user.password,
            "phone": user.phone,
            "userStatus": user.userStatus
        }

        return json.dumps(user_json)
