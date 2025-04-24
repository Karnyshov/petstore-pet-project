from random import randint
from typing import Any, Union
from dataclasses import dataclass
import json

#TODO: add fake ship date
@dataclass
class Order:
    order_id: Union[int, Any] = randint(1, 1000)
    pet_id: Union[int, Any] = randint(5, 10)
    quantity: Union[int, Any] = randint(10, 15)
    shipDate: str = "2024-12-02T11:22:47.641Z"
    status: str = "placed"
    complete: Union[bool, Any] = randint(0, 1)

    def to_json(self) -> str:
        order_json = {"id": self.order_id,
                      "petId": self.pet_id,
                      "quantity": self.quantity,
                      "shipDate": self.shipDate,
                      "status": self.status,
                      "complete": self.complete}

        return json.dumps(order_json)
