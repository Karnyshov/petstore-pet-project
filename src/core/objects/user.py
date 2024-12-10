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

    def user_to_json(self) -> str:
        # TODO: move as function
        user_json = {
            "id": self.id,
            "username": self.username,
            "firstName": self.firstName,
            "lastName": self.lastName,
            "email": self.email,
            "password": self.password,
            "phone": self.phone,
            "userStatus": self.userStatus
        }

        return json.dumps(user_json)
