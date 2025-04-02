import logging
import random
from src.core.objects.order import Order
from src.core.objects.pet import Pet
from src.core.objects.user import User
from faker import Faker
from random import randint, uniform, choices
import string


fake = Faker()

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler()  # Ensure logs are output to console
handler.setLevel(logging.DEBUG)

if not logger.handlers:  # Prevent duplicate logs
    logger.addHandler(handler)

logger.propagate = False  # Ensure pytest does not block the logs


def random_int(minimal=1, maximum=1000):
    return randint(minimal, maximum)


def random_float(minimal=1.0, maximum=1000.0):
    return uniform(minimal, maximum)


def random_string(length=10):
    rand_str = ''.join(choices(string.ascii_letters + string.digits, k=length))
    return rand_str


def auto_generate_orders(order_test_data):
    logging.info("Generating list of Order test data")
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
    logger.info("Generating invalid Order test data")
    return Order(
        order_id=random.choice(test_data.get("id")),
        pet_id=random.choice(test_data.get("pet_id")),
        quantity=random.choice(test_data.get("quantity")),
        shipDate=random.choice(test_data.get("ship_date")),
        status=random.choice(test_data.get("status")),
        complete=random.choice(test_data.get("complete"))
    )


def auto_generate_pets(pet_test_data):
    logger.info("Generating list of Pet test data")
    auto_generated_pets = []

    for test_data in pet_test_data:
        auto_generated_pets.append(
            Pet(
                name=test_data.get("name"),
                photoUrls=test_data.get("photo_urls"),
                pet_id=test_data.get("id"),
                category=test_data.get("category"),
                tags=test_data.get("tags"),
                status=test_data.get("status")
            )
        )

    return auto_generated_pets


def generate_updated_pets(pet_test_data, petId=None):
    logger.info("Generating list of updated Pet test data")
    auto_generated_updated_pets = []

    for test_data in pet_test_data:
        auto_generated_updated_pets.append(
            Pet(
                name=test_data.get("name"),
                photoUrls=test_data.get("photo_urls"),
                pet_id=petId,
                category=test_data.get("category"),
                tags=test_data.get("tags"),
                status=test_data.get("status")
            )
        )

    return auto_generated_updated_pets


def generate_invalid_pet(test_data):
    logger.info("Generating invalid Pet test data")
    return Pet(
        name=random.choice(test_data.get("name")),
        photoUrls=random.choice(test_data.get("photo_urls")),
        pet_id=random.choice(test_data.get("id")),
        category=random.choice(test_data.get("category")),
        tags=random.choice(test_data.get("tags")),
        status=random.choice(test_data.get("status"))
    )


def generate_form_data_pet(pet_status, name):
    logger.info(f"Generating valid random data for form-data request: {name}, {pet_status}")
    return {"name": name, "status": pet_status}


def generate_invalid_form_data_pet(invalid_form_data, pet_status, name):
    logger.info(f"Generating invalid random data for form-data request: {name}, {pet_status}")
    return {
        random.choice(invalid_form_data.get("name")): name,
        random.choice(invalid_form_data.get("status")): pet_status
    }


def auto_generate_users(user_test_data):
    logger.debug("Generating list of User test data")
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


def auto_generate_updated_users(user_test_data, username=None):
    logger.info("Generating list of updated User test data")
    auto_generated_updated_users = []

    for test_data in user_test_data:
        auto_generated_updated_users.append(
            User(
                user_id=test_data.get("id"),
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
    logger.info("Generating invalid User test data")
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
