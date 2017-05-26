import re
import time
import tarfile

try:
    # python 2
    from cStringIO import StringIO
except ImportError:
    # python 3
    from io import StringIO

from bs4 import BeautifulSoup

from dlkit.abstract_osid.repository import record_templates as abc_repository_records
from dlkit.abstract_osid.osid.errors import IllegalState, NotFound
from dlkit.primordium.id.primitives import Id
from dlkit.primordium.type.primitives import Type

from ...osid.base_records import TextsRecord, TextsFormRecord

from ..registry import COMPOSITION_GENUS_TYPES, COMPOSITION_RECORD_TYPES

from ..edx.utilities import EdXUtilitiesMixin, clean_str

EDX_COMPOSITION_RECORD_TYPE = Type(**COMPOSITION_RECORD_TYPES['edx-composition'])


class LoreRepositoryRecord(TextsRecord, abc_repository_records.RepositoryRecord):
    """basic LORE repository content"""
    _implemented_record_type_identifiers = [
        'lore-repo',
        'texts'
    ]

    @property
    def id(self):
        return str(self.my_osid_object.ident)

    @property
    def name(self):
        return self.my_osid_object.display_name.text

    @property
    def slug(self):
        try:
            from django.utils.text import slugify
            return slugify(self.my_osid_object.display_name.text)
        except ImportError:
            name = re.sub('[^\w\s-]', '', self.my_osid_object.display_name.text.lower())
            return re.sub('[-\s]+', '-', name)

    def _update_object_map(self, obj_map):
        obj_map.update({
            'slug': self.my_osid_object.slug
        })
        super(LoreRepositoryRecord, self)._update_object_map(obj_map)


class LoreRepositoryFormRecord(TextsFormRecord, abc_repository_records.RepositoryFormRecord):
    """basic LORE repository content"""
    _implemented_record_type_identifiers = [
        'lore-repo',
        'texts'
    ]

    def __init__(self, osid_object_form):
        if osid_object_form is not None:
            self.my_osid_object_form = osid_object_form
        self._init_metadata()
        if not osid_object_form.is_for_update():
            self._init_map()

    def _init_map(self):
        TextsFormRecord._init_map(self)

    def _init_metadata(self):
        TextsFormRecord._init_metadata(self)


class LoreCourseRepositoryRecord(TextsRecord, abc_repository_records.RepositoryRecord):
    """basic LORE repository content"""
    _implemented_record_type_identifiers = [
        'course-repo',
        'texts-item'
    ]

    @property
    def org(self):
        return self.get_text('org')


class LoreCourseRepositoryFormRecord(TextsFormRecord, abc_repository_records.RepositoryFormRecord):
    """basic LORE repository content"""
    _implemented_record_type_identifiers = [
        'course-repo',
        'texts-item'
    ]

    def __init__(self, osid_object_form):
        if osid_object_form is not None:
            self.my_osid_object_form = osid_object_form
        self._init_metadata()
        if not osid_object_form.is_for_update():
            self._init_map()
        super(LoreCourseRepositoryFormRecord, self).__init__()

    def _init_map(self):
        TextsFormRecord._init_map(self)
        super(LoreCourseRepositoryFormRecord, self)._init_map()

    def _init_metadata(self):
        TextsFormRecord._init_metadata(self)
        super(LoreCourseRepositoryFormRecord, self)._init_metadata()

    def set_org(self, org):
        self.add_text(str(org), 'org')

    def clear_org(self):
        self.clear_text('org')


