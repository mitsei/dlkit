# Did the tests fail?  First, check make sure you are running them from outside
# the package
import codecs
import unittest
import vcr

from dlkit.handcar import utilities
from dlkit.handcar import settings
from dlkit.handcar.primitives import Id, Type, DisplayText
from dlkit.handcar.osid.osid_errors import AlreadyExists, NotFound, OperationFailed
# from dlkit.handcar.learning.managers import LearningManager
# from dlkit.handcar.repository.managers import RepositoryManager
from dlkit.handcar.type.managers import TypeManager
from dlkit.abstract_osid.learning import sessions as abc_learning_sessions
from dlkit.abstract_osid.learning import objects as abc_learning_objects
from dlkit.abstract_osid.repository import objects as abc_repository_objects

from dlkit.runtime import PROXY_SESSION
from dlkit.runtime.managers import Runtime

CONDITION = PROXY_SESSION.get_proxy_condition()
PROXY = PROXY_SESSION.get_proxy(CONDITION)

SANDBOX_TYPE = Type({
    'authority': 'this.is.a.bogus.authority',
    'namespace': 'this.is.a.bogus.namespace',
    'identifier': 'mc3-objectivebank%3Amc3.learning.objectivebank.sandbox%40MIT-OEIT',
    'domain': '',
    'displayName': '',
    'description': '',
    'displayLabel': ''})


class TestLearningManager(unittest.TestCase):

    def setUp(self):
        self.lm = Runtime().get_service_manager('LEARNING',
                                                implementation='TEST_SERVICE_HANDCAR')

    def test_get_display_name(self):
        self.assertTrue(isinstance(
            self.lm.get_display_name().get_text(), str))

    def test_get_description(self):
        self.assertTrue(isinstance(
            self.lm.get_description().get_text(), str))

    def test_get_profile_language_type(self):
        # print self.lm.get_display_name()._my_map
        self.assertTrue(isinstance(
            self.lm.get_display_name().get_language_type(),
            Type))

    def test_get_profile_script_type(self):
        self.assertTrue(isinstance(
            self.lm.get_display_name().get_script_type(),
            Type))

    def test_get_profile_format_type(self):
        self.assertTrue(isinstance(
            self.lm.get_display_name().get_format_type(),
            Type))

    def test_display_name_turtles(self):
        self.assertTrue(utilities.is_string(
            self.lm.get_display_name().get_language_type().get_display_name().get_script_type().get_display_label().get_text()))  # when handcar reports type domains again, include that too

    def test_supports_objective_bank_lookup(self):
        self.assertTrue(self.lm.supports_objective_bank_lookup())

    def test_supports_objective_lookup(self):
        self.assertTrue(self.lm.supports_objective_lookup())

    def test_supports_objective_query(self):
        self.assertTrue(self.lm.supports_objective_query())

    def test_get_objective_bank_lookup_session(self):
        obls = self.lm.get_objective_bank_lookup_session()
        self.assertTrue(isinstance(
            obls,
            abc_learning_sessions.ObjectiveBankLookupSession))

    def test_get_objective_lookup_session(self):
        ols = self.lm.get_objective_bank_lookup_session()
        self.assertTrue(isinstance(
            ols,
            abc_learning_sessions.ObjectiveBankLookupSession))

    def test_get_objective_lookup_session_for_objective_bank(self):
        ols = self.lm.get_objective_lookup_session()
        ols_for_ob = self.lm.get_objective_lookup_session_for_objective_bank(ols.get_objective_bank_id())
        self.assertTrue(ols.get_objective_bank_id().get_identifier() ==
                        ols_for_ob.get_objective_bank_id().get_identifier())


class TestObjectiveBankLookup(unittest.TestCase):

    def setUp(self):
        self.lm = Runtime().get_service_manager('LEARNING',
                                                implementation='TEST_SERVICE_HANDCAR')
        self.obls = self.lm.get_objective_bank_lookup_session()

    @vcr.use_cassette('tests/fixtures/vcr_cassettes/handcar/TestObjectiveBankLookup/test_get_objective_banks.yaml', record_mode='new_episodes')
    def test_get_objective_banks(self):
        all_banks = self.obls.get_objective_banks()
        self.assertTrue(all_banks.available() > 0)

    @vcr.use_cassette('tests/fixtures/vcr_cassettes/handcar/TestObjectiveBankLookup/test_get_objective_bank.yaml', record_mode='new_episodes')
    def test_get_objective_bank(self):
        all_banks = self.obls.get_objective_banks()
        self.assertTrue(all_banks.available() > 0)
        for bank in all_banks:
            self.assertTrue(isinstance(bank, abc_learning_objects.ObjectiveBank))

    @vcr.use_cassette('tests/fixtures/vcr_cassettes/handcar/TestObjectiveBankLookup/test_get_objective_banks_by_ids.yaml', record_mode='new_episodes')
    def test_get_objective_banks_by_ids(self):
        from dlkit.handcar.id import objects as id_objects
        all_banks = self.obls.get_objective_banks()
        all_banks_count = all_banks.available()
        all_bank_ids = []
        for bank in all_banks:
            all_bank_ids.append(bank.get_id())
        id_list = id_objects.IdList(all_bank_ids)
        self.assertTrue(id_list.available() == all_banks_count)
        all_banks_by_ids = self.obls.get_objective_banks_by_ids(id_list)
        self.assertTrue(all_banks_by_ids.available() == all_banks_count)
        for bank in all_banks_by_ids:
            self.assertTrue(isinstance(bank, abc_learning_objects.ObjectiveBank))


class TestIdEquality(unittest.TestCase):

    @vcr.use_cassette('tests/fixtures/vcr_cassettes/handcar/TestIdEquality/setUp.yaml', record_mode='new_episodes')
    def setUp(self):
        self.equiv_id1 = utilities.get_bank_by_name('Crosslinks').ident
        self.equiv_id2 = utilities.get_bank_by_name('Crosslinks').ident
        self.non_equiv_id = utilities.get_bank_by_name('Chemistry Bridge').ident

    def test_equivelant_ids(self):
        self.assertTrue(isinstance(self.equiv_id1, Id))
        self.assertTrue(isinstance(self.equiv_id2, Id))
        self.assertEqual(self.equiv_id1, self.equiv_id2)

    def test_non_equivelant_ids(self):
        self.assertTrue(isinstance(self.equiv_id1, Id))
        self.assertTrue(isinstance(self.non_equiv_id, Id))
        self.assertNotEqual(self.equiv_id1, self.non_equiv_id)

    def test_list_inclusion(self):
        id_list = [self.equiv_id1, self.non_equiv_id]
        self.assertTrue(self.equiv_id2 in id_list)


