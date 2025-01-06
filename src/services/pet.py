from src.core.baseAPI import BaseAPI
from requests.api import get, post, put, delete


class PetService:
    pet_url = f"{BaseAPI.base_url}pet/"
    find_by_status_url = f"{pet_url}findByStatus?status"

    headers = BaseAPI.headers

    def get_pet(self, pet_id):
        return get(url=self.pet_url + f"{pet_id}", headers=self.headers)

    def find_by_status(self, status):
        return get(url=self.find_by_status_url + f"{status}", headers=self.headers)

    def create_pet(self, pet):
        return post(url=self.pet_url, data=pet, headers=self.headers)

    def update_pet(self, pet_updated):
        return put(url=self.pet_url, data=pet_updated, headers=self.headers)

    def delete_pet(self, pet_id):
        return delete(url=self.pet_url + f"{pet_id}", headers=self.headers)
