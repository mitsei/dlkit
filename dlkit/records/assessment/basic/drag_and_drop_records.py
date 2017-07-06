"""
records.basic.drag_and_drop
"""
from bson.objectid import ObjectId

from copy import deepcopy

from random import shuffle

from dlkit.abstract_osid.assessment import record_templates as abc_assessment_records
from dlkit.abstract_osid.mapping import primitives as abc_mapping_primitives
from dlkit.json_.id.objects import IdList
from dlkit.json_.osid import record_templates as osid_records
from dlkit.json_.osid.metadata import Metadata
from dlkit.json_.primitives import Id, Type, DisplayText
from dlkit.json_.osid.osid_errors import IllegalState, NoAccess, NotFound, InvalidArgument
from dlkit.json_ import types, utilities
from dlkit.primordium.mapping.spatial_units import SpatialUnitFactory
from dlkit.primordium.mapping.coordinate_primitives import BasicCoordinate

from .feedback_item_records import FeedbackAnswerItemRecord, FeedbackAnswerItemFormRecord
from .base_records import MultiLanguageQuestionFormRecord, MultiLanguageQuestionRecord

DEFAULT_LANGUAGE_TYPE = Type(**types.Language().get_type_data('DEFAULT'))
DEFAULT_SCRIPT_TYPE = Type(**types.Script().get_type_data('DEFAULT'))
DEFAULT_FORMAT_TYPE = Type(**types.Format().get_type_data('DEFAULT'))


class DragAndDropItemRecord(FeedbackAnswerItemRecord):
    """A record for a basic drag-and-drop ``Item``.

    Can evaluate provided Responses with related Answers

    """
    _implemented_record_type_identifiers = [
        'drag-and-drop'
    ]

    def __init__(self, osid_object_form=None):
        super(DragAndDropItemRecord, self).__init__(osid_object_form)
        self._zones = None
        self._condition_maps = {}

    def _make_conditions_map(self, answer):
        match_inc_exc = {True: 'include', False: 'exclude'}
        if self._zones is None:
            self._zones = {}
            for zone in self.my_osid_object.get_question().get_zones():
                zone['spatialUnit'] = SpatialUnitFactory().get_spatial_unit(spatial_unit_map=zone['spatialUnit'])
                self._zones[zone['id']] = zone
        spatial_unit_conditions = {'include': {}, 'exclude': {}}
        coordinate_conditions = {'include': {}, 'exclude': {}}

        for condition in answer.get_zone_conditions():
            inc_exc = match_inc_exc[condition['match']]
            if condition['droppableId'] not in spatial_unit_conditions[inc_exc]:
                spatial_unit_conditions[inc_exc][condition['droppableId']] = []
            spatial_unit_conditions[inc_exc][condition['droppableId']].append(self._zones[condition['zoneId']])

        for condition in answer.get_spatial_unit_conditions():
            inc_exc = match_inc_exc[condition['match']]
            if condition['droppableId'] not in spatial_unit_conditions[inc_exc]:
                spatial_unit_conditions[inc_exc][condition['droppableId']] = []
            spatial_unit_conditions[inc_exc][condition['droppableId']].append(condition)

        for condition in answer.get_coordinate_conditions():
            inc_exc = match_inc_exc[condition['match']]
            if condition['droppableId'] not in coordinate_conditions[inc_exc]:
                coordinate_conditions[inc_exc][condition['droppableId']] = []
            coordinate_conditions[inc_exc][condition['droppableId']].append(condition)

        return {'spatial_unit_conditions': spatial_unit_conditions, 'coordinate_conditions': coordinate_conditions}

    def _get_conditions_map(self, answer):
        if answer.get_id() not in self._condition_maps:
            self._condition_maps[answer.get_id()] = self._make_conditions_map(answer)
        return self._condition_maps[answer.get_id()]

    def _is_match(self, response, answer):
        """Does the response match the answer """

        def compare_conditions(droppable_id, spatial_units, response_conditions):
            """Compare response coordinates with spatial units for droppable_id"""
            coordinate_match = True
            for coordinate in response_conditions['coordinate_conditions']['include'][droppable_id]:
                answer_match = False
                for spatial_unit in spatial_units:
                    if (coordinate['containerId'] == spatial_unit['containerId'] and
                            coordinate['coordinate'] in spatial_unit['spatialUnit']):
                        answer_match = True
                        break
                coordinate_match = coordinate_match and answer_match
            return coordinate_match

        # Did the consumer application already do the work for us?
        if response.has_zone_conditions():
            return bool(response.get_zone_conditions() == answer.get_zone_conditions())

        answer_conditions = self._get_conditions_map(answer)
        response_conditions = self._get_conditions_map(response)

        # Check to see if the lists of droppables used are the same:
        if set(answer_conditions['spatial_unit_conditions']['include']) != set(response_conditions['coordinate_conditions']['include']):
            return False

        # Compare included answer spatial unit areas to response coordinates
        for droppable_id, spatial_units in answer_conditions['spatial_unit_conditions']['include'].items():
            # Do the number of defined include conditions match:
            if len(spatial_units) != len(response_conditions['coordinate_conditions']['include'][droppable_id]):
                return False
            if not compare_conditions(droppable_id, spatial_units, response_conditions):
                return False

        # Compare excluded answer spatial unit areas to response coordinates
        for droppable_id, spatial_units in answer_conditions['spatial_unit_conditions']['exclude'].items():
            if compare_conditions(droppable_id, spatial_units, response_conditions):
                return False
        return True

    def is_correctness_available_for_response(self, response):
        """is a measure of correctness available for a particular d&d response"""
        return True

    def is_response_correct(self, response):
        """returns True if response evaluates to an Item Answer that is 100 percent correct"""
        for answer in self.my_osid_object.get_answers():
            if self._is_match(response, answer):
                return True
        return False

    def get_correctness_for_response(self, response):
        """get measure of correctness available for a particular response"""
        for answer in self.my_osid_object.get_answers():
            if self._is_match(response, answer):
                try:
                    return answer.get_score()
                except AttributeError:
                    return 100
        for answer in self.my_osid_object.get_wrong_answers():
            if self._is_match(response, answer):
                try:
                    return answer.get_score()
                except AttributeError:
                    return 0
        return 0

    def get_answer_for_response(self, response):
        for answer in self.my_osid_object.get_answers():
            if self._is_match(response, answer):
                return answer
        for answer in self.my_osid_object.get_wrong_answers():
            if self._is_match(response, answer):
                return answer
        # look for a generic wrong-answer
        for answer in self.my_osid_object.get_wrong_answers():
            if (not answer.has_coordinate_conditions() and
                    not answer.has_spatial_unit_conditions() and
                    not answer.has_zone_conditions()):
                return answer
        raise NotFound('no matching answer found for response')

    def is_feedback_available_for_response(self, response):
        try:
            answer = self.get_answer_for_response(response)
        except NotFound:
            return False
        try:
            return answer.has_feedback()
        except AttributeError:
            return False

    def get_feedback_for_response(self, response):
        try:
            answer = self.get_answer_for_response(response)
        except NotFound:
            raise IllegalState('no answer matching response was found')
        answer.object_map  # this will generate any source URLs from the adapter...kind of a hack
        return answer.get_feedback()  # raises IllegalState

    def get_confused_learning_objective_ids_for_response(self, response):
        try:
            answer = self.get_answer_for_response(response)
        except NotFound:
            raise IllegalState('no answer matching response was found')
        try:
            return answer.get_confused_learning_objective_ids()
        except AttributeError:
            return IdList([])


