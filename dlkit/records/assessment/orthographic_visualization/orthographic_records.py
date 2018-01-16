"""
records.assessment.orthographic_visualization.orthographic_records.py
"""

from dlkit.json_.osid.metadata import Metadata

from dlkit.primordium.id.primitives import Id
from dlkit.primordium.transport.objects import DataInputStream
from dlkit.primordium.type.primitives import Type
from dlkit.abstract_osid.osid.errors import InvalidArgument, NullArgument,\
    NoAccess, NotFound, IllegalState
from dlkit.json_.id.objects import IdList

from ..basic.simple_records import QuestionTextRecord,\
    QuestionTextFormRecord,\
    QuestionFilesRecord,\
    QuestionFilesFormRecord,\
    IntegerAnswersRecord,\
    IntegerAnswersFormRecord,\
    QuestionTextAndFilesMixin
from ...osid.base_records import ObjectInitRecord
from ...registry import ASSET_CONTENT_GENUS_TYPES, ASSET_GENUS_TYPES

MANIP_ASSET_TYPE = Type(**ASSET_GENUS_TYPES['manipulateable-asset-type'])
MANIP_ASSET_CONTENT_TYPE = Type(**ASSET_CONTENT_GENUS_TYPES['manipulateable-asset-content'])
OV_ASSET_TYPE = Type(**ASSET_GENUS_TYPES['ortho-view-asset'])
OV_ASSET_CONTENT_TYPE = Type(**ASSET_CONTENT_GENUS_TYPES['ortho-view-asset-content'])


class FirstAngleProjectionRecord(ObjectInitRecord):
    """flag for first-angle projection or not"""
    _implemented_record_type_identifiers = [
        'first-angle-projection'
    ]

    def is_first_angle_projection(self):
        """stub"""
        return bool(self.my_osid_object._my_map['firstAngle'])


class FirstAngleProjectionFormRecord(ObjectInitRecord):
    """form for including first-angle information"""
    _implemented_record_type_identifiers = [
        'first-angle-projection'
    ]

    def __init__(self, osid_object_form=None):
        if osid_object_form is not None:
            self.my_osid_object_form = osid_object_form
        self._init_metadata()
        if not self.my_osid_object_form.is_for_update():
            self._init_map()
        super(FirstAngleProjectionFormRecord, self).__init__(osid_object_form)

    def _init_map(self):
        """stub"""
        self.my_osid_object_form._my_map['firstAngle'] = \
            self._first_angle_metadata['default_boolean_values'][0]

    def _init_metadata(self):
        """stub"""
        self._first_angle_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'first_angle'),
            'element_label': 'First Angle',
            'instructions': 'set boolean, is this a first angle projection',
            'required': False,
            'read_only': False,
            'linked': False,
            'array': False,
            'default_boolean_values': [False],
            'syntax': 'BOOLEAN',
        }

    def get_first_angle_projection_metadata(self):
        """stub"""
        return Metadata(**self._first_angle_metadata)

    def set_first_angle_projection(self, value=None):
        """stub"""
        if value is None:
            raise NullArgument()
        if self.get_first_angle_projection_metadata().is_read_only():
            raise NoAccess()
        if not self.my_osid_object_form._is_valid_boolean(value):
            raise InvalidArgument()
        self.my_osid_object_form._my_map['firstAngle'] = value

    def clear_first_angle_projection(self):
        """stub"""
        if (self.get_first_angle_projection_metadata().is_read_only() or
                self.get_first_angle_projection_metadata().is_required()):
            raise NoAccess()
        self.my_osid_object_form._my_map['firstAngle'] = \
            self._first_angle_metadata['default_boolean_values'][0]

    first_angle_projection = property(fset=set_first_angle_projection,
                                      fdel=clear_first_angle_projection)


