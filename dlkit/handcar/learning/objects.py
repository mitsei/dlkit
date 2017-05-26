# -*- coding: utf-8 -*-

# This module contains all the Object classes used by the MIT Core Concept
# Catalog (MC3) Handcar based implementation of the OSID Learning Service.

import json
import pdb
from ...abstract_osid.learning import objects as abc_learning_objects
from ..osid import objects as osid_objects
from ..osid import markers
from ..osid.metadata import Metadata
from .. import settings
from ..primitives import Id, Type, DisplayText
from ..id.objects import IdList
from ..osid.osid_errors import NullArgument, InvalidArgument, NotFound, NoAccess, IllegalState, OperationFailed, Unimplemented, Unsupported, PermissionDenied

INVALID = 0
VALID = 1


class Objective(abc_learning_objects.Objective, osid_objects.OsidObject, markers.Federateable):
    """An Objective is a statable learning objective."""
    _namespace = 'learning.Objective'

    def _get_extension_map(self):
        if self._my_extension_map is None:
            url_path = ('/handcar/services/learning/objectivebanks/' +
                        self._my_map['objectiveBankId'] + '/objectives/' +
                        self._my_map['id'] + '/extension')
            self._my_extension_map = self._get_request(url_path)

    def _get_grade_map(self, grade_identifier):
        url_str = (self._base_url + '/objectivebanks/' +
                   self._my_map['objectiveBankId'] + '/grades/' + grade_identifier)
        return self._load_json(url_str)

    def has_assessment(self):
        """Tests if an assessment is associated with this objective.

        return: (boolean) - true if an assessment exists, false
                otherwise
        compliance: mandatory - This method must be implemented.

        """
        return 'assessmentId' in self._my_map and bool(self._my_map['assessmentId'])

    def get_assessment_id(self):
        """Gets the assessment Id associated with this learning objective.

        return: (osid.id.Id) - the assessment Id
        raise:  IllegalState - has_assessment() is false
        compliance: mandatory - This method must be implemented.

        """
        if not self.has_assessment():
            raise IllegalState()
        else:
            return Id(self._my_map['assessmentId'])

    def get_assessment(self):
        """Gets the assessment associated with this learning objective.

        return: (osid.assessment.Assessment) - the assessment
        raise:  IllegalState - has_assessment() is false
        raise:  OperationFailed - unable to complete request
        compliance: mandatory - This method must be implemented.

        """
        if not self.has_assessment:
            raise IllegalState()
        else:
            raise Unimplemented()

    def has_knowledge_category(self):
        """Tests if this objective has a knowledge dimension.

        return: (boolean) - true if a knowledge category exists, false
                otherwise
        compliance: mandatory - This method must be implemented.

        """
        return 'knowledgeCategoryId' in self._my_map and bool(self._my_map['knowledgeCategoryId'])

    def get_knowledge_category_id(self):
        """Gets the grade Id associated with the knowledge dimension.

        return: (osid.id.Id) - the grade Id
        raise:  IllegalState - has_knowledge_category() is false
        compliance: mandatory - This method must be implemented.

        """
        if not self.has_knowledge_category():
            raise IllegalState()
        else:
            return Id(self._my_map['knowledgeCategoryId'])

    def get_knowledge_category(self):
        """Gets the grade associated with the knowledge dimension.

        return: (osid.grading.Grade) - the grade
        raise:  IllegalState - has_knowledge_category() is false
        raise:  OperationFailed - unable to complete request
        compliance: mandatory - This method must be implemented.

        """
        if not self.has_knowledge_category():
            raise IllegalState()
        else:
            return Grade(self._get_grade_map(self._my_map['knowledgeCategoryId'])),

    def has_cognitive_process(self):
        """Tests if this objective has a cognitive process type.

        return: (boolean) - true if a cognitive process exists, false
                otherwise
        compliance: mandatory - This method must be implemented.

        """
        return 'cognitiveProcessId' in self._my_map and bool(self._my_map['cognitiveProcessId'])

    def get_cognitive_process_id(self):
        """Gets the grade Id associated with the cognitive process.

        return: (osid.id.Id) - the grade Id
        raise:  IllegalState - has_cognitive_process() is false
        compliance: mandatory - This method must be implemented.

        """
        if not self.has_cognitive_process():
            raise IllegalState()
        else:
            return Id(self._my_map['cognitiveProcessId'])

    def get_cognitive_process(self):
        """Gets the grade associated with the cognitive process.

        return: (osid.grading.Grade) - the grade
        raise:  IllegalState - has_cognitive_process() is false
        raise:  OperationFailed - unable to complete request
        compliance: mandatory - This method must be implemented.

        """
        if not self.has_cognitive_process():
            raise IllegalState()
        else:
            return Grade(self._get_grade_map(self._my_map['cognitiveProcessId'])),

    def get_objective_record(self, objective_record_type=None):
        """Gets the objective bank record corresponding to the given
        Objective record Type.
        This method is used to retrieve an object implementing the
        requested record. The objectiveRecordType may be the Type
        returned in get_record_types() or any of its parents in a Type
        hierarchy where hasRecordType(objectiveRecordType) is true .
        arg:    objectiveRecordType (osid.type.Type): an objective
                record type
        return: (osid.learning.records.ObjectiveRecord) - the objective
                record
        raise:  NullArgument - objectiveRecordType is null
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported - hasRecordType(objectiveRecordType) is
                false
        compliance: mandatory - This method must be implemented.

        """
        if not self.has_record_type():
            raise Unsupported()
        else:  # This should never get called:
            raise Unimplemented()

    assessment_id = property(get_assessment_id)
    assessment = property(get_assessment)
    knowledge_category_id = property(get_knowledge_category_id)
    knowledge_category = property(get_knowledge_category)
    cognitive_process_id = property(get_cognitive_process_id)
    cognitive_process = property(get_cognitive_process)


