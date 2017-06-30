"""Unit tests of authorization searches."""


import pytest


from ..utilities.general import is_never_authz, is_no_authz


@pytest.mark.usefixtures("authorization_search_class_fixture", "authorization_search_test_fixture")
class TestAuthorizationSearch(object):
    """Tests for AuthorizationSearch"""
    @pytest.mark.skip('unimplemented test')
    def test_search_among_authorizations(self):
        """Tests search_among_authorizations"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_order_authorization_results(self):
        """Tests order_authorization_results"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_authorization_search_record(self):
        """Tests get_authorization_search_record"""
        pass


@pytest.mark.usefixtures("authorization_search_results_class_fixture", "authorization_search_results_test_fixture")
class TestAuthorizationSearchResults(object):
    """Tests for AuthorizationSearchResults"""
    @pytest.mark.skip('unimplemented test')
    def test_get_authorizations(self):
        """Tests get_authorizations"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_authorization_query_inspector(self):
        """Tests get_authorization_query_inspector"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_authorization_search_results_record(self):
        """Tests get_authorization_search_results_record"""
        pass


@pytest.mark.usefixtures("vault_search_class_fixture", "vault_search_test_fixture")
class TestVaultSearch(object):
    """Tests for VaultSearch"""
    @pytest.mark.skip('unimplemented test')
    def test_search_among_vaults(self):
        """Tests search_among_vaults"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_order_vault_results(self):
        """Tests order_vault_results"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_vault_search_record(self):
        """Tests get_vault_search_record"""
        pass


@pytest.mark.usefixtures("vault_search_results_class_fixture", "vault_search_results_test_fixture")
class TestVaultSearchResults(object):
    """Tests for VaultSearchResults"""
    @pytest.mark.skip('unimplemented test')
    def test_get_vaults(self):
        """Tests get_vaults"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_vault_query_inspector(self):
        """Tests get_vault_query_inspector"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_vault_search_results_record(self):
        """Tests get_vault_search_results_record"""
        pass
