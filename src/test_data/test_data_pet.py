import random
from src.test_data.test_data_generation import auto_generate_pets, generate_updated_pets, generate_invalid_pet, generate_form_data_pet, generate_invalid_form_data_pet, fake, random_string, random_float, random_int

def random_pet_status():
    return random.choice(["available", "pending", "sold"])

pet_status = ["available", "pending", "sold"]
invalid_pet_status = [random_string(), ""]
invalid_pet_id = [[], {}, random_string()]

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
    {"name": fake.name(), "photo_urls": fake.url(), "id": random_int(),
     "category": {
         "id": random_int(),
         "name": fake.name()
     },
     "tags": [{
         "id": random_int(),
         "name": fake.name()
     }],
     "status": "sold"},
    {"name": fake.name(), "photo_urls": fake.url(), "id": random_int(), "category": {random_string(): random_string()}, #dict is 200
     "tags": [{random_string(): random_string()}], "status": "sold"} #dict is 200
]

invalid_pet_data = [
    # null excluded for now
    # expect E500 for invalid data
    # E500 via Postman, PASS using automation {"name": [], "photo_urls": [], "id": [], "category": [], "tags": [], "status": ""},
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

pet_form_data = [
    {"name": fake.name(),
     "status": random_pet_status()
    },
    {"name": random_string(),
     "status": random_pet_status()
    },
    {"name": random_int(),
     "status": random_pet_status()
    },
    {"name": random_float(),
     "status": random_pet_status()
    },
    {"name": [],
     "status": random_pet_status()
    },
    {"name": {},
     "status": random_pet_status()
    },
    {"name": fake.name(),
     "status": random_string()
    },
    {"name": fake.name(),
     "status": random_int()
    },
    {"name": fake.name(),
     "status": random_float()
    },
    {"name": fake.name(),
     "status": []
    },
    {"name": fake.name(),
     "status": {}
    }
]

# invalid data doesn't update the object
invalid_pet_form_data = [
    {
        random_int(): fake.name(),
        "status": random_pet_status()
    },
    {
        random_float(): fake.name(),
        "status": random_pet_status()
    },
    {
        random_string(): fake.name(),
        "status": random_pet_status()
    },
    {
        "name": fake.name(),
        random_int(): random_pet_status()
    },
    {
        "name": fake.name(),
        random_float(): random_pet_status()
    },
    {
        "name": fake.name(),
        random_string(): random_pet_status()
    }
]

invalid_pet_form_data_random = {
    "name" : [random_int(), random_float(), random_string()],
    "status" : [random_int(), random_float(), random_string()]
}

generated_pets = auto_generate_pets(pet_data)
generated_invalid_pets = auto_generate_pets(invalid_pet_data)
generated_updated_pets = generate_updated_pets(pet_test_data=pet_data)
generated_invalid_pet = generate_invalid_pet(invalid_pet_random)
generated_pet_form_data = generate_form_data_pet(random_pet_status(), fake.name())
generated_invalid_pet_form_data = generate_invalid_form_data_pet(invalid_pet_form_data_random, random_pet_status(), fake.name())
