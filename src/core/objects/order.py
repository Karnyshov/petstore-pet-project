from random import randint
from typing import Any
from dataclasses import dataclass
import json


@dataclass
class Order:
    order_id: int
    pet_id: Any
    quantity: int
    shipDate: str
    status: str
    complete: bool

    @classmethod
    def generate_order(cls):
        cls.order_id = randint(0, 10)
        cls.pet_id = randint(0, 10)
        cls.quantity = randint(0, 10)
        cls.shipDate = "2023-06-26T15:38:10.849Z"
        cls.status = "complete"
        cls.complete = bool(randint(0, 1))

# TODO: move as function
        order_json = {"id": cls.order_id,
                      "petId": cls.pet_id,
                      "quantity": cls.quantity,
                      "shipDate": cls.shipDate,
                      "status": cls.status,
                      "complete": cls.complete}

        return json.dumps(order_json)

    @classmethod
    def generate_invalid_order(cls):
        cls.order_id = bool(randint(0, 1))
        cls.pet_id = randint(0, 10)
        cls.quantity = randint(0, 10)
        cls.shipDate = "2023-06-26T15:38:10.849Z"
        cls.status = "complete"
        cls.complete = bool(randint(0, 1))

# TODO: move as function
        order_json = {"id": cls.order_id,
                      "petId": cls.pet_id,
                      "quantity": cls.quantity,
                      "shipDate": cls.shipDate,
                      "status": cls.status,
                      "complete": cls.complete}

        return json.dumps(order_json)