class ObjectiveForm(abc_learning_objects.ObjectiveForm, osid_objects.OsidObjectForm, osid_objects.OsidFederateableForm):
    """This is the form for creating and updating Objectives.

    Like all OsidForm objects, various data elements may be set here for
    use in the create and update methods in the ObjectiveAdminSession.
    For each data element that may be set, metadata may be examined to
    provide display hints or data constraints.

    """
    _namespace = 'learning.Objective'

    def _init_map(self):
        osid_objects.OsidObjectForm._init_map(self)
        self._my_map['assessmentId'] = ''
        self._my_map['cognitiveProcessId'] = ''
        self._my_map['knowledgeCategoryId'] = ''

    def _init_validity_map(self):
        osid_objects.OsidObjectForm._init_validity_map(self)
        self._validity_map['assessment_id'] = VALID
        self._validity_map['cognitive_process_id'] = VALID
        self._validity_map['knowledge_category_id'] = VALID

    def get_assessment_metadata(self):
        """Gets the metadata for an assessment.

        return: (osid.Metadata) - metadata for the assessment
        compliance: mandatory - This method must be implemented.

        """
        return Metadata(**settings.METADATA['assessment_id'])

    def set_assessment(self, assessment_id=None):
        """Sets the assessment.

        arg:    assessmentId (osid.id.Id): the new assessment
        raise:  INVALID_ARGUMENT - assessmentId is invalid
        raise:  NoAccess - assessmentId cannot be modified
        raise:  NullArgument - assessmentId is null
        compliance: mandatory - This method must be implemented.

        """
        if assessment_id is None:
            raise NullArgument()
        metadata = Metadata(**settings.METADATA['assessment_id'])
        if metadata.is_read_only():
            raise NoAccess()
        if self._is_valid_input(assessment_id, metadata, array=False):
            self._my_map['assessmentId'] = str(assessment_id)
        else:
            raise InvalidArgument

    def clear_assessment(self):
        """Clears the assessment.

        raise:  NoAccess - metadata.is_required() or
                metadata.is_read_only() is true
        compliance: mandatory - This method must be implemented.

        """
        metadata = Metadata(**settings.METADATA['assessment_id'])
        if metadata.is_read_only() or metadata.is_required():
            raise NoAccess()
        self._my_map['assessmentId'] = ''

    def get_knowledge_category_metadata(self):
        """Gets the metadata for a knowledge category.

        return: (osid.Metadata) - metadata for the knowledge category
        compliance: mandatory - This method must be implemented.

        """
        return Metadata(**settings.METADATA['knowledge_category_id'])

    def set_knowledge_category(self, grade_id=None):
        """Sets the knowledge category.

        arg:    gradeId (osid.id.Id): the new knowledge category
        raise:  INVALID_ARGUMENT - gradeId is invalid
        raise:  NoAccess - gradeId cannot be modified
        raise:  NullArgument - gradeId is null
        compliance: mandatory - This method must be implemented.

        """
        if grade_id is None:
            raise NullArgument()
        metadata = Metadata(**settings.METADATA['knowledge_category_id'])
        if metadata.is_read_only():
            raise NoAccess()
        if self._is_valid_input(grade_id, metadata, array=False):
            self._my_map['knowledgeCategoryId'] = str(grade_id)
        else:
            raise InvalidArgument

    def clear_knowledge_category(self):
        """Clears the knowledge category.

        raise:  NoAccess - metadata.is_required() or
                metadata.is_read_only() is true
        compliance: mandatory - This method must be implemented.

        """
        metadata = Metadata(**settings.METADATA['knowledge_category_id'])
        if metadata.is_read_only() or metadata.is_required():
            raise NoAccess()
        self._my_map['knowledgeCategoryId'] = ''

    def get_cognitive_process_metadata(self):
        """Gets the metadata for a cognitive process.

        return: (osid.Metadata) - metadata for the cognitive process
        compliance: mandatory - This method must be implemented.

        """
        return Metadata(**settings.METADATA['cognitive_process_id'])

    def set_cognitive_process(self, grade_id=None):
        """Sets the cognitive process.

        arg:    gradeId (osid.id.Id): the new cognitive process
        raise:  INVALID_ARGUMENT - gradeId is invalid
        raise:  NoAccess - gradeId cannot be modified
        raise:  NullArgument - gradeId is null
        compliance: mandatory - This method must be implemented.

        """
        if grade_id is None:
            raise NullArgument()
        metadata = Metadata(**settings.METADATA['cognitive_process_id'])
        if metadata.is_read_only():
            raise NoAccess()
        if self._is_valid_input(grade_id, metadata, array=False):
            self._my_map['cognitiveProcessId'] = str(grade_id)
        else:
            raise InvalidArgument

    def clear_cognitive_process(self):
        """Clears the cognitive process.

        raise:  NoAccess - metadata.is_required() or
                metadata.is_read_only() is true
        compliance: mandatory - This method must be implemented.

        """
        metadata = Metadata(**settings.METADATA['cognitive_process_id'])
        if metadata.is_read_only() or metadata.is_required():
            raise NoAccess()
        self._my_map['cognitiveProcessId'] = ''

    def get_objective_form_record(self, objective_record_type=None):
        """Gets the ObjectiveFormRecord corresponding to the given
        objective record Type.

        arg:    objectiveRecordType (osid.type.Type): the objective
                record type
        return: (osid.learning.records.ObjectiveFormRecord) - the
                objective form record
        raise:  NullArgument - objectiveRecordType is null
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported - hasRecordType(objectiveRecordType) is
                false
        compliance: mandatory - This method must be implemented.

        """
        if not self.has_record_type():
            raise Unsupported()
        else:  # This should never get called:
            raise Unimplemented()

    assessment_metadata = property(get_assessment_metadata)
    knowledge_category_metadata = property(get_knowledge_category_metadata)
    cognitive_process_metadata = property(get_cognitive_process_metadata)
    assessment = property(fset=set_assessment, fdel=clear_assessment)
    knowledge_category = property(fset=set_knowledge_category, fdel=clear_knowledge_category)
    cognitive_process = property(fset=set_cognitive_process, fdel=clear_cognitive_process)


