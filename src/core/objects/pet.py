from dataclasses import dataclass, field
from typing import Union
from random import randint
from faker import Faker
import json


@dataclass
class Pet:
    pet_id: Union[int, dict, list, str] = randint(0, 10)
    name: Union[str, dict, list] = Faker().first_name()
    status: str = "available"
    photoUrls: Union[list, dict] = field(default_factory=lambda: [Faker().url()])
    tags: Union[list, dict, int, str, float] = field(default_factory=lambda: [{"id": randint(10, 20),
                   "firstname": Faker().name()}])
    category: Union[list, dict, int, str, float] = field(default_factory=lambda: {"id": randint(0, 10),
                      "gender": Faker().passport_gender(0)})


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
