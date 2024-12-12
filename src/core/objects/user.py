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

    @classmethod
    def generate_user(cls):
        cls.id = randint(0, 10)
        cls.username = "Bob User"
        cls.firstName = "Bob"
        cls.lastName = "Balan"
        cls.email = "test@email.com"
        cls.password = "p@sw0rd"
        cls.phone = "0991234567"
        cls.userStatus = randint(0, 2)

        return cls

    @classmethod
    def generate_invalid_user(cls):
        cls.id = randint(0, 10)
        cls.username = "Bob User"
        cls.firstName = "Bob"
        cls.lastName = "Balan"
        cls.email = "test@email.com"
        cls.password = "p@sw0rd"
        cls.phone = []
        cls.userStatus = randint(0, 2)

        return cls

    # overrides result of generate_invalid_user() and generate_user() and generate_updated_invalid_user()
    @classmethod
    def generate_updated_user(cls, user):
        cls.id = randint(0, 10)
        cls.username = user.username
        cls.firstName = "Bob Updated"
        cls.lastName = "Balan Updated"
        cls.email = "test_updated@email.com"
        cls.password = "p@sw0rd_updated"
        cls.phone = "123456789"
        cls.userStatus = randint(0, 2)

        return cls

    # overrides result of generate_invalid_user() and generate_user() and generate_updated_user()
    @staticmethod
    def generate_updated_invalid_user(user):
        user.id = randint(0, 10)
        user.username = user.username
        user.firstName = "Bob Updated"
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
