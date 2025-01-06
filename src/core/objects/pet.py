from dataclasses import dataclass
from typing import Any
from random import randint
import json


@dataclass
class Pet:
    pet_id: Any
    name: str
    status: str
    photoUrls: list
    tags: list
    category: dict

    # TODO: move to fixture
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

    # TODO: move to fixture
    @staticmethod
    def update_pet(created_pet):
        created_pet.name = "Bob_updated"
        created_pet.status = "sold"
        created_pet.photoUrls = ["https://youtube.com"]
        created_pet.tags = [{
            "id": randint(0, 10),
            "name": "Tag Test Updated"
        }]
        created_pet.category = {
            "id": randint(0, 10),
            "name": "dog updated"
        }

        return created_pet

    # TODO: move to fixture
    @staticmethod
    def update_pet_invalid_id(created_pet):
        created_pet.pet_id = "qwe",
        created_pet.name = "Bob_updated",
        created_pet.status = "sold",
        created_pet.photoUrls = ["https://youtube.com"],
        created_pet.tags = [{
                "id": randint(0, 10),
                "name": "Tag Test Updated"
            }],
        created_pet.category = {
                "id": randint(0, 10),
                "name": "dog updated"
            }

        return created_pet

    # TODO: move to fixture
    @staticmethod
    def update_pet_invalid_body(created_pet):
        created_pet.name = "Bob_updated"
        created_pet.status = "sold"
        created_pet.photoUrls = ["https://youtube.com"]
        created_pet.tags = [{
            "id": "qwe",
            "name": "Tag Test Updated"
        }]
        created_pet.category = {
            "id": randint(0, 10),
            "name": "dog updated"
        }

        return created_pet

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
