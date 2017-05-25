import re
import json
import time
import tarfile
import functools

try:
    # python 2
    from cStringIO import StringIO
except ImportError:
    # python 3
    from io import StringIO

from bs4 import BeautifulSoup

from bson import ObjectId

from dlkit.abstract_osid.assessment.objects import Item
from dlkit.abstract_osid.osid.errors import IllegalState, NotFound
from dlkit.primordium.id.primitives import Id
from dlkit.primordium.type.primitives import Type

from ...osid.base_records import TextsFormRecord, TextsRecord,\
    TemporalFormRecord, TemporalRecord, ObjectInitRecord, DEFAULT_FORMAT_TYPE,\
    DEFAULT_LANGUAGE_TYPE, DEFAULT_SCRIPT_TYPE, ProvenanceFormRecord, QueryInitRecord
from ...osid.edx_base import edXQueryMethods

from ...registry import COMPOSITION_GENUS_TYPES, COMPOSITION_RECORD_TYPES
from .utilities import EdXUtilitiesMixin, clean_str
from ..basic.base_records import ProvenanceCompositionRecord


def valid_for(whitelist):
    """ descriptor to check the genus type of an item, to see
    if the method is valid for that type
    From http://stackoverflow.com/questions/30809814/python-descriptors-with-arguments
    :param func:
    :return:
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(self, *args):
            valid_item = False
            try:
                if Id(self.my_osid_object_form._my_map['genusTypeId']).identifier in whitelist:
                    valid_item = True
            except AttributeError:
                if Id(self.my_osid_object._my_map['genusTypeId']).identifier in whitelist:
                    valid_item = True
            finally:
                if valid_item:
                    return func(self, *args)
                else:
                    raise IllegalState('Method not allowed for this object.')
        return wrapper
    return decorator


class EdXCompositionFormRecord(TemporalFormRecord, TextsFormRecord, ProvenanceFormRecord):
    """for managing edX compositions, like
    course / chapter / sequential / split_test / vertical"""
    _implemented_record_type_identifiers = [
        'edx-composition',
        'text-records',
        'provenance'
    ]

    def __init__(self, osid_object_form=None):
        if osid_object_form is not None:
            self.my_osid_object_form = osid_object_form
        super(EdXCompositionFormRecord, self).__init__()
        self._init_metadata()
        if not self.my_osid_object_form.is_for_update():
            self._init_map()

    def _init_map(self):
        """stub"""
        super(EdXCompositionFormRecord, self)._init_map()
        TextsFormRecord._init_map(self)  # because the OsidForm breaks the MRO chain for super, in TemporalFormRecord
        ProvenanceFormRecord._init_map(self)  # because the OsidForm breaks the MRO chain for super, in TemporalFormRecord

        self.my_osid_object_form._my_map['texts']['fileName'] = \
            self._text_metadata['default_string_values'][0]
        self.my_osid_object_form._my_map['texts']['format'] = \
            self._text_metadata['default_string_values'][0]  # homework, exam, lab, etc.
        self.my_osid_object_form._my_map['visibleToStudents'] = \
            self._visible_to_students_metadata['default_boolean_values'][0]
        self.my_osid_object_form._my_map['draft'] = \
            self._draft_metadata['default_boolean_values'][0]
        self.my_osid_object_form._my_map['texts']['userPartitionId'] = \
            self._user_partition_id_metadata['default_string_values'][0]
        self.my_osid_object_form._my_map['texts']['org'] = \
            self._org_metadata['default_string_values'][0]
        self.my_osid_object_form._my_map['learningObjectiveIds'] = \
            self._learning_objective_ids_metadata['default_string_values'][0]

    def _init_metadata(self):
        """stub"""
        super(EdXCompositionFormRecord, self)._init_metadata()
        TextsFormRecord._init_metadata(self)  # because the OsidForm breaks the MRO chain for super, in TemporalFormRecord
        ProvenanceFormRecord._init_metadata(self)  # because the OsidForm breaks the MRO chain for super, in TemporalFormRecord
        self._visible_to_students_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'visible_to_students'),
            'element_label': 'Visible to students',
            'instructions': 'enter a boolean value',
            'required': False,
            'read_only': False,
            'linked': False,
            'array': False,
            'default_boolean_values': [True],
            'syntax': 'BOOLEAN'
        }
        self._draft_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'draft'),
            'element_label': 'Draft',
            'instructions': 'enter a boolean value',
            'required': False,
            'read_only': False,
            'linked': False,
            'array': False,
            'default_boolean_values': [False],
            'syntax': 'BOOLEAN'
        }
        self._user_partition_id_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'user_partition_id'),
            'element_label': 'user_partition_id',
            'instructions': 'enter a text string',
            'required': False,
            'read_only': False,
            'linked': False,
            'array': False,
            'default_string_values': [''],
            'syntax': 'STRING',
            'minimum_string_length': self._min_string_length,
            'maximum_string_length': self._max_string_length,
            'string_set': []
        }
        self._org_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'org'),
            'element_label': 'org',
            'instructions': 'enter a text string',
            'required': False,
            'read_only': False,
            'linked': False,
            'array': False,
            'default_string_values': [''],
            'syntax': 'STRING',
            'minimum_string_length': self._min_string_length,
            'maximum_string_length': self._max_string_length,
            'string_set': []
        }

        # ideally this would be type LIST?
        self._learning_objective_ids_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'learning_objectives'),
            'element_label': 'learning_objectives',
            'instructions': 'enter a list of strings',
            'required': False,
            'read_only': False,
            'linked': False,
            'array': False,
            'default_string_values': [[]],
            'syntax': 'STRING',
            'minimum_string_length': self._min_string_length,
            'maximum_string_length': self._max_string_length,
            'string_set': []
        }

    def set_file_name(self, file_name):
        if Id(self.my_osid_object_form._my_map['genusTypeId']).identifier == 'course':
            file_name = 'course.xml'  # this may not be true...also need one that is /<run>.xml?
        self.add_text(str(file_name), 'fileName')

    def clear_file_name(self):
        self.my_osid_object_form._my_map['texts']['fileName'] = \
            self._text_metadata['default_string_values'][0]

    @valid_for(['chapter', 'sequential'])
    def set_start_date(self, start_date):
        super(EdXCompositionFormRecord, self).set_start_date(start_date)

    @valid_for(['chapter', 'sequential'])
    def clear_start_date(self):
        super(EdXCompositionFormRecord, self).clear_start_date()

    @valid_for(['chapter', 'sequential'])
    def set_visible_to_students(self, visible):
        self.my_osid_object_form._my_map['visibleToStudents'] = bool(visible)

    @valid_for(['chapter', 'sequential'])
    def clear_visible_to_students(self):
        self.my_osid_object_form._my_map['visibleToStudents'] = \
            self._visible_to_students_metadata['default_boolean_values'][0]

    @valid_for(['course'])
    def set_org(self, org):
        self.add_text(str(org), 'org')

    @valid_for(['course'])
    def clear_org(self):
        self.my_osid_object_form._my_map['texts']['org'] = \
            self._org_metadata['default_string_values'][0]

    @valid_for(['vertical'])
    def set_draft(self, is_draft):
        self.my_osid_object_form._my_map['draft'] = bool(is_draft)

    @valid_for(['vertical'])
    def clear_draft(self):
        self.my_osid_object_form._my_map['draft'] = \
            self._draft_metadata['default_boolean_values'][0]

    @valid_for(['split_test'])
    def set_user_partition_id(self, user_partition_id):
        self.add_text(str(user_partition_id), 'userPartitionId')

    @valid_for(['split_test'])
    def clear_user_partition_id(self):
        self.my_osid_object_form._my_map['userPartitionId'] = \
            self._user_partition_id_metadata['default_string_values'][0]

    @valid_for(['vertical', 'chapter', 'sequential', 'split_test'])
    def set_learning_objective_ids(self, learning_objective_ids):
        lo_ids_str = [str(lo) for lo in learning_objective_ids]
        self.my_osid_object_form._my_map['learningObjectiveIds'] = lo_ids_str

    @valid_for(['vertical', 'chapter', 'sequential', 'split_test'])
    def clear_learning_objective_ids(self):
        self.my_osid_object_form._my_map['learningObjectiveIds'] = \
            self._learning_objective_ids_metadata['default_string_values'][0]


class EdXCompositionQueryRecord(edXQueryMethods, QueryInitRecord):
    def match_learning_objective(self, learning_objective_id, match):
        self._my_osid_query._add_match('learningObjectiveIds', str(learning_objective_id), match)

    def clear_match_learning_objective(self):
        self._my_osid_query._clear_terms('learningObjectiveIds')

    def match_any_learning_objective(self, match):
        """Matches an item with any objective.

        arg:    match (boolean): ``true`` to match items with any
                learning objective, ``false`` to match items with no
                learning objectives
        *compliance: mandatory -- This method must be implemented.*

        """
        match_key = 'learningObjectiveIds'
        param = '$exists'
        if match:
            flag = 'true'
        else:
            flag = 'false'
        if match_key in self._my_osid_query._query_terms:
            self._my_osid_query._query_terms[match_key][param] = flag
        else:
            self._my_osid_query._query_terms[match_key] = {param: flag}
        self._my_osid_query._query_terms[match_key]['$nin'] = [[], ['']]

    def clear_learning_objective_terms(self):
        """Clears all learning objective terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        self._my_osid_query._clear_terms('learningObjectiveIds')

    def match_composition_descendants(self, composition_id, repository_id, match):
        if match:
            inin = '$in'
        else:
            inin = '$nin'
        mgr = self._my_osid_query._get_provider_manager('REPOSITORY')
        child_ids = self._get_descendant_ids(composition_id, repository_id, mgr)
        child_identifiers = [ObjectId(_id.identifier) for _id in child_ids]
        child_identifiers += [ObjectId(composition_id.identifier)]
        child_identifiers = list(set(child_identifiers))
        self._my_osid_query._query_terms['_id'] = {inin: child_identifiers}

    def clear_match_composition_descendants(self):
        self._my_osid_query._clear_terms('_id')