class TestObjectiveLookup(unittest.TestCase):

    @vcr.use_cassette('tests/fixtures/vcr_cassettes/handcar/TestObjectiveLookup/setUp.yaml', record_mode='new_episodes')
    def setUp(self):
        try:
            # python 2
            import urllib2
            urlopen = urllib2.urlopen
        except ImportError:
            import urllib.request
            import urllib.error
            import urllib.parse
            urlopen = urllib.request.urlopen

        import json
        from dlkit.handcar.learning import objects
        self.lm = Runtime().get_service_manager('LEARNING',
                                                implementation='TEST_SERVICE_HANDCAR')

        self.obls = self.lm.get_objective_bank_lookup_session()
        # Get the first Objective Bank (I know... sketchy)
        all_banks = self.obls.get_objective_banks()
        self.first_bank = all_banks.get_next_objective_bank()
        self.ols = self.lm.get_objective_lookup_session_for_objective_bank(self.first_bank.get_id())
        # Get list of supported Objective Types (Note: This does not use the osid contract)
        url_string = 'http://' + settings.HOST + '/handcar/services/learning/objectivebanks/' + str(self.first_bank.get_id()) + '/types/genus/objective'
        response = urlopen(url_string)
        reader = codecs.getreader('utf8')
        self.objective_genus_types = json.load(reader(response))

    @vcr.use_cassette('tests/fixtures/vcr_cassettes/handcar/TestObjectiveLookup/test_get_objective_bank.yaml', record_mode='new_episodes')
    def test_get_objective_bank(self):
        test_bank_id = self.ols.get_objective_bank().get_id().get_identifier()
        self.assertTrue(test_bank_id == self.first_bank.get_id().get_identifier())

    @vcr.use_cassette('tests/fixtures/vcr_cassettes/handcar/TestObjectiveLookup/test_get_objectives.yaml', record_mode='new_episodes')
    def test_get_objectives(self):
        objectives = self.ols.get_objectives()
        self.assertTrue(isinstance(objectives, abc_learning_objects.ObjectiveList))
        for objective in objectives:
            self.assertTrue(isinstance(objective, abc_learning_objects.Objective))

    @vcr.use_cassette('tests/fixtures/vcr_cassettes/handcar/TestObjectiveLookup/test_get_objective.yaml', record_mode='new_episodes')
    def test_get_objective(self):
        all_objectives = self.ols.get_objectives()
        objective = all_objectives.get_next_objective()
        objective = self.ols.get_objective(objective.get_id())
        self.assertTrue(objective.get_id().get_identifier() ==
                        objective.get_id().get_identifier())

    @vcr.use_cassette('tests/fixtures/vcr_cassettes/handcar/TestObjectiveLookup/test_get_objectives_by_type.yaml', record_mode='new_episodes')
    def test_get_objectives_by_type(self):
        type_map = self.objective_genus_types[0]
        objectives = self.ols.get_objectives_by_genus_type(Type(type_map))
        for objective in objectives:
            self.assertTrue(objective.get_genus_type().get_identifier() == type_map['identifier'])

    @vcr.use_cassette('tests/fixtures/vcr_cassettes/handcar/TestObjectiveLookup/test_objective_is_of_genus_type.yaml', record_mode='new_episodes')
    def test_objective_is_of_genus_type(self):
        type_map = self.objective_genus_types[0]
        objectives = self.ols.get_objectives_by_genus_type(Type(type_map))
        for objective in objectives:
            self.assertTrue(objective.is_of_genus_type(Type(type_map)))


class TestObjectiveRequisite(unittest.TestCase):

    @vcr.use_cassette('tests/fixtures/vcr_cassettes/handcar/TestObjectiveRequisite/setUp.yaml', record_mode='new_episodes')
    def setUp(self):
        from dlkit.handcar.learning import objects
        from dlkit.handcar.learning import managers
        self.lm = Runtime().get_service_manager('LEARNING',
                                                implementation='TEST_SERVICE_HANDCAR')

        self.obls = self.lm.get_objective_bank_lookup_session()
        # Get the first Objective Bank (I know... sketchy)
        all_banks = self.obls.get_objective_banks()
        self.first_bank = all_banks.get_next_objective_bank()
        self.ors = self.lm.get_objective_requisite_session_for_objective_bank(self.first_bank.get_id())
        test_objective = utilities.get_objective_by_bank_id_and_name(
            utilities.get_bank_by_name('Crosslinks').ident,
            'Definite integral')
        self.test_objective_copy_id = Id(
            authority=test_objective.ident.authority,
            namespace=test_objective.ident.namespace,
            identifier=test_objective.ident.identifier)
        self.test_objective_id = test_objective.ident
        req_objective = utilities.get_objective_by_bank_id_and_name(
            utilities.get_bank_by_name('Crosslinks').ident,
            'Summation')
        self.req_objective_copy_id = Id(
            authority=req_objective.ident.authority,
            namespace=req_objective.ident.namespace,
            identifier=req_objective.ident.identifier)
        self.req_objective_id = req_objective.ident

    @vcr.use_cassette('tests/fixtures/vcr_cassettes/handcar/TestObjectiveRequisite/test_get_requisite_objectives.yaml', record_mode='new_episodes')
    def test_get_requisite_objectives(self):
        objectives = self.ors.get_requisite_objectives(self.test_objective_id)
        self.assertTrue(isinstance(objectives, abc_learning_objects.ObjectiveList))
        for objective in objectives:
            self.assertTrue(isinstance(objective, abc_learning_objects.Objective))

    @vcr.use_cassette('tests/fixtures/vcr_cassettes/handcar/TestObjectiveRequisite/test_get_all_requisite_objectives.yaml', record_mode='new_episodes')
    def test_get_all_requisite_objectives(self):
        objectives = self.ors.get_all_requisite_objectives(self.test_objective_id)
        self.assertTrue(isinstance(objectives, abc_learning_objects.ObjectiveList))
        for objective in objectives:
            self.assertTrue(isinstance(objective, abc_learning_objects.Objective))

    @vcr.use_cassette('tests/fixtures/vcr_cassettes/handcar/TestObjectiveRequisite/test_get_dependent_objectives.yaml', record_mode='new_episodes')
    def test_get_dependent_objectives(self):
        objectives = self.ors.get_dependent_objectives(self.test_objective_id)
        self.assertTrue(isinstance(objectives, abc_learning_objects.ObjectiveList))
        for objective in objectives:
            self.assertTrue(isinstance(objective, abc_learning_objects.Objective))

    @vcr.use_cassette('tests/fixtures/vcr_cassettes/handcar/TestObjectiveRequisite/test_is_objective_required.yaml', record_mode='new_episodes')
    def test_is_objective_required(self):
        self.assertTrue(self.ors.is_objective_required(self.test_objective_id,
                                                       self.req_objective_id))

    @vcr.use_cassette('tests/fixtures/vcr_cassettes/handcar/TestObjectiveRequisite/test_is_objective_required_copy.yaml', record_mode='new_episodes')
    def test_is_objective_required_copy(self):
        self.assertTrue(self.ors.is_objective_required(self.test_objective_copy_id,
                                                       self.req_objective_copy_id))

    @vcr.use_cassette('tests/fixtures/vcr_cassettes/handcar/TestObjectiveRequisite/test_objective_id_copy.yaml', record_mode='new_episodes')
    def test_objective_id_copy(self):
        self.assertTrue(self.test_objective_id == self.test_objective_copy_id)

    @vcr.use_cassette('tests/fixtures/vcr_cassettes/handcar/TestObjectiveRequisite/test_req_objective_id_copy.yaml', record_mode='new_episodes')
    def test_req_objective_id_copy(self):
        self.assertTrue(self.req_objective_id == self.req_objective_copy_id)

    def test_get_equivalent_objectives(self):
        # Don't know how to test this yet.  Probably need to replace all of the
        # Requisite tests with more of a CRuD pattern
        self.assertTrue(True)


