"""
Multiple choice ortho3d records
"""

import base64

from dlkit.abstract_osid.id.primitives import Id as ABCId
from dlkit.abstract_osid.transport.objects import DataInputStream as ABCDataInputStream
from dlkit.abstract_osid.osid.errors import InvalidArgument, IllegalState
from dlkit.primordium.id.primitives import Id
from dlkit.primordium.type.primitives import Type

from .orthographic_records import FirstAngleProjectionFormRecord,\
    FirstAngleProjectionRecord,\
    BaseInitMixin
from ..basic.simple_records import QuestionFilesRecord,\
    QuestionFilesFormRecord
from ..basic.multi_choice_records import MultiChoiceFileQuestionRecord,\
    MultiChoiceFileQuestionFormRecord,\
    MultiChoiceFileAnswerRecord,\
    MultiChoiceFileAnswerFormRecord

from ...registry import ASSET_GENUS_TYPES, ASSET_CONTENT_GENUS_TYPES

MANIP_ASSET_TYPE = Type(**ASSET_GENUS_TYPES['manipulateable-asset-type'])  # This may be obsolete
O3D_ASSET_TYPE = Type(**ASSET_GENUS_TYPES['ortho3d-asset-type'])
MANIP_ASSET_CONTENT_TYPE = Type(**ASSET_CONTENT_GENUS_TYPES['manipulateable-asset-content'])
OV_SET_ASSET_TYPE = Type(**ASSET_GENUS_TYPES['ortho-view-set-asset'])  # This may be obsolete
OV_SET_SMALL_ASSET_CONTENT_TYPE = Type(**ASSET_CONTENT_GENUS_TYPES['ortho-view-set-small'])
OV_SET_LARGE_ASSET_CONTENT_TYPE = Type(**ASSET_CONTENT_GENUS_TYPES['ortho-view-set-large'])


class MultiChoiceOrthoQuestionRecord(MultiChoiceFileQuestionRecord,
                                     QuestionFilesRecord,
                                     FirstAngleProjectionRecord):
    """multiple choice ortho3D question...files for Q and choices"""
    _implemented_record_type_identifiers = [
        'multi-choice-ortho',
        'multi-choice-file',
        'question-text',
        'question-files',
        'first-angle-projection'
    ]

    def has_manip(self):
        """stub"""
        return self.has_file('manip')

    def get_manip_id(self):
        """stub"""
        return self.get_asset_id_by_label('manip')

    def get_manip(self):
        """stub"""
        return self.get_file_by_label('manip', MANIP_ASSET_CONTENT_TYPE)

    def get_choices_files_map(self):
        """stub"""
        files_map = []
        for choice in self.get_choices():
            choice = dict(choice)
            choice['smallOrthoViewSet'] = base64.b64encode(
                self._get_asset_content(Id(choice['assetId']),
                                        OV_SET_SMALL_ASSET_CONTENT_TYPE
                                        ).get_data().read())
            choice['largeOrthoViewSet'] = base64.b64encode(
                self._get_asset_content(Id(choice['assetId']),
                                        OV_SET_LARGE_ASSET_CONTENT_TYPE
                                        ).get_data().read())
            del choice['assetId']
            files_map.append(choice)
        return files_map

    def get_choices_file_urls_map(self):
        """stub"""
        file_urls_map = []
        for choice in self.get_choices():
            choice = dict(choice)
            small_asset_content = self._get_asset_content(
                Id(choice['assetId']), OV_SET_SMALL_ASSET_CONTENT_TYPE)
            choice['smallOrthoViewSet'] = small_asset_content.get_url()

            small_asset_content = self._get_asset_content(
                Id(choice['assetId']), OV_SET_LARGE_ASSET_CONTENT_TYPE)
            choice['largeOrthoViewSet'] = small_asset_content.get_url()

            del choice['assetId']
            file_urls_map.append(choice)
        return file_urls_map

    file_urls_map = property(fget=get_choices_file_urls_map)

    def get_files(self):
        """stub"""
        files_map = {}
        try:
            files_map['choices'] = self.get_choices_file_urls_map()
            try:
                files_map.update(self.get_file_urls_map())
            except IllegalState:
                pass
        except Exception:
            files_map['choices'] = self.get_choices_files_map()
            try:
                files_map.update(self.get_files_map())
            except IllegalState:
                pass
        return files_map

    manip_id = property(fget=get_manip_id)
    manip = property(fget=get_manip)
    choices_files_map = property(fget=get_choices_files_map)


