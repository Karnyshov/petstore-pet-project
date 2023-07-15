def test_get_inventory(store_service):
    response = store_service.get_inventory()
    assert 200 == response.status_code
    assert {} != response.json()


def test_create_order(store_service):
    response = store_service.create_order()
    assert 200 == response.status_code


def test_get_order_by_id(store_service):
    created_order = store_service.create_order()
    parsed_created_order = created_order.json()
    created_order_id = parsed_created_order.get("id")
    response = store_service.get_order(created_order_id)
    assert 200 == response.status_code
    assert created_order_id == response.json().get("id")
