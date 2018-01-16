"""
Defines records for assessment parts
"""
import json

from bson import ObjectId
from collections import OrderedDict
from random import shuffle

try:
    # python 2
    from urllib import quote, unquote
except ImportError:
    # python 3
    from urllib.parse import quote, unquote

from collections import OrderedDict

from dlkit.json_.assessment.assessment_utilities import get_assessment_part_lookup_session
from dlkit.json_.assessment_authoring.objects import AssessmentPartList
from dlkit.json_.assessment_authoring.sessions import AssessmentPartLookupSession
from dlkit.json_.id.objects import IdList
from dlkit.json_.osid import record_templates as osid_records
from dlkit.json_.osid.metadata import Metadata
from dlkit.json_.utilities import JSONClientValidated

from dlkit.abstract_osid.assessment_authoring import record_templates as abc_assessment_authoring_records
from dlkit.abstract_osid.osid.errors import IllegalState, InvalidArgument, NoAccess, NotFound, OperationFailed
from dlkit.primordium.id.primitives import Id

from ...osid.base_records import ObjectInitRecord

MAGIC_PART_AUTHORITY = 'magic-part-authority'
ENDLESS = 10000  # For seemingly endless waypoints


def get_part_from_magic_part_lookup_session(section, part_id, *args, **kwargs):
    mpls = MagicAssessmentPartLookupSession(section, *args, **kwargs)
    mpls.use_unsequestered_assessment_part_view()
    mpls.use_federated_bank_view()
    return mpls.get_assessment_part(part_id)


