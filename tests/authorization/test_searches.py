"""Unit tests of authorization searches."""


import unittest


class TestAuthorizationSearch(unittest.TestCase):
    """Tests for AuthorizationSearch"""

    def test_search_among_authorizations(self):
        """Tests search_among_authorizations"""
        with self.assertRaises(errors.Unimplemented):
            self.searche.search_among_authorizations(True)

    def test_order_authorization_results(self):
        """Tests order_authorization_results"""
        with self.assertRaises(errors.Unimplemented):
            self.searche.order_authorization_results(True)

    def test_get_authorization_search_record(self):
        """Tests get_authorization_search_record"""
        with self.assertRaises(errors.Unimplemented):
            self.searche.get_authorization_search_record(True)


class TestAuthorizationSearchResults(unittest.TestCase):
    """Tests for AuthorizationSearchResults"""

    def test_get_authorizations(self):
        """Tests get_authorizations"""
        with self.assertRaises(errors.Unimplemented):
            self.searche.get_authorizations()

    def test_get_authorization_query_inspector(self):
        """Tests get_authorization_query_inspector"""
        with self.assertRaises(errors.Unimplemented):
            self.searche.get_authorization_query_inspector()

    def test_get_authorization_search_results_record(self):
        """Tests get_authorization_search_results_record"""
        with self.assertRaises(errors.Unimplemented):
            self.searche.get_authorization_search_results_record(True)


class TestVaultSearch(unittest.TestCase):
    """Tests for VaultSearch"""

    def test_search_among_vaults(self):
        """Tests search_among_vaults"""
        with self.assertRaises(errors.Unimplemented):
            self.searche.search_among_vaults(True)

    def test_order_vault_results(self):
        """Tests order_vault_results"""
        with self.assertRaises(errors.Unimplemented):
            self.searche.order_vault_results(True)

    def test_get_vault_search_record(self):
        """Tests get_vault_search_record"""
        with self.assertRaises(errors.Unimplemented):
            self.searche.get_vault_search_record(True)


class TestVaultSearchResults(unittest.TestCase):
    """Tests for VaultSearchResults"""

    def test_get_vaults(self):
        """Tests get_vaults"""
        with self.assertRaises(errors.Unimplemented):
            self.searche.get_vaults()

    def test_get_vault_query_inspector(self):
        """Tests get_vault_query_inspector"""
        with self.assertRaises(errors.Unimplemented):
            self.searche.get_vault_query_inspector()

    def test_get_vault_search_results_record(self):
        """Tests get_vault_search_results_record"""
        with self.assertRaises(errors.Unimplemented):
            self.searche.get_vault_search_results_record(True)
