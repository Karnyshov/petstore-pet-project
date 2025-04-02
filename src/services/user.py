import json

from src.core.baseAPI import BaseAPI
from src.core.objects.user import User
from requests.api import get, post, put, delete
import logging

class UserService:
    user_url = f"{BaseAPI.base_url}user/"
    login_url = f"{user_url}login"
    logout_url = f"{user_url}logout"
    create_with_array_url = f"{user_url}createWithArray"
    create_with_list_url = f"{user_url}createWithList"

    headers = BaseAPI.headers

    # TODO: Try filtering using separate Logger object (e.g. log.py)
    @staticmethod
    def filter_sensitive_data(request_data):
        data = json.loads(request_data)
        data["password"] = "***"
        data["email"] = "***"
        data["phone"] = "***"
        return data

    def get_user(self, username):
        logging.info(f"GET request to {self.user_url} with username: {username}")
        return get(url=self.user_url + f"{username}", headers=self.headers)

    def create_user(self, user):
        logging.info(f"POST request to {self.user_url} with data: {self.filter_sensitive_data(user)}")
        return post(url=self.user_url, data=user, headers=self.headers)

    def update_user(self, username, user_updated):
        logging.info(f"PUT request to {self.user_url}{username} with data: {user_updated}")
        return put(url=self.user_url + f"{username}", data=user_updated, headers=self.headers)

    def delete_user(self, username):
        logging.info(f"DELETE request to {self.user_url}{username}")
        return delete(url=self.user_url + f"{username}", headers=self.headers)

    def login_user(self, username, password):
        logging.info(f"GET request to login: {self.login_url} with username: {username}")
        return get(url=self.login_url + f"?username={username}&password={password}", headers=self.headers)

    def logout_user(self):
        logging.info(f"GET request to logout: {self.logout_url}")
        return get(url=self.logout_url, headers=self.headers)

    #TODO: implement tests
    def create_user_with_list(self, user_list):
        logging.info(f"POST creating users using list with URL: {self.user_url} and data: {user_list}")
        return post(url=self.user_url, data=user_list, headers=self.headers)

    #TODO: implement tests
    def create_user_with_array(self, user_array):
        logging.info(f"POST creating users using array with URL: {self.user_url} and data: {user_array}")
        return post(url=self.user_url, data=user_array, headers=self.headers)

    @staticmethod
    def updating_user(created_user):
        logging.info(f"updating user: {created_user.username}")
        return User(username=created_user.username)

    @staticmethod
    def updating_users(created_user, user):
        logging.info(f"valid case, updating user: {created_user} with data: {user}")
        user.username = created_user
        return user

    @staticmethod
    def invalid_update_user(created_user, user):
        logging.info(f"invalid case, updating user: {created_user} with data: {user}")
        user.username = created_user.username
        return user