class ScaffoldDownAssessmentPartRecord(ObjectInitRecord):
    """magic assessment part record for scaffold down adaptive questions"""
    _implemented_record_type_identifiers = [
        'scaffold-down'
    ]

    def __init__(self, *args, **kwargs):
        super(ScaffoldDownAssessmentPartRecord, self).__init__(*args, **kwargs)
        self._magic_identifier = None
        self._assessment_section = None
        self._magic_parent_id = None
        self._level = 0
        self._part_map = dict()
        self._child_parts = None
        if self.my_osid_object._my_map['maxWaypointItems'] is None:
            self._max_waypoints = ENDLESS
        else:
            self._max_waypoints = self.my_osid_object._my_map['maxWaypointItems']

    def get_id(self):
        """override get_id to generate our "magic" id that encodes scaffolding information"""
        waypoint_index = 0
        if 'waypointIndex' in self.my_osid_object._my_map:
            waypoint_index = self.my_osid_object._my_map['waypointIndex']
        # NOTE that the order of the dict **must** match the order in generate_children()
        #   when creating the child_part_id
        #   1) level
        #   2) objective_ids
        #   3) parent_id
        #   4) waypoint_index
        magic_identifier = OrderedDict({
            'level': self._level,
            'objective_ids': self.my_osid_object._my_map['learningObjectiveIds'],
        })
        if self._magic_parent_id is not None:
            magic_identifier['parent_id'] = str(self._magic_parent_id)
        magic_identifier['waypoint_index'] = waypoint_index

        identifier = quote('{0}?{1}'.format(str(self.my_osid_object._my_map['_id']),
                                            json.dumps(magic_identifier)))
        return Id(namespace='assessment_authoring.AssessmentPart',
                  identifier=identifier,
                  authority=MAGIC_PART_AUTHORITY)

    ident = property(fget=get_id)
    id_ = property(fget=get_id)

    def initialize(self, magic_identifier, assessment_section):
        """This method is to be called by a magic AssessmentPart lookup session.

        magic_identifier_part includes:
            parent_id = id string of the parent part that created this part
            level = how many levels deep
            objective_id = the Objective Id to for which to select an item
            waypoint_index = the index of this item in its parent part

        """
        arg_map = json.loads(unquote(magic_identifier).split('?')[-1],
                             object_pairs_hook=OrderedDict)
        self._magic_identifier = magic_identifier
        self._assessment_section = assessment_section
        if 'level' in arg_map:
            self._level = arg_map['level']
        else:
            self._level = 0
        if 'parent_id' in arg_map:
            self._magic_parent_id = Id(arg_map['parent_id'])
        self.my_osid_object._my_map['learningObjectiveIds'] = arg_map['objective_ids']
        self.my_osid_object._my_map['waypointIndex'] = arg_map['waypoint_index']

        if self.my_osid_object._my_map['learningObjectiveIds'] != ['']:
            try:
                self.my_osid_object._my_map['itemIds'] = [str(self.get_my_item_id_from_section(assessment_section))]
            except IllegalState:
                self.load_item_for_objective()
            except AttributeError:
                # when the magic part is being retrieved without a section ...
                # i.e. when authoring, but no itemId explicitly set (perhaps it
                #      was only set with a learningObjectiveId)
                self.my_osid_object._my_map['itemIds'] = []

    def get_parts(self, parts=None, reference_level=0):
        """Recursively returns a depth-first list of all known magic parts"""
        if parts is None:
            parts = list()
            new_reference_level = reference_level
        else:
            self._level_in_section = self._level + reference_level
            new_reference_level = self._level_in_section
            parts.append(self.my_osid_object)
        if self._child_parts is None:
            if self.has_magic_children():
                self.generate_children()
            else:
                return parts
        for part in self._child_parts:
            part.get_parts(parts, new_reference_level)
            # Don't need to append here, because parts is passed by reference
            # so appending is redundant
            # child_parts = part.get_parts(parts, new_reference_level)
            # known_part_ids = [str(part.ident) for part in parts]
            #
            # for child_part in child_parts:
            #     if str(child_part.ident) not in known_part_ids:
            #         parts.append(child_part)
            #         known_part_ids.append(str(child_part.ident))
        return parts

    def load_item_for_objective(self):
        """if this is the first time for this magic part, find an LO linked item"""
        mgr = self.my_osid_object._get_provider_manager('ASSESSMENT', local=True)
        if self.my_osid_object._my_map['itemBankId']:
            item_query_session = mgr.get_item_query_session_for_bank(Id(self.my_osid_object._my_map['itemBankId']),
                                                                     proxy=self.my_osid_object._proxy)
        else:
            item_query_session = mgr.get_item_query_session(proxy=self.my_osid_object._proxy)
        item_query_session.use_federated_bank_view()
        item_query = item_query_session.get_item_query()
        for objective_id_str in self.my_osid_object._my_map['learningObjectiveIds']:
            item_query.match_learning_objective_id(Id(objective_id_str), True)
        item_list = list(item_query_session.get_items_by_query(item_query))
        # Let's query all takens and their children sections for questions, to
        # remove seen ones
        taking_agent_id = self._assessment_section._assessment_taken.taking_agent_id
        atqs = mgr.get_assessment_taken_query_session(proxy=self.my_osid_object._proxy)
        atqs.use_federated_bank_view()
        querier = atqs.get_assessment_taken_query()
        querier.match_taking_agent_id(taking_agent_id, match=True)
        # let's seed this with the current section's questions
        seen_items = [item_id for item_id in self._assessment_section._item_id_list]
        taken_ids = [str(t.ident)
                     for t in atqs.get_assessments_taken_by_query(querier)]
        # Try to find the questions directly via Mongo query -- don't do
        # for section in taken._get_assessment_sections():
        #     seen_items += [question['itemId'] for question in section._my_map['questions']]
        # because standing up all the sections is wasteful
        collection = JSONClientValidated('assessment',
                                         collection='AssessmentSection',
                                         runtime=self.my_osid_object._runtime)
        results = collection.find({"assessmentTakenId": {"$in": taken_ids}})
        for section in results:
            if 'questions' in section:
                seen_items += [question['itemId'] for question in section['questions']]
        unseen_item_id = None
        # need to randomly shuffle this item_list
        shuffle(item_list)
        for item in item_list:
            if str(item.ident) not in seen_items:
                unseen_item_id = item.get_id()
                break
        if unseen_item_id is not None:
            self.my_osid_object._my_map['itemIds'] = [str(unseen_item_id)]
        elif self.my_osid_object._my_map['allowRepeatItems']:
            if len(item_list) > 0:
                self.my_osid_object._my_map['itemIds'] = [str(item_list[0].ident)]
            else:
                self.my_osid_object._my_map['itemIds'] = []  # don't put '' here, it will break when it tries to find an item with id ''
        else:
            self.my_osid_object._my_map['itemIds'] = []  # don't put '' here, it will break when it tries to find an item with id ''

    def has_magic_children(self):
        """checks if child parts are currently available for this part"""
        if self._child_parts is not None:  # generate_children has already been called
            return bool(self._child_parts)
        if self._assessment_section is not None:
            if (self.my_osid_object._my_map['maxLevels'] is None or
                    self.my_osid_object._my_map['maxLevels'] > self._level):
                try:
                    section = self._assessment_section
                    item_id = self.get_my_item_id_from_section(section)
                    if not section.is_correct(item_id) and section.get_confused_learning_objective_ids(item_id).available() > 0:
                        return True
                except IllegalState:
                    pass
        return False  # REALLY? What if this is the first, non-magic part?

    def finished_generating_children(self):
        # self._child_parts gets set to empty list () in self.generate_children()
        # so it should come into here as [], not None
        if self._child_parts is None or len(self._child_parts) == 0:
            if self.has_magic_children():
                self.generate_children()
            else:
                return True
        if len(self._child_parts) == self._max_waypoints:
            return True
        num_correct = 0
        for part in self._child_parts:
            question_id = self.get_question_id_for_assessment_part(part.get_id())
            if question_id is None:
                raise OperationFailed
            try:
                if self._assessment_section.is_correct(question_id):
                    num_correct += 1
            except IllegalState:
                pass
        if num_correct >= self.my_osid_object._my_map['waypointQuota']:
            return True
        return False

    def get_question_id_for_assessment_part(self, assessment_part_id):
        question_ids = self._assessment_section.get_question_ids_for_assessment_part(assessment_part_id)
        if not question_ids:
            return None
        return question_ids[0]  # There is only one expected, but this might change

    def generate_children(self):
        if not self.has_magic_children():
            return
        self._child_parts = list()

        scaffold_objective_ids = self.get_scaffold_objective_ids()
        if scaffold_objective_ids.available() == 0:
            return

        # Prepare common Id elements for children:
        objective_id = next(scaffold_objective_ids)  # Assume just one for now
        my_id = self.my_osid_object.get_id()
        namespace = 'assessment_authoring.AssessmentPart'
        level = self._level + 1
        # NOTE that the order of the dict **must** match the order in get_id()
        #    for the part record
        #   1) level
        #   2) objective_ids
        #   3) parent_id
        #   4) waypoint_index
        arg_map = OrderedDict({'level': level,
                               'objective_ids': [str(objective_id)]})
        arg_map['parent_id'] = str(my_id)
        orig_identifier = unquote(my_id.get_identifier()).split('?')[0]

        # Generate all parts already known to the section:
        section_part_ids = [p['assessmentPartId'] for p in self._assessment_section._my_map['assessmentParts']]
        for num in range(self._max_waypoints):
            arg_map['waypoint_index'] = num
            magic_identifier_part = quote('{0}?{1}'.format(orig_identifier,
                                                           json.dumps(arg_map)))
            child_part_id = Id(authority=MAGIC_PART_AUTHORITY,
                               namespace=namespace,
                               identifier=magic_identifier_part)
            if str(child_part_id) in section_part_ids:
                # First check if the part is already cached in the section:
                if child_part_id in self._assessment_section._assessment_parts:
                    child_part = self._assessment_section._assessment_parts[child_part_id]
                # Otherwise stand up the lookup session:
                else:
                    child_part = self._assessment_section._get_assessment_part(child_part_id)
                    # child_part = get_part_from_magic_part_lookup_session(
                    #     section=self._assessment_section,
                    #     part_id=child_part_id,
                    #     runtime=self.my_osid_object._runtime,
                    #     proxy=self.my_osid_object._proxy)
                self._child_parts.append(child_part)
            else:
                break
        if len(self._child_parts) == self._max_waypoints:
            return

        # Check if any child parts are finished. This will force them to generate children too
        # have to inspect the child_parts for waypoint quota, because only checking
        # child_part.finished_generating_children() skips the entire level of child_part,
        # since finished_generating_children() checks the children of the child_part.
        should_add_new_sibling = False
        num_correct = 0
        num_not_answered = 0
        for part in self._child_parts:
            try:
                # also count up waypoint quota for the child_parts level
                # only add a new sibling if the waypoint quota for this level has not been achieved
                question_id = self.get_question_id_for_assessment_part(part.get_id())
                if question_id is None:
                    raise OperationFailed
                try:
                    if self._assessment_section.is_correct(question_id):
                        num_correct += 1
                except IllegalState:
                    num_not_answered += 1

                # NOTE: finished_generating_children() can also throw
                #   OperationFailed if it has a child_part with
                #   a new question
                if part.finished_generating_children():
                    should_add_new_sibling = True

            except OperationFailed:
                pass  # there is a new question that hasn't appeared in the section yet

        waypoint_quota_met = (num_correct >= self.my_osid_object._my_map['waypointQuota'])

        if not self._child_parts or (should_add_new_sibling and not waypoint_quota_met and num_not_answered == 0):
            child_part = get_part_from_magic_part_lookup_session(
                section=self._assessment_section,
                part_id=child_part_id,
                runtime=self.my_osid_object._runtime,
                proxy=self.my_osid_object._proxy)
            self._child_parts.append(child_part)

    def get_child_ids(self):
        """gets the ids for the child parts"""
        if self.has_magic_children():
            if self._child_parts is None:
                self.generate_children()
            child_ids = list()
            for part in self._child_parts:
                child_ids.append(part.get_id())
            return IdList(child_ids,
                          runtime=self.my_osid_object._runtime,
                          proxy=self.my_osid_object._runtime)
        raise IllegalState()

    def get_children(self):
        """return the current child parts of this assessment part"""
        if self.has_magic_children():
            if self._child_parts is None:
                self.generate_children()
            return self._child_parts
        raise IllegalState()

    def has_item_ids(self):
        """does this part have any item ids associated with it"""
        return bool(self.my_osid_object._my_map['itemIds'])

    def get_item_ids(self):
        """get item ids associated with this assessment part"""
        if self.has_item_ids():
            return IdList(self.my_osid_object._my_map['itemIds'],
                          runtime=self.my_osid_object._runtime,
                          proxy=self.my_osid_object._proxy)
        raise IllegalState()

    def get_learning_objective_ids(self):
        """gets all LO ids associated with this assessment part (should be only one for now)"""
        return IdList(self.my_osid_object._my_map['learningObjectiveIds'],
                      runtime=self.my_osid_object._runtime,
                      proxy=self.my_osid_object._proxy)

    learning_objective_ids = property(fget=get_learning_objective_ids)

    def has_waypoint_quota(self):
        """is a quota on the number of required correct waypoint answers available"""
        return bool(self.my_osid_object._my_map['waypointQuota'])

    def get_waypoint_quota(self):
        """get the correct answer quota for this waypoint"""
        return self.my_osid_object._my_map['waypointQuota']

    waypoint_quota = property(fget=get_waypoint_quota)

    def get_scaffold_objective_ids(self):
        """Assumes that a scaffold objective id is available"""
        section = self._assessment_section
        item_id = self.get_my_item_id_from_section(section)
        return section.get_confused_learning_objective_ids(item_id)

    def get_my_item_id_from_section(self, section):
        """returns the first item associated with this magic Part Id in the Section"""
        for question_map in section._my_map['questions']:
            if question_map['assessmentPartId'] == str(self.get_id()):
                return section.get_question(question_map=question_map).get_id()
        raise IllegalState('This Part currently has no Item in the Section')

    def delete(self):
        """need this because the JSONClientValidated cannot deal with the magic identifier"""
        magic_identifier = unquote(self.get_id().identifier)
        orig_identifier = magic_identifier.split('?')[0]
        collection = JSONClientValidated('assessment_authoring',
                                         collection='AssessmentPart',
                                         runtime=self.my_osid_object._runtime)
        collection.delete_one({'_id': ObjectId(orig_identifier)})

    def has_parent_part(self):
        if self._magic_parent_id is None:
            # let my_osid_object handle it
            return bool(self.my_osid_object._my_map['assessmentPartId'])
        return True

    def get_assessment_part_id(self):
        if self._magic_parent_id is None:
            return Id(self.my_osid_object._my_map['assessmentPartId'])
            # raise AttributeError()  # let my_osid_object handle it
        return self._magic_parent_id

    def get_assessment_part(self):
        """If there's an AssessmentSection ask it first for the part.

        This will take advantage of the fact that the AssessmentSection may
        have already cached the Part in question.

        """
        if self._magic_parent_id is None:
            assessment_part_id = Id(self.my_osid_object._my_map['assessmentPartId'])
        else:
            assessment_part_id = self._magic_parent_id
        if self._assessment_section is not None:
            return self._assessment_section._get_assessment_part(assessment_part_id)
        # else:
        apls = get_assessment_part_lookup_session(runtime=self.my_osid_object._runtime,
                                                  proxy=self.my_osid_object._proxy,
                                                  section=self._assessment_section)
        apls.use_federated_bank_view()
        apls.use_unsequestered_assessment_part_view()
        return apls.get_assessment_part(assessment_part_id)