class BaseOrthoQuestionRecord(QuestionTextRecord,
                              QuestionFilesRecord,
                              FirstAngleProjectionRecord):
    """basic ortho3d question"""
    _implemented_record_type_identifiers = [
        'base-ortho',
        'question-text',
        'question-files',
        'first-angle-projection'
    ]

    def has_manip(self):
        """stub"""
        return self.has_file('manip')

    def get_manip_id(self):
        """stub"""
        return self.get_asset_id('manip')

    def get_manip(self):
        """stub"""
        return self.get_file_by_label('manip', MANIP_ASSET_CONTENT_TYPE)

    def has_ortho_view_set(self):
        """stub"""
        return bool(self.has_file('frontView') and
                    self.has_file('sideView') and
                    self.has_file('topView'))

    def get_front_view_id(self):
        """stub"""
        return self.get_asset_id('frontView')

    def get_front_view(self):
        """stub"""
        return self.get_file_by_label('frontView', OV_ASSET_CONTENT_TYPE)

    def get_side_view_id(self):
        """stub"""
        return self.get_asset_id('sideView')

    def get_side_view(self):
        """stub"""
        return self.get_file_by_label('sideView', OV_ASSET_CONTENT_TYPE)

    def get_top_view_id(self):
        """stub"""
        return self.get_asset_id('topView')

    def get_top_view(self):
        """stub"""
        return self.get_file_by_label('topView', OV_ASSET_CONTENT_TYPE)

    manip_id = property(fget=get_manip_id)
    manip = property(fget=get_manip)
    front_view_id = property(fget=get_front_view_id)
    front_view = property(fget=get_front_view)
    top_view_id = property(fget=get_top_view_id)
    top_view = property(fget=get_top_view)
    side_view_id = property(fget=get_side_view_id)
    side_view = property(fget=get_side_view)


class BaseInitMixin(QuestionTextAndFilesMixin,
                    FirstAngleProjectionFormRecord):
    """Mixin class to make the three classes compatible with super()
    for _init_map and _init_metadata

    """
    def _init_map(self):
        """stub"""
        FirstAngleProjectionFormRecord._init_map(self)
        super(BaseInitMixin, self)._init_map()

    def _init_metadata(self):
        """stub"""
        FirstAngleProjectionFormRecord._init_metadata(self)
        super(BaseInitMixin, self)._init_metadata()


class BaseOrthoQuestionFormRecord(BaseInitMixin):
    """form for basic ortho3d questions
    https://rhettinger.wordpress.com/2011/05/26/super-considered-super/
    Because QuestionTextFormRecord, QuestionFilesFormRecord, and
    FirstAngleProjectionFormRecord are all "terminal" classes with regards
    to _init_map and _init_metadata, (i.e. non-cooperative), we will
    have to call them manually here.
    """
    _implemented_record_type_identifiers = [
        'base-ortho',
        'question-text',
        'question-files',
        'first-angle-projection'
    ]

    def __init__(self, osid_object_form=None):
        if osid_object_form is not None:
            self.my_osid_object_form = osid_object_form
        self._init_metadata()
        if not self.my_osid_object_form.is_for_update():
            self._init_map()
        super(BaseOrthoQuestionFormRecord, self).__init__(
            osid_object_form=osid_object_form)

    def _init_map(self):
        """stub"""
        super(BaseOrthoQuestionFormRecord, self)._init_map()

    def _init_metadata(self):
        """stub"""
        super(BaseOrthoQuestionFormRecord, self)._init_metadata()
        self._ortho_view_set_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'ortho_view_set'),
            'element_label': 'Orthographic View Set',
            'instructions': '',
            'required': False,
            'read_only': False,
            'linked': False,
            'array': False,
            'default_object_values': [''],
            'syntax': 'OBJECT',
            'object_set': []
        }

    def get_manip_metadata(self):
        """stub"""
        return self.get_file_metadata()

    def set_manip(self, manipulatable):
        """stub"""
        if not isinstance(manipulatable, DataInputStream):
            raise InvalidArgument('Manipulatable object be an ' +
                                  'osid.transport.DataInputStream object')
        self.add_file(manipulatable,
                      label='manip',
                      asset_type=MANIP_ASSET_TYPE,
                      asset_content_type=MANIP_ASSET_CONTENT_TYPE)

    def get_ortho_view_set_metadata(self):
        """stub"""
        return Metadata(**self._ortho_view_set_metadata)

    def get_ovs_front_view_metadata(self):
        """stub"""
        return self.get_file_metadata()

    def get_ovs_top_view_metadata(self):
        """stub"""
        return self.get_file_metadata()

    def get_ovs_side_view_metadata(self):
        """stub"""
        return self.get_file_metadata()

    def set_ortho_view_set(self, front_view, side_view, top_view):
        """stub"""
        if (not isinstance(front_view, DataInputStream) or
                not isinstance(top_view, DataInputStream) or
                not isinstance(side_view, DataInputStream)):
            raise InvalidArgument('views must be osid.transport.DataInputStream objects')
        self.add_file(front_view,
                      label='frontView',
                      asset_type=OV_ASSET_TYPE,
                      asset_content_type=OV_ASSET_CONTENT_TYPE)
        self.add_file(side_view,
                      label='sideView',
                      asset_type=OV_ASSET_TYPE,
                      asset_content_type=OV_ASSET_CONTENT_TYPE)
        self.add_file(top_view,
                      label='topView',
                      asset_type=OV_ASSET_TYPE,
                      asset_content_type=OV_ASSET_CONTENT_TYPE)

    def clear_ortho_view_set(self):
        """stub"""
        if (self.get_ortho_view_set_metadata().is_read_only() or
                self.get_ortho_view_set_metadata().is_required()):
            raise NoAccess()
        self.clear_file('frontView')
        self.clear_file('sideView')
        self.clear_file('topView')

    def set_ovs_view(self, asset_data, view_name):
        """
        view_name should be frontView, sideView, or topView
        """
        if not isinstance(asset_data, DataInputStream):
            raise InvalidArgument('view file must be an ' +
                                  'osid.transport.DataInputStream object')
        if view_name not in ['frontView', 'sideView', 'topView']:
            raise InvalidArgument('View name must be frontView, sideView, or topView.')
        self.clear_file(view_name)
        self.add_file(asset_data,
                      label=view_name,
                      asset_type=OV_ASSET_TYPE,
                      asset_content_type=OV_ASSET_CONTENT_TYPE)


