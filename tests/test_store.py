import pytest
from pytest_check import check_functions as cf
from conftest import store_service, valid_order, parsed_order, invalid_order
from src.test_data.test_data_store import generated_orders, generated_invalid_orders, random_string

class TestStore:
    def test_get_inventory(self, store_service):
        response = store_service.get_inventory()
        assert 200 == response.status_code
        assert {} != response.json()

    def test_create_order(self, store_service, valid_order):
        response = store_service.create_order(valid_order.to_json())
        assert 200 == response.status_code
        parsed_response = response.json()
        cf.equal(valid_order.order_id, parsed_response.get("id"))
        cf.equal(valid_order.pet_id, parsed_response.get("petId"))
        cf.equal(valid_order.quantity, parsed_response.get("quantity"))
        cf.equal(valid_order.shipDate, parsed_response.get("shipDate"))
        cf.equal(valid_order.status, parsed_response.get("status"))
        cf.equal(valid_order.complete, parsed_response.get("complete"))

    @pytest.mark.parametrize("order", generated_orders)
    def test_create_param_order(self, store_service, order):
        response = store_service.create_order(order.to_json())
        assert 200 == response.status_code
        parsed_response = response.json()
        cf.equal(order.order_id, parsed_response.get("id"))
        cf.equal(order.pet_id, parsed_response.get("petId"))
        cf.equal(order.quantity, parsed_response.get("quantity"))
        cf.equal(order.shipDate, parsed_response.get("shipDate"))
        cf.equal(order.status, parsed_response.get("status"))
        cf.equal(order.complete, parsed_response.get("complete"))

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

    # return 404 instead of 400
    @pytest.mark.xfail
    def test_get_order_by_invalid_id(self, store_service):
        response = store_service.get_order(random_string)
        assert 400 == response.status_code

    # Flaky. Duplicates test_get_deleted_order
    @pytest.mark.xfail
    def test_get_absent_order(self, store_service):
        response = store_service.get_order(0)
        assert 404 == response.status_code

    def test_delete_order(self, store_service, valid_order, create_valid_order):
        response = store_service.delete_order(valid_order.order_id)
        assert 200 == response.status_code
        parsed_response = response.json()
        assert parsed_response.get("message") == str(valid_order.order_id)

    # Flaky
    @pytest.mark.xfail
    def test_delete_deleted_order(self, store_service, parsed_order):
        created_order_id = parsed_order.get("id")
        store_service.delete_order(created_order_id)
        response = store_service.delete_order(created_order_id)
        assert 404 == response.status_code

    # Flaky
    @pytest.mark.xfail
    def test_get_deleted_order(self, store_service, parsed_order):
        created_order_id = parsed_order.get("id")
        store_service.delete_order(created_order_id)
        response = store_service.get_order(created_order_id)
        assert 404 == response.status_code
