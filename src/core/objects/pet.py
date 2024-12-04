from dataclasses import dataclass
from random import randint
import json


@dataclass
class Pet:
    pet_id: int
    name: str
    status: str
    photoUrls: list
    tags: list
    category: dict

    @classmethod
    def generate_pet(cls):
        cls.pet_id = randint(0, 10)
        cls.name = "Bob"
        cls.status = "available"
        cls.photoUrls = ["https://youtube.com"]
        cls.tags = [{
            "id": randint(0, 10),
            "name": "Tag Test"
        }]
        cls.category = {
            "id": randint(0, 10),
            "name": "dog"
        }

        # TODO: move as function
        pet_json = {
            "id": cls.pet_id,
            "name": cls.name,
            "status": cls.status,
            "photoUrls": cls.photoUrls,
            "tags": cls.tags,
            "category": cls.category
        }

        return json.dumps(pet_json)

