from faker import Faker
from random import randint, random

from src.core.objects.user import User


class PetData:
    #null excluded for now
    #expect E500 for invalid data
    fake = Faker()

    name = ["", fake.name()]
    invalid_name = [[], {}]

    photo_urls = ["", fake.url()]
    invalid_photo_urls = [[], {}]

    id = [randint(1, 1000), 1.2] #float is floored
    invalid_id = [[], {}, "!@", "qwe"]

    category = [{"gender": fake.passport_gender(0)}] #dict is 200
    invalid_category = [{"qwe": "qwe"}, randint(1, 1000), 1.2, "qwe", [], {}] #dict is 200

    category_id = [randint(1, 1000), 1.2] #except float is 200 and floored
    invalid_category_id = [[], {}, "qwe", "1@"]

    category_name = [randint(1, 1000), 1.2, fake.name()] #float is floored
    invalid_category_name = [[], {}, randint(1, 1000), 1.2]

    tags = [{"firstname": fake.name()}] #dict is 200
    invalid_tags = [randint(1, 1000), 1.2, "qwe", [], {}]

    tags_id = [randint(1, 1000), 1.2] #float is floored
    invalid_tags_id = [[], {}, "qwe", "!@"]

    tags_name = [randint(1, 1000), 1.2, fake.name()] #float is floored
    invalid_tags_name = [[], {}]

    status = ["available", "pending", "sold"]
    invalid_status = ["123", "test", "!@", "123.2", ""]

    form_name = []
    invalid_form_name = []

    form_data = []
    invalid_form_data = []

class OrderData:
    #null excluded for now
    #expect E500 for invalid data
    fake = Faker()

    id = [randint(1, 1000), 1.2, ""] #empty string sets id to random
    invalid_id = [[], {}, "@1", "qwe", ""]

    pet_id = [randint(1, 1000), 1.2] #float is floored
    invalid_pet_id = [[], {}, "@1", "qwe"] #empty string sets id to 0

    quantity = [randint(1, 1000), 1.2] #float is floored
    invalid_quantity = [[], {}, "@1", "qwe"] #empty string sets id to 0

    ship_date = ["2024-12-02T11:22:47.641Z", randint(1, 1000)] #int sets default timestamp 1970 + mil sec
    invalid_ship_date = [[], {}, "@1", "qwe", 3.5]

    status = ["placed", "", randint(1, 1000), 1.2] #int and float are 200 (passed as string)
    invalid_statuses = [[], {}]

    complete = [0, 1, "True", "False", ""] #empty string sets to False. #int > 1 sets to True
    invalid_complete = [[], {}, "@1", "qwe", 3.5]

class UserData:
    # null excluded for now
    # expect E500 for invalid data
    fake = Faker()

    id = [randint(1, 1000), 2.2] #float is floored
    invalid_id = [[], {}, "1@", "qwe"]

    username = ["", fake.user_name(), randint(1, 1000), 2.2] #int and float are passed as string
    invalid_username = [[], {}]

    firstname = ["", fake.first_name(), randint(1, 1000), 2.2] #int and float are passed as string
    invalid_firstname = [[], {}]

    lastname = ["", fake.last_name(), randint(1, 1000), 2.2] #int and float are passed as string
    invalid_lastname = [[], {}]

    email = ["", fake.email(), randint(1, 1000), 2.2] #int and float are passed as string
    invalid_email = [[], {}]

    password = ["", fake.password(), randint(1, 1000), 2.2] #int and float are passed as string
    invalid_password = [[], {}]

    phone = ["1234567", 1234567, 1234567.2, "qwe", "1@"] #int and float are passed as string
    invalid_phone = [[], {}]

    user_status = [randint(1, 10), 3.4] #float is floored
    invalid_user_status = [[], {}, "qwe", "true", "false"]


def generate_user(ids):
    user = User(
    ids,
    randint(0, 1),
    Faker().user_name(),
    Faker().first_name(),
    Faker().last_name(),
    Faker().password(),
    Faker().email(),
    Faker().phone_number()
    )

    return user