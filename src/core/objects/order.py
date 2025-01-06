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

    @staticmethod
    def generate_order():
        order = Order(
            randint(0, 10),
            randint(0, 10),
            randint(0, 10),
            "2023-06-26T15:38:10.849Z",
            "complete",
            bool(randint(0, 1))
        )

        return order


    @staticmethod
    def generate_invalid_order():
        order = Order(
            bool(randint(0, 1)),
            randint(0, 10),
            randint(0, 10),
            "2023-06-26T15:38:10.849Z",
            "complete",
            bool(randint(0, 1))

        )

        return order

    def to_json(self) -> str:
        order_json = {"id": self.order_id,
                      "petId": self.pet_id,
                      "quantity": self.quantity,
                      "shipDate": self.shipDate,
                      "status": self.status,
                      "complete": self.complete}

        return json.dumps(order_json)
