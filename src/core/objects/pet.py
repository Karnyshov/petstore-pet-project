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

        pet_json = {
            "id": cls.pet_id,
            "name": cls.name,
            "status": cls.status,
            "photoUrls": cls.photoUrls,
            "tags": cls.tags,
            "category": cls.category
        }

        return json.dumps(pet_json)

    @classmethod
    def generate_updated_pet(cls, created_pet):
        parsed_created_pet = json.loads(created_pet)
        created_pet_id = parsed_created_pet.get("id")

        cls.pet_id = created_pet_id
        cls.name = "Bob_updated"
        cls.status = "sold"
        cls.photoUrls = ["https://youtube.com"]
        cls.tags = [{
            "id": randint(0, 10),
            "name": "Tag Test Updated"
        }]
        cls.category = {
            "id": randint(0, 10),
            "name": "dog updated"
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

    @classmethod
    def generate_updated_pet_invalid_id(cls):
        cls.pet_id = "qwe"
        cls.name = "Bob_updated"
        cls.status = "sold"
        cls.photoUrls = ["https://youtube.com"]
        cls.tags = [{
            "id": randint(0, 10),
            "name": "Tag Test Updated"
        }]
        cls.category = {
            "id": randint(0, 10),
            "name": "dog updated"
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

    @classmethod
    def generate_updated_pet_invalid_body(cls, created_pet):
        parsed_created_pet = json.loads(created_pet)
        created_pet_id = parsed_created_pet.get("id")

        cls.pet_id = created_pet_id
        cls.name = "Bob_updated"
        cls.status = "sold"
        cls.photoUrls = ["https://youtube.com"]
        cls.tags = [{
            "id": "qwe",
            "name": "Tag Test Updated"
        }]
        cls.category = {
            "id": randint(0, 10),
            "name": "dog updated"
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