class ObjectiveList(abc_learning_objects.ObjectiveList, osid_objects.OsidList):
    """Like all OsidLists,  ObjectiveList provides a means for accessing
    Objective elements sequentially either one at a time or many at a
    time.

    Examples: while (ol.hasNext()) { Objective objective =
    ol.getNextObjective(); }

    or
      while (ol.hasNext()) {
           Objective[] objectives = ol.getNextObjectives(ol.available());
      }

    """

    def get_next_objective(self):
        """Gets the next Objective in this list.

        return: (osid.learning.Objective) - the next Objective in this
                list. The has_next() method should be used to test that
                a next Objective is available before calling this
                method.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        compliance: mandatory - This method must be implemented.

        """
        try:
            next_object = next(self)
        except StopIteration:
            raise IllegalState('no more elements available in this list')
        except Exception:  # Need to specify exceptions here!
            raise OperationFailed()
        else:
            return next_object

    def next(self):
        try:
            next_object = osid_objects.OsidList.next(self)
        except StopIteration:
            raise
        except Exception:  # Need to specify exceptions here!
            raise OperationFailed
        if isinstance(next_object, dict):
            next_object = Objective(next_object)
        return next_object

    __next__ = next

    def get_next_objectives(self, n=None):
        """Gets the next set of Objective elements in this list which must
        be less than or equal to the number returned from available().

        arg:    n (cardinal): the number of Objective elements requested
                which should be less than or equal to available()
        return: (osid.learning.Objective) - an array of Objective
                elements.  The length of the array is less than or equal
                to the number specified.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        compliance: mandatory - This method must be implemented.

        """
        if n > self.available():
            # !!! This is not quite as specified (see method docs) !!!
            raise IllegalState('not enough elements available in this list')
        else:
            next_list = []
            x = 0
            while x < n:
                try:
                    next_list.append(next(self))
                except Exception:  # Need to specify exceptions here!
                    raise  # OperationFailed()
                x = x + 1
            return next_list

    next_objective = property(get_next_objective)


