import re
import sys
import time
import tarfile

from six import BytesIO

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
        return self.my_osid_object.ident

    @property
    def name(self):
        return self.my_osid_object.display_name

    @property
    def slug(self):
        if sys.version_info >= (3, 6):
            raised_exception = ModuleNotFoundError
        else:
            raised_exception = ImportError
        try:
            from django.utils.text import slugify
            return slugify(self.my_osid_object.display_name.text)
        except raised_exception:
            name = re.sub('[^\w\s-]', '', self.my_osid_object.display_name.text.lower())
            return re.sub('[-\s]+', '-', name)

    def _update_object_map(self, obj_map):
        obj_map.update({
            'slug': self.my_osid_object.slug
        })
        try:
            super(LoreRepositoryRecord, self)._update_object_map(obj_map)
        except AttributeError:
            pass


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
        return self.get_text('platform')

    @property
    def grading_policy(self):
        return self.get_text('gradingPolicy')

    @property
    def policy(self):
        return self.get_text('policy')

    @property
    def course_node(self):
        rm = self.my_osid_object._get_provider_manager('REPOSITORY')
        if self.my_osid_object._proxy is None:
            cls = rm.get_composition_lookup_session_for_repository(self.my_osid_object.ident)
        else:
            cls = rm.get_composition_lookup_session_for_repository(
                self.my_osid_object.ident,
                proxy=self.my_osid_object._proxy
            )
        cls.use_unsequestered_composition_view()
        try:
            return next(cls.get_compositions_by_genus_type(
                Type(**COMPOSITION_GENUS_TYPES['course'])))
        except StopIteration:
            raise AttributeError

    def export_olx(self):
        run_repo = self.my_osid_object
        rm = self.my_osid_object._get_provider_manager('REPOSITORY')
        if self.my_osid_object._proxy is None:
            rhs = rm.get_repository_hierarchy_session()
        else:
            rhs = rm.get_repository_hierarchy_session(proxy=self.my_osid_object._proxy)
        course_repo = next(rhs.get_parent_repositories(run_repo.ident))

        filename = '{0}_{1}_{2}'.format(course_repo.display_name.text,
                                        run_repo.display_name.text,
                                        str(int(time.time())))
        filename = clean_str(filename) + '.tar.gz'
        root_path = '{0}/'.format(run_repo.display_name.text)

        olx = BytesIO()
        tarball = tarfile.open(filename, mode='w', fileobj=olx)

        # write the course.xml files first
        soup = BeautifulSoup('<course/>', 'xml')
        soup.course['course'] = course_repo.display_name.text
        soup.course['url_name'] = run_repo.display_name.text
        soup.course['org'] = course_repo.org.text

        course_path = '{0}course.xml'.format(root_path)
        self.write_to_tarfile(tarball, course_path, soup)

        root_file_path = '{0}roots/{1}.xml'.format(root_path,
                                                   run_repo.display_name.text)
        self.write_to_tarfile(tarball, root_file_path, soup)

        # write policy files
        try:
            policy = run_repo.policy
        except IllegalState:
            pass
        else:
            policy_path = '{0}policies/{1}/policy.json'.format(root_path,
                                                               run_repo.display_name.text)
            self.write_to_tarfile(tarball,
                                  policy_path,
                                  soup=policy.text,
                                  prettify=False)
        try:
            grading_policy = run_repo.grading_policy
        except IllegalState:
            pass
        else:
            policy_path = '{0}policies/{1}/grading_policy.json'.format(root_path,
                                                                       run_repo.display_name.text)
            self.write_to_tarfile(tarball,
                                  policy_path,
                                  soup=grading_policy.text,
                                  prettify=False)

        exceptions = BeautifulSoup('<errors/>', 'xml')
        course_xml = BeautifulSoup('<course/>', 'xml')
        course_xml.course['number'] = course_repo.display_name.text
        course_xml_path = '{0}course/{1}.xml'.format(root_path,
                                                     run_repo.display_name.text)
        course_node = self.course_node
        for child_id in course_node.get_child_ids():
            if self.my_osid_object._proxy is None:
                cls = rm.get_composition_lookup_session_for_repository(run_repo.ident)
            else:
                cls = rm.get_composition_lookup_session_for_repository(
                    run_repo.ident,
                    proxy=self.my_osid_object._proxy
                )

            try:
                child = cls.get_composition(child_id)
            except NotFound:
                if self.my_osid_object._proxy is None:
                    cls = rm.get_composition_lookup_session()
                else:
                    cls = rm.get_composition_lookup_session(proxy=self.my_osid_object._proxy)

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
        olx.seek(0)

        return filename, olx

    def clean_up(self, user_repo):
        # For now, remove the old run, but need to check
        # any assets / compositions referred to. If they belong to another
        # composition, keep them. If they will be orphaned,
        # remove them.
        rm = self.my_osid_object._get_provider_manager('REPOSITORY')
        am = self.my_osid_object._get_provider_manager('ASSESSMENT')
        run_repo = self.my_osid_object

        if self.my_osid_object._proxy is None:
            bls = am.get_bank_lookup_session()
        else:
            bls = am.get_bank_lookup_session(proxy=self.my_osid_object._proxy)

        user_bank = bls.get_bank(user_repo.ident)

        if self.my_osid_object._proxy is None:
            cls = rm.get_composition_lookup_session_for_repository(run_repo.ident)
            cqs = rm.get_composition_query_session_for_repository(run_repo.ident)
            cas = rm.get_composition_admin_session_for_repository(run_repo.ident)
            cras = rm.get_composition_repository_assignment_session()
            crs = rm.get_composition_repository_session()
            acs = rm.get_asset_composition_session_for_repository(user_repo.ident)
            aas = rm.get_asset_admin_session_for_repository(user_repo.ident)
            assessment_as = am.get_assessment_admin_session_for_bank(user_bank.ident)
            abas = am.get_assessment_basic_authoring_session_for_bank(user_bank.ident)
            ias = am.get_item_admin_session_for_bank(user_bank.ident)
            aqs = am.get_assessment_query_session_for_bank(user_bank.ident)
        else:
            cls = rm.get_composition_lookup_session_for_repository(
                run_repo.ident,
                proxy=self.my_osid_object._proxy
            )
            cqs = rm.get_composition_query_session_for_repository(
                run_repo.ident,
                proxy=self.my_osid_object._proxy
            )
            cas = rm.get_composition_admin_session_for_repository(
                run_repo.ident,
                proxy=self.my_osid_object._proxy
            )
            cras = rm.get_composition_repository_assignment_session(proxy=self.my_osid_object._proxy)
            crs = rm.get_composition_repository_session(proxy=self.my_osid_object._proxy)
            acs = rm.get_asset_composition_session_for_repository(user_repo.ident,
                                                                  proxy=self.my_osid_object._proxy)
            aas = rm.get_asset_admin_session_for_repository(user_repo.ident,
                                                            proxy=self.my_osid_object._proxy)
            assessment_as = am.get_assessment_admin_session_for_bank(user_bank.ident,
                                                                     proxy=self.my_osid_object._proxy)
            abas = am.get_assessment_basic_authoring_session_for_bank(user_bank.ident,
                                                                      proxy=self.my_osid_object._proxy)
            ias = am.get_item_admin_session_for_bank(user_bank.ident,
                                                     proxy=self.my_osid_object._proxy)
            aqs = am.get_assessment_query_session_for_bank(user_bank.ident,
                                                           proxy=self.my_osid_object._proxy)

        cls.use_unsequestered_composition_view()
        cls.use_federated_repository_view()
        cqs.use_unsequestered_composition_view()
        cqs.use_federated_repository_view()
        acs.use_federated_repository_view()
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

        if self.my_osid_object._proxy is None:
            ras = rm.get_repository_admin_session()
        else:
            ras = rm.get_repository_admin_session(proxy=self.my_osid_object._proxy)
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
        self.add_text(str(grading_policy), 'gradingPolicy')

    def clear_grading_policy(self):
        self.clear_text('gradingPolicy')
