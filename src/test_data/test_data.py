from faker import Faker
from random import randint

class PetData:
    #null excluded for now
    #expect E500 for invalid data
    name = ["", "qwe", "1@"]
    invalid_name = [[], {}]

    photo_urls = ["", "qwe", "1@"]
    invalid_photo_urls = [[], {}]

    id = [1, 1.2] #float is floored
    invalid_id = [[], {}, "!@", "qwe"]

    category = [{"qwe": "qwe"}] #dict is 200
    invalid_category = [{"qwe": "qwe"}, 1, 1.2, "qwe", [], {}] #dict is 200

    category_id = [1, 1.2] #except float is 200 and floored
    invalid_category_id = [[], {}, "qwe", "1@"]

    category_name = [1, 1.2, "qwe", "1@"] #float is floored
    invalid_category_name = [[], {}, 1, 1.2]

    tags = [{"qwe": "qwe"}] #dict is 200
    invalid_tags = [1, 1.2, "qwe", [], {}]

    tags_id = [1, 1.2] #float is floored
    invalid_tags_id = [[], {}, "qwe", "!@"]

    tags_name = [1, 1.2, "qwe", "1@"] #float is floored
    invalid_tags_name = [[], {}]

    status = ["available", "pending", "sold"]
    invalid_status = ["123", "qwe", "test", "!@", "123.2", ""]

    form_name = []
    invalid_form_name = []

    form_data = []
    invalid_form_data = []

class OrderData:
    #null excluded for now
    #expect E500 for invalid data
    id = [1, 1.2, ""] #empty string sets id to random
    invalid_id = [[], {}, "@1", "qwe", ""]

    pet_id = [1, 1.2] #float is floored
    invalid_pet_id = [[], {}, "@1", "qwe"] #empty string sets id to 0

    quantity = [1, 1.2] #float is floored
    invalid_quantity = [[], {}, "@1", "qwe"] #empty string sets id to 0

    ship_date = ["2024-12-02T11:22:47.641Z", 2] #int sets default timestamp 1970 + mil sec
    invalid_ship_date = [[], {}, "@1", "qwe", 3.5]

    status = ["placed", "", "@1", 1, 1.2] #int and float are 200 (passed as string)
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