class EdXCompositionRecord(TextsRecord, TemporalRecord,
                           ProvenanceCompositionRecord, EdXUtilitiesMixin):
    """edX compositions, like course / chapter / etc."""
    def __init__(self, object_map):
        super(EdXCompositionRecord, self).__init__(object_map)
        if (not hasattr(self.my_osid_object, '_supported_record_type_ids') or
                self.my_osid_object._supported_record_type_ids is None):
            self.my_osid_object._supported_record_type_ids = []
        self.my_osid_object._supported_record_type_ids.append(
            str(Type(**COMPOSITION_RECORD_TYPES['edx-composition'])))

    @valid_for(['chapter', 'sequential'])
    def get_start_date(self):
        return super(EdXCompositionRecord, self).get_start_date()

    start_date = property(fget=get_start_date)

    @property
    def filename(self):
        return self.my_osid_object._my_map['texts']['fileName']

    @valid_for(['chapter', 'sequential'])
    def get_visible_to_students(self):
        return self.my_osid_object._my_map['visibleToStudents']

    visible_to_students = property(fget=get_visible_to_students)

    @valid_for(['vertical'])
    def get_draft(self):
        return self.my_osid_object._my_map['draft']

    draft = property(fget=get_draft)

    @valid_for(['course'])
    def get_org(self):
        return self.my_osid_object._my_map['texts']['org']

    org = property(fget=get_org)

    @valid_for(['split_test'])
    def get_user_partition_id(self):
        return self.my_osid_object._my_map['texts']['userPartitionId']

    user_partition_id = property(fget=get_user_partition_id)

    @valid_for(['split_test'])
    def get_group_id_to_child(self):
        # get the children compositions, then construct
        # the escaped-JSON structure for this split_test
        group_ids = {}
        # also need the course name...so go up the composition tree
        course_node = None
        found_course = False
        rm = self.my_osid_object._get_provider_manager('REPOSITORY')
        cqs = rm.get_composition_query_session_for_repository(Id(self.my_osid_object._my_map['assignedRepositoryIds'][0]))
        search_node = self.my_osid_object
        while not found_course:
            querier = cqs.get_composition_query()
            cqs.use_unsequestered_composition_view()
            querier.match_contained_composition_id(search_node.ident, True)
            parents = cqs.get_compositions_by_query(querier)
            if parents.available() == 0:
                found_course = True
            else:
                parent = next(parents)
                if parent.genus_type.identifier == 'course':
                    found_course = True
                    course_node = parent
                else:
                    search_node = parent

        if course_node is None:
            return ''
        else:
            for index, child in enumerate(self.my_osid_object.get_children()):
                group_ids[index] = 'i4x://{0}/{1}/{2}/{3}'.format(course_node.org,
                                                                  re.sub('[^\w\s-]', '', course_node.display_name.text),
                                                                  child.genus_type.identifier,
                                                                  child.url)
            return json.dumps(group_ids).replace('"', '&quot;')

    group_id_to_child = property(fget=get_group_id_to_child)

    @valid_for(['vertical', 'chapter', 'sequential', 'split_test'])
    def get_learning_objective_ids(self):
        return self.my_osid_object._my_map['learningObjectiveIds']

    learning_objective_ids = property(fget=get_learning_objective_ids)

    @property
    def assets(self):
        resources = []
        try:
            rm = self.my_osid_object._get_provider_manager('REPOSITORY')
            acs = rm.get_asset_composition_session_for_repository(
                Id(self.my_osid_object._my_map['assignedRepositoryIds'][0]))
            for asset in acs.get_composition_assets(self.my_osid_object.ident):
                asset_map = asset.object_map
                if 'enclosedObjectId' in asset_map:
                    assessment = asset.get_enclosed_object()
                    am = self.my_osid_object._get_provider_manager('ASSESSMENT')
                    abas = am.get_assessment_basic_authoring_session_for_bank(
                        Id(assessment.object_map['assignedBankIds'][0]))
                    for item in abas.get_items(assessment.ident):
                        resources.append(item)
                else:
                    resources.append(asset)
        except NotFound:
            # no assets
            pass
        return resources

    def all_children(self, repository=None):
        child_objects = []
        rm = self.my_osid_object._get_provider_manager('REPOSITORY')
        if repository is None:
            repository_id = Id(self.my_osid_object.object_map['assignedRepositoryIds'][0])
            rls = rm.get_repository_lookup_session()

            repository = rls.get_repository(repository_id)
        append_error_child = False
        error_compositions = []
        missing_child_ids = []

        for child_id in self.my_osid_object.get_child_ids():
            try:
                # need to use unsequestered view so get a lookup manager separately
                composition_lookup_session = rm.get_composition_lookup_session_for_repository(repository.ident)
                composition_lookup_session.use_federated_repository_view()
                composition_lookup_session.use_unsequestered_composition_view()
                child = composition_lookup_session.get_composition(child_id)
                if child.is_sequestered():
                    try:
                        for asset in child.assets:
                            child_objects.append((asset, False))  # For now, cannot edit assets...
                    except NotFound:
                        # no assets
                        pass
                else:
                    child_objects.append((child, True))
            except NotFound:
                try:
                    # append the child, but flag it as not belonging to the user...
                    composition_lookup_session = rm.get_composition_lookup_session()
                    composition_lookup_session.use_federated_repository_view()
                    composition_lookup_session.use_unsequestered_composition_view()
                    child = composition_lookup_session.get_composition(child_id)
                    if child.is_sequestered():
                        try:
                            for asset in child.assets:
                                child_objects.append((asset, False))
                        except NotFound:
                            # no assets
                            pass
                    else:
                        child_objects.append((child, False))
                except NotFound:
                    # the composition must be deleted or no longer accessible to
                    # the user. Remove the ID from the child_ids list, and
                    # add a sequestered child here notifying the user
                    cas = rm.get_composition_admin_session_for_repository(repository.ident)
                    form = cas.get_composition_form_for_create([Type(**COMPOSITION_RECORD_TYPES['edx-composition'])])
                    form.set_genus_type(Type(**COMPOSITION_GENUS_TYPES['error-deleted']))
                    form.display_name = 'Missing composition: ' + str(child_id)
                    form.description = 'This composition has been deleted, or you no longer have access to it.'
                    error_composition = cas.create_composition(form)
                    error_compositions.append(error_composition)
                    missing_child_ids.append(str(child_id))
                    append_error_child = True
                    child_objects.append((error_composition, False))

        if append_error_child:
            current_child_ids = self.my_osid_object.get_child_ids()
            current_child_idstrs = [str(i) for i in current_child_ids]
            for index, child_id in enumerate(current_child_idstrs):
                if child_id in missing_child_ids:
                    current_child_idstrs[index] = str(error_compositions[missing_child_ids.index(child_id)].ident)

            updated_child_ids = [Id(i) for i in current_child_idstrs]
            cas = rm.get_composition_admin_session_for_repository(repository.ident)
            form = cas.get_composition_form_for_update(self.my_osid_object.ident)
            form.set_children(updated_child_ids)
            cas.update_composition(form)
        return child_objects

    def clone_to(self, target_repo, target_parent=None):
        new_composition = target_repo.duplicate_composition(self.my_osid_object.ident)
        form = target_repo.get_composition_form_for_update(new_composition.ident)
        form.set_provenance(str(self.my_osid_object.ident))
        new_composition = target_repo.update_composition(form)

        if target_parent is not None:
            original_id = str(self.my_osid_object.ident)
            new_id = str(new_composition.ident)
            target_repo.use_unsequestered_composition_view()
            updated_parent = target_repo.get_composition(target_parent.ident)
            form = target_repo.get_composition_form_for_update(updated_parent.ident)
            current_child_ids = list(updated_parent.get_child_ids())
            current_child_ids = [Id(str(i).replace(original_id, new_id)) for i in current_child_ids]
            form.set_children(current_child_ids)
            target_repo.update_composition(form)

        return new_composition

    def export_olx(self, tarball, root_path):
        """if sequestered, only export the assets"""
        if self.my_osid_object.is_sequestered():
            pass  # just export assets
        else:
            # also add to the /<tag>/ folder
            my_tag = self.my_osid_object.genus_type.identifier
            my_path = '{0}{1}/{2}.xml'.format(root_path,
                                              my_tag,
                                              self.url)
            my_soup = BeautifulSoup('<' + my_tag + '/>', 'xml')
            getattr(my_soup, my_tag)['display_name'] = self.my_osid_object.display_name.text

            if my_tag == 'split_test':
                getattr(my_soup, my_tag)['group_id_to_child'] = self.my_osid_object.group_id_to_child
                getattr(my_soup, my_tag)['user_partition_id'] = self.my_osid_object.user_partition_id

            rm = self.my_osid_object._get_provider_manager('REPOSITORY')
            cls = rm.get_composition_lookup_session()
            cls.use_federated_repository_view()
            cls.use_unsequestered_composition_view()
            for child_id in self.my_osid_object.get_child_ids():
                child = cls.get_composition(child_id)
                if child.is_sequestered():
                    # append its assets here
                    for asset in child.assets:
                        if isinstance(asset, Item):
                            unique_url = asset.export_olx(tarball, root_path)
                            unique_name = unique_url.split('/')[-1].replace('.xml', '')
                            asset_type = asset.genus_type.identifier
                            asset_tag = my_soup.new_tag(asset_type)
                            # asset_tag['display_name'] = asset.display_name.text
                            asset_tag['url_name'] = unique_name
                            getattr(my_soup, my_tag).append(asset_tag)
                        else:
                            for ac in asset.get_asset_contents():
                                asset_type = ac.genus_type.identifier

                                if asset_type == 'video' or asset_type == 'videoalpha':
                                    asset_olx = ac.get_text().text
                                    asset_tag = BeautifulSoup(asset_olx, 'html5lib').find(asset_type)
                                else:
                                    unique_url = asset.export_olx(tarball, root_path)[0]  # Assumption
                                    unique_name = unique_url.split('/')[-1].replace('.xml', '')
                                    asset_tag = my_soup.new_tag(asset_type)
                                    # asset_tag['display_name'] = asset.display_name.text
                                    asset_tag['url_name'] = unique_name
                                getattr(my_soup, my_tag).append(asset_tag)
                else:
                    child_type = child.genus_type.identifier
                    child_tag = my_soup.new_tag(child_type)
                    # child_tag['display_name'] = child.display_name.text
                    child_tag['url_name'] = child.url
                    getattr(my_soup, my_tag).append(child_tag)

                    child.export_olx(tarball, root_path)

            self.write_to_tarfile(tarball, my_path, my_soup)

        for asset in self.assets:
            try:
                asset.export_olx(tarball, root_path)
            except AttributeError:
                pass

    def export_standalone_olx(self):
        filename = '{0}_{1}'.format(self.my_osid_object.display_name.text,
                                    str(int(time.time())))
        filename = clean_str(filename) + '.tar.gz'
        root_path = ''

        olx = StringIO()
        tarball = tarfile.open(filename, mode='w', fileobj=olx)
        self.my_osid_object.export_olx(tarball, root_path)

        return filename, olx


