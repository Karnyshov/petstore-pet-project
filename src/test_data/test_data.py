import random

from faker import Faker
from random import randint, uniform, choices, choice
import string

fake = Faker()

def random_username():
    return fake.user_name()

def random_string(length = 10):
    rand_str = ''.join(choices(string.ascii_letters + string.digits, k=length))
    return rand_str

def random_int(minimal = 1, maximum = 1000):
    return randint(minimal, maximum)

def random_float(minimal = 1.0, maximum = 1000.0):
    return uniform(minimal, maximum)

def random_invalid_username():
    return random.choice([[], {}])

order_data = [
        #empty string sets id to random for id, sets id to 0 for pet_id, quantity
        #float is floored for id, pet_id, quantity
        #int and float are 200 (passed as string) for status
        #int sets default timestamp 1970 + mil sec for ship_date
        {"id": "", "pet_id": "", "quantity": "", "ship_date": fake.iso8601(end_datetime=fake.future_datetime()),
         "status": "", "complete": ""},
        {"id": random_int(), "pet_id": random_int(), "quantity": random_int(), "ship_date": random_int(),
         "status": "placed", "complete": 0},
        {"id": random_float(), "pet_id": random_float(), "quantity": random_float(), "ship_date": None,
         "status": random_int(), "complete": 1}, #float is floored
        {"id": None, "pet_id": None, "quantity": None, "ship_date": None,
         "status": random_float(), "complete": "True"},
        {"id": None, "pet_id": None, "quantity": None, "ship_date": None,
         "status": None, "complete": "False"},
    ]

pet_data = [
    {"name": "", "photo_urls": "", "id": random_int(),
     "category": {
         "category_id": random_int(),
         "category_name": random_int()
     },
     "tags": {
         "tags_id": random_int(),
         "tags_name": random_int()
     },
     "status": "available"
     },
    {"name": fake.name(), "photo_urls": fake.url(), "id": random_float(),
     "category": {
         "category_id": random_float(),  # float is 200 and floored
         "category_name": random_float()  # float is 200 and floored
     },
     "tags": {
         "tags_id": random_float(),  # float is floored
         "tags_name": random_float()  # float is floored
     },
     "status": "pending"},
    {"name": None, "photo_urls": None, "id": None,
     "category": {
         "category_id": None,
         "category_name": fake.name()
     },
     "tags": {
         "tags_id": None,
         "tags_name": fake.name()
     },
     "status": "sold"}
]

user_data = [
        # float is floored for id, status
        # int and float are passed as string for username, firstname, lastname, email, password, phone
        {"id": random_int(), "username": "", "first_name": "", "last_name": "", "email": "", "password": "",
         "phone": fake.phone_number(), "user_status": random_int()},
        {"id": random_float(), "username": fake.user_name(), "first_name": fake.first_name(),
         "last_name": fake.last_name(), "email": fake.email(), "password": fake.password(), "phone": random_int(),
         "user_status": random_float()},
        {"id": None, "username": random_int(), "first_name": random_int(),
         "last_name": random_int(), "email": random_int(), "password": random_int(), "phone": random_float(),
         "user_status": None},
        {"id": None, "username": random_float(), "first_name": random_float(), "last_name": random_float(),
         "email": random_float(), "password": random_float(), "phone": random_string(), "user_status": None}
    ]

invalid_user_random = {
    # null excluded for now
    # expect E500 for invalid data
    "id": [random_string(), [], {}], "username": [[], {}], "first_name": [[], {}], "last_name": [[], {}],
    "email": [[], {}], "password": [[], {}], "phone": [[], {}], "user_status": [random_string(), [], {}]
}

invalid_user_data = [
    # null excluded for now
    # expect E500 for invalid data
        {"id": random_string(), "username": [], "first_name": [], "last_name": [], "email": [], "password": [],
         "phone": [], "user_status": random_string()},
        {"id": [], "username": {}, "first_name": {}, "last_name": {}, "email": {}, "password": {},
        "phone": {}, "user_status": []},
        {"id": {}, "username": None, "first_name": None, "last_name": None, "email": None, "password": None,
        "phone": None, "user_status": {}}
]