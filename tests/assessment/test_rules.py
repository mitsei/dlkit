"""Unit tests of assessment rules."""


import pytest


from ..utilities.general import is_never_authz, is_no_authz, uses_cataloging, uses_filesystem_only


@pytest.mark.usefixtures("response_class_fixture", "response_test_fixture")
class TestResponse(object):
    """Tests for Response"""
    @pytest.mark.skip('unimplemented test')
    def test_get_item_id(self):
        """Tests get_item_id"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_item(self):
        """Tests get_item"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_response_record(self):
        """Tests get_response_record"""
        pass