class DragAndDropItemFormRecord(FeedbackAnswerItemFormRecord):
    """A record for a basic multi-choice ``Item`` Form.

    Marker

    """
    _implemented_record_type_identifiers = [
        'drag-and-drop'
    ]


class DragAndDropAnswerRecord(osid_records.OsidRecord,
                              abc_assessment_records.AnswerRecord):
    """A record for an ``Answer``.

    The methods specified by the record type are available through the
    underlying object.

    """
    _implemented_record_type_identifiers = [
        'drag-and-drop'
    ]

    def __init__(self, osid_object):
        self.my_osid_object = osid_object
        super(DragAndDropAnswerRecord, self).__init__()

    def has_zone_conditions(self):
        return bool(self.my_osid_object._my_map['zoneConditions'])

    def get_zone_conditions(self):
        """stub"""
        return deepcopy(self.my_osid_object._my_map['zoneConditions'])

    def has_coordinate_conditions(self):
        return bool(self.my_osid_object._my_map['coordinateConditions'])

    def get_coordinate_conditions(self):
        """stub"""
        condition_list = deepcopy(self.my_osid_object._my_map['coordinateConditions'])
        for condition in condition_list:
            condition['coordinate'] = BasicCoordinate(condition['coordinate'])
        return condition_list

    def has_spatial_unit_conditions(self):
        return bool(self.my_osid_object._my_map['spatialUnitConditions'])

    def get_spatial_unit_conditions(self):
        """stub"""
        condition_list = deepcopy(self.my_osid_object._my_map['spatialUnitConditions'])
        for condition in condition_list:
            condition['spatialUnit'] = SpatialUnitFactory().get_spatial_unit(spatial_unit_map=condition['spatialUnit'])
        return condition_list


