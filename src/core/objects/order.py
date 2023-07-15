from random import randint
from dataclasses import dataclass
import json


@dataclass
class Order:
    order_id: int
    pet_id: int
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

        order_json = {"id": cls.order_id,
                      "petId": cls.pet_id,
                      "quantity": cls.quantity,
                      "shipDate": cls.shipDate,
                      "status": cls.status,
                      "complete": cls.complete}

        return json.dumps(order_json)