class LoreCourseRunRepositoryRecord(TextsRecord, EdXUtilitiesMixin, abc_repository_records.RepositoryRecord):
    """basic LORE repository content"""
    _implemented_record_type_identifiers = [
        'run-repo',
        'texts-item'
    ]

    @property
    def platform(self):
        try:
            return self.get_text('platform')
        except IllegalState:
            return ''

    @property
    def grading_policy(self):
        try:
            return self.get_text('grading_policy')
        except IllegalState:
            return ''

    @property
    def policy(self):
        try:
            return self.get_text('policy')
        except IllegalState:
            return ''

    @property
    def course_node(self):
        rm = self.my_osid_object._get_provider_manager('REPOSITORY')
        cls = rm.get_composition_lookup_session_for_repository(self.my_osid_object.ident)
        cls.use_unsequestered_composition_view()
        try:
            return next(cls.get_compositions_by_genus_type(
                Type(**COMPOSITION_GENUS_TYPES['course'])))
        except StopIteration:
            raise AttributeError

    def export_olx(self):
        run_repo = self.my_osid_object
        rm = self.my_osid_object._get_provider_manager('REPOSITORY')
        rhs = rm.get_repository_hierarchy_session()
        course_repo = next(rhs.get_parent_repositories(run_repo.ident))

        filename = '{0}_{1}_{2}'.format(course_repo.display_name.text,
                                        run_repo.display_name.text,
                                        str(int(time.time())))
        filename = clean_str(filename) + '.tar.gz'
        root_path = '{0}/'.format(run_repo.display_name.text)

        olx = StringIO()
        tarball = tarfile.open(filename, mode='w', fileobj=olx)

        # write the course.xml files first
        soup = BeautifulSoup('<course/>', 'xml')
        soup.course['course'] = course_repo.display_name.text
        soup.course['url_name'] = run_repo.display_name.text
        soup.course['org'] = course_repo.org

        course_path = '{0}course.xml'.format(root_path)
        self.write_to_tarfile(tarball, course_path, soup)

        root_file_path = '{0}roots/{1}.xml'.format(root_path,
                                                   run_repo.display_name.text)
        self.write_to_tarfile(tarball, root_file_path, soup)

        # write policy files
        if run_repo.policy != '':
            policy_path = '{0}policies/{1}/policy.json'.format(root_path,
                                                               run_repo.display_name.text)
            self.write_to_tarfile(tarball,
                                  policy_path,
                                  soup=run_repo.policy,
                                  prettify=False)
        if run_repo.grading_policy != '':
            policy_path = '{0}policies/{1}/grading_policy.json'.format(root_path,
                                                                       run_repo.display_name.text)
            self.write_to_tarfile(tarball,
                                  policy_path,
                                  soup=run_repo.grading_policy,
                                  prettify=False)

        exceptions = BeautifulSoup('<errors/>', 'xml')
        course_xml = BeautifulSoup('<course/>', 'xml')
        course_xml.course['number'] = course_repo.display_name.text
        course_xml_path = '{0}course/{1}.xml'.format(root_path,
                                                     run_repo.display_name.text)
        course_node = self.course_node
        for child_id in course_node.get_child_ids():
            try:
                cls = rm.get_composition_lookup_session_for_repository(run_repo.ident)
                child = cls.get_composition(child_id)
            except NotFound:
                cls = rm.get_composition_lookup_session()
                cls.use_unsequestered_composition_view()
                cls.use_federated_repository_view()
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

    def clean_up(self, user_repo):
        # For now, remove the old run, but need to check
        # any assets / compositions referred to. If they belong to another
        # composition, keep them. If they will be orphaned,
        # remove them.
        rm = self.my_osid_object._get_provider_manager('REPOSITORY')
        am = self.my_osid_object._get_provider_manager('ASSESSMENT')
        run_repo = self.my_osid_object

        bls = am.get_bank_lookup_session()
        user_bank = bls.get_bank(user_repo.ident)

        cls = rm.get_composition_lookup_session_for_repository(run_repo.ident)
        cls.use_unsequestered_composition_view()
        cls.use_federated_repository_view()

        cqs = rm.get_composition_query_session_for_repository(run_repo.ident)
        cqs.use_unsequestered_composition_view()
        cqs.use_federated_repository_view()

        cas = rm.get_composition_admin_session_for_repository(run_repo.ident)

        cras = rm.get_composition_repository_assignment_session()
        crs = rm.get_composition_repository_session()
        acs = rm.get_asset_composition_session_for_repository(user_repo.ident)
        acs.use_federated_repository_view()
        aas = rm.get_asset_admin_session_for_repository(user_repo.ident)

        assessment_as = am.get_assessment_admin_session_for_bank(user_bank.ident)
        abas = am.get_assessment_basic_authoring_session_for_bank(user_bank.ident)
        ias = am.get_item_admin_session_for_bank(user_bank.ident)
        aqs = am.get_assessment_query_session_for_bank(user_bank.ident)
        aqs.use_federated_bank_view()

        for composition in cls.get_compositions():
            # first check the composition assets
            try:
                for asset in acs.get_composition_assets(composition.ident):
                    if acs.get_compositions_by_asset(asset.ident).available() == 1:
                        # if asset is an enclosed asset, delete the enclosed object
                        try:
                            obj = aas.get_enclosed_object()
                            items = abas.get_items(obj.ident)
                            assessment_as.delete_assessment(obj.ident)
                            for item in items:
                                # only delete the item if it is not in any other assessments
                                querier = aqs.get_assessment_query()
                                querier.match_item_id(item.ident, True)
                                if aqs.get_assessments_by_query(querier).available() == 0:
                                    ias.delete_item(item.ident)
                        except AttributeError:
                            pass
                        # delete the asset / wrapper
                        aas.delete_asset(asset.ident)
                    else:
                        # keep the asset if used in multiple places
                        pass
            except NotFound:
                pass

            if crs.get_repositories_by_composition(composition.ident).available() == 1:
                # remove composition from all parents
                querier = cqs.get_composition_query()
                querier.match_contained_composition_id(composition.ident, True)
                for parent in cqs.get_compositions_by_query(querier):
                    # if parent belongs to another repository, update its child list
                    # otherwise, pass, because parent will be deleted eventually
                    if parent.object_map['assignedRepositoryIds'][0] != str(run_repo.ident):
                        current_child_idstrs = [str(i) for i in parent.get_child_ids()]
                        current_child_idstrs.remove(str(composition.ident))
                        updated_child_ids = [Id(i) for i in current_child_idstrs]
                        form = cas.get_composition_form_for_update(parent.ident)
                        form.set_children(updated_child_ids)
                        cas.update_composition(form)

                # delete the composition
                cas.delete_composition(composition.ident)
            else:
                # unassign the composition from this repository
                cras.unassign_composition_from_repository(composition.ident, run_repo.ident)

        ras = rm.get_repository_admin_session()
        ras.delete_repository(run_repo.ident)


class LoreCourseRunRepositoryFormRecord(TextsFormRecord, abc_repository_records.RepositoryFormRecord):
    """basic LORE repository content"""
    _implemented_record_type_identifiers = [
        'run-repo',
        'texts-item'
    ]

    def __init__(self, osid_object_form):
        if osid_object_form is not None:
            self.my_osid_object_form = osid_object_form
        self._init_metadata()
        if not osid_object_form.is_for_update():
            self._init_map()
        super(LoreCourseRunRepositoryFormRecord, self).__init__()

    def _init_map(self):
        TextsFormRecord._init_map(self)
        super(LoreCourseRunRepositoryFormRecord, self)._init_map()

    def _init_metadata(self):
        TextsFormRecord._init_metadata(self)
        super(LoreCourseRunRepositoryFormRecord, self)._init_metadata()

    def set_platform(self, platform):
        self.add_text(str(platform), 'platform')

    def clear_platform(self):
        self.clear_text('platform')

    def set_policy(self, policy):
        self.add_text(str(policy), 'policy')

    def clear_policy(self):
        self.clear_text('policy')

    def set_grading_policy(self, grading_policy):
        self.add_text(str(grading_policy), 'grading_policy')

    def clear_grading_policy(self):
        self.clear_text('grading_policy')
