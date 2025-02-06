from dataclasses import dataclass, field
from typing import Any, Union
from random import randint
from faker import Faker
import json


@dataclass
class Pet:
    pet_id: Union[int, Any] = randint(0, 10)
    name: str = Faker().first_name()
    status: str = "available"
    photoUrls: Union[list, Any] = field(default_factory=lambda: [Faker().url()])
    tags: Union[list, Any] = field(default_factory=lambda: [{"id": randint(10, 20),
                   "firstname": Faker().name()}])
    category: dict = field(default_factory=lambda: {"id": randint(0, 10),
                      "gender": Faker().passport_gender(0)})

    @staticmethod
    def generate_pet():
        pet = Pet(
            randint(0, 10),
            "Bob",
            "available",
            ["https://youtube.com"],
            [{
                "id": randint(0, 10),
                "name": "Tag Test"
            }],
            {
                "id": randint(0, 10),
                "name": "dog"
            }
        )

        return pet

    @staticmethod
    def update_pet(created_pet):
        updated_pet = Pet(
            created_pet.pet_id,
            "Bob_updated",
            "sold",
            ["https://youtube.com"],
            [{
                "id": randint(0, 10),
                "name": "Tag Test Updated"
            }],
            {
                "id": randint(0, 10),
                "name": "dog updated"
            }
        )

        return updated_pet

    @staticmethod
    def update_pet_invalid_id():
        pet_invalid_id = Pet(
            "qwe",
            "Bob_updated",
            "sold",
            ["https://youtube.com"],
            [{
                "id": randint(0, 10),
                "name": "Tag Test Updated"
            }],
            {
                "id": randint(0, 10),
                "name": "dog updated"
            }
        )

        return pet_invalid_id

    @staticmethod
    def update_pet_invalid_body(created_pet):
        pet_invalid_body = Pet(
            created_pet.pet_id,
            "Bob_updated",
            "sold",
            ["https://youtube.com"],
            [{
                "id": "qwe",
                "name": "Tag Test Updated"
            }],
            {
                "id": randint(0, 10),
                "name": "dog updated"
            },
        )

        return pet_invalid_body

    @staticmethod
    def generate_pet_update_form_data():
        form_data = {
            "name": "Bobr",
            "status": "sold"
        }

        return form_data

    def to_json(self) -> str:
        pet_json = {
            "id": self.pet_id,
            "name": self.name,
            "status": self.status,
            "photoUrls": self.photoUrls,
            "tags": self.tags,
            "category": self.category
        }

        return json.dumps(pet_json)
