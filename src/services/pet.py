from src.core.baseAPI import BaseAPI
from src.core.objects.pet import Pet
from requests.api import get, post, put, delete


class PetService:
    pet_url = f"{BaseAPI.base_url}pet/"
    pet = Pet.generate_pet()
    headers = BaseAPI.headers

    def get_pet(self, pet_id):
        return get(url=self.pet_url + f"{pet_id}", headers=self.headers)

    def create_pet(self):
        return post(url=self.pet_url, data=self.pet, headers=self.headers)

    def update_pet(self, pet_id):
        return put(url=self.pet_url + f"{pet_id}", data=self.pet, headers=self.headers)

    def delete_pet(self, pet_id):
        return delete(url=self.pet_url + f"{pet_id}", headers=self.headers)
