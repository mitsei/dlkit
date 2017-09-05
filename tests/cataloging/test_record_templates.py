"""Unit tests of cataloging records."""


import pytest


from ..utilities.general import is_never_authz, is_no_authz, uses_cataloging, uses_filesystem_only


@pytest.mark.usefixtures("catalog_record_class_fixture", "catalog_record_test_fixture")
class TestCatalogRecord(object):
    """Tests for CatalogRecord"""


@pytest.mark.usefixtures("catalog_query_record_class_fixture", "catalog_query_record_test_fixture")
class TestCatalogQueryRecord(object):
    """Tests for CatalogQueryRecord"""


@pytest.mark.usefixtures("catalog_form_record_class_fixture", "catalog_form_record_test_fixture")
class TestCatalogFormRecord(object):
    """Tests for CatalogFormRecord"""


@pytest.mark.usefixtures("catalog_search_record_class_fixture", "catalog_search_record_test_fixture")
class TestCatalogSearchRecord(object):
    """Tests for CatalogSearchRecord"""