class TestObjectiveHierarchy(unittest.TestCase):

    @vcr.use_cassette('tests/fixtures/vcr_cassettes/handcar/TestObjectiveHierarchy/setUp.yaml', record_mode='new_episodes')
    def setUp(self):
        from dlkit.handcar.learning import objects
        from dlkit.handcar.learning import managers
        self.lm = Runtime().get_service_manager('LEARNING',
                                                implementation='TEST_SERVICE_HANDCAR')

        self.test_bank = utilities.get_bank_by_name('Chemistry Bridge')
        self.ohs = self.lm.get_objective_hierarchy_session_for_objective_bank(self.test_bank.ident)
        self.test_objective = utilities.get_objective_by_bank_id_and_name(
            self.test_bank.ident,
            'Acids and Bases')
        self.test_objective_id = self.test_objective.ident
        self.test_parent = utilities.get_objective_by_bank_id_and_name(
            self.test_bank.ident,
            'Buffers: A study of Chemical Equilibria')
        self.test_parent_id = self.test_parent.ident
        self.test_child = utilities.get_objective_by_bank_id_and_name(
            self.test_bank.ident,
            'Strength of an acid/base')
        self.test_child_id = self.test_child.ident
        self.test_final_child = utilities.get_objective_by_bank_id_and_name(
            self.test_bank.ident,
            'Auto-Ionization of Water outcome 3D1')
        self.test_final_child_id = self.test_final_child.ident

    @vcr.use_cassette('tests/fixtures/vcr_cassettes/handcar/TestObjectiveHierarchy/test_get_root_objective_ids.yaml', record_mode='new_episodes')
    def test_get_root_objective_ids(self):
        from dlkit.handcar.id import objects as id_objects
        objective_ids = self.ohs.get_root_objective_ids()
        self.assertTrue(isinstance(objective_ids, id_objects.IdList))
        for objective_id in objective_ids:
            self.assertTrue(isinstance(objective_id, Id))

    @vcr.use_cassette('tests/fixtures/vcr_cassettes/handcar/TestObjectiveHierarchy/test_get_root_objectives.yaml', record_mode='new_episodes')
    def test_get_root_objectives(self):
        objectives = self.ohs.get_root_objectives()
        self.assertTrue(isinstance(objectives, abc_learning_objects.ObjectiveList))
        for objective in objectives:
            self.assertTrue(isinstance(objective, abc_learning_objects.Objective))

    @vcr.use_cassette('tests/fixtures/vcr_cassettes/handcar/TestObjectiveHierarchy/test_has_parent_objectives.yaml', record_mode='new_episodes')
    def test_has_parent_objectives(self):
        self.assertTrue(self.ohs.has_parent_objectives(self.test_objective_id))
        self.assertFalse(self.ohs.has_parent_objectives(self.test_parent_id))

    @vcr.use_cassette('tests/fixtures/vcr_cassettes/handcar/TestObjectiveHierarchy/test_is_parent_of_objective.yaml', record_mode='new_episodes')
    def test_is_parent_of_objective(self):
        self.assertTrue(self.ohs.is_parent_of_objective(self.test_parent_id,
                                                        self.test_objective_id))
        self.assertFalse(self.ohs.is_parent_of_objective(self.test_child_id,
                                                         self.test_objective_id))

    @vcr.use_cassette('tests/fixtures/vcr_cassettes/handcar/TestObjectiveHierarchy/test_get_parent_objective_ids.yaml', record_mode='new_episodes')
    def test_get_parent_objective_ids(self):
        from dlkit.handcar.id import objects as id_objects
        objective_ids = self.ohs.get_parent_objective_ids(self.test_objective_id)
        self.assertTrue(isinstance(objective_ids, id_objects.IdList))
        for objective_id in objective_ids:
            self.assertTrue(isinstance(objective_id, Id))

    @vcr.use_cassette('tests/fixtures/vcr_cassettes/handcar/TestObjectiveHierarchy/test_get_parent_objectives.yaml', record_mode='new_episodes')
    def test_get_parent_objectives(self):
        objectives = self.ohs.get_parent_objectives(self.test_objective_id)
        self.assertTrue(isinstance(objectives, abc_learning_objects.ObjectiveList))
        for objective in objectives:
            self.assertTrue(isinstance(objective, abc_learning_objects.Objective))

    @vcr.use_cassette('tests/fixtures/vcr_cassettes/handcar/TestObjectiveHierarchy/test_has_child_objectives.yaml', record_mode='new_episodes')
    def test_has_child_objectives(self):
        self.assertTrue(self.ohs.has_child_objectives(self.test_objective_id))
        self.assertFalse(self.ohs.has_child_objectives(self.test_final_child_id))

    @vcr.use_cassette('tests/fixtures/vcr_cassettes/handcar/TestObjectiveHierarchy/test_is_child_of_objective.yaml', record_mode='new_episodes')
    def test_is_child_of_objective(self):
        self.assertTrue(self.ohs.is_child_of_objective(self.test_child_id,
                                                       self.test_objective_id))
        self.assertFalse(self.ohs.is_child_of_objective(self.test_parent_id,
                                                        self.test_objective_id))

    @vcr.use_cassette('tests/fixtures/vcr_cassettes/handcar/TestObjectiveHierarchy/test_get_child_objective_ids.yaml', record_mode='new_episodes')
    def test_get_child_objective_ids(self):
        from dlkit.handcar.id import objects as id_objects
        objective_ids = self.ohs.get_child_objective_ids(self.test_objective_id)
        self.assertTrue(isinstance(objective_ids, id_objects.IdList))
        for objective_id in objective_ids:
            self.assertTrue(isinstance(objective_id, Id))

    @vcr.use_cassette('tests/fixtures/vcr_cassettes/handcar/TestObjectiveHierarchy/test_get_child_objectives.yaml', record_mode='new_episodes')
    def test_get_child_objectives(self):
        objectives = self.ohs.get_child_objectives(self.test_child_id)
        self.assertTrue(isinstance(objectives, abc_learning_objects.ObjectiveList))
        for objective in objectives:
            self.assertTrue(isinstance(objective, abc_learning_objects.Objective))


