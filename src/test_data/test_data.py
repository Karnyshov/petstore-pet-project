import random
from faker import Faker
from random import randint, uniform
import string
from src.core.objects.user import User

fake = Faker()

def generate_random_string(length = 10):
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    return random_string

def random_int(minimal = 1, maximum = 1000):
    return randint(minimal, maximum)

def random_float(minimal = 1.0, maximum = 1000.0):
    return uniform(minimal, maximum)


class PetData:
    #null excluded for now
    #expect E500 for invalid data
    fake = Faker()

    name = ["", fake.name()]
    invalid_name = [[], {}]

    photo_urls = ["", fake.url()]
    invalid_photo_urls = [[], {}]

    id = [random_int(), random_float()] #float is floored
    invalid_id = [[], {}, generate_random_string()]

    category = [{"gender": fake.passport_gender(0)}] #dict is 200
    invalid_category = [{generate_random_string(): generate_random_string()}, random_int(), random_float(), generate_random_string(), [], {}] #dict is 200

    category_id = [random_int(), random_float()] #except float is 200 and floored
    invalid_category_id = [[], {}, generate_random_string()]

    category_name = [random_int(), random_float(), fake.name()] #float is floored
    invalid_category_name = [[], {}, random_int(), random_float()]

    tags = [{"firstname": fake.name()}] #dict is 200
    invalid_tags = [random_int(), random_float(), generate_random_string(), [], {}]

    tags_id = [random_int(), random_float()] #float is floored
    invalid_tags_id = [[], {}, generate_random_string()]

    tags_name = [random_int(), random_float(), fake.name()] #float is floored
    invalid_tags_name = [[], {}]

    status = ["available", "pending", "sold"]
    invalid_status = [generate_random_string(), ""]

    form_name = []
    invalid_form_name = []

    form_data = []
    invalid_form_data = []

class OrderData:
    #null excluded for now
    #expect E500 for invalid data
    fake = Faker()

    id = [random_int(), random_float(), ""] #empty string sets id to random
    invalid_id = [[], {}, generate_random_string(), ""]

    pet_id = [random_int(), random_float()] #float is floored
    invalid_pet_id = [[], {}, generate_random_string()] #empty string sets id to 0

    quantity = [random_int(), random_float()] #float is floored
    invalid_quantity = [[], {}, generate_random_string()] #empty string sets id to 0

    ship_date = [fake.iso8601(end_datetime=fake.future_datetime()), random_int()] #int sets default timestamp 1970 + mil sec
    invalid_ship_date = [[], {}, generate_random_string(), random_float()]

    status = ["placed", "", random_int(), random_float()] #int and float are 200 (passed as string)
    invalid_statuses = [[], {}]

    complete = [0, 1, "True", "False", ""] #empty string sets to False. #int > 1 sets to True
    invalid_complete = [[], {}, generate_random_string(), random_float()]

class UserData:
    # null excluded for now
    # expect E500 for invalid data
    #fake = Faker()

    id = [random_int(), random_float()] #float is floored
    invalid_id = [[], {}, generate_random_string()]

    username = ["", fake.user_name(), random_int(), random_float()] #int and float are passed as string
    invalid_username = [[], {}]

    firstname = ["", fake.first_name(), random_int(), random_float()] #int and float are passed as string
    invalid_firstname = [[], {}]

    lastname = ["", fake.last_name(), random_int(), random_float()] #int and float are passed as string
    invalid_lastname = [[], {}]

    email = ["", fake.email(), random_int(), random_float()] #int and float are passed as string
    invalid_email = [[], {}]

    password = ["", fake.password(), random_int(), random_float()] #int and float are passed as string
    invalid_password = [[], {}]

    phone = [fake.phone_number(), random_int(), random_float(), generate_random_string()] #int and float are passed as string
    invalid_phone = [[], {}]

    user_status = [random_int(), random_float()] #float is floored
    invalid_user_status = [[], {}, generate_random_string(), "true", "false"]


# def generate_user(phone_number, password):
#     user = User(
#     randint(1, 1000),
#     randint(0, 1),
#     Faker().user_name(),
#     Faker().first_name(),
#     Faker().last_name(),
#     password,
#     Faker().email(),
#     phone_number
#     )
#
#     return user

# def generate_users():
#     return [
#         User(phone=UserData.phone, password=UserData.password)
#     ]
#
# users = generate_users()

def auto_generate_users():
    user_test_data = [
        {"id": random_int(), "username": "", "first_name": "", "last_name": "", "email": "", "password": "",
         "phone": fake.phone_number(), "user_status": random_int()},
        {"id": random_float(), "username": fake.user_name(), "first_name": fake.first_name(),
         "last_name": fake.last_name(), "email": fake.email(), "password": fake.password(), "phone": random_int(),
         "user_status": random_float()},
        {"id": None, "username": random_int(), "first_name": random_int(),
         "last_name": random_int(), "email": random_int(), "password": random_int(), "phone": random_float(),
         "user_status": None},
        {"id": None, "username": random_float(), "first_name": random_float(), "last_name": random_float(),
         "email": random_float(), "password": random_float(), "phone": generate_random_string(), "user_status": None}
    ]

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

generated_users = auto_generate_users()