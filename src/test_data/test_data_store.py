from src.test_data.test_data_generation import auto_generate_orders, generate_invalid_order, fake, random_string, random_float, random_int

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
        {"id": random_float(), "pet_id": random_float(), "quantity": random_float(),
         "ship_date": fake.iso8601(end_datetime=fake.future_datetime()), "status": random_int(),
         "complete": 1}, #float is floored
        {"id": random_int(), "pet_id": random_int(), "quantity": random_int(),
         "ship_date": fake.iso8601(end_datetime=fake.future_datetime()), "status": random_float(), "complete": "True"},
        {"id": random_int(), "pet_id": random_int(), "quantity": random_int(),
         "ship_date": fake.iso8601(end_datetime=fake.future_datetime()), "status": "placed", "complete": "False"}
    ]

invalid_order_data = [
    # null excluded for now
    # expect E500 for invalid data
        {"id": [], "pet_id": [], "quantity": [], "ship_date": [],
         "status": [], "complete": []},
        {"id": {}, "pet_id": {}, "quantity": {}, "ship_date": {},
         "status": {}, "complete": {}},
        {"id": random_string(), "pet_id": random_string(), "quantity": random_string(), "ship_date": random_string(),
         "status": "placed", "complete": random_string()},
        {"id": random_int(), "pet_id": random_int(), "quantity": random_int(), "ship_date": random_float(),
         "status": "placed", "complete": random_float()}
]

invalid_order_random = {
    # null excluded for now
    # expect E500 for invalid data
    "id": [[], {}, random_string()], "pet_id": [[], {}, random_string()], "quantity": [[], {}, random_string()],
     "ship_date": [[], {}, random_string(), random_float()], "status": [[], {}, random_float()],
     "complete": [[], {}, random_string(), random_float()]
}

generated_orders = auto_generate_orders(order_data)
generated_invalid_orders = auto_generate_orders(invalid_order_data)
generated_invalid_order = generate_invalid_order(invalid_order_random)