class TestActivityLookup(unittest.TestCase):

    @vcr.use_cassette('tests/fixtures/vcr_cassettes/handcar/TestActivityLookup/setUp.yaml', record_mode='new_episodes')
    def setUp(self):
        try:
            # python 2
            import urllib2
            urlopen = urllib2.urlopen
        except ImportError:
            # python 3
            import urllib.request
            import urllib.error
            import urllib.parse
            urlopen = urllib.request.urlopen

        import json
        from dlkit.handcar.learning import objects
        from dlkit.handcar.learning import managers
        self.lm = Runtime().get_service_manager('LEARNING',
                                                implementation='TEST_SERVICE_HANDCAR')

        self.obls = self.lm.get_objective_bank_lookup_session()
        # Get the first Objective Bank (I know... sketchy)
        all_banks = self.obls.get_objective_banks()
        self.first_bank = all_banks.get_next_objective_bank()
        self.als = self.lm.get_activity_lookup_session_for_objective_bank(self.first_bank.get_id())
        # Get list of supported Activity Types (Note: This does not use the osid contract yet)
        url_string = 'http://' + settings.HOST + '/handcar/services/learning/objectivebanks/' + str(self.first_bank.get_id()) + '/types/genus/activity'
        response = urlopen(url_string)
        reader = codecs.getreader('utf8')
        self.activity_genus_types = json.load(reader(response))

    @vcr.use_cassette('tests/fixtures/vcr_cassettes/handcar/TestActivityLookup/test_get_objective_bank.yaml', record_mode='new_episodes')
    def test_get_objective_bank(self):
        test_bank_id = self.als.get_objective_bank().get_id().get_identifier()
        self.assertTrue(test_bank_id == self.first_bank.get_id().get_identifier())

    @vcr.use_cassette('tests/fixtures/vcr_cassettes/handcar/TestActivityLookup/test_get_activities.yaml', record_mode='new_episodes')
    def test_get_activities(self):
        activities = self.als.get_activities()
        self.assertTrue(isinstance(activities, abc_learning_objects.ActivityList))
        for activity in activities:
            self.assertTrue(isinstance(activity, abc_learning_objects.Activity))

    @vcr.use_cassette('tests/fixtures/vcr_cassettes/handcar/TestActivityLookup/test_get_activity.yaml', record_mode='new_episodes')
    def test_get_activity(self):
        all_activities = self.als.get_activities()
        activity = all_activities.get_next_activity()
        activity = self.als.get_activity(activity.get_id())
        self.assertTrue(activity.get_id().get_identifier() ==
                        activity.get_id().get_identifier())

    @vcr.use_cassette('tests/fixtures/vcr_cassettes/handcar/TestActivityLookup/test_get_activities_by_type.yaml', record_mode='new_episodes')
    def test_get_activities_by_type(self):
        type_map = self.activity_genus_types[0]
        activities = self.als.get_activities_by_genus_type(Type(type_map))
        for activity in activities:
            self.assertTrue(activity.get_genus_type().get_identifier() == type_map['identifier'])

    @vcr.use_cassette('tests/fixtures/vcr_cassettes/handcar/TestActivityLookup/test_activity_is_of_genus_type.yaml', record_mode='new_episodes')
    def test_activity_is_of_genus_type(self):
        type_map = self.activity_genus_types[0]
        activities = self.als.get_activities_by_genus_type(Type(type_map))
        for activity in activities:
            self.assertTrue(activity.is_of_genus_type(Type(type_map)))


