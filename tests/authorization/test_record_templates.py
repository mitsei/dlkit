"""Unit tests of authorization records."""


import pytest


from ..utilities.general import is_never_authz, is_no_authz, uses_cataloging, uses_filesystem_only


@pytest.mark.usefixtures("authorization_record_class_fixture", "authorization_record_test_fixture")
class TestAuthorizationRecord(object):
    """Tests for AuthorizationRecord"""


@pytest.mark.usefixtures("authorization_query_record_class_fixture", "authorization_query_record_test_fixture")
class TestAuthorizationQueryRecord(object):
    """Tests for AuthorizationQueryRecord"""


@pytest.mark.usefixtures("authorization_form_record_class_fixture", "authorization_form_record_test_fixture")
class TestAuthorizationFormRecord(object):
    """Tests for AuthorizationFormRecord"""


@pytest.mark.usefixtures("authorization_search_record_class_fixture", "authorization_search_record_test_fixture")
class TestAuthorizationSearchRecord(object):
    """Tests for AuthorizationSearchRecord"""


@pytest.mark.usefixtures("vault_record_class_fixture", "vault_record_test_fixture")
class TestVaultRecord(object):
    """Tests for VaultRecord"""


@pytest.mark.usefixtures("vault_query_record_class_fixture", "vault_query_record_test_fixture")
class TestVaultQueryRecord(object):
    """Tests for VaultQueryRecord"""


@pytest.mark.usefixtures("vault_form_record_class_fixture", "vault_form_record_test_fixture")
class TestVaultFormRecord(object):
    """Tests for VaultFormRecord"""


@pytest.mark.usefixtures("vault_search_record_class_fixture", "vault_search_record_test_fixture")
class TestVaultSearchRecord(object):
    """Tests for VaultSearchRecord"""