class DragAndDropAnswerFormRecord(osid_records.OsidRecord,
                                  abc_assessment_records.AnswerFormRecord):
    """A record for an ``AnswerForm``.

    Drag-and-Drop Answer/Responses can be authored by defining multiple
    'conditions' of various kinds, whcih can be used together to describe
    more complex Answers.

    Drag-and-Drop Answers consist of three primary member elements:

        {'zoneConditions': [list of zone condition objects],
         'coordinateConditions': [list of coordinate condition objects],
         'spatialUnitConditions': [list of spatial unit condition objects]}

        Object members of a Zone Condition: # Most likely used for defining Answers
            {'type': 'ZoneCondition',
             'droppableId': droppable_id,
             'zoneId': zone_id,
             'match': boolean - defines inclusion, defaults to True}


        Object members of a Coordinate Conditions: # Most likely used for defining Responses
            {'type': 'CoordinateCondition',
             'droppableId': droppable_id,
             'coordinate': a Coordinate
             'containerId': container_id,
             'match': boolean - indicates inclusion, defaults to True}


        Object members of a Spatial Unit Condition: # Used to define "secure" spatial units
            {'type': 'SpatialUnitCondition',
             'droppableId': droppable_id,
             'spatialUnit': a Spatial Unit # See examples for Question zones
             'containerId': container_id,
             'match': boolean - indicates inclusion, defaults to True}


        Example of a Coordinate - this is a three dimensional one.
            {
                'type': 'Coordinate',
                'values': [150, 300, 250],
                'uncertaintyMinus': [20, 20, 20],  # Optional, not supported for CLIx
                'uncertaintryPlus': [20, 20, 20]   # Optional, not supported for CLIx
            }

    """
    _implemented_record_type_identifiers = [
        'drag-and-drop'
    ]

    def __init__(self, osid_object_form):
        self.my_osid_object_form = osid_object_form
        self._init_metadata()
        if not osid_object_form.is_for_update():
            self._init_map()
        super(DragAndDropAnswerFormRecord, self).__init__()

    def _init_map(self):
        """stub"""
        self.my_osid_object_form._my_map['zoneConditions'] = \
            self._zone_conditions_metadata['default_object_values'][0]
        self.my_osid_object_form._my_map['coordinateConditions'] = \
            self._coordinate_conditions_metadata['default_object_values'][0]
        self.my_osid_object_form._my_map['spatialUnitConditions'] = \
            self._spatial_unit_conditions_metadata['default_object_values'][0]

    def _init_metadata(self):
        """stub"""
        self._zone_conditions_metadata = {
            'zone_matches': Id(self.my_osid_object_form._authority,
                               self.my_osid_object_form._namespace,
                               'zone_conditions'),
            'element_label': 'zone conditions',
            'instructions': 'zone conditions for answer',
            'required': False,
            'read_only': False,
            'linked': False,
            'array': False,
            'default_object_values': [[]],
            'syntax': 'OBJECT',
        }
        self._coordinate_conditions_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'coordinate_conditions'),
            'element_label': 'coordinate conditions',
            'instructions': 'coordinate conditions for answer',
            'required': False,
            'read_only': False,
            'linked': False,
            'array': False,
            'default_object_values': [[]],
            'syntax': 'OBJECT',
        }
        self._spatial_unit_conditions_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'spatial_unit_conditions'),
            'element_label': 'spatial unit conditions',
            'instructions': 'spatial unit conditions for answer',
            'required': False,
            'read_only': False,
            'linked': False,
            'array': False,
            'default_object_values': [[]],
            'syntax': 'OBJECT',
        }

    def get_zone_conditions_metadata(self):
        """stub"""
        return Metadata(**self._zone_conditions_metadata)

    def add_zone_condition(self, droppable_id, zone_id, match=True):
        """stub"""
        self.my_osid_object_form._my_map['zoneConditions'].append(
            {'droppableId': droppable_id, 'zoneId': zone_id, 'match': match})
        self.my_osid_object_form._my_map['zoneConditions'].sort(key=lambda k: k['zoneId'])

    def clear_zone_conditions(self):
        """stub"""
        if (self.get_zone_conditions_metadata().is_read_only() or
                self.get_zone_conditions_metadata().is_required()):
            raise NoAccess()
        self.my_osid_object_form._my_map['zoneConditions'] = \
            self._zone_conditions_metadata['default_object_values'][0]

    def get_coordinate_conditions_metadata(self):
        """stub"""
        return Metadata(**self._coordinate_conditions_metadata)

    def add_coordinate_condition(self, droppable_id, container_id, coordinate, match=True):
        """stub"""
        if not isinstance(coordinate, BasicCoordinate):
            raise InvalidArgument('coordinate is not a BasicCoordinate')
        self.my_osid_object_form._my_map['coordinateConditions'].append(
            {'droppableId': droppable_id, 'containerId': container_id, 'coordinate': coordinate.get_values(), 'match': match})
        self.my_osid_object_form._my_map['coordinateConditions'].sort(key=lambda k: k['containerId'])

    def clear_coordinate_conditions(self):
        """stub"""
        if (self.get_zone_conditions_metadata().is_read_only() or
                self.get_zone_conditions_metadata().is_required()):
            raise NoAccess()
        self.my_osid_object_form._my_map['coordinateConditions'] = \
            self._coordinate_conditions_metadata['default_object_values'][0]

    def get_spatial_unit_conditions_metadata(self):
        """stub"""
        return Metadata(**self._spatial_unit_conditions_metadata)

    def add_spatial_unit_condition(self, droppable_id, container_id, spatial_unit, match=True):
        """stub"""
        if not isinstance(spatial_unit, abc_mapping_primitives.SpatialUnit):
            raise InvalidArgument('spatial_unit is not a SpatialUnit')

        self.my_osid_object_form._my_map['spatialUnitConditions'].append(
            {'droppableId': droppable_id, 'containerId': container_id, 'spatialUnit': spatial_unit.get_spatial_unit_map(), 'match': match})
        self.my_osid_object_form._my_map['spatialUnitConditions'].sort()

    def clear_spatial_unit_conditions(self):
        """stub"""
        if (self.get_spatial_unit_conditions_metadata().is_read_only() or
                self.get_zone_conditions_metadata().is_required()):
            raise NoAccess()
        self.my_osid_object_form._my_map['spatialUnitConditions'] = \
            self._zone_conditions_metadata['default_object_values'][0]