class ScaffoldDownAssessmentPartFormRecord(abc_assessment_authoring_records.AssessmentPartFormRecord,
                                           osid_records.OsidRecord):
    """magic assessment part form record for scaffold down adaptive assessments"""

    _implemented_record_type_identifiers = [
        'scaffold-down'
    ]

    def __init__(self, osid_object_form=None):
        if osid_object_form is not None:
            self.my_osid_object_form = osid_object_form
        self._init_metadata()
        if not self.my_osid_object_form.is_for_update():
            self._init_map()
        super(ScaffoldDownAssessmentPartFormRecord, self).__init__()

    def _init_metadata(self):
        self._item_ids_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'item'),
            'element_label': 'Item',
            'instructions': 'accepts an Item id',
            'required': False,
            'read_only': False,
            'linked': False,
            'array': False,
            'default_id_values': [''],
            'syntax': 'ID',
            'id_set': []
        }
        self._learning_objective_ids_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'learning-objective'),
            'element_label': 'Learning Objective',
            'instructions': 'accepts a Learning Objective id',
            'required': False,
            'read_only': False,
            'linked': False,
            'array': False,
            'default_id_values': [''],
            'syntax': 'ID',
            'id_set': []
        }
        self._max_levels_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'max-levels'),
            'element_label': 'Max Levels',
            'instructions': 'accepts an integer value',
            'required': True,
            'read_only': False,
            'linked': False,
            'array': False,
            'default_cardinal_values': [None],
            'syntax': 'CARDINAL',
            'minimum_cardinal': 0,
            'maximum_cardinal': None,
            'cardinal_set': []
        }
        self._max_waypoint_items_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'max-waypoint-items'),
            'element_label': 'Max Waypoint Items',
            'instructions': 'accepts an integer value',
            'required': True,
            'read_only': False,
            'linked': False,
            'array': False,
            'default_cardinal_values': [None],
            'syntax': 'CARDINAL',
            'minimum_cardinal': 0,
            'maximum_cardinal': None,
            'cardinal_set': []
        }
        self._waypoint_quota_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'waypoint-quota'),
            'element_label': 'Waypoint Quota',
            'instructions': 'accepts an integer value',
            'required': True,
            'read_only': False,
            'linked': False,
            'array': False,
            'default_cardinal_values': [0],
            'syntax': 'CARDINAL',
            'minimum_cardinal': 0,
            'maximum_cardinal': None,
            'cardinal_set': []
        }
        self._item_bank_id_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'item-bank'),
            'element_label': 'Item Bank',
            'instructions': 'accepts an assessment Bank Id',
            'required': False,
            'read_only': False,
            'linked': False,
            'array': False,
            'default_id_values': [''],
            'syntax': 'ID',
            'id_set': []
        }
        self._allow_repeat_items_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'allow-repeat-items'),
            'element_label': 'Allow Repeat Items',
            'instructions': 'accepts a boolean value',
            'required': True,
            'read_only': False,
            'linked': False,
            'array': False,
            'default_boolean_values': [True],
            'syntax': 'BOOLEAN'
        }

    def _init_map(self):
        """stub"""
        # super(ScaffoldDownAssessmentPartFormRecord, self)._init_map()
        self.my_osid_object_form._my_map['itemIds'] = \
            [str(self._item_ids_metadata['default_id_values'][0])]
        self.my_osid_object_form._my_map['learningObjectiveIds'] = \
            [str(self._learning_objective_ids_metadata['default_id_values'][0])]
        self.my_osid_object_form._my_map['maxLevels'] = \
            self._max_levels_metadata['default_cardinal_values'][0]
        self.my_osid_object_form._my_map['maxWaypointItems'] = \
            self._max_waypoint_items_metadata['default_cardinal_values'][0]
        self.my_osid_object_form._my_map['waypointQuota'] = \
            self._waypoint_quota_metadata['default_cardinal_values'][0]
        self.my_osid_object_form._my_map['itemBankId'] = \
            self._item_bank_id_metadata['default_id_values'][0]
        self.my_osid_object_form._my_map['allowRepeatItems'] = \
            bool(self._allow_repeat_items_metadata['default_boolean_values'][0])

    def get_item_ids_metadata(self):
        """get the metadata for item"""
        metadata = dict(self._item_ids_metadata)
        metadata.update({'existing_id_values': self.my_osid_object_form._my_map['itemIds']})
        return Metadata(**metadata)

    def set_item_ids(self, item_ids):
        '''the target Item

        This can only be set if there is no learning objective set

        '''
        if self.get_item_ids_metadata().is_read_only():
            raise NoAccess()
        for item_id in item_ids:
            if not self.my_osid_object_form._is_valid_id(item_id):
                raise InvalidArgument()
        if self.my_osid_object_form._my_map['learningObjectiveIds'][0]:
            raise IllegalState()
        self.my_osid_object_form._my_map['itemIds'] = [str(i) for i in item_ids]

    def clear_item_ids(self):
        if (self.get_item_ids_metadata().is_read_only() or
                self.get_item_ids_metadata().is_required()):
            raise NoAccess()
        self.my_osid_object_form._my_map['itemIds'] = \
            [str(self.get_item_ids_metadata().get_default_id_values()[0])]

    def get_learning_objective_ids_metadata(self):
        """get the metadata for learning objective"""
        metadata = dict(self._learning_objective_ids_metadata)
        metadata.update({'existing_id_values': self.my_osid_object_form._my_map['learningObjectiveIds'][0]})
        return Metadata(**metadata)

    def set_learning_objective_ids(self, learning_objective_ids):
        """the learning objective to find related items for

        This can only be set if there are no items specifically set

        """
        if self.get_learning_objective_ids_metadata().is_read_only():
            raise NoAccess()
        for learning_objective_id in learning_objective_ids:
            if not self.my_osid_object_form._is_valid_id(learning_objective_id):
                raise InvalidArgument()
        if self.my_osid_object_form._my_map['itemIds'][0]:
            raise IllegalState()
        self.my_osid_object_form._my_map['learningObjectiveIds'] = [str(lo) for lo in learning_objective_ids]

    def clear_learning_objective_ids(self):
        if (self.get_learning_objective_ids_metadata().is_read_only() or
                self.get_learning_objective_ids_metadata().is_required()):
            raise NoAccess()
        self.my_osid_object_form._my_map['learningObjectiveIds'] = \
            [str(self.get_learning_objective_ids_metadata().get_default_id_values()[0])]

    def get_max_levels_metadata(self):
        """get the metadata for max levels"""
        metadata = dict(self._max_levels_metadata)
        metadata.update({'existing_cardinal_values': self.my_osid_object_form._my_map['maxLevels']})
        return Metadata(**metadata)

    def set_max_levels(self, max_levels):
        if self.get_max_levels_metadata().is_read_only():
            raise NoAccess()
        if not self.my_osid_object_form._is_valid_cardinal(max_levels):
            raise InvalidArgument()
        self.my_osid_object_form._my_map['maxLevels'] = max_levels

    def clear_max_levels(self):
        if (self.get_max_levels_metadata().is_read_only() or
                self.get_max_levels_metadata().is_required()):
            raise NoAccess()
        self.my_osid_object_form._my_map['maxLevels'] = \
            self.get_max_levels_metadata().get_default_cardinal_values()[0]

    def get_max_waypoint_items_metadata(self):
        """get the metadata for max waypoint items"""
        metadata = dict(self._max_waypoint_items_metadata)
        metadata.update({'existing_cardinal_values': self.my_osid_object_form._my_map['maxWaypointItems']})
        return Metadata(**metadata)

    def set_max_waypoint_items(self, max_waypoint_items):
        """This determines how many waypoint items will be seen for a scaffolded wrong answer"""
        if self.get_max_waypoint_items_metadata().is_read_only():
            raise NoAccess()
        if not self.my_osid_object_form._is_valid_cardinal(max_waypoint_items,
                                                           self.get_max_waypoint_items_metadata()):
            raise InvalidArgument()
        self.my_osid_object_form._my_map['maxWaypointItems'] = max_waypoint_items

    def clear_max_waypoint_items(self):
        if (self.get_max_waypoint_items_metadata().is_read_only() or
                self.get_max_waypoint_items_metadata().is_required()):
            raise NoAccess()
        self.my_osid_object_form._my_map['maxWaypointItems'] = \
            self.get_max_waypoint_items_metadata().get_default_cardinal_values()[0]

    def get_waypoint_quota_metadata(self):
        """get the metadata for waypoint quota"""
        metadata = dict(self._waypoint_quota_metadata)
        metadata.update({'existing_cardinal_values': self.my_osid_object_form._my_map['waypointQuota']})
        return Metadata(**metadata)

    def set_waypoint_quota(self, waypoint_quota):
        """how many waypoint questions need to be answered correctly"""
        if self.get_waypoint_quota_metadata().is_read_only():
            raise NoAccess()
        if not self.my_osid_object_form._is_valid_cardinal(waypoint_quota,
                                                           self.get_waypoint_quota_metadata()):
            raise InvalidArgument()
        self.my_osid_object_form._my_map['waypointQuota'] = waypoint_quota

    def clear_waypoint_quota(self):
        if (self.get_waypoint_quota_metadata().is_read_only() or
                self.get_waypoint_quota_metadata().is_required()):
            raise NoAccess()
        self.my_osid_object_form._my_map['waypointQuota'] = \
            self.get_waypoint_quota_metadata().get_default_cardinal_values()[0]

    def get_item_bank_id_metadata(self):
        """get the metadata for item bank"""
        metadata = dict(self._item_bank_id_metadata)
        metadata.update({'existing_id_values': self.my_osid_object_form._my_map['itemBankId']})
        return Metadata(**metadata)

    def set_item_bank_id(self, bank_id):
        """the assessment bank in which to search for items, such as related to an objective"""
        if self.get_item_bank_id_metadata().is_read_only():
            raise NoAccess()
        if not self.my_osid_object_form._is_valid_id(bank_id):
            raise InvalidArgument()
        self.my_osid_object_form._my_map['itemBankId'] = str(bank_id)

    def clear_item_bank_id(self):
        if (self.get_item_bank_id_metadata().is_read_only() or
                self.get_item_bank_id_metadata().is_required()):
            raise NoAccess()
        self.my_osid_object_form._my_map['itemBankId'] = \
            self.get_item_bank_id_metadata().get_default_id_values()[0]

    def get_allow_repeat_items_metadata(self):
        """get the metadata for allow repeat items"""
        metadata = dict(self._allow_repeat_items_metadata)
        metadata.update({'existing_id_values': self.my_osid_object_form._my_map['allowRepeatItems']})
        return Metadata(**metadata)

    def set_allow_repeat_items(self, allow_repeat_items):
        """determines if repeat items will be shown, or if the scaffold iteration will simply stop"""
        if self.get_allow_repeat_items_metadata().is_read_only():
            raise NoAccess()
        if not self.my_osid_object_form._is_valid_boolean(allow_repeat_items):
            raise InvalidArgument()
        self.my_osid_object_form._my_map['allowRepeatItems'] = allow_repeat_items

    def clear_allow_repeat_items(self):
        """reset allow repeat itmes to default value"""
        if (self.get_allow_repeat_items_metadata().is_read_only() or
                self.get_allow_repeat_items_metadata().is_required()):
            raise NoAccess()
        self.my_osid_object_form._my_map['allowRepeatItems'] = \
            bool(self._allow_repeat_items_metadata['default_boolean_values'][0])


