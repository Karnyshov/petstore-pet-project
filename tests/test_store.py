import pytest
from conftest import store_service, valid_order, parsed_order, invalid_order
from src.test_data.test_data_store import generated_orders, generated_invalid_orders

class TestStore:
    def test_get_inventory(self, store_service):
        response = store_service.get_inventory()
        assert 200 == response.status_code
        assert {} != response.json()

    def test_create_order(self, store_service, valid_order):
        response = store_service.create_order(valid_order.to_json())
        assert 200 == response.status_code

    @pytest.mark.parametrize("order", generated_orders)
    def test_create_param_order(self, store_service, order):
        response = store_service.create_order(order.to_json())
        assert 200 == response.status_code

    # returns 500 instead of 400
    @pytest.mark.xfail
    def test_create_invalid_order(self, store_service, invalid_order):
        response = store_service.create_order(invalid_order.to_json())
        assert 400 == response.status_code

    # returns 500 instead of 400
    @pytest.mark.parametrize("order", generated_invalid_orders)
    @pytest.mark.xfail
    def test_create_param_invalid_order(self, store_service, order):
        response = store_service.create_order(order.to_json())
        assert 400 == response.status_code

    def test_get_order_by_id(self, store_service, parsed_order):
        parsed_order_id = parsed_order.get("id")
        response = store_service.get_order(parsed_order_id)
        assert 200 == response.status_code
        assert parsed_order_id == response.json().get("id")

    # TODO: add more invalid cases
    # return 404 instead of 400
    @pytest.mark.xfail
    def test_get_order_by_invalid_id(self, store_service):
        response = store_service.get_order("qwe")
        assert 400 == response.status_code

    # TODO: add more cases for 404
    def test_get_absent_order(self, store_service):
        response = store_service.get_order(0)
        assert 404 == response.status_code

    def test_delete_order(self, store_service, parsed_order):
        created_order_id = parsed_order.get("id")
        response = store_service.delete_order(created_order_id)
        assert 200 == response.status_code

    def test_delete_deleted_order(self, store_service, parsed_order):
        created_order_id = parsed_order.get("id")
        store_service.delete_order(created_order_id)
        response = store_service.delete_order(created_order_id)
        assert 404 == response.status_code

    def test_get_deleted_order(self, store_service, parsed_order):
        created_order_id = parsed_order.get("id")
        store_service.delete_order(created_order_id)
        response = store_service.get_order(created_order_id)
        assert 404 == response.status_code
