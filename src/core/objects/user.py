import random
from dataclasses import dataclass
from typing import Any, Union
from random import randint
from test_data.test_data import random_string
import json
from faker import Faker

#TODO: try pydanctic for validation
#TODO: try separate class for invalid data
@dataclass
class User:
    user_id: Union[int, float, str, list, dict] = randint(1, 5)
    userStatus: Union[int, str, list, dict] = randint(0, 1)
    username: Union[str, list, dict] = Faker().user_name()
    firstName: Union[str, list, dict] = Faker().first_name()
    lastName: Union[str, list, dict] = Faker().last_name()
    email: Union[str, list, dict] = Faker().email()
    password: Union[str, list, dict] = Faker().password()
    phone: Union[str, list, dict] = Faker().phone_number()

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