class MultiChoiceOrthoQuestionFormRecord(BaseInitMixin,
                                         MultiChoiceFileQuestionFormRecord,
                                         QuestionFilesFormRecord,
                                         FirstAngleProjectionFormRecord):
    """form for making an ortho3d multiple choice question
    https://rhettinger.wordpress.com/2011/05/26/super-considered-super/
    Because QuestionFilesFormRecord, and
    FirstAngleProjectionFormRecord are all "terminal" classes with regards
    to _init_map and _init_metadata, (i.e. non-cooperative), we will
    have to call them manually here.
    """
    _implemented_record_type_identifiers = [
        'multi-choice-ortho',
        'multi-choice-file',
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
        super(MultiChoiceOrthoQuestionFormRecord, self).__init__(
            osid_object_form=osid_object_form)

    def _init_map(self):
        """stub"""
        QuestionFilesFormRecord._init_map(self)
        FirstAngleProjectionFormRecord._init_map(self)
        super(MultiChoiceOrthoQuestionFormRecord, self)._init_map()

    def _init_metadata(self):
        """stub"""
        QuestionFilesFormRecord._init_metadata(self)
        FirstAngleProjectionFormRecord._init_metadata(self)
        super(MultiChoiceOrthoQuestionFormRecord, self)._init_metadata()

    def get_manip_metadata(self):
        """stub"""
        return self.get_file_metadata()

    def set_manip_id(self, o3d_asset_id):
        """stub"""
        if not isinstance(o3d_asset_id, ABCId):
            raise InvalidArgument('Argument must be a valid Id')
        self.add_asset(o3d_asset_id,
                       label='manip',
                       asset_content_type=MANIP_ASSET_CONTENT_TYPE)

    def create_o3d_asset(self,
                         manip=None,
                         small_ov_set=None,
                         large_ov_set=None,
                         display_name='',
                         description=''):
        """stub"""
        if manip and not isinstance(manip, ABCDataInputStream):
            raise InvalidArgument('Manipulatable object must be an ' +
                                  'osid.transport.DataInputStream object')
        if small_ov_set and not isinstance(small_ov_set, ABCDataInputStream):
            raise InvalidArgument('Small OV Set object must be an ' +
                                  'osid.transport.DataInputStream object')
        if large_ov_set and not isinstance(large_ov_set, ABCDataInputStream):
            raise InvalidArgument('Large OV Set object must be an ' +
                                  'osid.transport.DataInputStream object')
        asset_id, asset_content_id = self.create_asset(asset_type=O3D_ASSET_TYPE,
                                                       display_name=display_name,
                                                       description=description)
        if manip is not None:
            self.add_content_to_asset(asset_id=asset_id,
                                      asset_data=manip,
                                      asset_content_type=MANIP_ASSET_CONTENT_TYPE,
                                      asset_label='3d manipulatable')
        if small_ov_set is not None:
            self.add_content_to_asset(asset_id=asset_id,
                                      asset_data=small_ov_set,
                                      asset_content_type=OV_SET_SMALL_ASSET_CONTENT_TYPE,
                                      asset_label='small orthoviewset')
        if large_ov_set is not None:
            self.add_content_to_asset(asset_id=asset_id,
                                      asset_data=large_ov_set,
                                      asset_content_type=OV_SET_LARGE_ASSET_CONTENT_TYPE,
                                      asset_label='large orthoviewset')
        return asset_id

    # convenience methods that make and set the assets
    def set_manip(self, manip, ovs_sm=None, ovs_lg=None, name='A manipulatable'):
        """stub"""
        o3d_manip_id = self.create_o3d_asset(manip,
                                             small_ov_set=ovs_sm,
                                             large_ov_set=ovs_lg,
                                             display_name=name)
        self.set_manip_id(o3d_manip_id)

    def set_ortho_choice(self, small_asset_data, large_asset_data, name='Choice'):
        """stub"""
        o3d_asset_id = self.create_o3d_asset(manip=None,
                                             small_ov_set=small_asset_data,
                                             large_ov_set=large_asset_data,
                                             display_name=name)
        self.add_choice(o3d_asset_id, name=name)


class MultiChoiceOrthoAnswerRecord(MultiChoiceFileAnswerRecord):
    """ortho multichoice answer"""
    _implemented_record_type_identifiers = [
        'multi-choice'
    ]


class MultiChoiceOrthoAnswerFormRecord(MultiChoiceFileAnswerFormRecord):
    """ form for multi choice answer"""

    _implemented_record_type_identifiers = [
        'multi-choice'
    ]
