from dlkit.runtime.primordium import Id

from .utilities.testing import DLKitTestCase


class ConfigurationTests(DLKitTestCase):
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
        from dlkit.runtime.configs import TEST_JSON_1
        authority_param_id = Id('parameter:authority@json')
        computed_authority = self._bank._osid_object._runtime.get_configuration().get_value_by_parameter(
            authority_param_id).get_string_value()
        self.assertEqual(
            computed_authority,
            TEST_JSON_1['parameters']['authority']['values'][0]['value']
        )

    def test_can_configure_mongo_indexes(self):
        import dlkit.runtime.configs
        from dlkit.runtime.configs import impl_key_dict,\
            DLKIT_AUTHORITY, MONGO_HOST_URI, FILESYSTEM_ASSET_CONTENT_TYPE
        from dlkit.json_.utilities import JSONClientValidated

        index_to_test = 'genusTypeId'  # assumes this will never be set in the config
        test_collection = JSONClientValidated('assessment',
                                              collection='Bank',
                                              runtime=self._bank._osid_object._runtime)
        current_indexes = test_collection.raw().index_information()
        index_keys = [v['key'][0][0] for k, v in current_indexes.items()]
        self.assertFalse(index_to_test in index_keys)

        dlkit.runtime.configs.TEST_JSON_1 = {
            'id': 'mongo_configuration_1',
            'displayName': 'Mongo Configuration',
            'description': 'Configuration for Mongo Implementation',
            'parameters': {
                'implKey': impl_key_dict('json'),
                'mongoDBNamePrefix': {
                    'syntax': 'STRING',
                    'displayName': 'Mongo DB Name Prefix',
                    'description': 'Prefix for naming mongo databases.',
                    'values': [
                        {'value': 'test_dlkit_', 'priority': 1}
                    ]
                },
                'authority': {
                    'syntax': 'STRING',
                    'displayName': 'Mongo Authority',
                    'description': 'Authority.',
                    'values': [
                        {'value': DLKIT_AUTHORITY, 'priority': 1}
                    ]
                },
                'mongoHostURI': {
                    'syntax': 'STRING',
                    'displayName': 'Mongo Host URI',
                    'description': 'URI for setting the MongoClient host.',
                    'values': [
                        {'value': MONGO_HOST_URI, 'priority': 1}
                    ]
                },
                'recordsRegistry': {
                    'syntax': 'STRING',
                    'displayName': 'Python path to the extension records registry file',
                    'description': 'dot-separated path to the extension records registry file',
                    'values': [
                        {'value': 'dlkit.records.registry', 'priority': 1}
                    ]
                },
                'repositoryProviderImpl': {
                    'syntax': 'STRING',
                    'displayName': 'Repository Provider Implementation',
                    'description': 'Implementation for repository service provider',
                    'values': [
                        {'value': 'TEST_FILESYSTEM_ADAPTER_1', 'priority': 1}
                    ]
                },
                'assetContentRecordTypeForFiles': {
                    'syntax': 'TYPE',
                    'displayName': 'Asset Content Type for Files',
                    'description': 'Asset Content Type for Records that store Files in a repository',
                    'values': [
                        {'value': FILESYSTEM_ASSET_CONTENT_TYPE, 'priority': 1}
                    ]
                },
                'magicItemLookupSessions': {
                    'syntax': 'STRING',
                    'displayName': 'Which magic item lookup sessions to try',
                    'description': 'To handle magic IDs.',
                    'values': [
                        {'value': 'dlkit.records.adaptive.multi_choice_questions.randomized_questions.RandomizedMCItemLookupSession', 'priority': 1}
                    ]
                },
                'magicAssessmentPartLookupSessions': {
                    'syntax': 'STRING',
                    'displayName': 'Which magic assessment part lookup sessions to try',
                    'description': 'To handle magic IDs.',
                    'values': [
                        {'value': 'dlkit.records.adaptive.magic_parts.assessment_part_records.MagicAssessmentPartLookupSession', 'priority': 1}
                    ]
                },
                'indexes': {
                    'syntax': 'OBJECT',
                    'displayName': 'Mongo DB Indexes',
                    'description': 'Indexes to set in MongoDB',
                    'values': [
                        {'value': {'assessment.Bank': [index_to_test]}, 'priority': 1}
                    ]
                },
            }
        }
        new_bank = self.create_new_bank()
        test_collection = JSONClientValidated('assessment',
                                              collection='Bank',
                                              runtime=new_bank._osid_object._runtime)
        current_indexes = test_collection.raw().index_information()
        index_keys = [v['key'][0][0] for k, v in current_indexes.items()]
        self.assertTrue(index_to_test in index_keys)