class TestObjectiveMetadata(unittest.TestCase):

    @vcr.use_cassette('tests/fixtures/vcr_cassettes/handcar/TestObjectiveMetadata/setUp.yaml', record_mode='new_episodes')
    def setUp(self):
        from dlkit.handcar.learning import objects
        from dlkit.handcar.learning import managers
        self.lm = Runtime().get_service_manager('LEARNING',
                                                implementation='TEST_SERVICE_HANDCAR')

        self.obls = self.lm.get_objective_bank_lookup_session()
        # Get the first Objective Bank (I know... sketchy)
        all_banks = self.obls.get_objective_banks()
        self.first_bank = all_banks.get_next_objective_bank()
        self.ols = self.lm.get_objective_lookup_session_for_objective_bank(self.first_bank.get_id())
        all_objectives = self.ols.get_objectives()
        self.objective = all_objectives.get_next_objective()

    def test_get_journal_comment_metadata(self):
        from dlkit.handcar.learning import objects
        from dlkit.handcar.osid import metadata
        objective_form = objects.ObjectiveForm()
        cm = objective_form.get_journal_comment_metadata()
        self.assertEqual(cm.get_syntax(), 'STRING')

    def test_get_display_name_metadata(self):
        from dlkit.handcar.learning import objects
        from dlkit.handcar.osid import metadata
        objective_form = objects.ObjectiveForm()
        cm = objective_form.get_display_name_metadata()
        self.assertEqual(cm.get_syntax(), 'STRING')

    def test_get_description_metadata(self):
        from dlkit.handcar.learning import objects
        from dlkit.handcar.osid import metadata
        objective_form = objects.ObjectiveForm()
        cm = objective_form.get_description_metadata()
        self.assertEqual(cm.get_syntax(), 'STRING')

    def test_get_genus_type_metadata(self):
        from dlkit.handcar.learning import objects
        from dlkit.handcar.osid import metadata
        objective_form = objects.ObjectiveForm()
        cm = objective_form.get_genus_type_metadata()
        self.assertEqual(cm.get_syntax(), 'TYPE')

    def test_get_assessment_metadata(self):
        from dlkit.handcar.learning import objects
        from dlkit.handcar.osid import metadata
        objective_form = objects.ObjectiveForm()
        cm = objective_form.get_assessment_metadata()
        self.assertEqual(cm.get_syntax(), 'ID')

    def test_get_cognitive_process_metadata(self):
        from dlkit.handcar.learning import objects
        from dlkit.handcar.osid import metadata
        objective_form = objects.ObjectiveForm()
        cm = objective_form.get_cognitive_process_metadata()
        self.assertEqual(cm.get_syntax(), 'ID')

    def test_get_knowledge_category_metadata(self):
        from dlkit.handcar.learning import objects
        from dlkit.handcar.osid import metadata
        objective_form = objects.ObjectiveForm()
        cm = objective_form.get_knowledge_category_metadata()
        self.assertEqual(cm.get_syntax(), 'ID')


class TestObjectiveBankCrUD(unittest.TestCase):

    @vcr.use_cassette('tests/fixtures/vcr_cassettes/handcar/TestObjectiveBankCrUD/setUp.yaml', record_mode='new_episodes')
    def setUp(self):
        lm = Runtime().get_service_manager('LEARNING',
                                           implementation='TEST_SERVICE_HANDCAR')

        self.obas = lm.get_objective_bank_admin_session()
        self.obls = lm.get_objective_bank_lookup_session()
        self.sandbox_bank_type = SANDBOX_TYPE

    @vcr.use_cassette('tests/fixtures/vcr_cassettes/handcar/TestObjectiveBankCrUD/test_crud_objective_banks.yaml', record_mode='new_episodes')
    def test_crud_objective_banks(self):
        # test create:
        obfc = self.obas.get_objective_bank_form_for_create([])
        obfc.display_name = 'CRuD-Test Objective Bank'
        obfc.description = 'This is a Test Objective Bank for CRuD'
        new_objective_bank = self.obas.create_objective_bank(obfc)
        self.assertEqual(new_objective_bank.display_name.text, 'CRuD-Test Objective Bank')
        # test update:
        new_objective_bank_id = new_objective_bank.get_id()
        obfu = self.obas.get_objective_bank_form_for_update(new_objective_bank_id)
        obfu.set_display_name('New Name for CRuD-Test Objective Bank')
        updated_objective_bank = self.obas.update_objective_bank(obfu)
        updated_objective_bank_id = updated_objective_bank.ident
        self.assertEqual(new_objective_bank_id.identifier, updated_objective_bank_id.identifier)
        self.assertEqual(self.obls.get_objective_bank(updated_objective_bank_id).display_name.text, 'New Name for CRuD-Test Objective Bank')
        # test delete:
        self.obas.delete_objective_bank(updated_objective_bank_id)
        with self.assertRaises(NotFound):
            self.obls.get_objective_bank(updated_objective_bank_id)

    def test_truth(self):
        self.assertTrue(True)


class TestObjectiveCrUD(unittest.TestCase):

    @vcr.use_cassette('tests/fixtures/vcr_cassettes/handcar/TestObjectiveCrUD/setUp.yaml', record_mode='new_episodes')
    def setUp(self):
        lm = Runtime().get_service_manager('LEARNING',
                                           implementation='TEST_SERVICE_HANDCAR')

        obls = lm.get_objective_bank_lookup_session()
        try:
            test_bank = utilities.get_bank_by_name('Python Test Sandbox')
        except NotFound:
            test_bank = utilities.create_sandbox_bank('Python Test Sandbox', 'a sandbox objective bank for testing Python implementations.')
        test_bank_id = test_bank.ident
        self.test_bank = obls.get_objective_bank(test_bank_id)
        self.assertEqual(self.test_bank.get_display_name().get_text(), 'Python Test Sandbox')
        self.ols = lm.get_objective_lookup_session_for_objective_bank(test_bank_id)
        self.oas = lm.get_objective_admin_session_for_objective_bank(test_bank_id)

    @vcr.use_cassette('tests/fixtures/vcr_cassettes/handcar/TestObjectiveCrUD/test_crud_objective.yaml', record_mode='new_episodes')
    def test_crud_objective(self):
        # test create:
        ofc = self.oas.get_objective_form_for_create([])
        ofc.set_display_name('Test Objective')
        ofc.set_description('This is a Test Objective')
        new_objective = self.oas.create_objective(ofc)
        self.assertEqual(new_objective.get_display_name().get_text(), 'Test Objective')
        # test update:
        new_objective_id = new_objective.get_id()
        ofu = self.oas.get_objective_form_for_update(new_objective_id)
        ofu.set_display_name('New Name for Test Objective')
        updated_objective = self.oas.update_objective(ofu)
        updated_objective_id = updated_objective.get_id()
        self.assertEqual(new_objective_id.get_identifier(), updated_objective_id.get_identifier())
        self.assertEqual(self.ols.get_objective(updated_objective_id).get_display_name().get_text(), 'New Name for Test Objective')
        # test delete:
        self.oas.delete_objective(updated_objective_id)
        with self.assertRaises(NotFound):
            self.ols.get_objective(updated_objective_id)

    def test_truth(self):
        self.assertTrue(True)