class Activity(abc_learning_objects.Activity, osid_objects.OsidObject):
    """An Activity represents learning material or other learning
    activities to meet an objective.

    An Activity has may relate to a set of Asssts for self learning,
    recommended Courses to take, or a learning Assessment. The learning
    Assessment differs from the Objective Assessment in that the latter
    used to test for proficiency in the Objective.

    Generally, an Activity should focus on one of assets, courses,
    assessments, or some other specific activity related to the
    objective described or related in the ActivityRecord.

    """
    _namespace = 'learning.Activity'

    def _get_extension_map(self):
        if self._my_extension_map is None:
            url_path = ('/handcar/services/learning/objectivebanks/' +
                        self._my_map['objectiveBankId'] + '/activities/' +
                        self._my_map['id'] + '/extension')
            self._my_extension_map = self._get_request(url_path)

    def get_objective_id(self):
        """Gets the Id of the related objective.

        return: (osid.id.Id) - the objective Id
        compliance: mandatory - This method must be implemented.

        """
        return Id(self._my_map['objectiveId'])

    def get_objective(self):
        """Gets the related objective.

        return: (osid.learning.Objective) - the related objective
        raise:  OperationFailed - unable to complete request
        compliance: mandatory - This method must be implemented.

        """
        # Note that this makes the generic objectives call to Handcar
        # without specifying the objectiveBank:
        url_str = (self._base_url + '/objectives/' +
                   self._my_map['objectiveId'])
        return Objective(self._load_json(url_str))

    def is_asset_based_activity(self):
        """Tests if this is an asset based activity.

        return: (boolean) - true if this activity is based on assets,
                false otherwise
        compliance: mandatory - This method must be implemented.

        """
        return bool(self._my_map['assetIds'])

    def get_asset_ids(self):
        """Gets the Ids of any assets associated with this activity.

        return: (osid.id.IdList) - list of asset Ids
        raise:  IllegalState - is_asset_based_activity() is false
        compliance: mandatory - This method must be implemented.

        """
        if not self.is_asset_based_activity():
            raise IllegalState()
        else:
            ids = []
            for i in self._my_map['assetIds']:
                ids.append(Id(i))
            return IdList(ids)

    def get_assets(self):
        """Gets any assets associated with this activity.

        return: (osid.repository.AssetList) - list of assets
        raise:  IllegalState - is_asset_based_activity() is false
        raise:  OperationFailed - unable to complete request
        compliance: mandatory - This method must be implemented.

        """
        # This includes a kludge to get the objectiveBankId directly from
        # this Activity's Objective's private _my_map :o
        from ..repository.objects import AssetList
        if not self.is_asset_based_activity():
            raise IllegalState()
        url_str = (self._base_url + '/objectivebanks/' +
                   self.get_objective()._my_map['objectiveBankId'] +
                   '/assets/bulk?id=' + '&id='.join(self._my_map['assetIds']))
        return AssetList(self._load_json(url_str))

    def is_course_based_activity(self):
        """Tests if this is a course based activity.

        return: (boolean) - true if this activity is based on courses,
                false otherwise
        compliance: mandatory - This method must be implemented.

        """
        return False

    def get_course_ids(self):
        """Gets the Ids of any courses associated with this activity.

        return: (osid.id.IdList) - list of course Ids
        raise:  IllegalState - is_course_based_activity() is false
        compliance: mandatory - This method must be implemented.

        """
        if not self.is_course_based_activity():
            raise IllegalState()
        else:
            raise Unimplemented()

    def get_courses(self):
        """Gets any courses associated with this activity.

        return: (osid.course.CourseList) - list of courses
        raise:  IllegalState - is_course_based_activity() is false
        raise:  OperationFailed - unable to complete request
        compliance: mandatory - This method must be implemented.

        """
        if not self.is_course_based_activity():
            raise IllegalState()
        else:
            raise Unimplemented()

    def is_assessment_based_activity(self):
        """Tests if this is an assessment based activity.
        These assessments are for learning the objective and not for
        assessing proficiency in the objective.
        return: (boolean) - true if this activity is based on
                assessments, false otherwise
        compliance: mandatory - This method must be implemented.

        """
        return 'assessmentIds' in self._my_map and bool(self._my_map['assessmentIds'])

    def get_assessment_ids(self):
        """Gets the Ids of any assessments associated with this activity.

        return: (osid.id.IdList) - list of assessment Ids
        raise:  IllegalState - is_assessment_based_activity() is false
        compliance: mandatory - This method must be implemented.

        """
        if not self.is_assessment_based_activity():
            raise IllegalState()
        else:
            return [Id(a) for a in self._my_map['assessmentIds']]

    def get_assessments(self):
        """Gets any assessments associated with this activity.

        return: (osid.assessment.AssessmentList) - list of assessments
        raise:  IllegalState - is_assessment_based_activity() is false
        raise:  OperationFailed - unable to complete request
        compliance: mandatory - This method must be implemented.

        """
        if not self.is_assessment_based_activity():
            raise IllegalState()
        else:
            raise Unimplemented()

    def get_activity_record(self, activity_record_type=None):
        """Gets the activity record corresponding to the given Activity
        record Type.
        This method is used to retrieve an object implementing the
        requested record. The activityRecordType may be the Type
        returned in get_record_types() or any of its parents in a Type
        hierarchy where hasRecordType(activityRecordType) is true .
        arg:    activityRecordType (osid.type.Type): the type of the
                record to retrieve
        return: (osid.learning.records.ActivityRecord) - the activity
                record
        raise:  NullArgument - activityRecordType is null
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported - hasRecordType(activityRecordType) is false
        compliance: mandatory - This method must be implemented.

        """
        if not self.has_record_type():
            raise IllegalState()
        else:  # This should never get called:
            raise Unimplemented()

    objective_id = property(get_objective_id)
    objective = property(get_objective)
    asset_ids = property(get_asset_ids)
    assets = property(get_assets)
    course_ids = property(get_course_ids)
    courses = property(get_courses)
    assessment_ids = property(get_assessment_ids)
    assessments = property(get_assessments)