class MultiLanguageDragAndDropQuestionRecord(MultiLanguageQuestionRecord):
    def __init__(self, osid_object):
        self.my_osid_object = osid_object
        self._original_droppable_order = deepcopy(osid_object._my_map['droppables'])
        self._original_target_order = deepcopy(osid_object._my_map['targets'])
        self._original_zone_order = deepcopy(osid_object._my_map['zones'])
        try:
            self.my_osid_object._my_map['multiLanguageDroppables'] = deepcopy(self.my_osid_object._original_droppable_order)
        except AttributeError:
            self.my_osid_object._my_map['multiLanguageDroppables'] = deepcopy(self.my_osid_object._my_map['droppables'])

        try:
            self.my_osid_object._my_map['multiLanguageTargets'] = deepcopy(self.my_osid_object._original_target_order)
        except AttributeError:
            self.my_osid_object._my_map['multiLanguageTargets'] = deepcopy(self.my_osid_object._my_map['targets'])

        try:
            self.my_osid_object._my_map['multiLanguageZones'] = deepcopy(self.my_osid_object._original_zone_order)
        except AttributeError:
            self.my_osid_object._my_map['multiLanguageZones'] = deepcopy(self.my_osid_object._my_map['zones'])

        super(MultiLanguageDragAndDropQuestionRecord, self).__init__(osid_object)

        if ('shuffleDroppables' not in self.my_osid_object._my_map or
                self.my_osid_object._my_map['shuffleDroppables']):
            droppables = self.my_osid_object._my_map['droppables']
            shuffle(droppables)
            self.my_osid_object._my_map['droppables'] = droppables

        if ('shuffleTargets' not in self.my_osid_object._my_map or
                self.my_osid_object._my_map['shuffleTargets']):
            targets = self.my_osid_object._my_map['targets']
            shuffle(targets)
            self.my_osid_object._my_map['targets'] = targets

        if ('shuffleZones' not in self.my_osid_object._my_map or
                self.my_osid_object._my_map['shuffleZones']):
            zones = self.my_osid_object._my_map['zones']
            shuffle(zones)
            self.my_osid_object._my_map['zones'] = zones

    def get_unrandomized_droppables(self):
        return self._original_droppable_order

    def get_droppables(self):
        """stub"""
        droppables = []
        for current_droppable in self.my_osid_object._my_map['droppables']:
            droppables.append({
                'id': current_droppable['id'],
                'text': self.get_matching_language_value('texts',
                                                         dictionary=current_droppable).text,
                'name': self.get_matching_language_value('names',
                                                         dictionary=current_droppable).text,
                'reuse': current_droppable['reuse'],
                'dropBehaviorType': current_droppable['dropBehaviorType']
            })
        return droppables

    droppables = property(fget=get_droppables)

    def get_unrandomized_targets(self):
        return self._original_target_order

    def get_targets(self):
        """stub"""
        targets = []
        for current_target in self.my_osid_object._my_map['targets']:
            targets.append({
                'id': current_target['id'],
                'text': self.get_matching_language_value('texts',
                                                         dictionary=current_target).text,
                'name': self.get_matching_language_value('names',
                                                         dictionary=current_target).text,
                'dropBehaviorType': current_target['dropBehaviorType']
            })
        return targets

    targets = property(fget=get_targets)

    def get_unrandomized_zones(self):
        return self._original_zone_order

    def get_zones(self):
        """stub"""
        zones = []
        for current_zone in self.my_osid_object._my_map['zones']:
            zones.append({
                'id': current_zone['id'],
                'name': self.get_matching_language_value('names',
                                                         dictionary=current_zone).text,
                'description': self.get_matching_language_value('descriptions',
                                                                dictionary=current_zone).text,
                'spatialUnit': SpatialUnitFactory().get_spatial_unit(current_zone['spatialUnit']).get_spatial_unit_map(),
                'containerId': current_zone['containerId'],
                'visible': current_zone['visible'],
                'reuse': current_zone['reuse'],
                'dropBehaviorType': current_zone['dropBehaviorType']
            })
        return zones

    zones = property(fget=get_zones)

    def _update_object_map(self, obj_map):
        """unclear if it's better to use this method or get_object_map
        My main consideration is that MultiLanguageQuestionRecord already
        overrides get_object_map
        """
        obj_map['droppables'] = self.get_droppables()
        obj_map['targets'] = self.get_targets()
        obj_map['zones'] = self.get_zones()


