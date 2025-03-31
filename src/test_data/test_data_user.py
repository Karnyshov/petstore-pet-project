import random
from src.test_data.test_data_generation import generate_invalid_user, auto_generate_users, auto_generate_updated_users, fake, random_string, random_float, random_int

def random_username():
    return fake.user_name()

def random_name():
    return fake.name()

def random_invalid_username():
    return random.choice([[], {}])

user_data = [
        # float is floored for id, status
        # int and float are passed as string for username, firstname, lastname, email, password, phone
        {"id": random_int(), "username": "", "first_name": "", "last_name": "", "email": "", "password": "",
         "phone": fake.phone_number(), "user_status": random_int()},
        {"id": random_float(), "username": fake.user_name(), "first_name": fake.first_name(),
         "last_name": fake.last_name(), "email": fake.email(), "password": fake.password(), "phone": random_int(),
         "user_status": random_float()},
        {"id": random_int(), "username": random_int(), "first_name": random_int(),
         "last_name": random_int(), "email": random_int(), "password": random_int(), "phone": random_float(),
         "user_status": random_int()},
        {"id": random_int(), "username": random_float(), "first_name": random_float(), "last_name": random_float(),
         "email": random_float(), "password": random_float(), "phone": random_string(), "user_status": random_int()}
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
        {"id": {}, "username": fake.user_name(), "first_name": fake.first_name(), "last_name": fake.last_name(),
         "email": fake.email(), "password": fake.password(),
        "phone": fake.phone_number(), "user_status": {}}
]

generated_invalid_user = generate_invalid_user(invalid_user_random)
generated_users = auto_generate_users(user_data)
generated_invalid_users = auto_generate_users(invalid_user_data)
generated_updated_users = auto_generate_updated_users(user_test_data=user_data)
generated_updated_invalid_users = auto_generate_updated_users(user_test_data=invalid_user_data)
generated_invalid_username = random_invalid_username()
generated_username = random_username()