class ActivityForm(abc_learning_objects.ActivityForm, osid_objects.OsidObjectForm):
    # need to add osid_objects.OsidSubjugateableForm  ^^
    """This is the form for creating and updating Activities.

    Like all OsidForm objects, various data elements may be set here for
    use in the create and update methods in the ActivityAdminSession.
    For each data element that may be set, metadata may be examined to
    provide display hints or data constraints.

    """
    _namespace = 'learning.Activity'

    def _init_map(self):
        osid_objects.OsidObjectForm._init_map(self)
        self._my_map['objectiveId'] = str(self.kwargs['objective_id'])
        self._my_map['assessmentIds'] = []
        self._my_map['assetIds'] = []
        self._my_map['courseIds'] = []

    def _init_validity_map(self):
        osid_objects.OsidObjectForm._init_validity_map(self)
        self._validity_map['assessmentIds'] = VALID
        self._validity_map['assetIds'] = VALID
        self._validity_map['courseIds'] = VALID

    def get_assets_metadata(self):
        """Gets the metadata for the assets.

        return: (osid.Metadata) - metadata for the assets
        compliance: mandatory - This method must be implemented.

        """
        return Metadata(**settings.METADATA['asset_ids'])

    def set_assets(self, asset_ids=None):
        """Sets the assets.

        arg:    assetIds (osid.id.Id): the asset Ids
        raise:  INVALID_ARGUMENT - assetIds is invalid
        raise:  NullArgument - assetIds is null
        raise:  NoAccess - metadata.is_read_only() is true
        compliance: mandatory - This method must be implemented.

        """
        if asset_ids is None:
            raise NullArgument()
        metadata = Metadata(**settings.METADATA['asset_ids'])
        if metadata.is_read_only():
            raise NoAccess()
        if self._is_valid_input(asset_ids, metadata, array=True):
            for asset_id in asset_ids:
                self._my_map['assetIds'].append(str(asset_id))
        else:
            raise InvalidArgument

    def clear_assets(self):
        """Clears the assets.

        raise:  NoAccess - metadata.is_required() or
                metadata.is_read_only() is true
        compliance: mandatory - This method must be implemented.

        """
        metadata = Metadata(**settings.METADATA['asset_ids'])
        if metadata.is_read_only() or metadata.is_required():
            raise NoAccess()
        self._my_map['assetIds'] = []

    def get_courses_metadata(self):
        """Gets the metadata for the courses.

        return: (osid.Metadata) - metadata for the courses
        compliance: mandatory - This method must be implemented.

        """
        return Metadata(**settings.METADATA['course_ids'])

    def set_courses(self, course_ids=None):
        """Sets the courses.

        arg:    courseIds (osid.id.Id): the course Ids
        raise:  INVALID_ARGUMENT - courseIds is invalid
        raise:  NullArgument - courseIds is null
        raise:  NoAccess - metadata.is_read_only() is true
        compliance: mandatory - This method must be implemented.

        """
        if course_ids is None:
            raise NullArgument()
        metadata = Metadata(**settings.METADATA['course_ids'])
        if metadata.is_read_only():
            raise NoAccess()
        if self._is_valid_input(course_ids, metadata, array=True):
            for course_id in course_ids:
                self._my_map['courseIds'].append(str(course_id))
        else:
            raise InvalidArgument

    def clear_courses(self):
        """Clears the courses.

        raise:  NoAccess - metadata.is_required() or
                metadata.is_read_only() is true
        compliance: mandatory - This method must be implemented.

        """
        metadata = Metadata(**settings.METADATA['course_ids'])
        if metadata.is_read_only() or metadata.is_required():
            raise NoAccess()
        self._my_map['courseIds'] = []

    def get_assessments_metadata(self):
        """Gets the metadata for the assessments.

        return: (osid.Metadata) - metadata for the assessments
        compliance: mandatory - This method must be implemented.

        """
        return Metadata(**settings.METADATA['assessment_ids'])

    def set_assessments(self, assessment_ids=None):
        """Sets the assessments.

        arg:    assessmentIds (osid.id.Id): the assessment Ids
        raise:  INVALID_ARGUMENT - assessmentIds is invalid
        raise:  NullArgument - assessmentIds is null
        raise:  NoAccess - metadata.is_read_only() is true
        compliance: mandatory - This method must be implemented.

        """
        if assessment_ids is None:
            raise NullArgument()
        metadata = Metadata(**settings.METADATA['assessment_ids'])
        if metadata.is_read_only():
            raise NoAccess()
        if self._is_valid_input(assessment_ids, metadata, array=True):
            for assessment_id in assessment_ids:
                self._my_map['assessmentIds'].append(str(assessment_id))
        else:
            raise InvalidArgument

    def clear_assessments(self):
        """Clears the assessments.

        raise:  NoAccess - metadata.is_required() or
                metadata.is_read_only() is true
        compliance: mandatory - This method must be implemented.

        """
        metadata = Metadata(**settings.METADATA['assessment_ids'])
        if metadata.is_read_only() or metadata.is_required():
            raise NoAccess()
        self._my_map['assessmentIds'] = []

    def get_activity_form_record(self, activity_record_type=None):
        """Gets the ActivityFormRecord corresponding to the given activity
        record Type.

        arg:    activityRecordType (osid.type.Type): the activity record
                type
        return: (osid.learning.records.ActivityFormRecord) - the
                activity form record
        raise:  NullArgument - activityRecordType is null
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported - hasRecordType(activityRecordType) is false
        compliance: mandatory - This method must be implemented.

        """
        if not self.has_record_type():
            raise Unsupported()
        else:  # This should never get called:
            raise Unimplemented()

    assets_metadata = property(get_assets_metadata)
    courses_metadata = property(get_courses_metadata)
    assessments_metadata = property(get_assessments_metadata)
    assets = property(fset=set_assets, fdel=clear_assets)
    courses = property(fset=set_courses, fdel=clear_courses)
    assessments = property(fset=set_assessments, fdel=clear_assessments)


