import random
from faker import Faker
from random import randint, uniform, choices
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

def random_pet_status():
    return random.choice(["available", "pending", "sold"])

pet_status = ["available", "pending", "sold"]
invalid_pet_status = [random_string(), ""]
invalid_pet_id = [[], {}, random_string()]

order_data = [
        #empty string sets id to random for id, sets id to 0 for pet_id, quantity
        #empty string sets to False. #int > 1 sets to True for complete
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
         "status": None, "complete": "False"}
    ]

invalid_order_data = [
    # null excluded for now
    # expect E500 for invalid data
        {"id": [], "pet_id": [], "quantity": [], "ship_date": [],
         "status": [], "complete": []},
        {"id": {}, "pet_id": {}, "quantity": {}, "ship_date": {},
         "status": {}, "complete": {}},
        {"id": random_string(), "pet_id": random_string(), "quantity": random_string(), "ship_date": random_string(),
         "status": None, "complete": random_string()},
        {"id": None, "pet_id": None, "quantity": None, "ship_date": random_float(),
         "status": None, "complete": random_float()}
]

invalid_order_random = {
    # null excluded for now
    # expect E500 for invalid data
    "id": [[], {}, random_string()], "pet_id": [[], {}, random_string()], "quantity": [[], {}, random_string()],
     "ship_date": [[], {}, random_string(), random_float()], "status": [[], {}, random_float()],
     "complete": [[], {}, random_string(), random_float()]
}

pet_data = [
    {"name": "", "photo_urls": [random_string()], "id": random_int(),
     "category": {
         "id": random_int(),
         "name": random_int()
     },
     "tags": [{
         "id": random_int(),
         "name": random_int()
     }],
     "status": "available"
     },
    {"name": fake.name(), "photo_urls": [fake.url()], "id": random_float(),
     "category": {
         "id": random_float(),  # float is 200 and floored
         "name": random_float()  # float is 200 and floored
     },
     "tags": [{
         "id": random_float(),  # float is floored
         "name": random_float()  # float is floored
     }],
     "status": "pending"},
    {"name": None, "photo_urls": None, "id": None,
     "category": {
         "id": None,
         "name": fake.name()
     },
     "tags": [{
         "id": None,
         "name": fake.name()
     }],
     "status": "sold"},
    {"name": None, "photo_urls": None, "id": None, "category": {random_string(): random_string()}, #dict is 200
     "tags": [{random_string(): random_string()}], "status": "sold"} #dict is 200
]

invalid_pet_data = [
    # null excluded for now
    # expect E500 for invalid data
    {"name": [], "photo_urls": [], "id": [], "category": [], "tags": [], "status": ""},
    {"name": {}, "photo_urls": {}, "id": {}, "category": {}, "tags": {}, "status": random_string()},
    {"name": fake.name(), "photo_urls": fake.url(), "id": random_string(), "category": random_int(),
     "tags": random_int(), "status": random_pet_status()},
    {"name": fake.name(), "photo_urls": fake.url(), "id": random_int(), "category": random_float(),
     "tags": random_float(), "status": random_pet_status()},
    {"name": fake.name(), "photo_urls": fake.url(), "id": random_int(), "category": random_string(),
     "tags": random_string(), "status": random_pet_status()},
    {"name": fake.name(), "photo_urls": fake.url(), "id": random_int(),
     "category": {
         "id": [],
         "name": []
     },
     "tags": {
         "id": [],
         "name": []
     },
     "status": random_pet_status()},
    {"name": fake.name(), "photo_urls": fake.url(), "id": random_int(),
     "category": {
         "id": {},
         "name": {}
     },
     "tags": {
         "id": {},
         "name": {}
     },
     "status": random_pet_status()},
    {"name": fake.name(), "photo_urls": fake.url(), "id": random_int(),
     "category": {
         "id": random_string(),
         "name": random_int()
     },
     "tags": {
         "id": random_string(),
         "name": fake.name()
     },
     "status": random_pet_status()}
]

invalid_pet_random = {
    # null excluded for now
    # expect E500 for invalid data
    # invalid_id = [[], {}, random_string()]
    # invalid_category_id, invalid_tags_id = [[], {}, random_string()]
    # invalid_category_name = [[], {}, random_int(), random_float()]
    # invalid_tags_name, invalid_name, invalid_photo_urls = [[], {}]
    # invalid_category, invalid_tags = [random_int(), random_float(), random_string(), [], {}]
    # invalid_status = [random_string(), ""]

    "name": [[], {}],
    "photo_urls": [[], {}],
    "id": [[], {}, random_string()],
    "category": [random_int(), random_float(), random_string(), [], {}],
    "tags": [random_int(), random_float(), random_string(), [], {}],
    "status": [random_string(), ""]
}

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