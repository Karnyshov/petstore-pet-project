import pytest

class TestStore:
    def test_get_inventory(self, store_service):
        response = store_service.get_inventory()
        assert 200 == response.status_code
        assert {} != response.json()

    def test_create_order(self, store_service):
        response = store_service.create_order(store_service.order_json)
        assert 200 == response.status_code

    # Service return 500 instead of 400
    @pytest.mark.xfail
    def test_create_invalid_order(self, store_service):
        response = store_service.create_invalid_order(store_service.invalid_order_json)
        assert 400 == response.status_code

    # TODO: reduce number of lines
    def test_get_order_by_id(self, store_service):
        created_order = store_service.create_order(store_service.order_json)
        parsed_created_order = created_order.json()
        created_order_id = parsed_created_order.get("id")
        response = store_service.get_order(created_order_id)
        assert 200 == response.status_code
        assert created_order_id == response.json().get("id")

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

    # TODO: reduce number of lines
    def test_delete_order(self, store_service):
        created_order = store_service.create_order(store_service.order_json)
        parsed_created_order = created_order.json()
        created_order_id = parsed_created_order.get("id")
        response = store_service.delete_order(created_order_id)
        assert 200 == response.status_code

    # TODO: reduce number of lines
    def test_delete_deleted_order(self, store_service):
        created_order = store_service.create_order(store_service.order_json)
        parsed_created_order = created_order.json()
        created_order_id = parsed_created_order.get("id")
        store_service.delete_order(created_order_id)
        response = store_service.delete_order(created_order_id)
        assert 404 == response.status_code

    # TODO: reduce number of lines
    def test_get_deleted_order(self, store_service):
        created_order = store_service.create_order(store_service.order_json)
        parsed_created_order = created_order.json()
        created_order_id = parsed_created_order.get("id")
        store_service.delete_order(created_order_id)
        response = store_service.get_order(created_order_id)
        assert 404 == response.status_code