class ActivityList(abc_learning_objects.ActivityList, osid_objects.OsidList):
    """Like all OsidLists,  ActivityList provides a means for accessing
    Activity elements sequentially either one at a time or many at a
    time.

    Examples: while (al.hasNext()) { Activity activity =
    al.getNextActivity(); }

    or
      while (al.hasNext()) {
           Activity[] activities = al.getNextActivities(al.available());
      }
    """

    def get_next_activity(self):
        """Gets the next Activity in this list.

        return: (osid.learning.Activity) - the next Activity in this
                list. The has_next() method should be used to test that
                a next Activity is available before calling this method.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        compliance: mandatory - This method must be implemented.

        """
        try:
            next_object = next(self)
        except StopIteration:
            raise IllegalState('no more elements available in this list')
        except Exception:  # Need to specify exceptions here!
            raise OperationFailed()
        else:
            return next_object

    def next(self):
        try:
            next_object = osid_objects.OsidList.next(self)
        except StopIteration:
            raise
        except Exception:  # Need to specify exceptions here!
            raise OperationFailed()
        if isinstance(next_object, dict):
            next_object = Activity(next_object)
        return next_object

    __next__ = next

    def get_next_activities(self, n=None):
        """Gets the next set of Activity elements in this list which must
        be less than or equal to the number returned from available().

        arg:    n (cardinal): the number of Activity elements requested
                which should be less than or equal to available()
        return: (osid.learning.Activity) - an array of Activity
                elements.  The length of the array is less than or equal
                to the number specified.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        compliance: mandatory - This method must be implemented.

        """

        if n > self.available():
            # !!! This is not quite as specified (see method docs) !!!
            raise IllegalState('not enough elements available in this list')
        else:
            next_list = []
            x = 0
            while x < n:
                try:
                    next_list.append(next(self))
                except Exception:  # Need to specify exceptions here!
                    raise OperationFailed()
                x = x + 1
            return next_list

    next_activity = property(get_next_activity)