class LabelOrthoFacesQuestionRecord(BaseOrthoQuestionRecord):
    """label the 3 faces on a manipulatable object"""
    _implemented_record_type_identifiers = [
        'label-ortho-faces',
        'base_ortho',
        'question-text',
        'question-files'
    ]


class LabelOrthoFacesQuestionFormRecord(BaseOrthoQuestionFormRecord):
    """form to create this type of question"""
    _implemented_record_type_identifiers = [
        'label-ortho-faces',
        'base_ortho',
        'question-text',
        'question-files'
    ]


class LabelOrthoFacesItemFormRecord(ObjectInitRecord):
    _implemented_record_type_identifiers = [
        'label-ortho-faces'
    ]
    pass


class LabelOrthoFacesItemRecord(ObjectInitRecord):
    _implemented_record_type_identifiers = [
        'label-ortho-faces'
    ]

    def _is_match(self, response, answer):
        match = False
        if (int(answer.get_front_face_value()) == int(response.get_front_face_value()) and
                int(answer.get_side_face_value()) == int(response.get_side_face_value()) and
                int(answer.get_top_face_value()) == int(response.get_top_face_value())):
            match = True
        return match

    def is_correctness_available_for_response(self, response):
        """is a measure of correctness available for a particular mc response"""
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

    def get_answer_for_response(self, response):
        for answer in self.my_osid_object.get_answers():
            if self._is_match(response, answer):
                return answer

        wrong_answers = None
        try:
            wrong_answers = list(self.my_osid_object.get_wrong_answers())
        except AttributeError:
            pass
        else:
            for answer in wrong_answers:
                if self._is_match(response, answer):
                    return answer
        # also look for generic incorrect answer
        if wrong_answers is not None:
            for answer in wrong_answers:
                if not answer.has_face_values():
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


class LabelOrthoFacesAnswerRecord(IntegerAnswersRecord):
    """the three face value answers"""
    _implemented_record_type_identifiers = [
        'label-ortho-faces'
    ]

    def has_face_values(self):
        """stub"""
        return (self.has_integer_value('frontFaceValue') and
                self.has_integer_value('topFaceValue') and
                self.has_integer_value('sideFaceValue'))

    def get_front_face_value(self):
        """stub"""
        return self.get_integer_value('frontFaceValue')

    def get_top_face_value(self):
        """stub"""
        return self.get_integer_value('topFaceValue')

    def get_side_face_value(self):
        """stub"""
        return self.get_integer_value('sideFaceValue')