class TestActivityCrUD(unittest.TestCase):

    @vcr.use_cassette('tests/fixtures/vcr_cassettes/handcar/TestActivityCrUD/setUp.yaml', record_mode='new_episodes')
    def setUp(self):
        lm = Runtime().get_service_manager('LEARNING',
                                           implementation='TEST_SERVICE_HANDCAR')

        obls = lm.get_objective_bank_lookup_session()
        try:
            self.test_bank = utilities.get_bank_by_name('Python Test Sandbox')
        except NotFound:
            self.test_bank = utilities.create_sandbox_bank('Python Test Sandbox', 'a sandbox objective bank for testing Python implementations.')
        test_bank_id = self.test_bank.ident
        self.assertEqual(self.test_bank.get_display_name().get_text(), 'Python Test Sandbox')
        self.als = lm.get_activity_lookup_session_for_objective_bank(test_bank_id)
        self.aas = lm.get_activity_admin_session_for_objective_bank(test_bank_id)
        self.ols = lm.get_objective_lookup_session_for_objective_bank(test_bank_id)
        self.oas = lm.get_objective_admin_session_for_objective_bank(test_bank_id)
        ofc = self.oas.get_objective_form_for_create([])
        ofc.set_display_name('Activity CrUD Test Objective')
        ofc.set_description('This is a Test Objective for testing Activity CrUD')
        self.test_objective = self.oas.create_objective(ofc)
        self.test_objective_id = self.test_objective.get_id()

    @vcr.use_cassette('tests/fixtures/vcr_cassettes/handcar/TestActivityCrUD/test_crud_activities.yaml', record_mode='new_episodes')
    def test_crud_activities(self):
        # test create:
        afc = self.aas.get_activity_form_for_create(self.test_objective_id, [])
        afc.set_display_name('Test Activity')
        afc.set_description('This is a Test Activity')
        new_activity = self.aas.create_activity(afc)
        self.assertEqual(new_activity.get_display_name().get_text(), 'Test Activity')
        # test update:
        new_activity_id = new_activity.get_id()
        afu = self.aas.get_activity_form_for_update(new_activity_id)
        afu.set_display_name('New Name for Test Activity')
        updated_activity = self.aas.update_activity(afu)
        updated_activity_id = updated_activity.get_id()
        self.assertEqual(new_activity_id.get_identifier(), updated_activity_id.get_identifier())
        self.assertEqual(self.als.get_activity(updated_activity_id).get_display_name().get_text(), 'New Name for Test Activity')
        # test delete
        self.aas.delete_activity(updated_activity_id)
        with self.assertRaises(NotFound):
            self.als.get_activity(updated_activity_id)

    def test_truth(self):
        self.assertTrue(True)

    @vcr.use_cassette('tests/fixtures/vcr_cassettes/handcar/TestActivityCrUD/tearDown.yaml', record_mode='new_episodes')
    def tearDown(self):
        self.oas.delete_objective(self.test_objective_id)
        with self.assertRaises(NotFound):
            self.ols.get_objective(self.test_objective_id)


class TestObjectiveDesignAndSeq(unittest.TestCase):

    @vcr.use_cassette('tests/fixtures/vcr_cassettes/handcar/TestObjectiveDesignAndSeq/setUp.yaml', record_mode='new_episodes')
    def setUp(self):
        lm = Runtime().get_service_manager('LEARNING',
                                           implementation='TEST_SERVICE_HANDCAR')

        obls = lm.get_objective_bank_lookup_session()
        try:
            self.test_bank = utilities.get_bank_by_name('Python Test Sandbox')
        except NotFound:
            self.test_bank = utilities.create_sandbox_bank('Python Test Sandbox', 'a sandbox objective bank for testing Python implementations.')
        self.test_bank_id = self.test_bank.ident
        self.ohds = lm.get_objective_hierarchy_design_session_for_objective_bank(self.test_bank_id)
        self.ohs = lm.get_objective_hierarchy_session_for_objective_bank(self.test_bank_id)
        self.oss = lm.get_objective_sequencing_session_for_objective_bank(self.test_bank_id)
        self.parent_objective = utilities.create_objective(
            self.test_bank_id,
            'parent objective', 'parent objective for testing hierarchy design')
        self.child_objectives = list()
        i = 0
        while i < 5:
            i += 1
            self.child_objectives.append(utilities.create_objective(
                self.test_bank_id,
                'child objective ' + str(i),
                '# ' + str(i) + ' child objective for testing hierarchy design'))

    @vcr.use_cassette('tests/fixtures/vcr_cassettes/handcar/TestObjectiveDesignAndSeq/test_add_remove_child_objective.yaml', record_mode='new_episodes')
    def test_add_remove_child_objective(self):
        for child_objective in self.child_objectives:
            try:
                self.ohds.add_child_objective(self.parent_objective.ident,
                                              child_objective.ident)
            except AlreadyExists:
                pass
        self.assertEqual(len(self.ohs.get_child_objectives(self.parent_objective.ident)), 5)
        self.ohds.remove_child_objective(self.parent_objective.ident, self.child_objectives[0].ident)
        self.assertEqual(len(self.ohs.get_child_objectives(self.parent_objective.ident)), 4)
        self.oss.move_objective_ahead(self.parent_objective.ident,
                                      self.child_objectives[1].ident,
                                      self.child_objectives[3].ident)
        self.oss.move_objective_behind(self.parent_objective.ident,
                                       self.child_objectives[2].ident,
                                       self.child_objectives[3].ident)
        self.ohds.remove_child_objectives(self.parent_objective.ident)
        self.assertEqual(len(self.ohs.get_child_objectives(self.parent_objective.ident)), 0)

    def test_five_children_in_list(self):
        self.assertEqual(len(self.child_objectives), 5)


