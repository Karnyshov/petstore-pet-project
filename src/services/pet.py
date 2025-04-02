from src.core.baseAPI import BaseAPI
from src.core.objects.pet import Pet
from requests.api import get, post, put, delete
import logging


class PetService:
    pet_url = f"{BaseAPI.base_url}pet/"
    find_by_status_url = f"{pet_url}findByStatus?status"

    headers = BaseAPI.headers

    def get_pet(self, pet_id):
        logging.info(f"GET request to {self.pet_url} with ID: {pet_id}")
        return get(url=self.pet_url + f"{pet_id}", headers=self.headers)

    def find_by_status(self, status):
        logging.info(f"GET request to {self.find_by_status_url} with status: {status}")
        return get(url=self.find_by_status_url + f"{status}", headers=self.headers)

    def create_pet(self, pet):
        logging.info(f"POST request to {self.pet_url} with data: {pet}")
        return post(url=self.pet_url, data=pet, headers=self.headers)

    def update_pet(self, pet_updated):
        logging.info(f"PUT request to {self.pet_url} with ID: {pet_updated}")
        return put(url=self.pet_url, data=pet_updated, headers=self.headers)

    def update_pet_form(self, pet_id, update_data):
        logging.info(f"Updating Pet using form-data with URL: {self.pet_url}{pet_id} and data: {update_data}")
        return post(url=self.pet_url + f"{pet_id}", data=update_data)

    def delete_pet(self, pet_id):
        logging.info(f"DELETE request to {self.pet_url} with ID: {pet_id}")
        return delete(url=self.pet_url + f"{pet_id}", headers=self.headers)

    @staticmethod
    def update_pets(created_pet, pet):
        logging.info(f"Updating pet: {created_pet} with data: {pet}")
        pet.pet_id = created_pet
        return pet

    @staticmethod
    def update_single_pet(created_pet):
        logging.info(f"Updating pet: {created_pet}")
        return Pet(pet_id=created_pet.pet_id)
