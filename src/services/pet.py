from src.core.baseAPI import BaseAPI
from src.core.objects.pet import Pet
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

    def update_pet_form(self, pet_id, update_data):
        return post(url=self.pet_url + f"{pet_id}", data=update_data)

    def delete_pet(self, pet_id):
        return delete(url=self.pet_url + f"{pet_id}", headers=self.headers)

    @staticmethod
    def form_data():
        return Pet.generate_pet_update_form_data()

    @staticmethod
    def update_valid_pet(pet_to_update):
        return Pet.update_pet(pet_to_update)

    @staticmethod
    def update_pet_invalid_id():
        return Pet.update_pet_invalid_id()

    @staticmethod
    def update_pet_invalid_body(pet_to_update):
        return Pet.update_pet_invalid_body(pet_to_update)