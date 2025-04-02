from src.core.baseAPI import BaseAPI
from requests.api import get, post, delete

from utils.logger import logger


class StoreService:
    store_url = f"{BaseAPI.base_url}store/order/"
    inventory_url = f"{BaseAPI.base_url}store/inventory/"

    headers = BaseAPI.headers

    def get_inventory(self):
        logger.info(f"GET request to {self.inventory_url}")
        return get(url=self.inventory_url, headers=self.headers)

    def get_order(self, order_id):
        logger.info(f"GET request to {self.store_url} with ID: {order_id}")
        return get(url=self.store_url + f"{order_id}", headers=self.headers)

    def create_order(self, order):
        logger.info(f"POST request to {self.store_url} with data: {order}")
        return post(url=self.store_url, data=order, headers=self.headers)

    def create_invalid_order(self, invalid_order):
        logger.info(f"POST request to {self.store_url} with data: {invalid_order}")
        return post(url=self.store_url, data=invalid_order, headers=self.headers)

    def delete_order(self, order_id):
        logger.info(f"DELETE request to {self.store_url} with ID: {order_id}")
        return delete(url=self.store_url + f"{order_id}", headers=self.headers)
