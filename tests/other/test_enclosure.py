"""Unit tests of enclosure functionality."""

import pytest
import unittest
from dlkit.runtime import PROXY_SESSION, proxy_example
from dlkit.runtime import Runtime
from dlkit.abstract_osid.osid import errors
from dlkit.primordium.type.primitives import Type

REQUEST = proxy_example.SimpleRequest()
CONDITION = PROXY_SESSION.get_proxy_condition()
CONDITION.set_http_request(REQUEST)
PROXY = PROXY_SESSION.get_proxy(CONDITION)

ENCLOSURE_RECORD_TYPE = Type(
    **{'identifier': 'enclosure',
       'namespace': 'osid-object',
       'authority': 'ODL.MIT.EDU'})

ENCLOSED_ASSESSMENT_TYPE = Type(
    **{'identifier': 'Assessment',
       'namespace': 'assessment',
       'authority': 'OSID.ORG'})


class TestEnclosure(unittest.TestCase):
    """Tests for enclosed object record"""

    @classmethod
    def setUpClass(cls):
        # cls.asset_list = list()
        # cls.asset_ids = list()
        cls.repo_mgr = Runtime().get_service_manager('REPOSITORY', 'TEST_SERVICE', PROXY)
        create_form = cls.repo_mgr.get_repository_form_for_create([])
        create_form.display_name = 'Test Repository'
        create_form.description = 'Test Repository for Enclosure tests'
        cls.repository = cls.repo_mgr.create_repository(create_form)
        cls.assess_mgr = Runtime().get_service_manager('ASSESSMENT', 'TEST_SERVICE', PROXY)
        create_form = cls.assess_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for Enclosure tests'
        cls.bank = cls.assess_mgr.create_bank(create_form)
        create_form = cls.bank.get_assessment_form_for_create([])
        create_form.display_name = 'Test Assessment'
        create_form.description = 'Test Assessment for Enclosure tests'
        cls.assessment = cls.bank.create_assessment(create_form)

    @classmethod
    def tearDownClass(cls):
        for repository in cls.repo_mgr.get_repositories():
            for obj in repository.get_assets():
                repository.delete_asset(obj.ident)
            for obj in repository.get_compositions():
                repository.delete_composition(obj.ident)
            cls.repo_mgr.delete_repository(repository.ident)
        for bank in cls.assess_mgr.get_banks():
            for obj in bank.get_assessments():
                bank.delete_assessment(obj.ident)
            cls.assess_mgr.delete_bank(bank.ident)

    def test_create_enclosed_assessment(self):
        """Tests creating an assessment enclosed in an asset"""
        create_form = self.repository.get_asset_form_for_create([ENCLOSURE_RECORD_TYPE])
        create_form.set_enclosed_object(self.assessment.ident)
        with pytest.raises(errors.NoAccess):
            create_form.set_display_name('This should fail')
        with pytest.raises(errors.NoAccess):
            create_form.set_description('This should also fail')
        with pytest.raises(errors.NoAccess):
            create_form.set_genus_type(ENCLOSURE_RECORD_TYPE)
        asset = self.repository.create_asset(create_form)
        assert asset.get_display_name().text == self.assessment.get_display_name().text
        assert asset.get_description().text == self.assessment.get_description().text
        assert asset.get_genus_type() == ENCLOSED_ASSESSMENT_TYPE

    # def test_update_asset_with_assessment(self):
    #     """
    #     Tests silently creating an assessment enclosed in an asset through update
    #
    #     And that if one already exists, that we get it instead.
    #
    #     """
    #     update_form = self.repository.get_asset_form_for_update(self.assessment.ident)
    #     update_form.set_title('This is the Asset Title')
    #     updated_asset = self.repository.update_asset(update_form)
    #     updated_asset_assessment_id = updated_asset.enclosed_object_id
    #     assert updated_asset.title.text == 'This is the Asset Title'
    #     new_update_form = self.repository.get_asset_form_for_update(self.assessment.ident)
    #     new_updated_asset = self.repository.update_asset(new_update_form)
    #     assert new_updated_asset.enclosed_object_id == updated_asset_assessment_id
    #     assert updated_asset.title.text == 'This is the Asset Title'

    def test_assessment_asset_composition(self):
        """Tests silently creating an enclosure through asset composition design."""

        create_form = self.repository.get_composition_form_for_create([])
        create_form.display_name = 'Test Composition'
        create_form.description = 'Test Composition for Enclosure tests'
        composition = self.repository.create_composition(create_form)
        self.repository.add_asset(self.assessment.ident, composition.ident)
        asset_list = self.repository.get_composition_assets(composition.ident)
        assert asset_list.available() == 1
        assert asset_list.next().display_name.text == 'Test Assessment'