class MagicAssessmentPartLookupSession(AssessmentPartLookupSession):
    """This magic session should be used for getting magic AssessmentParts"""

    def __init__(self, assessment_section=None, *args, **kwargs):
        super(MagicAssessmentPartLookupSession, self).__init__(*args, **kwargs)
        self._my_assessment_section = assessment_section
        self._magic_parts = {}

    def update_section(self, assessment_section):
        # because we are now caching this lookup session in the AssessmentSession,
        #   in order to check the right seen_items for each magic part, we need to
        #   pass the parts an updated section...
        self._my_assessment_section = assessment_section
        for part in self._magic_parts:
            part._assessment_section = assessment_section

    def get_assessment_part(self, assessment_part_id):
        authority = assessment_part_id.get_authority()
        if assessment_part_id not in self._magic_parts:
            if authority == MAGIC_PART_AUTHORITY:
                magic_identifier = unquote(assessment_part_id.identifier)
                orig_identifier = magic_identifier.split('?')[0]
                assessment_part = super(MagicAssessmentPartLookupSession, self).get_assessment_part(assessment_part_id=Id(authority=self._catalog.ident.authority,
                                                                                                                          namespace=assessment_part_id.get_identifier_namespace(),
                                                                                                                          identifier=orig_identifier))
                # should a magic assessment part's parent be the original part?
                # Or that original part's parent?
                assessment_part.initialize(assessment_part_id.identifier, self._my_assessment_section)
            else:
                assessment_part = super(MagicAssessmentPartLookupSession, self).get_assessment_part(assessment_part_id)
            self._magic_parts[assessment_part_id] = assessment_part
            return assessment_part
        else:
            return self._magic_parts[assessment_part_id]

    def get_assessment_parts_by_ids(self, assessment_part_ids):
        part_list = []
        for assessment_part_id in assessment_part_ids:
            try:
                part_list.append(self.get_assessment_part(assessment_part_id))
            except NotFound:
                # sequestered?
                pass
        return AssessmentPartList(part_list, runtime=self._runtime, proxy=self._proxy)
