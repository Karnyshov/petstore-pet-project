from src.core.baseAPI import BaseAPI
from src.core.objects.user import User
from requests.api import get, post, put, delete

class UserService:
    user_url = f"{BaseAPI.base_url}user/"
    login_url = f"{user_url}login"
    logout_url = f"{user_url}logout"
    create_with_array_url = f"{user_url}createWithArray"
    create_with_list_url = f"{user_url}createWithList"

    headers = BaseAPI.headers

    def get_user(self, username):
        return get(url=self.user_url + f"{username}", headers=self.headers)

    def create_user(self, user):
        return post(url=self.user_url, data=user, headers=self.headers)

    def update_user(self, username, user_updated):
        return put(url=self.user_url + f"{username}", data=user_updated, headers=self.headers)

    def delete_user(self, username):
        return delete(url=self.user_url + f"{username}", headers=self.headers)

    def login_user(self, username, password):
        return get(url=self.login_url + f"?username={username}&password={password}", headers=self.headers)

    def logout_user(self):
        return get(url=self.logout_url, headers=self.headers)

    def create_user_with_list(self, user_list):
        return post(url=self.user_url, data=user_list, headers=self.headers)

    def create_user_with_array(self, user_array):
        return post(url=self.user_url, data=user_array, headers=self.headers)

    @staticmethod
    def updating_user(created_user):
        return User(username=created_user.username)

    @staticmethod
    def updating_users(created_user, user):
        user.username = created_user
        return user

    @staticmethod
    def invalid_update_user(created_user, user):
        user.username = created_user.username
        return user