class MultiLanguageDragAndDropQuestionFormRecord(MultiLanguageQuestionFormRecord):
    """

    Drag-and-Drop Questions consist of of three primary member elements:
        {'droppables': [list of droppable objects]
        'targets': [list of target objects, like a target image]
        'zones': [list of zone objects, geometric areas within targets on which droppables can be dropped]}

        Both targets and droppables can serve as containers for zones, allowing for
        droppables dropped on droppables to be evaluated.

        Zones define geometric areas within targets on which droppables are expected to be
        dropped or snapped to.  Zones define areas that are expected to be known to the
        question.  Other areas, not known to the question, can be defined in Answers.

    Object members for a 'target':
        {'id': str(ObjectId)
        'name': name or label for target - Do we need this??? should this be a Display Text???
        'text': Display Text, or content, of droppable, will likely include image url, alt tag, etc.
        'dropBehaviorType': defines the drop behavior on this container}

    Object members for a 'droppable':
        {'id': unique identifier str(ObjectId)
        'name': name or label for droppable - should this be a Display Text???
        'text': Display Text, or content, of droppable, will likely include image url, alt tag, etc.
        'reuse': int - number of times this droppable can be reused, 0 means unlimited.  Defaults to 1
        'dropBehaviorType': defines the drop behavior on this container}

        We can imagine drop behavior types that would indicate to the palyer what to do
        when a droppable is dropped on a target or droppable container outside of a zone.
            Drop - 'drop.behavior%3Adrop%40ODL.MIT.EDU'
            Reject - 'drop.behavior%3Areject%40ODL.MIT.EDU'

    Object members for a 'zone':
        {'id' str(ObjectId):
        'name': Display Text representing the name of the zone,
        'description': 'Display Text representing an "alt-tag" description for the zone,
        'spatialUnit': Spatial Unit object, initially, for CLIx, a two dimensional rectangle,
        'containerId': id string of the target that thie zone is contained in,
        'visible': boolean, determines whether the zone can be seen.  Defaults to True
        'reuse': int - mumber of things that can be dropped in this zone, 0 means unlimited.  Defaults to 1,
        'dropBehaviorType': defines the drop behavior}

        Initially we will support two drop behavior types for zones:
            Drop - 'drop.behavior%3Adrop%40ODL.MIT.EDU'
            Snap - 'drop.behavior%3Asnap%40ODL.MIT.EDU'

    Examples of Spatial Units:

        Rectangle - the only supported spatial unit for the CLIx project:
            {
                'type': 'SpatialUnit',
                'recordType': 'osid.mapping.SpatialUnit%3Arectangle%40ODL.MIT.EDU',
                'coordinateValues: [40, 70],
                'width': 200,
                'height: 300
            }

        Rectangular Prism:
            {
                'type': 'SpatialUnit',
                'recordType': 'osid.mapping.SpatialUnit%3Arectangular.prism%40ODL.MIT.EDU',
                'coordinateValues: [400, 700],
                'width': 200,
                'height: 300,
                'depth': 100
            }

        Circle:
            {
                'type': 'SpatialUnit,
                'recordType': 'osid.mapping.SpatialUnit%3Acircle%40ODL.MIT.EDU',
                'centerCoordinateValues: [150, 300],
                'radius': 50
            }
    """

    def __init__(self, osid_object_form=None):
        if osid_object_form is not None:
            self.my_osid_object_form = osid_object_form
        self._init_metadata()
        if not self.my_osid_object_form.is_for_update():
            self._init_map()
        super(MultiLanguageDragAndDropQuestionFormRecord, self).__init__(osid_object_form)

    def _init_map(self):
        """stub"""
        super(MultiLanguageDragAndDropQuestionFormRecord, self)._init_map()
        self.my_osid_object_form._my_map['droppables'] = \
            self._droppables_metadata['default_object_values'][0]
        self.my_osid_object_form._my_map['targets'] = \
            self._targets_metadata['default_object_values'][0]
        self.my_osid_object_form._my_map['zones'] = \
            self._zones_metadata['default_object_values'][0]
        self.my_osid_object_form._my_map['shuffleDroppables'] = \
            bool(self._shuffle_droppables_metadata['default_boolean_values'][0])
        self.my_osid_object_form._my_map['shuffleTargets'] = \
            bool(self._shuffle_targets_metadata['default_boolean_values'][0])
        self.my_osid_object_form._my_map['shuffleZones'] = \
            bool(self._shuffle_zones_metadata['default_boolean_values'][0])

    def _init_metadata(self):
        """stub"""
        super(MultiLanguageDragAndDropQuestionFormRecord, self)._init_metadata()
        self._droppables_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'droppables'),
            'element_label': 'droppables',
            'instructions': 'Enter as many droppables as you wish',
            'required': True,
            'read_only': False,
            'linked': False,
            'array': True,
            'default_object_values': [[]],
            'syntax': 'OBJECT',
            'object_set': []
        }
        self._targets_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'targets'),
            'element_label': 'targets',
            'instructions': 'Enter as many targets as you wish',
            'required': True,
            'read_only': False,
            'linked': False,
            'array': True,
            'default_object_values': [[]],
            'syntax': 'OBJECT',
            'object_set': []
        }
        self._zones_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'zones'),
            'element_label': 'zones',
            'instructions': 'Enter as many zones as you wish',
            'required': True,
            'read_only': False,
            'linked': False,
            'array': True,
            'default_object_values': [[]],
            'syntax': 'OBJECT',
            'object_set': []
        }
        self._shuffle_droppables_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'shuffleDroppables'),
            'element_label': 'Shuffle Droppables',
            'instructions': 'Shuffle droppables',
            'required': True,
            'read_only': False,
            'linked': True,
            'array': False,
            'default_boolean_values': [True],
            'syntax': 'BOOLEAN',
        }
        self._shuffle_targets_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'shuffleTargets'),
            'element_label': 'Shuffle Targets',
            'instructions': 'Shuffle targets',
            'required': True,
            'read_only': False,
            'linked': True,
            'array': False,
            'default_boolean_values': [True],
            'syntax': 'BOOLEAN',
        }
        self._shuffle_zones_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'shuffleZones'),
            'element_label': 'Shuffle Zones',
            'instructions': 'Shuffle zones',
            'required': True,
            'read_only': False,
            'linked': True,
            'array': False,
            'default_boolean_values': [True],
            'syntax': 'BOOLEAN',
        }

    def get_shuffle_droppables_metadata(self):
        return Metadata(**self._shuffle_droppables_metadata)

    def get_shuffle_targets_metadata(self):
        return Metadata(**self._shuffle_targets_metadata)

    def get_shuffle_zones_metadata(self):
        return Metadata(**self._shuffle_zones_metadata)

    def clear_shuffle_droppables(self):
        self.my_osid_object_form._my_map['shuffleDroppables'] = \
            bool(self._shuffle_droppables_metadata['default_boolean_values'][0])

    def clear_shuffle_targets(self):
        self.my_osid_object_form._my_map['shuffleTargets'] = \
            bool(self._shuffle_targets_metadata['default_boolean_values'][0])

    def clear_shuffle_zones(self):
        self.my_osid_object_form._my_map['shuffleZones'] = \
            bool(self._shuffle_zones_metadata['default_boolean_values'][0])

    def set_shuffle_droppables(self, shuffle):
        if not self.my_osid_object_form._is_valid_boolean(
                shuffle):
            raise InvalidArgument('shuffleDroppables')
        self.my_osid_object_form._my_map['shuffleDroppables'] = shuffle

    def set_shuffle_targets(self, shuffle):
        if not self.my_osid_object_form._is_valid_boolean(
                shuffle):
            raise InvalidArgument('shuffleTargets')
        self.my_osid_object_form._my_map['shuffleTargets'] = shuffle

    def set_shuffle_zones(self, shuffle):
        if not self.my_osid_object_form._is_valid_boolean(
                shuffle):
            raise InvalidArgument('shuffleZones')
        self.my_osid_object_form._my_map['shuffleZones'] = shuffle

    def get_droppables_metadata(self):
        """stub"""
        return Metadata(**self._droppables_metadata)

    def add_droppable(self, droppable_text, name='', reuse=1, drop_behavior_type=None):
        """stub"""
        if not isinstance(droppable_text, DisplayText):
            raise InvalidArgument('droppable_text is not a DisplayText object')
        if not isinstance(reuse, int):
            raise InvalidArgument('reuse must be an integer')
        if reuse < 0:
            raise InvalidArgument('reuse must be >= 0')
        if not isinstance(name, DisplayText):
            # if default ''
            name = self._str_display_text(name)
        droppable = {
            'id': str(ObjectId()),
            'texts': [self._dict_display_text(droppable_text)],
            'names': [self._dict_display_text(name)],
            'reuse': reuse,
            'dropBehaviorType': drop_behavior_type
        }
        self.my_osid_object_form._my_map['droppables'].append(droppable)
        return droppable

    def clear_droppables(self):
        """stub"""
        if self.get_droppables_metadata().is_read_only():
            raise NoAccess()
        self.my_osid_object_form._my_map['droppables'] = \
            self._droppables_metadata['default_object_values'][0]

    @utilities.arguments_not_none
    def clear_droppable_texts(self, droppable_id):
        """stub"""
        if self.get_droppables_metadata().is_read_only():
            raise NoAccess()
        updated_droppables = []
        for current_droppable in self.my_osid_object_form._my_map['droppables']:
            if current_droppable['id'] != droppable_id:
                updated_droppables.append(current_droppable)
            else:
                updated_droppables.append({
                    'id': current_droppable['id'],
                    'texts': [],
                    'names': current_droppable['names'],
                    'reuse': current_droppable['reuse'],
                    'dropBehaviorType': current_droppable['dropBehaviorType']
                })
        self.my_osid_object_form._my_map['droppables'] = updated_droppables

    @utilities.arguments_not_none
    def clear_droppable_names(self, droppable_id):
        """stub"""
        if self.get_droppables_metadata().is_read_only():
            raise NoAccess()
        updated_droppables = []
        for current_droppable in self.my_osid_object_form._my_map['droppables']:
            if current_droppable['id'] != droppable_id:
                updated_droppables.append(current_droppable)
            else:
                updated_droppables.append({
                    'id': current_droppable['id'],
                    'texts': current_droppable['texts'],
                    'names': [],
                    'reuse': current_droppable['reuse'],
                    'dropBehaviorType': current_droppable['dropBehaviorType']
                })
        self.my_osid_object_form._my_map['droppables'] = updated_droppables

    @utilities.arguments_not_none
    def remove_droppable_text_language(self, language_type, droppable_id):
        if self.get_droppables_metadata().is_read_only():
            raise NoAccess()

        droppables = [d for d in self.my_osid_object_form._my_map['droppables'] if d['id'] == droppable_id]
        if len(droppables) == 0:
            raise InvalidArgument('invalid droppable_id')

        for current_droppable in self.my_osid_object_form._my_map['droppables']:
            if droppable_id == current_droppable['id']:
                self.remove_field_by_language('texts',
                                              language_type,
                                              dictionary=current_droppable)

    @utilities.arguments_not_none
    def remove_droppable_name_language(self, language_type, droppable_id):
        if self.get_droppables_metadata().is_read_only():
            raise NoAccess()

        droppables = [d for d in self.my_osid_object_form._my_map['droppables'] if d['id'] == droppable_id]
        if len(droppables) == 0:
            raise InvalidArgument('invalid droppable_id')

        for current_droppable in self.my_osid_object_form._my_map['droppables']:
            if droppable_id == current_droppable['id']:
                self.remove_field_by_language('names',
                                              language_type,
                                              dictionary=current_droppable)

    def update_droppable(self, droppable_id, droppable_text=None, name=None, reuse=None, drop_behavior_type=None):
        if self.get_droppables_metadata().is_read_only():
            raise NoAccess()
        if droppable_text is not None and not isinstance(droppable_text, DisplayText):
            raise InvalidArgument('droppable_text must be a DisplayText object')
        if name is not None and not isinstance(name, DisplayText):
            raise InvalidArgument('name must be a DisplayText object')
        if reuse is not None and not isinstance(reuse, int):
            raise InvalidArgument('reuse must be an integer')
        if reuse is not None and reuse < 0:
            raise InvalidArgument('reuse must be >= 0')
        for current_droppable in self.my_osid_object_form._my_map['droppables']:
            if droppable_id == current_droppable['id']:
                if droppable_text is not None:
                    self.add_or_replace_value(
                        'texts', droppable_text, dictionary=current_droppable)
                if reuse is not None:
                    current_droppable['reuse'] = reuse
                if drop_behavior_type is not None:
                    current_droppable['dropBehaviorType'] = drop_behavior_type
                if name is not None:
                    self.add_or_replace_value(
                        'names', name, dictionary=current_droppable)
                return
        raise NotFound('droppable_id not found in question')

    @utilities.arguments_not_none
    def remove_droppable(self, droppable_id):
        """remove a droppable, given the id"""
        updated_droppables = []
        for droppable in self.my_osid_object_form._my_map['droppables']:
            if droppable['id'] != droppable_id:
                updated_droppables.append(droppable)
        self.my_osid_object_form._my_map['droppables'] = updated_droppables

    @utilities.arguments_not_none
    def set_droppable_order(self, droppable_ids):
        """ reorder droppables per the passed in list
        :param droppable_ids:
        :return:
        """
        reordered_droppables = []
        current_droppable_ids = [d['id'] for d in self.my_osid_object_form._my_map['droppables']]
        if set(droppable_ids) != set(current_droppable_ids):
            raise IllegalState('droppable_ids do not match existing droppables')

        for droppable_id in droppable_ids:
            for current_droppable in self.my_osid_object_form._my_map['droppables']:
                if droppable_id == current_droppable['id']:
                    reordered_droppables.append(current_droppable)
                    break

        self.my_osid_object_form._my_map['droppables'] = reordered_droppables

    def get_targets_metadata(self):
        """stub"""
        return Metadata(**self._targets_metadata)

    def add_target(self, target_text, name='', drop_behavior_type=None):
        """stub"""
        if not isinstance(target_text, DisplayText):
            raise InvalidArgument('target_text is not a DisplayText object')
        if not isinstance(name, DisplayText):
            # if default ''
            name = self._str_display_text(name)
        target = {
            'id': str(ObjectId()),
            'texts': [self._dict_display_text(target_text)],
            'names': [self._dict_display_text(name)],
            'dropBehaviorType': drop_behavior_type
        }
        self.my_osid_object_form._my_map['targets'].append(target)
        return target

    def clear_targets(self):
        """stub"""
        if self.get_targets_metadata().is_read_only():
            raise NoAccess()
        self.my_osid_object_form._my_map['targets'] = \
            self._targets_metadata['default_object_values'][0]

    @utilities.arguments_not_none
    def clear_target_texts(self, target_id):
        """stub"""
        if self.get_targets_metadata().is_read_only():
            raise NoAccess()
        updated_targets = []
        for current_target in self.my_osid_object_form._my_map['targets']:
            if current_target['id'] != target_id:
                updated_targets.append(current_target)
            else:
                updated_targets.append({
                    'id': current_target['id'],
                    'texts': [],
                    'names': current_target['names'],
                    'dropBehaviorType': current_target['dropBehaviorType']
                })
        self.my_osid_object_form._my_map['targets'] = updated_targets

    @utilities.arguments_not_none
    def clear_target_names(self, target_id):
        """stub"""
        if self.get_targets_metadata().is_read_only():
            raise NoAccess()
        updated_targets = []
        for current_target in self.my_osid_object_form._my_map['targets']:
            if current_target['id'] != target_id:
                updated_targets.append(current_target)
            else:
                updated_targets.append({
                    'id': current_target['id'],
                    'texts': current_target['texts'],
                    'names': [],
                    'dropBehaviorType': current_target['dropBehaviorType']
                })
        self.my_osid_object_form._my_map['targets'] = updated_targets

    @utilities.arguments_not_none
    def remove_target_text_language(self, language_type, target_id):
        if self.get_targets_metadata().is_read_only():
            raise NoAccess()

        targets = [t for t in self.my_osid_object_form._my_map['targets'] if t['id'] == target_id]
        if len(targets) == 0:
            raise InvalidArgument('invalid target_id')

        for current_target in self.my_osid_object_form._my_map['targets']:
            if target_id == current_target['id']:
                self.remove_field_by_language('texts',
                                              language_type,
                                              dictionary=current_target)

    @utilities.arguments_not_none
    def remove_target_name_language(self, language_type, target_id):
        if self.get_targets_metadata().is_read_only():
            raise NoAccess()

        targets = [t for t in self.my_osid_object_form._my_map['targets'] if t['id'] == target_id]
        if len(targets) == 0:
            raise InvalidArgument('invalid target_id')

        for current_target in self.my_osid_object_form._my_map['targets']:
            if target_id == current_target['id']:
                self.remove_field_by_language('names',
                                              language_type,
                                              dictionary=current_target)

    def update_target(self, target_id, target_text=None, name=None, drop_behavior_type=None):
        if self.get_targets_metadata().is_read_only():
            raise NoAccess()
        if target_text is not None and not isinstance(target_text, DisplayText):
            raise InvalidArgument('target_text must be a DisplayText object')
        if name is not None and not isinstance(name, DisplayText):
            raise InvalidArgument('name must be a DisplayText object')
        for current_target in self.my_osid_object_form._my_map['targets']:
            if target_id == current_target['id']:
                if target_text is not None:
                    self.add_or_replace_value(
                        'texts', target_text, dictionary=current_target)
                if drop_behavior_type is not None:
                    current_target['dropBehaviorType'] = drop_behavior_type
                if name is not None:
                    self.add_or_replace_value(
                        'names', name, dictionary=current_target)
                return
        raise NotFound('target_id not found in question')

    @utilities.arguments_not_none
    def remove_target(self, target_id):
        """remove a target, given the id"""
        updated_targets = []
        for target in self.my_osid_object_form._my_map['targets']:
            if target['id'] != target_id:
                updated_targets.append(target)
        self.my_osid_object_form._my_map['targets'] = updated_targets

    @utilities.arguments_not_none
    def set_target_order(self, target_ids):
        """ reorder targets per the passed in list
        :param target_ids:
        :return:
        """
        reordered_targets = []
        current_target_ids = [t['id'] for t in self.my_osid_object_form._my_map['targets']]
        if set(target_ids) != set(current_target_ids):
            raise IllegalState('target_ids do not match existing targets')

        for target_id in target_ids:
            for current_target in self.my_osid_object_form._my_map['targets']:
                if target_id == current_target['id']:
                    reordered_targets.append(current_target)
                    break

        self.my_osid_object_form._my_map['targets'] = reordered_targets

    def get_zones_metadata(self):
        """stub"""
        return Metadata(**self._zones_metadata)

    def add_zone(self, spatial_unit, container_id, name='', description='', visible=True, reuse=0, drop_behavior_type=None):
        """container_id is a targetId that the zone belongs to
        """
        if not isinstance(spatial_unit, abc_mapping_primitives.SpatialUnit):
            raise InvalidArgument('zone is not a SpatialUnit')
        # if not isinstance(name, DisplayText):
        #     raise InvalidArgument('name is not a DisplayText object')
        if not isinstance(reuse, int):
            raise InvalidArgument('reuse must be an integer')
        if reuse < 0:
            raise InvalidArgument('reuse must be >= 0')
        if not isinstance(name, DisplayText):
            # if default ''
            name = self._str_display_text(name)
        if not isinstance(description, DisplayText):
            # if default ''
            description = self._str_display_text(description)
        zone = {
            'id': str(ObjectId()),
            'spatialUnit': spatial_unit.get_spatial_unit_map(),
            'containerId': container_id,
            'names': [self._dict_display_text(name)],
            'descriptions': [self._dict_display_text(description)],
            'visible': visible,
            'reuse': reuse,
            'dropBehaviorType': str(drop_behavior_type)
        }
        self.my_osid_object_form._my_map['zones'].append(zone)
        return zone

    def clear_zones(self):
        """stub"""
        if self.get_zones_metadata().is_read_only():
            raise NoAccess()
        self.my_osid_object_form._my_map['zones'] = \
            self._zones_metadata['default_object_values'][0]

    def clear_zone_names(self, zone_id):
        if self.get_zones_metadata().is_read_only():
            raise NoAccess()
        updated_zones = []
        for current_zone in self.my_osid_object_form._my_map['zones']:
            if current_zone['id'] != zone_id:
                updated_zones.append(current_zone)
            else:
                updated_zones.append({
                    'id': current_zone['id'],
                    'names': [],
                    'descriptions': current_zone['descriptions'],
                    'spatialUnit': current_zone['spatialUnit'],
                    'containerId': current_zone['containerId'],
                    'visible': current_zone['visible'],
                    'reuse': current_zone['reuse'],
                    'dropBehaviorType': current_zone['dropBehaviorType']
                })
        self.my_osid_object_form._my_map['zones'] = updated_zones

    def clear_zone_descriptions(self, zone_id):
        if self.get_zones_metadata().is_read_only():
            raise NoAccess()
        updated_zones = []
        for current_zone in self.my_osid_object_form._my_map['zones']:
            if current_zone['id'] != zone_id:
                updated_zones.append(current_zone)
            else:
                updated_zones.append({
                    'id': current_zone['id'],
                    'names': current_zone['names'],
                    'descriptions': [],
                    'spatialUnit': current_zone['spatialUnit'],
                    'containerId': current_zone['containerId'],
                    'visible': current_zone['visible'],
                    'reuse': current_zone['reuse'],
                    'dropBehaviorType': current_zone['dropBehaviorType']
                })
        self.my_osid_object_form._my_map['zones'] = updated_zones

    @utilities.arguments_not_none
    def remove_zone_name_language(self, language_type, zone_id):
        if self.get_zones_metadata().is_read_only():
            raise NoAccess()

        zones = [z for z in self.my_osid_object_form._my_map['zones'] if z['id'] == zone_id]
        if len(zones) == 0:
            raise InvalidArgument('invalid zone_id')

        for current_zone in self.my_osid_object_form._my_map['zones']:
            if zone_id == current_zone['id']:
                self.remove_field_by_language('names',
                                              language_type,
                                              dictionary=current_zone)

    @utilities.arguments_not_none
    def remove_zone_description_language(self, language_type, zone_id):
        if self.get_zones_metadata().is_read_only():
            raise NoAccess()

        zones = [z for z in self.my_osid_object_form._my_map['zones'] if z['id'] == zone_id]
        if len(zones) == 0:
            raise InvalidArgument('invalid zone_id')

        for current_zone in self.my_osid_object_form._my_map['zones']:
            if zone_id == current_zone['id']:
                self.remove_field_by_language('descriptions',
                                              language_type,
                                              dictionary=current_zone)

    def update_zone(self, zone_id, spatial_unit=None, container_id=None, name=None, description=None, visible=None, reuse=None, drop_behavior_type=None):
        if self.get_zones_metadata().is_read_only():
            raise NoAccess()
        if spatial_unit is not None and not isinstance(spatial_unit, abc_mapping_primitives.SpatialUnit):
            raise InvalidArgument('spatial_unit must be a SpatialUnit')
        if name is not None and not isinstance(name, DisplayText):
            raise InvalidArgument('name must be a DisplayText object')
        if description is not None and not isinstance(description, DisplayText):
            raise InvalidArgument('description must be a DisplayText object')
        if reuse is not None and not isinstance(reuse, int):
            raise InvalidArgument('reuse must be an integer')
        if reuse is not None and reuse < 0:
            raise InvalidArgument('reuse must be >= 0')
        for current_zone in self.my_osid_object_form._my_map['zones']:
            if zone_id == current_zone['id']:
                if spatial_unit is not None:
                    current_zone['spatialUnit'] = spatial_unit.get_spatial_unit_map()
                if name is not None:
                    self.add_or_replace_value(
                        'names', name, dictionary=current_zone)
                if description is not None:
                    self.add_or_replace_value(
                        'descriptions', description, dictionary=current_zone)
                if container_id is not None:
                    current_zone['containerId'] = container_id
                if visible is not None:
                    current_zone['visible'] = visible
                if reuse is not None:
                    current_zone['reuse'] = reuse
                if drop_behavior_type is not None:
                    current_zone['dropBehaviorType'] = drop_behavior_type
                return
        raise NotFound('zone_id not found in question')

    @utilities.arguments_not_none
    def remove_zone(self, zone_id):
        """remove a zone, given the id"""
        updated_zones = []
        for zone in self.my_osid_object_form._my_map['zones']:
            if zone['id'] != zone_id:
                updated_zones.append(zone)
        self.my_osid_object_form._my_map['zones'] = updated_zones

    @utilities.arguments_not_none
    def set_zone_order(self, zone_ids):
        """ reorder zones per the passed in list
        :param zone_ids:
        :return:
        """
        reordered_zones = []
        current_zone_ids = [z['id'] for z in self.my_osid_object_form._my_map['zones']]
        if set(zone_ids) != set(current_zone_ids):
            raise IllegalState('zone_ids do not match existing zones')

        for zone_id in zone_ids:
            for current_zone in self.my_osid_object_form._my_map['zones']:
                if zone_id == current_zone['id']:
                    reordered_zones.append(current_zone)
                    break

        self.my_osid_object_form._my_map['zones'] = reordered_zones