class LabelOrthoFacesAnswerFormRecord(IntegerAnswersFormRecord):
    """form to set the answer faces"""
    _implemented_record_type_identifiers = [
        'label-ortho-faces'
    ]

    def __init__(self, osid_object_form):
        if osid_object_form is not None:
            self.my_osid_object_form = osid_object_form
        self._init_metadata()
        if not self.my_osid_object_form.is_for_update():
            self._init_map()
        super(LabelOrthoFacesAnswerFormRecord, self).__init__(
            osid_object_form=osid_object_form)

    def _init_map(self):
        """stub"""
        super(LabelOrthoFacesAnswerFormRecord, self)._init_map()

    def _init_metadata(self):
        """stub"""
        super(LabelOrthoFacesAnswerFormRecord, self)._init_metadata()
        self._face_values_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'face_values'),
            'element_label': 'Orthographic Face Values',
            'instructions': '',
            'required': True,
            'read_only': False,
            'linked': True,
            'array': False,
            'default_object_values': [{}],
            'syntax': 'OBJECT',
            'object_set': []
        }

    def get_face_values_metadata(self):
        """stub"""
        return Metadata(**self._face_values_metadata)

    def set_face_values(self, front_face_value, side_face_value, top_face_value):
        """stub"""
        if front_face_value is None or side_face_value is None or top_face_value is None:
            raise NullArgument()
        self.add_integer_value(value=int(front_face_value), label='frontFaceValue')
        self.add_integer_value(value=int(side_face_value), label='sideFaceValue')
        self.add_integer_value(value=int(top_face_value), label='topFaceValue')

    def clear_face_values(self):
        """stub"""
        if (self.get_face_values_metadata().is_read_only() or
                self.get_face_values_metadata().is_required()):
            raise NoAccess()
        self.clear_integer_value('frontFaceValue')
        self.clear_integer_value('sideFaceValue')
        self.clear_integer_value('topFaceValue')


class EulerRotationQuestionRecord(BaseOrthoQuestionRecord):
    """students can orient the manipulatable at the right angle"""
    _implemented_record_type_identifiers = [
        'euler-rotation',
        'base_ortho'
        'question-text',
        'question-files'
    ]


class EulerRotationQuestionFormRecord(BaseOrthoQuestionFormRecord):
    """form to create these questions"""
    _implemented_record_type_identifiers = [
        'euler-rotation',
        'base_ortho'
        'question-text',
        'question-files'
    ]


class EulerRotationAnswerRecord(IntegerAnswersRecord):
    """correct angle answers"""
    _implemented_record_type_identifiers = [
        'euler-rotation'
    ]

    def has_angle_values(self):
        """stub"""
        return (self.has_integer_value('xAngle') and
                self.has_integer_value('yAngle') and
                self.has_integer_value('zAngle'))

    def get_x_angle_value(self):
        """stub"""
        return self.get_integer_value('xAngle')

    def get_y_angle_value(self):
        """stub"""
        return self.get_integer_value('yAngle')

    def get_z_angle_value(self):
        """stub"""
        return self.get_integer_value('zAngle')


class EulerRotationAnswerFormRecord(IntegerAnswersFormRecord):
    """form to create the answer"""
    _implemented_record_type_identifiers = [
        'euler-rotation'
    ]

    def __init__(self, osid_object_form):
        if osid_object_form is not None:
            self.my_osid_object_form = osid_object_form
        self._init_metadata()
        if not self.my_osid_object_form.is_for_update():
            self._init_map()
        super(EulerRotationAnswerFormRecord, self).__init__(
            osid_object_form=osid_object_form)

    def _init_map(self):
        """stub"""
        super(EulerRotationAnswerFormRecord, self)._init_map()

    def _init_metadata(self):
        """stub"""
        super(EulerRotationAnswerFormRecord, self)._init_metadata()
        self._euler_rotation_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'angle_values'),
            'element_label': 'Euler Angle Values',
            'instructions': 'Provide X, Y, and Z euler angle rotation values',
            'required': True,
            'read_only': False,
            'linked': True,
            'array': False,
            'default_object_values': [{}],
            'syntax': 'OBJECT',
            'object_set': []
        }

    def get_euler_rotation_values_metadata(self):
        """stub"""
        return Metadata(**self._euler_rotation_metadata)

    def set_euler_angle_values(self, x_angle, y_angle, z_angle):
        """stub"""
        if x_angle is None or y_angle is None or z_angle is None:
            raise NullArgument()
        self.add_integer_value(value=x_angle, label='xAngle')
        self.add_integer_value(value=y_angle, label='yAngle')
        self.add_integer_value(value=z_angle, label='zAngle')

    def clear_angle_values(self):
        """stub"""
        if (self.get_euler_rotation_values_metadata().is_read_only() or
                self.get_euler_rotation_values_metadata().is_required()):
            raise NoAccess()
        self.clear_integer_value('xAngle')
        self.clear_integer_value('yAngle')
        self.clear_integer_value('zAngle')
