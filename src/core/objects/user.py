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
    phone: str
    userStatus: int

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

    @staticmethod
    def user_to_json(user) -> str:
        # TODO: move as function
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
