from src.core.baseAPI import BaseAPI
from src.core.objects.order import Order
from requests.api import get, post, delete


class StoreService:
    store_url = f"{BaseAPI.base_url}store/order/"
    inventory_url = f"{BaseAPI.base_url}store/inventory/"
    order = Order.generate_order()
    headers = BaseAPI.headers

    def get_inventory(self):
        return get(url=self.inventory_url, headers=self.headers)

    def get_order(self, order_id):
        return get(url=self.store_url + f"{order_id}", headers=self.headers)

    def create_order(self):
        return post(url=self.store_url, data=self.order, headers=self.headers)

    def delete_order(self, order_id):
        return delete(url=self.store_url + f"{order_id}", headers=self.headers)