class TestObjectiveRequisiteAssignment(unittest.TestCase):

    @vcr.use_cassette('tests/fixtures/vcr_cassettes/handcar/TestObjectiveRequisiteAssignment/setUp.yaml', record_mode='new_episodes')
    def setUp(self):
        lm = Runtime().get_service_manager('LEARNING',
                                           implementation='TEST_SERVICE_HANDCAR')

        obls = lm.get_objective_bank_lookup_session()
        try:
            self.test_bank = utilities.get_bank_by_name('Python Test Sandbox')
        except NotFound:
            self.test_bank = utilities.create_sandbox_bank('Python Test Sandbox', 'a sandbox objective bank for testing Python implementations.')
        self.test_bank_id = self.test_bank.ident
        self.oras = lm.get_objective_requisite_assignment_session_for_objective_bank(self.test_bank_id)
        self.ors = lm.get_objective_requisite_session_for_objective_bank(self.test_bank_id)
        self.dependent_objective = utilities.create_objective(
            self.test_bank_id,
            'dependent objective', 'dependent objective for testing requisite assignment')
        self.required_objectives = list()
        i = 0
        while i < 3:
            i += 1
            self.required_objectives.append(utilities.create_objective(
                self.test_bank_id,
                'required objective ' + str(i),
                '# ' + str(i) + ' required objective for testing requisite assignment'))

    @vcr.use_cassette('tests/fixtures/vcr_cassettes/handcar/TestObjectiveRequisiteAssignment/test_requisite_assignment.yaml', record_mode='new_episodes')
    def test_requisite_assignment(self):
        for required_objective in self.required_objectives:
            try:
                self.oras.assign_objective_requisite(self.dependent_objective.ident,
                                                     required_objective.ident)
            except AlreadyExists:
                pass
        self.assertEqual(len(self.ors.get_requisite_objectives(self.dependent_objective.ident)), 3)
        self.oras.unassign_objective_requisite(self.dependent_objective.ident, self.required_objectives[0].ident)
        self.assertEqual(len(self.ors.get_requisite_objectives(self.dependent_objective.ident)), 2)
        for required_objective in self.ors.get_requisite_objectives(self.dependent_objective.ident):
            self.oras.unassign_objective_requisite(self.dependent_objective.ident, required_objective.ident)
        self.assertEqual(len(self.ors.get_requisite_objectives(self.dependent_objective.ident)), 0)

    def test_five_children_in_list(self):
        self.assertEqual(len(self.required_objectives), 3)


class TestTypeLookup(unittest.TestCase):

    @vcr.use_cassette('tests/fixtures/vcr_cassettes/handcar/TestTypeLookup/setUp.yaml', record_mode='new_episodes')
    def setUp(self):
        tm = Runtime().get_service_manager('TYPE',
                                           implementation='TEST_SERVICE_HANDCAR')

        self.tls = tm.get_type_lookup_session()

    @vcr.use_cassette('tests/fixtures/vcr_cassettes/handcar/TestTypeLookup/test_get_types.yaml', record_mode='new_episodes')
    def test_get_types(self):
        from dlkit.abstract_osid.type import primitives as abc_type_primitives
        for t in self.tls.get_types():
            self.assertTrue(isinstance(t, abc_type_primitives.Type))

    @vcr.use_cassette('tests/fixtures/vcr_cassettes/handcar/TestTypeLookup/test_get_type.yaml', record_mode='new_episodes')
    def test_get_type(self):
        from dlkit.abstract_osid.type import primitives as abc_type_primitives
        type_to_get = self.tls.get_types().get_next_type()
        type_elements = {'identifier': type_to_get.identifier,
                         'namespace': type_to_get.namespace,
                         'authority': type_to_get.authority}
        self.assertTrue(isinstance(self.tls.get_type(**type_elements),
                                   abc_type_primitives.Type))


class TestRepositoryLookup(unittest.TestCase):

    def setUp(self):
        # Not sure why Repository requires the proxy...
        self.rm = Runtime().get_service_manager('REPOSITORY',
                                                proxy=PROXY,
                                                implementation='TEST_SERVICE_HANDCAR')

        self.rls = self.rm.get_repository_lookup_session(proxy=PROXY)

    @vcr.use_cassette('tests/fixtures/vcr_cassettes/handcar/TestRepositoryLookup/test_repositories.yaml', record_mode='new_episodes')
    def test_repositories(self):
        all_repositories = self.rls.get_repositories()
        self.assertTrue(all_repositories.available() > 0)

    @vcr.use_cassette('tests/fixtures/vcr_cassettes/handcar/TestRepositoryLookup/test_get_repository.yaml', record_mode='new_episodes')
    def test_get_repository(self):
        all_repositories = self.rls.get_repositories()
        self.assertTrue(all_repositories.available() > 0)
        for repository in all_repositories:
            self.assertTrue(isinstance(repository, abc_repository_objects.Repository))

    @vcr.use_cassette('tests/fixtures/vcr_cassettes/handcar/TestRepositoryLookup/test_get_repositories_by_ids.yaml', record_mode='new_episodes')
    def test_get_repositories_by_ids(self):
        from dlkit.handcar.id import objects as id_objects
        all_repositories = self.rls.get_repositories()
        all_repositories_count = all_repositories.available()
        all_repository_ids = []
        for repository in all_repositories:
            all_repository_ids.append(repository.get_id())
        id_list = id_objects.IdList(all_repository_ids)
        self.assertTrue(id_list.available() == all_repositories_count)
        all_repositories_by_ids = self.rls.get_repositories_by_ids(id_list)
        self.assertTrue(all_repositories_by_ids.available() == all_repositories_count)
        for repository in all_repositories_by_ids:
            self.assertTrue(isinstance(repository, abc_repository_objects.Repository))


class TestRepositoryCrUD(unittest.TestCase):
    def setUp(self):
        # Not sure why Repository requires the proxy...
        rm = Runtime().get_service_manager('REPOSITORY',
                                           proxy=PROXY,
                                           implementation='TEST_SERVICE_HANDCAR')

        self.ras = rm.get_repository_admin_session(proxy=PROXY)
        self.rls = rm.get_repository_lookup_session(proxy=PROXY)
        self.sandbox_repository_type = SANDBOX_TYPE

    @vcr.use_cassette('tests/fixtures/vcr_cassettes/handcar/TestRepositoryCrUD/test_crud_repositories.yaml', record_mode='new_episodes')
    def test_crud_repositories(self):
        # test create:
        rfc = self.ras.get_repository_form_for_create([])
        rfc.display_name = 'CrUD-Test Repository'
        rfc.description = 'This is a Test Repository for CrUD'
        new_repository = self.ras.create_repository(rfc)
        self.assertEqual(new_repository.display_name.text, 'CrUD-Test Repository')
        self.assertEqual(new_repository.description.text, 'This is a Test Repository for CrUD')
        # test update:
        new_repository_id = new_repository.get_id()
        rfu = self.ras.get_repository_form_for_update(new_repository_id)
        rfu.set_display_name('New Name for CrUD-Test Repository')
        updated_repository = self.ras.update_repository(rfu)
        updated_repository_id = updated_repository.ident
        self.assertEqual(new_repository_id.identifier, updated_repository_id.identifier)
        self.assertEqual(self.rls.get_repository(updated_repository_id).display_name.text, 'New Name for CrUD-Test Repository')
        # test delete:
        self.ras.delete_repository(updated_repository_id)
        with self.assertRaises(NotFound):
            self.rls.get_repository(updated_repository_id)

    def test_truth(self):
        self.assertTrue(True)


