"""Unit tests of repository objects."""


import pytest


from ..utilities.general import is_never_authz, is_no_authz, uses_cataloging, uses_filesystem_only
from dlkit.abstract_osid.id.primitives import Id as ABC_Id
from dlkit.abstract_osid.locale.primitives import DisplayText as ABC_DisplayText
from dlkit.abstract_osid.osid import errors
from dlkit.abstract_osid.osid.objects import OsidCatalog
from dlkit.abstract_osid.repository import objects as ABCObjects
from dlkit.json_.id.objects import IdList
from dlkit.json_.osid.metadata import Metadata
from dlkit.primordium.calendaring.primitives import DateTime, Duration
from dlkit.primordium.id.primitives import Id
from dlkit.primordium.locale.primitives import DisplayText
from dlkit.primordium.type.primitives import Type
from dlkit.runtime import PROXY_SESSION, proxy_example
from dlkit.runtime.managers import Runtime


REQUEST = proxy_example.SimpleRequest()
CONDITION = PROXY_SESSION.get_proxy_condition()
CONDITION.set_http_request(REQUEST)
PROXY = PROXY_SESSION.get_proxy(CONDITION)

DEFAULT_TYPE = Type(**{'identifier': 'DEFAULT', 'namespace': 'DEFAULT', 'authority': 'DEFAULT'})


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def asset_class_fixture(request):
    # From test_templates/resource.py::Resource::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'REPOSITORY',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_repository_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        request.cls.catalog = request.cls.svc_mgr.create_repository(create_form)

        form = request.cls.catalog.get_asset_form_for_create([])
        form.display_name = 'Test object'
        request.cls.object = request.cls.catalog.create_asset(form)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_assets():
                request.cls.catalog.delete_asset(obj.ident)
            request.cls.svc_mgr.delete_repository(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def asset_test_fixture(request):
    pass


@pytest.mark.usefixtures("asset_class_fixture", "asset_test_fixture")
class TestAsset(object):
    """Tests for Asset"""
    def test_get_title(self):
        """Tests get_title"""
        # From test_templates/repository.py::Asset::get_title_template
        result = self.object.get_title()
        assert isinstance(result, DisplayText)
        assert result.text == ''

    def test_is_copyright_status_known(self):
        """Tests is_copyright_status_known"""
        # From test_templates/resources.py::Resource::is_group_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.object.is_copyright_status_known(), bool)

    def test_is_public_domain(self):
        """Tests is_public_domain"""
        # From test_templates/resources.py::Resource::is_group_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.object.is_public_domain(), bool)

    def test_get_copyright(self):
        """Tests get_copyright"""
        # From test_templates/repository.py::Asset::get_title_template
        result = self.object.get_copyright()
        assert isinstance(result, DisplayText)
        assert result.text == ''

    def test_get_copyright_registration(self):
        """Tests get_copyright_registration"""
        # From test_templates/repository.py::AssetContent::get_url_template
        if not is_never_authz(self.service_config):
            with pytest.raises(errors.IllegalState):
                self.object.get_copyright_registration()

    def test_can_distribute_verbatim(self):
        """Tests can_distribute_verbatim"""
        with pytest.raises(errors.IllegalState):
            self.object.can_distribute_verbatim()

    def test_can_distribute_alterations(self):
        """Tests can_distribute_alterations"""
        with pytest.raises(errors.IllegalState):
            self.object.can_distribute_alterations()

    def test_can_distribute_compositions(self):
        """Tests can_distribute_compositions"""
        with pytest.raises(errors.IllegalState):
            self.object.can_distribute_compositions()

    def test_get_source_id(self):
        """Tests get_source_id"""
        # From test_templates/resources.py::Resource::get_avatar_id_template
        if not is_never_authz(self.service_config):
            pytest.raises(errors.IllegalState,
                          self.object.get_source_id)

    def test_get_source(self):
        """Tests get_source"""
        # From test_templates/resources.py::Resource::get_avatar_template
        if not is_never_authz(self.service_config):
            pytest.raises(errors.IllegalState,
                          self.object.get_source)

    def test_get_provider_link_ids(self):
        """Tests get_provider_link_ids"""
        # From test_templates/learning.py::Activity::get_asset_ids_template
        if not is_never_authz(self.service_config):
            result = self.object.get_provider_link_ids()
            assert isinstance(result, IdList)
            assert result.available() == 0

    def test_get_provider_links(self):
        """Tests get_provider_links"""
        # Override because no providerLinkIds
        with pytest.raises(errors.IllegalState):
            self.object.get_provider_links()

    def test_get_created_date(self):
        """Tests get_created_date"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.object.get_created_date()

    def test_is_published(self):
        """Tests is_published"""
        # From test_templates/resources.py::Resource::is_group_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.object.is_published(), bool)

    def test_get_published_date(self):
        """Tests get_published_date"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.object.get_published_date()

    def test_get_principal_credit_string(self):
        """Tests get_principal_credit_string"""
        # From test_templates/repository.py::Asset::get_title_template
        result = self.object.get_principal_credit_string()
        assert isinstance(result, DisplayText)
        assert result.text == ''

    def test_get_asset_content_ids(self):
        """Tests get_asset_content_ids"""
        results = self.object.get_asset_content_ids()
        assert isinstance(results, IdList)

    def test_get_asset_contents(self):
        """Tests get_asset_contents"""
        results = self.object.get_asset_contents()
        assert isinstance(results, ABCObjects.AssetContentList)

    def test_is_composition(self):
        """Tests is_composition"""
        result = self.object.is_composition()
        assert isinstance(result, bool)

    def test_get_composition_id(self):
        """Tests get_composition_id"""
        with pytest.raises(errors.IllegalState):
            self.object.get_composition_id()

    def test_get_composition(self):
        """Tests get_composition"""
        with pytest.raises(errors.IllegalState):
            self.object.get_composition()

    def test_get_asset_record(self):
        """Tests get_asset_record"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unsupported):
                self.object.get_asset_record(True)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def asset_form_class_fixture(request):
    # From test_templates/resource.py::ResourceForm::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'REPOSITORY',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_repository_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        request.cls.catalog = request.cls.svc_mgr.create_repository(create_form)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.svc_mgr.delete_repository(request.cls.catalog.ident)


@pytest.fixture(scope="function")
def asset_form_test_fixture(request):
    # From test_templates/resource.py::ResourceForm::init_template
    if not is_never_authz(request.cls.service_config):
        request.cls.form = request.cls.catalog.get_asset_form_for_create([])


@pytest.mark.usefixtures("asset_form_class_fixture", "asset_form_test_fixture")
class TestAssetForm(object):
    """Tests for AssetForm"""
    def test_get_title_metadata(self):
        """Tests get_title_metadata"""
        # From test_templates/resource.py::ResourceForm::get_group_metadata_template
        mdata = self.form.get_title_metadata()
        assert isinstance(mdata, Metadata)
        assert isinstance(mdata.get_element_id(), ABC_Id)
        assert isinstance(mdata.get_element_label(), ABC_DisplayText)
        assert isinstance(mdata.get_instructions(), ABC_DisplayText)
        assert mdata.get_syntax() == 'STRING'
        assert not mdata.is_array()
        assert isinstance(mdata.is_required(), bool)
        assert isinstance(mdata.is_read_only(), bool)
        assert isinstance(mdata.is_linked(), bool)

    def test_set_title(self):
        """Tests set_title"""
        # From test_templates/repository.py::AssetForm::set_title_template
        default_value = self.form.get_title_metadata().get_default_string_values()[0]
        assert self.form._my_map['title'] == default_value
        self.form.set_title('String')
        assert self.form._my_map['title']['text'] == 'String'
        with pytest.raises(errors.InvalidArgument):
            self.form.set_title(42)

    def test_clear_title(self):
        """Tests clear_title"""
        # From test_templates/repository.py::AssetForm::clear_title_template
        self.form.set_title('A String to Clear')
        assert self.form._my_map['title']['text'] == 'A String to Clear'
        self.form.clear_title()
        assert self.form._my_map['title'] == self.form.get_title_metadata().get_default_string_values()[0]

    def test_get_public_domain_metadata(self):
        """Tests get_public_domain_metadata"""
        # From test_templates/resource.py::ResourceForm::get_group_metadata_template
        mdata = self.form.get_public_domain_metadata()
        assert isinstance(mdata, Metadata)
        assert isinstance(mdata.get_element_id(), ABC_Id)
        assert isinstance(mdata.get_element_label(), ABC_DisplayText)
        assert isinstance(mdata.get_instructions(), ABC_DisplayText)
        assert mdata.get_syntax() == 'BOOLEAN'
        assert not mdata.is_array()
        assert isinstance(mdata.is_required(), bool)
        assert isinstance(mdata.is_read_only(), bool)
        assert isinstance(mdata.is_linked(), bool)

    def test_set_public_domain(self):
        """Tests set_public_domain"""
        # From test_templates/resource.py::ResourceForm::set_group_template
        self.form.set_public_domain(True)
        assert self.form._my_map['publicDomain']
        with pytest.raises(errors.InvalidArgument):
            self.form.set_public_domain('false')

    def test_clear_public_domain(self):
        """Tests clear_public_domain"""
        # From test_templates/resource.py::ResourceForm::clear_group_template
        self.form.set_public_domain(True)
        assert self.form._my_map['publicDomain']
        self.form.clear_public_domain()
        assert self.form._my_map['publicDomain'] is None

    def test_get_copyright_metadata(self):
        """Tests get_copyright_metadata"""
        # From test_templates/resource.py::ResourceForm::get_group_metadata_template
        mdata = self.form.get_copyright_metadata()
        assert isinstance(mdata, Metadata)
        assert isinstance(mdata.get_element_id(), ABC_Id)
        assert isinstance(mdata.get_element_label(), ABC_DisplayText)
        assert isinstance(mdata.get_instructions(), ABC_DisplayText)
        assert mdata.get_syntax() == 'STRING'
        assert not mdata.is_array()
        assert isinstance(mdata.is_required(), bool)
        assert isinstance(mdata.is_read_only(), bool)
        assert isinstance(mdata.is_linked(), bool)

    def test_set_copyright(self):
        """Tests set_copyright"""
        # From test_templates/repository.py::AssetForm::set_title_template
        default_value = self.form.get_copyright_metadata().get_default_string_values()[0]
        assert self.form._my_map['copyright'] == default_value
        self.form.set_copyright('String')
        assert self.form._my_map['copyright']['text'] == 'String'
        with pytest.raises(errors.InvalidArgument):
            self.form.set_copyright(42)

    def test_clear_copyright(self):
        """Tests clear_copyright"""
        # From test_templates/repository.py::AssetForm::clear_title_template
        self.form.set_copyright('A String to Clear')
        assert self.form._my_map['copyright']['text'] == 'A String to Clear'
        self.form.clear_copyright()
        assert self.form._my_map['copyright'] == self.form.get_copyright_metadata().get_default_string_values()[0]

    def test_get_copyright_registration_metadata(self):
        """Tests get_copyright_registration_metadata"""
        # From test_templates/resource.py::ResourceForm::get_group_metadata_template
        mdata = self.form.get_copyright_registration_metadata()
        assert isinstance(mdata, Metadata)
        assert isinstance(mdata.get_element_id(), ABC_Id)
        assert isinstance(mdata.get_element_label(), ABC_DisplayText)
        assert isinstance(mdata.get_instructions(), ABC_DisplayText)
        assert mdata.get_syntax() == 'STRING'
        assert not mdata.is_array()
        assert isinstance(mdata.is_required(), bool)
        assert isinstance(mdata.is_read_only(), bool)
        assert isinstance(mdata.is_linked(), bool)

    def test_set_copyright_registration(self):
        """Tests set_copyright_registration"""
        # From test_templates/repository.py::AssetContentForm::set_url_template
        default_value = self.form.get_copyright_registration_metadata().get_default_string_values()[0]
        assert self.form._my_map['copyrightRegistration'] == default_value
        self.form.set_copyright_registration('String')
        assert self.form._my_map['copyrightRegistration'] == 'String'
        with pytest.raises(errors.InvalidArgument):
            self.form.set_copyright_registration(42)

    def test_clear_copyright_registration(self):
        """Tests clear_copyright_registration"""
        # From test_templates/repository.py::AssetContentForm::clear_url_template
        self.form.set_copyright_registration('A String to Clear')
        assert self.form._my_map['copyrightRegistration'] == 'A String to Clear'
        self.form.clear_copyright_registration()
        assert self.form._my_map['copyrightRegistration'] == self.form.get_copyright_registration_metadata().get_default_string_values()[0]

    def test_get_distribute_verbatim_metadata(self):
        """Tests get_distribute_verbatim_metadata"""
        # From test_templates/resource.py::ResourceForm::get_group_metadata_template
        mdata = self.form.get_distribute_verbatim_metadata()
        assert isinstance(mdata, Metadata)
        assert isinstance(mdata.get_element_id(), ABC_Id)
        assert isinstance(mdata.get_element_label(), ABC_DisplayText)
        assert isinstance(mdata.get_instructions(), ABC_DisplayText)
        assert mdata.get_syntax() == 'BOOLEAN'
        assert not mdata.is_array()
        assert isinstance(mdata.is_required(), bool)
        assert isinstance(mdata.is_read_only(), bool)
        assert isinstance(mdata.is_linked(), bool)

    def test_set_distribute_verbatim(self):
        """Tests set_distribute_verbatim"""
        # From test_templates/resource.py::ResourceForm::set_group_template
        self.form.set_distribute_verbatim(True)
        assert self.form._my_map['distributeVerbatim']
        with pytest.raises(errors.InvalidArgument):
            self.form.set_distribute_verbatim('false')

    def test_clear_distribute_verbatim(self):
        """Tests clear_distribute_verbatim"""
        # From test_templates/resource.py::ResourceForm::clear_group_template
        self.form.set_distribute_verbatim(True)
        assert self.form._my_map['distributeVerbatim']
        self.form.clear_distribute_verbatim()
        assert self.form._my_map['distributeVerbatim'] is None

    def test_get_distribute_alterations_metadata(self):
        """Tests get_distribute_alterations_metadata"""
        # From test_templates/resource.py::ResourceForm::get_group_metadata_template
        mdata = self.form.get_distribute_alterations_metadata()
        assert isinstance(mdata, Metadata)
        assert isinstance(mdata.get_element_id(), ABC_Id)
        assert isinstance(mdata.get_element_label(), ABC_DisplayText)
        assert isinstance(mdata.get_instructions(), ABC_DisplayText)
        assert mdata.get_syntax() == 'BOOLEAN'
        assert not mdata.is_array()
        assert isinstance(mdata.is_required(), bool)
        assert isinstance(mdata.is_read_only(), bool)
        assert isinstance(mdata.is_linked(), bool)

    def test_set_distribute_alterations(self):
        """Tests set_distribute_alterations"""
        # From test_templates/resource.py::ResourceForm::set_group_template
        self.form.set_distribute_alterations(True)
        assert self.form._my_map['distributeAlterations']
        with pytest.raises(errors.InvalidArgument):
            self.form.set_distribute_alterations('false')

    def test_clear_distribute_alterations(self):
        """Tests clear_distribute_alterations"""
        # From test_templates/resource.py::ResourceForm::clear_group_template
        self.form.set_distribute_alterations(True)
        assert self.form._my_map['distributeAlterations']
        self.form.clear_distribute_alterations()
        assert self.form._my_map['distributeAlterations'] is None

    def test_get_distribute_compositions_metadata(self):
        """Tests get_distribute_compositions_metadata"""
        # From test_templates/resource.py::ResourceForm::get_group_metadata_template
        mdata = self.form.get_distribute_compositions_metadata()
        assert isinstance(mdata, Metadata)
        assert isinstance(mdata.get_element_id(), ABC_Id)
        assert isinstance(mdata.get_element_label(), ABC_DisplayText)
        assert isinstance(mdata.get_instructions(), ABC_DisplayText)
        assert mdata.get_syntax() == 'BOOLEAN'
        assert not mdata.is_array()
        assert isinstance(mdata.is_required(), bool)
        assert isinstance(mdata.is_read_only(), bool)
        assert isinstance(mdata.is_linked(), bool)

    def test_set_distribute_compositions(self):
        """Tests set_distribute_compositions"""
        # From test_templates/resource.py::ResourceForm::set_group_template
        self.form.set_distribute_compositions(True)
        assert self.form._my_map['distributeCompositions']
        with pytest.raises(errors.InvalidArgument):
            self.form.set_distribute_compositions('false')

    def test_clear_distribute_compositions(self):
        """Tests clear_distribute_compositions"""
        # From test_templates/resource.py::ResourceForm::clear_group_template
        self.form.set_distribute_compositions(True)
        assert self.form._my_map['distributeCompositions']
        self.form.clear_distribute_compositions()
        assert self.form._my_map['distributeCompositions'] is None

    def test_get_source_metadata(self):
        """Tests get_source_metadata"""
        # From test_templates/resource.py::ResourceForm::get_avatar_metadata_template
        mdata = self.form.get_source_metadata()
        assert isinstance(mdata, Metadata)
        assert isinstance(mdata.get_element_id(), ABC_Id)
        assert isinstance(mdata.get_element_label(), ABC_DisplayText)
        assert isinstance(mdata.get_instructions(), ABC_DisplayText)
        assert mdata.get_syntax() == 'ID'
        assert not mdata.is_array()
        assert isinstance(mdata.is_required(), bool)
        assert isinstance(mdata.is_read_only(), bool)
        assert isinstance(mdata.is_linked(), bool)

    def test_set_source(self):
        """Tests set_source"""
        # From test_templates/resource.py::ResourceForm::set_avatar_template
        assert self.form._my_map['sourceId'] == ''
        self.form.set_source(Id('repository.Asset%3Afake-id%40ODL.MIT.EDU'))
        assert self.form._my_map['sourceId'] == 'repository.Asset%3Afake-id%40ODL.MIT.EDU'
        with pytest.raises(errors.InvalidArgument):
            self.form.set_source(True)

    def test_clear_source(self):
        """Tests clear_source"""
        # From test_templates/resource.py::ResourceForm::clear_avatar_template
        self.form.set_source(Id('repository.Asset%3Afake-id%40ODL.MIT.EDU'))
        assert self.form._my_map['sourceId'] == 'repository.Asset%3Afake-id%40ODL.MIT.EDU'
        self.form.clear_source()
        assert self.form._my_map['sourceId'] == self.form.get_source_metadata().get_default_id_values()[0]

    def test_get_provider_links_metadata(self):
        """Tests get_provider_links_metadata"""
        # From test_templates/learning.py::ActivityForm::get_assets_metadata_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.form.get_provider_links_metadata(), Metadata)

    def test_set_provider_links(self):
        """Tests set_provider_links"""
        # From test_templates/learning.py::ActivityForm::set_assets_template
        if not is_never_authz(self.service_config):
            test_id = Id('osid.Osid%3A1%40ODL.MIT.EDU')
            self.form.set_provider_links([test_id])
            assert len(self.form._my_map['providerLinkIds']) == 1
            assert self.form._my_map['providerLinkIds'][0] == str(test_id)
            with pytest.raises(errors.InvalidArgument):
                self.form.set_provider_links('this is not a list')
            # reset this for other tests
            self.form._my_map['providerLinkIds'] = list()

    def test_clear_provider_links(self):
        """Tests clear_provider_links"""
        # From test_templates/learning.py::ActivityForm::clear_assets_template
        if not is_never_authz(self.service_config):
            test_id = Id('osid.Osid%3A1%40ODL.MIT.EDU')
            self.form.set_provider_links([test_id])
            assert len(self.form._my_map['providerLinkIds']) == 1
            assert self.form._my_map['providerLinkIds'][0] == str(test_id)
            self.form.clear_provider_links()
            assert self.form._my_map['providerLinkIds'] == []

    def test_get_created_date_metadata(self):
        """Tests get_created_date_metadata"""
        # From test_templates/resource.py::ResourceForm::get_group_metadata_template
        mdata = self.form.get_created_date_metadata()
        assert isinstance(mdata, Metadata)
        assert isinstance(mdata.get_element_id(), ABC_Id)
        assert isinstance(mdata.get_element_label(), ABC_DisplayText)
        assert isinstance(mdata.get_instructions(), ABC_DisplayText)
        assert mdata.get_syntax() == 'DATETIME'
        assert not mdata.is_array()
        assert isinstance(mdata.is_required(), bool)
        assert isinstance(mdata.is_read_only(), bool)
        assert isinstance(mdata.is_linked(), bool)

    def test_set_created_date(self):
        """Tests set_created_date"""
        # From test_templates/assessment.py::AssessmentOfferedForm::set_start_time_template
        if not is_never_authz(self.service_config):
            test_time = DateTime.utcnow()
            assert self.form._my_map['createdDate'] is None
            self.form.set_created_date(test_time)
            assert self.form._my_map['createdDate'] == test_time
            with pytest.raises(errors.InvalidArgument):
                self.form.set_created_date(True)
            # reset this for other tests
            self.form._my_map['createdDate'] = None

    def test_clear_created_date(self):
        """Tests clear_created_date"""
        # From test_templates/assessment.py::AssessmentOfferedForm::clear_start_time_template
        if not is_never_authz(self.service_config):
            test_time = DateTime.utcnow()
            assert self.form._my_map['createdDate'] is None
            self.form.set_created_date(test_time)
            assert self.form._my_map['createdDate'] == test_time
            self.form.clear_created_date()
            assert self.form._my_map['createdDate'] == self.form.get_created_date_metadata().get_default_date_time_values()[0]

    def test_get_published_metadata(self):
        """Tests get_published_metadata"""
        # From test_templates/resource.py::ResourceForm::get_group_metadata_template
        mdata = self.form.get_published_metadata()
        assert isinstance(mdata, Metadata)
        assert isinstance(mdata.get_element_id(), ABC_Id)
        assert isinstance(mdata.get_element_label(), ABC_DisplayText)
        assert isinstance(mdata.get_instructions(), ABC_DisplayText)
        assert mdata.get_syntax() == 'BOOLEAN'
        assert not mdata.is_array()
        assert isinstance(mdata.is_required(), bool)
        assert isinstance(mdata.is_read_only(), bool)
        assert isinstance(mdata.is_linked(), bool)

    def test_set_published(self):
        """Tests set_published"""
        # From test_templates/resource.py::ResourceForm::set_group_template
        self.form.set_published(True)
        assert self.form._my_map['published']
        with pytest.raises(errors.InvalidArgument):
            self.form.set_published('false')

    def test_clear_published(self):
        """Tests clear_published"""
        # From test_templates/resource.py::ResourceForm::clear_group_template
        self.form.set_published(True)
        assert self.form._my_map['published']
        self.form.clear_published()
        assert self.form._my_map['published'] is None

    def test_get_published_date_metadata(self):
        """Tests get_published_date_metadata"""
        # From test_templates/resource.py::ResourceForm::get_group_metadata_template
        mdata = self.form.get_published_date_metadata()
        assert isinstance(mdata, Metadata)
        assert isinstance(mdata.get_element_id(), ABC_Id)
        assert isinstance(mdata.get_element_label(), ABC_DisplayText)
        assert isinstance(mdata.get_instructions(), ABC_DisplayText)
        assert mdata.get_syntax() == 'DATETIME'
        assert not mdata.is_array()
        assert isinstance(mdata.is_required(), bool)
        assert isinstance(mdata.is_read_only(), bool)
        assert isinstance(mdata.is_linked(), bool)

    def test_set_published_date(self):
        """Tests set_published_date"""
        # From test_templates/assessment.py::AssessmentOfferedForm::set_start_time_template
        if not is_never_authz(self.service_config):
            test_time = DateTime.utcnow()
            assert self.form._my_map['publishedDate'] is None
            self.form.set_published_date(test_time)
            assert self.form._my_map['publishedDate'] == test_time
            with pytest.raises(errors.InvalidArgument):
                self.form.set_published_date(True)
            # reset this for other tests
            self.form._my_map['publishedDate'] = None

    def test_clear_published_date(self):
        """Tests clear_published_date"""
        # From test_templates/assessment.py::AssessmentOfferedForm::clear_start_time_template
        if not is_never_authz(self.service_config):
            test_time = DateTime.utcnow()
            assert self.form._my_map['publishedDate'] is None
            self.form.set_published_date(test_time)
            assert self.form._my_map['publishedDate'] == test_time
            self.form.clear_published_date()
            assert self.form._my_map['publishedDate'] == self.form.get_published_date_metadata().get_default_date_time_values()[0]

    def test_get_principal_credit_string_metadata(self):
        """Tests get_principal_credit_string_metadata"""
        # From test_templates/resource.py::ResourceForm::get_group_metadata_template
        mdata = self.form.get_principal_credit_string_metadata()
        assert isinstance(mdata, Metadata)
        assert isinstance(mdata.get_element_id(), ABC_Id)
        assert isinstance(mdata.get_element_label(), ABC_DisplayText)
        assert isinstance(mdata.get_instructions(), ABC_DisplayText)
        assert mdata.get_syntax() == 'STRING'
        assert not mdata.is_array()
        assert isinstance(mdata.is_required(), bool)
        assert isinstance(mdata.is_read_only(), bool)
        assert isinstance(mdata.is_linked(), bool)

    def test_set_principal_credit_string(self):
        """Tests set_principal_credit_string"""
        # From test_templates/repository.py::AssetForm::set_title_template
        default_value = self.form.get_principal_credit_string_metadata().get_default_string_values()[0]
        assert self.form._my_map['principalCreditString'] == default_value
        self.form.set_principal_credit_string('String')
        assert self.form._my_map['principalCreditString']['text'] == 'String'
        with pytest.raises(errors.InvalidArgument):
            self.form.set_principal_credit_string(42)

    def test_clear_principal_credit_string(self):
        """Tests clear_principal_credit_string"""
        # From test_templates/repository.py::AssetForm::clear_title_template
        self.form.set_principal_credit_string('A String to Clear')
        assert self.form._my_map['principalCreditString']['text'] == 'A String to Clear'
        self.form.clear_principal_credit_string()
        assert self.form._my_map['principalCreditString'] == self.form.get_principal_credit_string_metadata().get_default_string_values()[0]

    def test_get_composition_metadata(self):
        """Tests get_composition_metadata"""
        # From test_templates/resource.py::ResourceForm::get_avatar_metadata_template
        mdata = self.form.get_composition_metadata()
        assert isinstance(mdata, Metadata)
        assert isinstance(mdata.get_element_id(), ABC_Id)
        assert isinstance(mdata.get_element_label(), ABC_DisplayText)
        assert isinstance(mdata.get_instructions(), ABC_DisplayText)
        assert mdata.get_syntax() == 'ID'
        assert not mdata.is_array()
        assert isinstance(mdata.is_required(), bool)
        assert isinstance(mdata.is_read_only(), bool)
        assert isinstance(mdata.is_linked(), bool)

    def test_set_composition(self):
        """Tests set_composition"""
        # From test_templates/resource.py::ResourceForm::set_avatar_template
        assert self.form._my_map['compositionId'] == ''
        self.form.set_composition(Id('repository.Asset%3Afake-id%40ODL.MIT.EDU'))
        assert self.form._my_map['compositionId'] == 'repository.Asset%3Afake-id%40ODL.MIT.EDU'
        with pytest.raises(errors.InvalidArgument):
            self.form.set_composition(True)

    def test_clear_composition(self):
        """Tests clear_composition"""
        # From test_templates/resource.py::ResourceForm::clear_avatar_template
        self.form.set_composition(Id('repository.Asset%3Afake-id%40ODL.MIT.EDU'))
        assert self.form._my_map['compositionId'] == 'repository.Asset%3Afake-id%40ODL.MIT.EDU'
        self.form.clear_composition()
        assert self.form._my_map['compositionId'] == self.form.get_composition_metadata().get_default_id_values()[0]

    def test_get_asset_form_record(self):
        """Tests get_asset_form_record"""
        with pytest.raises(errors.Unsupported):
            self.form.get_asset_form_record(Type('osid.Osid%3Afake-record%40ODL.MIT.EDU'))
        # Here check for a real record?


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def asset_list_class_fixture(request):
    # Implemented from init template for ResourceList
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'REPOSITORY',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_repository_form_for_create([])
        create_form.display_name = 'Test Repository'
        create_form.description = 'Test Repository for AssetList tests'
        request.cls.catalog = request.cls.svc_mgr.create_repository(create_form)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_assets():
                request.cls.catalog.delete_asset(obj.ident)
            request.cls.svc_mgr.delete_repository(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def asset_list_test_fixture(request):
    # Implemented from init template for ResourceList
    from dlkit.json_.repository.objects import AssetList
    request.cls.asset_list = list()
    request.cls.asset_ids = list()
    if not is_never_authz(request.cls.service_config):
        for num in [0, 1]:
            create_form = request.cls.catalog.get_asset_form_for_create([])
            create_form.display_name = 'Test Asset ' + str(num)
            create_form.description = 'Test Asset for AssetList tests'
            obj = request.cls.catalog.create_asset(create_form)
            request.cls.asset_list.append(obj)
            request.cls.asset_ids.append(obj.ident)
    request.cls.asset_list = AssetList(request.cls.asset_list)
    request.cls.object = request.cls.asset_list


@pytest.mark.usefixtures("asset_list_class_fixture", "asset_list_test_fixture")
class TestAssetList(object):
    """Tests for AssetList"""
    def test_get_next_asset(self):
        """Tests get_next_asset"""
        # From test_templates/resource.py::ResourceList::get_next_resource_template
        from dlkit.abstract_osid.repository.objects import Asset
        if not is_never_authz(self.service_config):
            assert isinstance(self.asset_list.get_next_asset(), Asset)

    def test_get_next_assets(self):
        """Tests get_next_assets"""
        # From test_templates/resource.py::ResourceList::get_next_resources_template
        from dlkit.abstract_osid.repository.objects import AssetList, Asset
        if not is_never_authz(self.service_config):
            new_list = self.asset_list.get_next_assets(2)
            assert isinstance(new_list, AssetList)
            for item in new_list:
                assert isinstance(item, Asset)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def asset_content_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'REPOSITORY',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_repository_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        request.cls.catalog = request.cls.svc_mgr.create_repository(create_form)

        form = request.cls.catalog.get_asset_form_for_create([])
        form.display_name = 'Asset'
        request.cls.asset = request.cls.catalog.create_asset(form)

        form = request.cls.catalog.get_asset_content_form_for_create(request.cls.asset.ident,
                                                                     [])
        form.display_name = 'Test asset content'
        form.set_url('https://www.google.com')
        request.cls.object = request.cls.catalog.create_asset_content(form)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_assets():
                request.cls.catalog.delete_asset(obj.ident)
            request.cls.svc_mgr.delete_repository(request.cls.catalog.ident)
        request.cls.object = None
        request.cls.catalog = None

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def asset_content_test_fixture(request):
    pass


@pytest.mark.usefixtures("asset_content_class_fixture", "asset_content_test_fixture")
class TestAssetContent(object):
    """Tests for AssetContent"""
    def test_get_asset_id(self):
        """Tests get_asset_id"""
        # From test_templates/learning.py::Activity::get_objective_id_template
        if not is_never_authz(self.service_config):
            result = self.object.get_asset_id()
            assert isinstance(result, Id)
            assert str(result) == str(self.asset.ident)

    def test_get_asset(self):
        """Tests get_asset"""
        # From test_templates/learning.py::Activity::get_objective_template
        if not is_never_authz(self.service_config):
            result = self.object.get_asset()
            assert isinstance(result, ABCObjects.Asset)
            assert str(result.ident) == str(self.asset.ident)

    def test_get_accessibility_types(self):
        """Tests get_accessibility_types"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.object.get_accessibility_types()

    def test_has_data_length(self):
        """Tests has_data_length"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.object.has_data_length()

    def test_get_data_length(self):
        """Tests get_data_length"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.object.get_data_length()

    def test_get_data(self):
        """Tests get_data"""
        if not is_never_authz(self.service_config):
            with pytest.raises(errors.IllegalState):
                self.object.get_data()

    def test_has_url(self):
        """Tests has_url"""
        # From test_templates/repository.py::AssetContent::has_url_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.object.has_url(), bool)

    def test_get_url(self):
        """Tests get_url"""
        if not is_never_authz(self.service_config):
            result = self.object.get_url()
            assert result == 'https://www.google.com'

    def test_get_asset_content_record(self):
        """Tests get_asset_content_record"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unsupported):
                self.object.get_asset_content_record(True)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def asset_content_form_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'REPOSITORY',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_repository_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        request.cls.catalog = request.cls.svc_mgr.create_repository(create_form)

        form = request.cls.catalog.get_asset_form_for_create([])
        form.display_name = 'Asset'
        request.cls.asset = request.cls.catalog.create_asset(form)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_assets():
                request.cls.catalog.delete_asset(obj.ident)
            request.cls.svc_mgr.delete_repository(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def asset_content_form_test_fixture(request):
    if not is_never_authz(request.cls.service_config):
        request.cls.form = request.cls.catalog.get_asset_content_form_for_create(request.cls.asset.ident,
                                                                                 [])
    request.cls.object = request.cls.form


@pytest.mark.usefixtures("asset_content_form_class_fixture", "asset_content_form_test_fixture")
class TestAssetContentForm(object):
    """Tests for AssetContentForm"""
    def test_get_accessibility_type_metadata(self):
        """Tests get_accessibility_type_metadata"""
        # From test_templates/logging.py::LogEntryForm::get_priority_metadata_template
        mdata = self.form.get_accessibility_type_metadata()
        assert isinstance(mdata, Metadata)
        assert isinstance(mdata.get_element_id(), ABC_Id)
        assert isinstance(mdata.get_element_label(), ABC_DisplayText)
        assert isinstance(mdata.get_instructions(), ABC_DisplayText)
        assert mdata.get_syntax() == 'TYPE'
        assert not mdata.is_array()
        assert isinstance(mdata.is_required(), bool)
        assert isinstance(mdata.is_read_only(), bool)
        assert isinstance(mdata.is_linked(), bool)

    def test_add_accessibility_type(self):
        """Tests add_accessibility_type"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.object.add_accessibility_type(True)

    def test_remove_accessibility_type(self):
        """Tests remove_accessibility_type"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.object.remove_accessibility_type(True)

    def test_clear_accessibility_types(self):
        """Tests clear_accessibility_types"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.object.clear_accessibility_types()

    def test_get_data_metadata(self):
        """Tests get_data_metadata"""
        # From test_templates/resource.py::ResourceForm::get_group_metadata_template
        mdata = self.form.get_data_metadata()
        assert isinstance(mdata, Metadata)
        assert isinstance(mdata.get_element_id(), ABC_Id)
        assert isinstance(mdata.get_element_label(), ABC_DisplayText)
        assert isinstance(mdata.get_instructions(), ABC_DisplayText)
        assert mdata.get_syntax() == 'OBJECT'
        assert not mdata.is_array()
        assert isinstance(mdata.is_required(), bool)
        assert isinstance(mdata.is_read_only(), bool)
        assert isinstance(mdata.is_linked(), bool)

    def test_set_data(self):
        """Tests set_data"""
        with pytest.raises(errors.InvalidArgument):
            self.form.set_data('foo')
        # TODO: should test setting actual data...

    def test_clear_data(self):
        """Tests clear_data"""
        self.form.clear_data()

    def test_get_url_metadata(self):
        """Tests get_url_metadata"""
        # From test_templates/resource.py::ResourceForm::get_group_metadata_template
        mdata = self.form.get_url_metadata()
        assert isinstance(mdata, Metadata)
        assert isinstance(mdata.get_element_id(), ABC_Id)
        assert isinstance(mdata.get_element_label(), ABC_DisplayText)
        assert isinstance(mdata.get_instructions(), ABC_DisplayText)
        assert mdata.get_syntax() == 'STRING'
        assert not mdata.is_array()
        assert isinstance(mdata.is_required(), bool)
        assert isinstance(mdata.is_read_only(), bool)
        assert isinstance(mdata.is_linked(), bool)

    def test_set_url(self):
        """Tests set_url"""
        # From test_templates/repository.py::AssetContentForm::set_url_template
        default_value = self.form.get_url_metadata().get_default_string_values()[0]
        assert self.form._my_map['url'] == default_value
        self.form.set_url('String')
        assert self.form._my_map['url'] == 'String'
        with pytest.raises(errors.InvalidArgument):
            self.form.set_url(42)

    def test_clear_url(self):
        """Tests clear_url"""
        # From test_templates/repository.py::AssetContentForm::clear_url_template
        self.form.set_url('A String to Clear')
        assert self.form._my_map['url'] == 'A String to Clear'
        self.form.clear_url()
        assert self.form._my_map['url'] == self.form.get_url_metadata().get_default_string_values()[0]

    def test_get_asset_content_form_record(self):
        """Tests get_asset_content_form_record"""
        with pytest.raises(errors.Unsupported):
            self.form.get_asset_content_form_record(Type('osid.Osid%3Afake-record%40ODL.MIT.EDU'))
        # Here check for a real record?


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def asset_content_list_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'REPOSITORY',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_repository_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        request.cls.catalog = request.cls.svc_mgr.create_repository(create_form)

        form = request.cls.catalog.get_asset_form_for_create([])
        form.display_name = 'Asset'
        request.cls.asset = request.cls.catalog.create_asset(form)

        request.cls.form = request.cls.catalog.get_asset_content_form_for_create(request.cls.asset.ident,
                                                                                 [])

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_assets():
                request.cls.catalog.delete_asset(obj.ident)
            request.cls.svc_mgr.delete_repository(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def asset_content_list_test_fixture(request):
    from dlkit.json_.repository.objects import AssetContentList
    request.cls.asset_content_list = list()
    request.cls.asset_content_ids = list()
    if not is_never_authz(request.cls.service_config):
        for num in [0, 1]:
            form = request.cls.catalog.get_asset_content_form_for_create(request.cls.asset.ident,
                                                                         [])
            form.display_name = 'Test AssetContent ' + str(num)
            form.description = 'Test AssetContent for AssetContentList tests'
            obj = request.cls.catalog.create_asset_content(form)

            request.cls.asset_content_list.append(obj)
            request.cls.asset_content_ids.append(obj.ident)
    request.cls.asset_content_list = AssetContentList(request.cls.asset_content_list)


@pytest.mark.usefixtures("asset_content_list_class_fixture", "asset_content_list_test_fixture")
class TestAssetContentList(object):
    """Tests for AssetContentList"""
    def test_get_next_asset_content(self):
        """Tests get_next_asset_content"""
        # From test_templates/resource.py::ResourceList::get_next_resource_template
        from dlkit.abstract_osid.repository.objects import AssetContent
        if not is_never_authz(self.service_config):
            assert isinstance(self.asset_content_list.get_next_asset_content(), AssetContent)

    def test_get_next_asset_contents(self):
        """Tests get_next_asset_contents"""
        # From test_templates/resource.py::ResourceList::get_next_resources_template
        from dlkit.abstract_osid.repository.objects import AssetContentList, AssetContent
        if not is_never_authz(self.service_config):
            new_list = self.asset_content_list.get_next_asset_contents(2)
            assert isinstance(new_list, AssetContentList)
            for item in new_list:
                assert isinstance(item, AssetContent)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def composition_class_fixture(request):
    # From test_templates/resource.py::Resource::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'REPOSITORY',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_repository_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        request.cls.catalog = request.cls.svc_mgr.create_repository(create_form)

        form = request.cls.catalog.get_composition_form_for_create([])
        form.display_name = 'Test object'
        request.cls.object = request.cls.catalog.create_composition(form)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_compositions():
                request.cls.catalog.delete_composition(obj.ident)
            request.cls.svc_mgr.delete_repository(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def composition_test_fixture(request):
    pass


@pytest.mark.usefixtures("composition_class_fixture", "composition_test_fixture")
class TestComposition(object):
    """Tests for Composition"""
    def test_get_children_ids(self):
        """Tests get_children_ids"""
        # From test_templates/learning.py::Activity::get_asset_ids_template
        if not is_never_authz(self.service_config):
            result = self.object.get_children_ids()
            assert isinstance(result, IdList)
            assert result.available() == 0

    def test_get_children(self):
        """Tests get_children"""
        with pytest.raises(errors.IllegalState):
            self.object.get_children()

    def test_get_composition_record(self):
        """Tests get_composition_record"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unsupported):
                self.object.get_composition_record(True)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def composition_form_class_fixture(request):
    # From test_templates/resource.py::ResourceForm::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'REPOSITORY',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_repository_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        request.cls.catalog = request.cls.svc_mgr.create_repository(create_form)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.svc_mgr.delete_repository(request.cls.catalog.ident)


@pytest.fixture(scope="function")
def composition_form_test_fixture(request):
    # From test_templates/resource.py::ResourceForm::init_template
    if not is_never_authz(request.cls.service_config):
        request.cls.form = request.cls.catalog.get_composition_form_for_create([])


@pytest.mark.usefixtures("composition_form_class_fixture", "composition_form_test_fixture")
class TestCompositionForm(object):
    """Tests for CompositionForm"""
    def test_get_composition_form_record(self):
        """Tests get_composition_form_record"""
        with pytest.raises(errors.Unsupported):
            self.form.get_composition_form_record(Type('osid.Osid%3Afake-record%40ODL.MIT.EDU'))
        # Here check for a real record?


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def composition_list_class_fixture(request):
    # Implemented from init template for ResourceList
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'REPOSITORY',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_repository_form_for_create([])
        create_form.display_name = 'Test Repository'
        create_form.description = 'Test Repository for CompositionList tests'
        request.cls.catalog = request.cls.svc_mgr.create_repository(create_form)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_compositions():
                request.cls.catalog.delete_composition(obj.ident)
            request.cls.svc_mgr.delete_repository(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def composition_list_test_fixture(request):
    # Implemented from init template for ResourceList
    from dlkit.json_.repository.objects import CompositionList
    request.cls.composition_list = list()
    request.cls.composition_ids = list()
    if not is_never_authz(request.cls.service_config):
        for num in [0, 1]:
            create_form = request.cls.catalog.get_composition_form_for_create([])
            create_form.display_name = 'Test Composition ' + str(num)
            create_form.description = 'Test Composition for CompositionList tests'
            obj = request.cls.catalog.create_composition(create_form)
            request.cls.composition_list.append(obj)
            request.cls.composition_ids.append(obj.ident)
    request.cls.composition_list = CompositionList(request.cls.composition_list)
    request.cls.object = request.cls.composition_list


@pytest.mark.usefixtures("composition_list_class_fixture", "composition_list_test_fixture")
class TestCompositionList(object):
    """Tests for CompositionList"""
    def test_get_next_composition(self):
        """Tests get_next_composition"""
        # From test_templates/resource.py::ResourceList::get_next_resource_template
        from dlkit.abstract_osid.repository.objects import Composition
        if not is_never_authz(self.service_config):
            assert isinstance(self.composition_list.get_next_composition(), Composition)

    def test_get_next_compositions(self):
        """Tests get_next_compositions"""
        # From test_templates/resource.py::ResourceList::get_next_resources_template
        from dlkit.abstract_osid.repository.objects import CompositionList, Composition
        if not is_never_authz(self.service_config):
            new_list = self.composition_list.get_next_compositions(2)
            assert isinstance(new_list, CompositionList)
            for item in new_list:
                assert isinstance(item, Composition)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def repository_class_fixture(request):
    # From test_templates/resource.py::Bin::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'REPOSITORY',
        proxy=PROXY,
        implementation=request.cls.service_config)

    def class_tear_down():
        pass

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def repository_test_fixture(request):
    # From test_templates/resource.py::Bin::init_template
    if not is_never_authz(request.cls.service_config):
        form = request.cls.svc_mgr.get_repository_form_for_create([])
        form.display_name = 'for testing'
        request.cls.object = request.cls.svc_mgr.create_repository(form)

    def test_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.svc_mgr.delete_repository(request.cls.object.ident)

    request.addfinalizer(test_tear_down)


@pytest.mark.usefixtures("repository_class_fixture", "repository_test_fixture")
class TestRepository(object):
    """Tests for Repository"""
    def test_get_repository_record(self):
        """Tests get_repository_record"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.object.get_repository_record(True)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def repository_form_class_fixture(request):
    # From test_templates/resource.py::BinForm::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'REPOSITORY',
        proxy=PROXY,
        implementation=request.cls.service_config)

    def class_tear_down():
        pass

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def repository_form_test_fixture(request):
    # From test_templates/resource.py::BinForm::init_template
    if not is_never_authz(request.cls.service_config):
        request.cls.object = request.cls.svc_mgr.get_repository_form_for_create([])

    def test_tear_down():
        pass

    request.addfinalizer(test_tear_down)


@pytest.mark.usefixtures("repository_form_class_fixture", "repository_form_test_fixture")
class TestRepositoryForm(object):
    """Tests for RepositoryForm"""
    def test_get_repository_form_record(self):
        """Tests get_repository_form_record"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.object.get_repository_form_record(True)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def repository_list_class_fixture(request):
    # Implemented from init template for BinList
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'REPOSITORY',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_repository_form_for_create([])
        create_form.display_name = 'Test Repository'
        create_form.description = 'Test Repository for RepositoryList tests'
        request.cls.catalog = request.cls.svc_mgr.create_repository(create_form)
        request.cls.repository_ids = list()

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.repository_ids:
                request.cls.svc_mgr.delete_repository(obj)
            request.cls.svc_mgr.delete_repository(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def repository_list_test_fixture(request):
    # Implemented from init template for BinList
    from dlkit.json_.repository.objects import RepositoryList
    request.cls.repository_list = list()
    if not is_never_authz(request.cls.service_config):
        for num in [0, 1]:
            create_form = request.cls.svc_mgr.get_repository_form_for_create([])
            create_form.display_name = 'Test Repository ' + str(num)
            create_form.description = 'Test Repository for RepositoryList tests'
            obj = request.cls.svc_mgr.create_repository(create_form)
            request.cls.repository_list.append(obj)
            request.cls.repository_ids.append(obj.ident)
    request.cls.repository_list = RepositoryList(request.cls.repository_list)


@pytest.mark.usefixtures("repository_list_class_fixture", "repository_list_test_fixture")
class TestRepositoryList(object):
    """Tests for RepositoryList"""
    def test_get_next_repository(self):
        """Tests get_next_repository"""
        # From test_templates/resource.py::ResourceList::get_next_resource_template
        from dlkit.abstract_osid.repository.objects import Repository
        if not is_never_authz(self.service_config):
            assert isinstance(self.repository_list.get_next_repository(), Repository)

    def test_get_next_repositories(self):
        """Tests get_next_repositories"""
        # From test_templates/resource.py::ResourceList::get_next_resources_template
        from dlkit.abstract_osid.repository.objects import RepositoryList, Repository
        if not is_never_authz(self.service_config):
            new_list = self.repository_list.get_next_repositories(2)
            assert isinstance(new_list, RepositoryList)
            for item in new_list:
                assert isinstance(item, Repository)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def repository_node_class_fixture(request):
    # Implemented from init template for BinNode
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'REPOSITORY',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_repository_form_for_create([])
        create_form.display_name = 'Test Repository'
        create_form.description = 'Test Repository for RepositoryNode tests'
        request.cls.catalog = request.cls.svc_mgr.create_repository(create_form)
        request.cls.repository_ids = list()

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.svc_mgr.delete_repository(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def repository_node_test_fixture(request):
    # Implemented from init template for BinNode
    from dlkit.json_.repository.objects import RepositoryNode
    request.cls.repository_list = list()
    if not is_never_authz(request.cls.service_config):
        for num in [0, 1]:
            create_form = request.cls.svc_mgr.get_repository_form_for_create([])
            create_form.display_name = 'Test Repository ' + str(num)
            create_form.description = 'Test Repository for RepositoryNode tests'
            obj = request.cls.svc_mgr.create_repository(create_form)
            request.cls.repository_list.append(RepositoryNode(
                obj.object_map,
                runtime=request.cls.svc_mgr._runtime,
                proxy=request.cls.svc_mgr._proxy))
            request.cls.repository_ids.append(obj.ident)
        # Not put the catalogs in a hierarchy
        request.cls.svc_mgr.add_root_repository(request.cls.repository_list[0].ident)
        request.cls.svc_mgr.add_child_repository(
            request.cls.repository_list[0].ident,
            request.cls.repository_list[1].ident)

        request.cls.object = request.cls.svc_mgr.get_repository_nodes(
            request.cls.repository_list[0].ident, 0, 5, False)

    def test_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.svc_mgr.remove_child_repository(
                request.cls.repository_list[0].ident,
                request.cls.repository_list[1].ident)
            request.cls.svc_mgr.remove_root_repository(request.cls.repository_list[0].ident)
            for node in request.cls.repository_list:
                request.cls.svc_mgr.delete_repository(node.ident)

    request.addfinalizer(test_tear_down)


@pytest.mark.usefixtures("repository_node_class_fixture", "repository_node_test_fixture")
class TestRepositoryNode(object):
    """Tests for RepositoryNode"""
    def test_get_repository(self):
        """Tests get_repository"""
        # from test_templates/resource.py::BinNode::get_bin_template
        from dlkit.abstract_osid.repository.objects import Repository
        if not is_never_authz(self.service_config):
            assert isinstance(self.repository_list[0].get_repository(), OsidCatalog)
            assert str(self.repository_list[0].get_repository().ident) == str(self.repository_list[0].ident)

    def test_get_parent_repository_nodes(self):
        """Tests get_parent_repository_nodes"""
        # from test_templates/resource.py::BinNode::get_parent_bin_nodes
        from dlkit.abstract_osid.repository.objects import RepositoryNodeList
        if not is_never_authz(self.service_config):
            node = self.svc_mgr.get_repository_nodes(
                self.repository_list[1].ident,
                1,
                0,
                False)
            assert isinstance(node.get_parent_repository_nodes(), RepositoryNodeList)
            assert node.get_parent_repository_nodes().available() == 1
            assert str(node.get_parent_repository_nodes().next().ident) == str(self.repository_list[0].ident)

    def test_get_child_repository_nodes(self):
        """Tests get_child_repository_nodes"""
        # from test_templates/resource.py::BinNode::get_child_bin_nodes_template
        from dlkit.abstract_osid.repository.objects import RepositoryNodeList
        if not is_never_authz(self.service_config):
            node = self.svc_mgr.get_repository_nodes(
                self.repository_list[0].ident,
                0,
                1,
                False)
            assert isinstance(node.get_child_repository_nodes(), RepositoryNodeList)
            assert node.get_child_repository_nodes().available() == 1
            assert str(node.get_child_repository_nodes().next().ident) == str(self.repository_list[1].ident)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def repository_node_list_class_fixture(request):
    # Implemented from init template for BinNodeList
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'REPOSITORY',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_repository_form_for_create([])
        create_form.display_name = 'Test Repository'
        create_form.description = 'Test Repository for RepositoryNodeList tests'
        request.cls.catalog = request.cls.svc_mgr.create_repository(create_form)
        request.cls.repository_node_ids = list()

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.repository_node_ids:
                request.cls.svc_mgr.delete_repository(obj)
            request.cls.svc_mgr.delete_repository(request.cls.catalog.ident)


@pytest.fixture(scope="function")
def repository_node_list_test_fixture(request):
    # Implemented from init template for BinNodeList
    from dlkit.json_.repository.objects import RepositoryNodeList, RepositoryNode
    request.cls.repository_node_list = list()
    if not is_never_authz(request.cls.service_config):
        for num in [0, 1]:
            create_form = request.cls.svc_mgr.get_repository_form_for_create([])
            create_form.display_name = 'Test RepositoryNode ' + str(num)
            create_form.description = 'Test RepositoryNode for RepositoryNodeList tests'
            obj = request.cls.svc_mgr.create_repository(create_form)
            request.cls.repository_node_list.append(RepositoryNode(obj.object_map))
            request.cls.repository_node_ids.append(obj.ident)
        # Not put the catalogs in a hierarchy
        request.cls.svc_mgr.add_root_repository(request.cls.repository_node_list[0].ident)
        request.cls.svc_mgr.add_child_repository(
            request.cls.repository_node_list[0].ident,
            request.cls.repository_node_list[1].ident)
    request.cls.repository_node_list = RepositoryNodeList(request.cls.repository_node_list)


@pytest.mark.usefixtures("repository_node_list_class_fixture", "repository_node_list_test_fixture")
class TestRepositoryNodeList(object):
    """Tests for RepositoryNodeList"""
    def test_get_next_repository_node(self):
        """Tests get_next_repository_node"""
        # From test_templates/resource.py::ResourceList::get_next_resource_template
        from dlkit.abstract_osid.repository.objects import RepositoryNode
        if not is_never_authz(self.service_config):
            assert isinstance(self.repository_node_list.get_next_repository_node(), RepositoryNode)

    def test_get_next_repository_nodes(self):
        """Tests get_next_repository_nodes"""
        # From test_templates/resource.py::ResourceList::get_next_resources_template
        from dlkit.abstract_osid.repository.objects import RepositoryNodeList, RepositoryNode
        if not is_never_authz(self.service_config):
            new_list = self.repository_node_list.get_next_repository_nodes(2)
            assert isinstance(new_list, RepositoryNodeList)
            for item in new_list:
                assert isinstance(item, RepositoryNode)
