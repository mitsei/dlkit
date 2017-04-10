from dlkit.runtime.primordium import Id
from dlkit.runtime.proxy_example import TestRequest

from .utilities.testing import DjangoTestCase


class ConfigurationTests(DjangoTestCase):
    def add_item(self, bank):
        form = bank.get_item_form_for_create([])
        form.display_name = 'a test item!'
        form.description = 'for testing with'
        form.set_learning_objectives([Id(self._lo)])
        new_item = bank.create_item(form)

        question_form = bank.get_question_form_for_create(new_item.ident,
                                                          [])
        question_form.display_name = 'Question for ' + new_item.display_name.text
        question_form.description = ''
        new_question = bank.create_question(question_form)

        answer_form = bank.get_answer_form_for_create(new_item.ident,
                                                      [])
        answer_form.display_name = 'Answer for ' + new_item.display_name.text
        new_answer = bank.create_answer(answer_form)

        item = bank.get_item(new_item.ident)
        return item

    def setUp(self):
        super(ConfigurationTests, self).setUp()

        self._lo = 'foo%3A1%40MIT'
        self._bank = self._get_test_bank()
        self._item = self.add_item(self._bank)

    def tearDown(self):
        """
        Remove the test user from all groups in Membership
        Start from the smallest groupId because need to
        remove "parental" roles like for DepartmentAdmin / DepartmentOfficer
        """
        super(ConfigurationTests, self).tearDown()

    def test_confirm_runtime_matches_test_config(self):
        from dlkit_runtime.configs import JSON_1
        authority_param_id = Id('parameter:authority@json')
        computed_authority = self._bank._osid_object._runtime.get_configuration().get_value_by_parameter(
            authority_param_id).get_string_value()
        self.assertEqual(
            computed_authority,
            JSON_1['parameters']['authority']['values'][0]['value']
        )

    def test_can_configure_mongo_indexes(self):
        from dlkit.json_.utilities import JSONClientValidated
        from dlkit_tests.functional.utilities.testing import configure_test_bucket

        index_to_test = 'genusTypeId'  # assumes this will never be set in the config
        test_collection = JSONClientValidated('assessment',
                                              collection='Bank',
                                              runtime=self._bank._osid_object._runtime)
        current_indexes = test_collection.raw().index_information()
        index_keys = [v['key'][0][0] for k, v in current_indexes.iteritems()]
        self.assertFalse(index_to_test in index_keys)

        with self.settings(DLKIT_MONGO_DB_INDEXES={'assessment.Bank': [index_to_test]}):
            configure_test_bucket()
            new_bank = self.create_new_bank()
            test_collection = JSONClientValidated('assessment',
                                                  collection='Bank',
                                                  runtime=new_bank._osid_object._runtime)
            current_indexes = test_collection.raw().index_information()
            index_keys = [v['key'][0][0] for k, v in current_indexes.iteritems()]
            self.assertTrue(index_to_test in index_keys)
