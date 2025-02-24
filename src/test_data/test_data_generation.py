import random
from faker import Faker
from random import randint, uniform
import string

from core.objects.order import Order
from core.objects.pet import Pet
from src.core.objects.user import User
from test_data.test_data import pet_data, order_data, user_data, invalid_user_random, invalid_user_data, \
    random_invalid_username, invalid_order_data, invalid_order_random

fake = Faker()

def random_username():
    return fake.user_name()

def random_string(length = 10):
    rand_str = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    return rand_str

def random_int(minimal = 1, maximum = 1000):
    return randint(minimal, maximum)

def random_float(minimal = 1.0, maximum = 1000.0):
    return uniform(minimal, maximum)


class PetData:
    #null excluded for now
    #expect E500 for invalid data

    invalid_name = [[], {}]
    invalid_photo_urls = [[], {}]
    invalid_id = [[], {}, random_string()]

    category = [{"gender": fake.passport_gender(0)}] #dict is 200
    invalid_category = [{random_string(): random_string()}, random_int(), random_float(), random_string(), [], {}] #dict is 200

    invalid_category_id = [[], {}, random_string()]
    invalid_category_name = [[], {}, random_int(), random_float()]

    tags = [{"firstname": fake.name()}] #dict is 200
    invalid_tags = [random_int(), random_float(), random_string(), [], {}]

    invalid_tags_id = [[], {}, random_string()]
    invalid_tags_name = [[], {}]

    status = ["available", "pending", "sold"]
    invalid_status = [random_string(), ""]

    form_name = []
    invalid_form_name = []

    form_data = []
    invalid_form_data = []

def auto_generate_pets(pet_test_data):
    auto_generated_pets = []

    for test_data in pet_test_data:
        auto_generated_pets.append(
            Pet(
                name=test_data.get("name"),
                photoUrls=[test_data.get("photo_urls")],
                pet_id = test_data.get("id"),
                category=test_data.get("category"),
                tags = [test_data.get("tags")],
                status = test_data.get("status")
            )
        )

    return auto_generated_pets

def auto_generate_orders(order_test_data):
    auto_generated_orders = []

    for test_data in order_test_data:
        auto_generated_orders.append(
            Order(
                order_id=test_data.get("id"),
                pet_id=test_data.get("pet_id"),
                quantity=test_data.get("quantity"),
                shipDate=test_data.get("ship_date"),
                status=test_data.get("status"),
                complete=test_data.get("complete")
            )
        )

    return auto_generated_orders

def generate_invalid_order(test_data):
    return Order(
        order_id=random.choice(test_data.get("id")),
        pet_id=random.choice(test_data.get("pet_id")),
        quantity=random.choice(test_data.get("quantity")),
        shipDate=random.choice(test_data.get("ship_date")),
        status=random.choice(test_data.get("status")),
        complete=random.choice(test_data.get("complete"))
    )

def auto_generate_users(user_test_data):
    auto_generated_users = []

    for test_data in user_test_data:
        auto_generated_users.append(
            User(
                user_id=test_data.get("id"),
                username=test_data.get("username"),
                firstName=test_data.get("first_name"),
                lastName=test_data.get("last_name"),
                email=test_data.get("email"),
                password=test_data.get("password"),
                phone=test_data.get("phone"),
                userStatus=test_data.get("user_status")
            )
        )

    return auto_generated_users

def auto_generate_updated_users(username=None, user_test_data=user_data):
    auto_generated_updated_users = []

    for test_data in user_test_data:
        auto_generated_updated_users.append(
            User(
                user_id = test_data.get("id"),
                username=username,
                firstName=test_data.get("first_name"),
                lastName=test_data.get("last_name"),
                email=test_data.get("email"),
                password=test_data.get("password"),
                phone=test_data.get("phone"),
                userStatus=test_data.get("user_status")
            )
        )

    return auto_generated_updated_users

def generate_invalid_user(test_data):
    return User(
        user_id=random.choice(test_data.get("id")),
        username=random.choice(test_data.get("username")),
        firstName=random.choice(test_data.get("first_name")),
        lastName=random.choice(test_data.get("last_name")),
        email=random.choice(test_data.get("email")),
        password=random.choice(test_data.get("password")),
        phone=random.choice(test_data.get("phone")),
        userStatus=random.choice(test_data.get("user_status")),
    )

generated_pets = auto_generate_pets(pet_data)

generated_orders = auto_generate_orders(order_data)
generated_invalid_orders = auto_generate_orders(invalid_order_data)
generated_invalid_order = generate_invalid_order(invalid_order_random)

generated_invalid_user = generate_invalid_user(invalid_user_random)
generated_users = auto_generate_users(user_data)
generated_invalid_users = auto_generate_users(invalid_user_data)
generated_updated_users = auto_generate_updated_users(user_test_data=user_data)
generated_updated_invalid_users = auto_generate_updated_users(user_test_data=invalid_user_data)
generated_invalid_username = random_invalid_username()
generated_username = random_username()