class TestAssetCrUD(unittest.TestCase):

    @vcr.use_cassette('tests/fixtures/vcr_cassettes/handcar/TestAssetCrUD/setUp.yaml', record_mode='new_episodes')
    def setUp(self):
        # Not sure why Repository requires the proxy...
        rm = Runtime().get_service_manager('REPOSITORY',
                                           proxy=PROXY,
                                           implementation='TEST_SERVICE_HANDCAR')

        rls = rm.get_repository_lookup_session(proxy=PROXY)
        try:
            test_repository = utilities.get_repository_by_name('Python Test Sandbox')
        except NotFound:
            test_repository = utilities.create_sandbox_bank('Python Test Sandbox', 'a sandbox catalog for testing Python implementations.')
        test_repository_id = test_repository.ident
        self.test_repository = rls.get_repository(test_repository_id)
        self.assertEqual(self.test_repository.get_display_name().get_text(), 'Python Test Sandbox')
        self.als = rm.get_asset_lookup_session_for_repository(test_repository_id,
                                                              proxy=PROXY)
        self.aas = rm.get_asset_admin_session_for_repository(test_repository_id,
                                                             proxy=PROXY)

    @vcr.use_cassette('tests/fixtures/vcr_cassettes/handcar/TestAssetCrUD/test_crud_asset.yaml', record_mode='new_episodes')
    def test_crud_asset(self):
        # test create:
        afc = self.aas.get_asset_form_for_create([])
        afc.set_display_name('Test Asset')
        afc.set_description('This is a Test Asset')
        new_asset = self.aas.create_asset(afc)
        self.assertEqual(new_asset.get_display_name().get_text(), 'Test Asset')
        # test update:
        new_asset_id = new_asset.get_id()
        afu = self.aas.get_asset_form_for_update(new_asset_id)
        afu.set_display_name('New Name for Test Asset')
        updated_asset = self.aas.update_asset(afu)
        updated_asset_id = new_asset.get_id()
        self.assertEqual(new_asset_id.get_identifier(), updated_asset_id.get_identifier())
        self.assertEqual(self.als.get_asset(updated_asset_id).get_display_name().get_text(), 'New Name for Test Asset')
        # test delete:
        self.aas.delete_asset(new_asset_id)
        with self.assertRaises(NotFound):
            self.als.get_asset(new_asset_id)

    def test_truth(self):
        self.assertTrue(True)


class TestAssetContentCrUD(unittest.TestCase):

    @vcr.use_cassette('tests/fixtures/vcr_cassettes/handcar/TestAssetContentCrUD/setUp.yaml', record_mode='new_episodes')
    def setUp(self):
        # Not sure why Repository requires the proxy...
        rm = Runtime().get_service_manager('REPOSITORY',
                                           proxy=PROXY,
                                           implementation='TEST_SERVICE_HANDCAR')

        rls = rm.get_repository_lookup_session(proxy=PROXY)
        try:
            test_repository = utilities.get_repository_by_name('Python Test Sandbox')
        except NotFound:
            test_repository = utilities.create_sandbox_bank('Python Test Sandbox', 'a sandbox catalog for testing Python implementations.')
        test_repository_id = test_repository.ident
        self.test_asset = utilities.create_asset(test_repository_id, 'AssetContent CrUD Asset', 'Asset for testing AssetContent CrUD')
        self.test_repository = rls.get_repository(test_repository_id)
        self.als = rm.get_asset_lookup_session_for_repository(test_repository_id,
                                                              proxy=PROXY)
        self.aas = rm.get_asset_admin_session_for_repository(test_repository_id,
                                                             proxy=PROXY)

    @vcr.use_cassette('tests/fixtures/vcr_cassettes/handcar/TestAssetContentCrUD/test_crud_asset_content.yaml', record_mode='new_episodes')
    def test_crud_asset_content(self):
        # test create:
        acfc = self.aas.get_asset_content_form_for_create(self.test_asset.ident, [])
        acfc.set_display_name('Test Asset Content')
        acfc.set_description('This is a Test Asset Content')
        acfc.set_url('http://web.mit.edu')
        self.aas.create_asset_content(acfc)
        new_asset = self.als.get_asset(self.test_asset.ident)
        new_asset_content = next(new_asset.get_asset_contents())
        self.assertEqual(new_asset_content.get_display_name().get_text(), 'Test Asset Content')
        self.assertEqual(new_asset_content.get_description().get_text(), 'This is a Test Asset Content')
        self.assertEqual(new_asset_content.get_url(), 'http://web.mit.edu')
        # test update:
        new_asset_content_id = new_asset_content.get_id()
        acfu = self.aas.get_asset_content_form_for_update(new_asset_content_id)
        acfu.set_display_name('New Name for Test Asset Content')
        acfu.set_description('This is an updated description for Test Asset Content')
        acfu.set_url('http://www.stanford.edu')
        self.aas.update_asset_content(acfu)
        updated_asset = self.als.get_asset(self.test_asset.ident)
        updated_asset_contents = updated_asset.get_asset_contents()
        self.assertEqual(updated_asset_contents.available(), 1)
        updated_asset_content = next(updated_asset_contents)
        self.assertEqual(updated_asset_content.get_display_name().get_text(), 'New Name for Test Asset Content')
        self.assertEqual(updated_asset_content.get_description().get_text(), 'This is an updated description for Test Asset Content')
        self.assertEqual(updated_asset_content.get_url(), 'http://www.stanford.edu')
        # test delete:
        self.aas.delete_asset_content(new_asset_content_id)
        self.assertEqual(self.als.get_asset(self.test_asset.ident).get_asset_contents().available(), 0)

    def test_truth(self):
        self.assertTrue(True)

    @vcr.use_cassette('tests/fixtures/vcr_cassettes/handcar/TestAssetContentCrUD/tearDown.yaml', record_mode='new_episodes')
    def tearDown(self):
        self.aas.delete_asset(self.test_asset.ident)
