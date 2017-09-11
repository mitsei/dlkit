"""Unit tests of resource records."""


import pytest


from ..utilities.general import is_never_authz, is_no_authz, uses_cataloging, uses_filesystem_only


@pytest.mark.usefixtures("resource_record_class_fixture", "resource_record_test_fixture")
class TestResourceRecord(object):
    """Tests for ResourceRecord"""


@pytest.mark.usefixtures("resource_query_record_class_fixture", "resource_query_record_test_fixture")
class TestResourceQueryRecord(object):
    """Tests for ResourceQueryRecord"""


@pytest.mark.usefixtures("resource_form_record_class_fixture", "resource_form_record_test_fixture")
class TestResourceFormRecord(object):
    """Tests for ResourceFormRecord"""


@pytest.mark.usefixtures("resource_search_record_class_fixture", "resource_search_record_test_fixture")
class TestResourceSearchRecord(object):
    """Tests for ResourceSearchRecord"""


@pytest.mark.usefixtures("bin_record_class_fixture", "bin_record_test_fixture")
class TestBinRecord(object):
    """Tests for BinRecord"""


@pytest.mark.usefixtures("bin_query_record_class_fixture", "bin_query_record_test_fixture")
class TestBinQueryRecord(object):
    """Tests for BinQueryRecord"""


@pytest.mark.usefixtures("bin_form_record_class_fixture", "bin_form_record_test_fixture")
class TestBinFormRecord(object):
    """Tests for BinFormRecord"""


@pytest.mark.usefixtures("bin_search_record_class_fixture", "bin_search_record_test_fixture")
class TestBinSearchRecord(object):
    """Tests for BinSearchRecord"""
