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


    @staticmethod
    def to_json(order) -> str:
        order_json = {"id": order.order_id,
                      "petId": order.pet_id,
                      "quantity": order.quantity,
                      "shipDate": order.shipDate,
                      "status": order.status,
                      "complete": order.complete}

        return json.dumps(order_json)
