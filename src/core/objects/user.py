from dataclasses import dataclass
from typing import Any, Union
from random import randint
import json
from faker import Faker


@dataclass
class User:
    user_id: Union[int, Any] = randint(1, 5)
    userStatus: Union[int, Any] = randint(0, 1)
    username: str = Faker().user_name()
    firstName: str = Faker().first_name()
    lastName: str = Faker().last_name()
    email: str = Faker().email()
    password: Union[str, Any] = Faker().password()
    phone: Union[str, Any] = Faker().phone_number()

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

    @staticmethod
    def update_user(created_user):
        updated_user = User(
            randint(0, 10),
            created_user.username,
            "Bob Updated",
            "Balan Updated",
            "test_updated@email.com",
            "p@sw0rd_updated",
            "123456789",
            randint(0, 2)
        )

        return updated_user

    @staticmethod
    def invalid_update_user(created_user):
        invalid_updated_user = User(
            randint(0, 10),
            created_user.username,
            "Bob Invalid Updated",
            "Balan Updated",
            "test_updated@email.com",
            "p@sw0rd_updated",
            "123456789",
            "qwe"
        )

        return invalid_updated_user

    def to_json(self) -> str:
        user_json = {
            "id": self.user_id,
            "username": self.username,
            "firstName": self.firstName,
            "lastName": self.lastName,
            "email": self.email,
            "password": self.password,
            "phone": self.phone,
            "userStatus": self.userStatus
        }

        return json.dumps(user_json)
