from src.core.singleton import Singleton


class BaseAPI(Singleton):
    base_url = "https://petstore.swagger.io/v2/"
    headers = {"Content-Type": "application/json"}