class EdXCourseRunCompositionFormRecord(TextsFormRecord):
    """for managing edX course run"""
    _implemented_record_type_identifiers = [
        'edx-course-run',
        'text-records'
    ]

    def __init__(self, osid_object_form=None):
        if osid_object_form is not None:
            self.my_osid_object_form = osid_object_form
        super(EdXCourseRunCompositionFormRecord, self).__init__()
        self._init_metadata()
        if not self.my_osid_object_form.is_for_update():
            self._init_map()

    def _init_map(self):
        """stub"""
        super(EdXCourseRunCompositionFormRecord, self)._init_map()

    def _init_metadata(self):
        """stub"""
        super(EdXCourseRunCompositionFormRecord, self)._init_metadata()

    def set_policy(self, policy):
        self.add_text(str(policy), 'policy')

    def clear_policy(self):
        self.clear_text('policy')

    def set_grading_policy(self, grading_policy):
        self.add_text(str(grading_policy), 'grading_policy')

    def clear_grading_policy(self):
        self.clear_text('grading_policy')


class EdXCourseRunCompositionRecord(EdXUtilitiesMixin, TextsRecord, ObjectInitRecord):
    """edX user course run composition"""
    def __init__(self, object_map):
        super(EdXCourseRunCompositionRecord, self).__init__(object_map)
        if not hasattr(self.my_osid_object, '_supported_record_type_ids'):
            self.my_osid_object._supported_record_type_ids = []
        self.my_osid_object._supported_record_type_ids.append(
            str(Type(**COMPOSITION_RECORD_TYPES['edx-course-run'])))

    @property
    def grading_policy(self):
        return self.get_text('grading_policy')

    @property
    def policy(self):
        return self.get_text('policy')

    def export_run_olx(self):
        run_comp = self.my_osid_object
        rm = self.my_osid_object._get_provider_manager('REPOSITORY')
        cqs = rm.get_composition_query_session_for_repository(
            Id(self.my_osid_object._my_map['assignedRepositoryIds'][0]))
        cqs.use_unsequestered_composition_view()
        querier = cqs.get_composition_query()
        querier.match_contained_composition_id(run_comp.ident, True)
        course_comp = next(cqs.get_compositions_by_query(querier))

        filename = '{0}_{1}_{2}'.format(course_comp.display_name.text,
                                        run_comp.display_name.text,
                                        str(int(time.time())))
        filename = clean_str(filename) + '.tar.gz'
        root_path = '{0}/'.format(run_comp.display_name.text)

        olx = StringIO()
        tarball = tarfile.open(filename, mode='w', fileobj=olx)

        # write the course.xml files first
        soup = BeautifulSoup('<course/>', 'xml')
        soup.course['course'] = course_comp.display_name.text
        soup.course['url_name'] = run_comp.display_name.text
        soup.course['org'] = 'MITx'

        course_path = '{0}course.xml'.format(root_path)
        self.write_to_tarfile(tarball, course_path, soup)

        root_file_path = '{0}roots/{1}.xml'.format(root_path,
                                                   run_comp.display_name.text)
        self.write_to_tarfile(tarball, root_file_path, soup)

        exceptions = BeautifulSoup('<errors/>', 'xml')
        course_xml = BeautifulSoup('<course/>', 'xml')
        course_xml.course['number'] = course_comp.display_name.text
        course_xml_path = '{0}course/{1}.xml'.format(root_path,
                                                     run_comp.display_name.text)
        for child_id in run_comp.get_child_ids():
            try:
                cls = rm.get_composition_lookup_session_for_repository(run_comp.ident)
                child = cls.get_composition(child_id)
            except NotFound:
                cls = rm.get_composition_lookup_session()
                cls.use_federated_repository_view()
                cls.use_unsequestered_composition_view()
                child = cls.get_composition(child_id)
            try:
                if child.is_sequestered():
                    pass
                else:
                    # add to the course/run.xml file
                    child_type = child.genus_type.identifier
                    child_tag = course_xml.new_tag(child_type)
                    # child_tag['display_name'] = child.display_name.text
                    child_tag['url_name'] = child.url
                    course_xml.course.append(child_tag)
                child.export_olx(tarball, root_path)
            except AttributeError:
                bad_child = exceptions.new_tag('composition')
                bad_child['id'] = str(child_id)
                bad_child.string = child.display_name.text
                exceptions.errors.append(bad_child)

        self.write_to_tarfile(tarball, course_xml_path, course_xml)

        errors_path = '{0}errors.xml'.format(root_path)
        self.write_to_tarfile(tarball, errors_path, exceptions)

        tarball.close()

        return filename, olx