class ObjectiveBank(abc_learning_objects.ObjectiveBank, osid_objects.OsidCatalog):
    """an objective bank defines a collection of objectives."""

    _namespace = 'learning.ObjectiveBank'

    def get_objective_bank_record(self, objective_bank_record_type=None):
        """Gets the objective bank record corresponding to the given
        ObjectiveBank record Type.
        This method is used to retrieve an object implementing the
        requested record. The objectiveBankRecordType may be the Type
        returned in get_record_types() or any of its parents in a Type
        hierarchy where hasRecordType(objectiveBankRecordType) is true .
        arg:    objectiveBankRecordType (osid.type.Type): an objective
                bank record type
        return: (osid.learning.records.ObjectiveBankRecord) - the
                objective bank record
        raise:  NullArgument - objectiveBankRecordType is null
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported - hasRecordType(objectiveBankRecordType) is
                false
        compliance: mandatory - This method must be implemented.

        """
        if not self.has_record_type():
            raise IllegalState()
        else:  # This should never get called.
            raise Unimplemented()

    def get_cognitive_process_grade_system(self):
        from ..grading.objects import GradeSystem
        url_path = ('/handcar/services/learning/objectivebanks/' +
                    self._my_map['id'] + '/gradesystems/cognitiveprocess')
        return GradeSystem(self._get_request(url_path))

    cognitive_process_grade_system = property(get_cognitive_process_grade_system)


class ObjectiveBankForm(abc_learning_objects.ObjectiveBankForm, osid_objects.OsidCatalogForm):
    """This is the form for creating and updating objective banks.

    Like all OsidForm objects, various data elements may be set here for
    use in the create and update methods in the
    ObjectiveBankAdminSession. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.

    """
    _namespace = 'learning.ObjectiveBank'

    def _init_map(self):
        osid_objects.OsidObjectForm._init_map(self)

    def _init_validity_map(self):
        osid_objects.OsidObjectForm._init_validity_map(self)

    def get_objective_bank_form_record(self, objective_bank_record_type=None):
        """Gets the ObjectiveBankFormRecord corresponding to the given
        objective bank record Type.

        arg:    objective_bank_record_type (osid.type.Type): an objective
                bank record type
        return: (osid.learning.records.ObjectiveBankFormRecord) - the
                objective bank form record
        raise:  NullArgument - objective_bank_record_type is null
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported - has_record_type(objective_bank_record_type) is
                false
        compliance: mandatory - This method must be implemented.

        """
        if not self.has_record_type():
            raise Unsupported()
        else:  # This should never get called:
            raise Unimplemented()


class ObjectiveBankList(abc_learning_objects.ObjectiveBankList, osid_objects.OsidList):
    """Like all OsidLists,  ObjectiveBankList provides a means for
    accessing ObjectiveBank elements sequentially either one at a time
    or many at a time.

    Examples: while (obl.hasNext()) { ObjectiveBank objectiveBanks =
    obl.getNextObjectiveBank(); }

    or
      while (obl.hasNext()) {
           ObjectiveBank[] objectivBanks = obl.getNextObjectiveBanks(obl.available());
      }
    """

    def get_next_objective_bank(self):
        """Gets the next ObjectiveBank in this list.

        return: (osid.learning.ObjectiveBank) - the next ObjectiveBank
                in this list. The has_next() method should be used to
                test that a next ObjectiveBank is available before
                calling this method.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        compliance: mandatory - This method must be implemented.

        """
        try:
            next_object = next(self)
        except StopIteration:
            raise IllegalState('no more elements available in this list')
        except Exception:  # Need to specify exceptions here!
            raise OperationFailed()
        else:
            return next_object

    def next(self):
        try:
            next_object = osid_objects.OsidList.next(self)
        except StopIteration:
            raise
        except Exception:  # Need to specify exceptions here!
            raise OperationFailed()
        if isinstance(next_object, dict):
            next_object = ObjectiveBank(next_object)
        return next_object

    __next__ = next

    def get_next_objective_banks(self, n=None):
        """Gets the next set of ObjectiveBank elements in this list which
        must be less than or equal to the return from available().

        arg:    n (cardinal): the number of ObjectiveBank elements
                requested which must be less than or equal to
                available()
        return: (osid.learning.ObjectiveBank) - an array of
                ObjectiveBank elements.  The length of the array is less
                than or equal to the number specified.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        compliance: mandatory - This method must be implemented.

        """
        if n > self.available():
            # !!! This is not quite as specified (see method docs) !!!
            raise IllegalState('not enough elements available in this list')
        else:
            next_list = []
            x = 0
            while x < n:
                try:
                    next_list.append(next(self))
                except Exception:  # Need to specify exceptions here!
                    raise OperationFailed()
                x = x + 1
            return next_list

    next_objective_bank = property(get_next_objective_bank)
