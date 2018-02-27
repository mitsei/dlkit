"""Unit tests of learning objects."""


import pytest


from ..utilities.general import is_never_authz, is_no_authz, uses_cataloging, uses_filesystem_only
from dlkit.abstract_osid.id.primitives import Id as ABC_Id
from dlkit.abstract_osid.learning import objects as ABCObjects
from dlkit.abstract_osid.learning.objects import Objective
from dlkit.abstract_osid.locale.primitives import DisplayText as ABC_DisplayText
from dlkit.abstract_osid.osid import errors
from dlkit.abstract_osid.osid.objects import OsidCatalog
from dlkit.json_.id.objects import IdList
from dlkit.json_.osid.metadata import Metadata
from dlkit.primordium.id.primitives import Id
from dlkit.primordium.type.primitives import Type
from dlkit.runtime import PROXY_SESSION, proxy_example
from dlkit.runtime.managers import Runtime


REQUEST = proxy_example.SimpleRequest()
CONDITION = PROXY_SESSION.get_proxy_condition()
CONDITION.set_http_request(REQUEST)
PROXY = PROXY_SESSION.get_proxy(CONDITION)

DEFAULT_TYPE = Type(**{'identifier': 'DEFAULT', 'namespace': 'DEFAULT', 'authority': 'DEFAULT'})
AGENT_ID = Id(**{'identifier': 'jane_doe', 'namespace': 'osid.agent.Agent', 'authority': 'MIT-ODL'})


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def objective_class_fixture(request):
    # From test_templates/resource.py::Resource::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'LEARNING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_objective_bank_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        request.cls.catalog = request.cls.svc_mgr.create_objective_bank(create_form)

        form = request.cls.catalog.get_objective_form_for_create([])
        form.display_name = 'Test object'
        request.cls.object = request.cls.catalog.create_objective(form)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_objectives():
                request.cls.catalog.delete_objective(obj.ident)
            request.cls.svc_mgr.delete_objective_bank(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def objective_test_fixture(request):
    pass


@pytest.mark.usefixtures("objective_class_fixture", "objective_test_fixture")
class TestObjective(object):
    """Tests for Objective"""
    def test_has_assessment(self):
        """Tests has_assessment"""
        # From test_templates/resources.py::Resource::has_avatar_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.object.has_assessment(), bool)

    def test_get_assessment_id(self):
        """Tests get_assessment_id"""
        # From test_templates/resources.py::Resource::get_avatar_id_template
        if not is_never_authz(self.service_config):
            pytest.raises(errors.IllegalState,
                          self.object.get_assessment_id)

    def test_get_assessment(self):
        """Tests get_assessment"""
        # From test_templates/resources.py::Resource::get_avatar_template
        if not is_never_authz(self.service_config):
            pytest.raises(errors.IllegalState,
                          self.object.get_assessment)

    def test_has_knowledge_category(self):
        """Tests has_knowledge_category"""
        # From test_templates/resources.py::Resource::has_avatar_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.object.has_knowledge_category(), bool)

    def test_get_knowledge_category_id(self):
        """Tests get_knowledge_category_id"""
        # From test_templates/resources.py::Resource::get_avatar_id_template
        if not is_never_authz(self.service_config):
            pytest.raises(errors.IllegalState,
                          self.object.get_knowledge_category_id)

    def test_get_knowledge_category(self):
        """Tests get_knowledge_category"""
        # From test_templates/resources.py::Resource::get_avatar_template
        if not is_never_authz(self.service_config):
            pytest.raises(errors.IllegalState,
                          self.object.get_knowledge_category)

    def test_has_cognitive_process(self):
        """Tests has_cognitive_process"""
        # From test_templates/resources.py::Resource::has_avatar_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.object.has_cognitive_process(), bool)

    def test_get_cognitive_process_id(self):
        """Tests get_cognitive_process_id"""
        # From test_templates/resources.py::Resource::get_avatar_id_template
        if not is_never_authz(self.service_config):
            pytest.raises(errors.IllegalState,
                          self.object.get_cognitive_process_id)

    def test_get_cognitive_process(self):
        """Tests get_cognitive_process"""
        # From test_templates/resources.py::Resource::get_avatar_template
        if not is_never_authz(self.service_config):
            pytest.raises(errors.IllegalState,
                          self.object.get_cognitive_process)

    def test_get_objective_record(self):
        """Tests get_objective_record"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unsupported):
                self.object.get_objective_record(True)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def objective_form_class_fixture(request):
    # From test_templates/resource.py::ResourceForm::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'LEARNING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_objective_bank_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        request.cls.catalog = request.cls.svc_mgr.create_objective_bank(create_form)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.svc_mgr.delete_objective_bank(request.cls.catalog.ident)


@pytest.fixture(scope="function")
def objective_form_test_fixture(request):
    # From test_templates/resource.py::ResourceForm::init_template
    if not is_never_authz(request.cls.service_config):
        request.cls.form = request.cls.catalog.get_objective_form_for_create([])


@pytest.mark.usefixtures("objective_form_class_fixture", "objective_form_test_fixture")
class TestObjectiveForm(object):
    """Tests for ObjectiveForm"""
    def test_get_assessment_metadata(self):
        """Tests get_assessment_metadata"""
        # From test_templates/resource.py::ResourceForm::get_avatar_metadata_template
        mdata = self.form.get_assessment_metadata()
        assert isinstance(mdata, Metadata)
        assert isinstance(mdata.get_element_id(), ABC_Id)
        assert isinstance(mdata.get_element_label(), ABC_DisplayText)
        assert isinstance(mdata.get_instructions(), ABC_DisplayText)
        assert mdata.get_syntax() == 'ID'
        assert not mdata.is_array()
        assert isinstance(mdata.is_required(), bool)
        assert isinstance(mdata.is_read_only(), bool)
        assert isinstance(mdata.is_linked(), bool)

    def test_set_assessment(self):
        """Tests set_assessment"""
        # From test_templates/resource.py::ResourceForm::set_avatar_template
        assert self.form._my_map['assessmentId'] == ''
        self.form.set_assessment(Id('repository.Asset%3Afake-id%40ODL.MIT.EDU'))
        assert self.form._my_map['assessmentId'] == 'repository.Asset%3Afake-id%40ODL.MIT.EDU'
        with pytest.raises(errors.InvalidArgument):
            self.form.set_assessment(True)

    def test_clear_assessment(self):
        """Tests clear_assessment"""
        # From test_templates/resource.py::ResourceForm::clear_avatar_template
        self.form.set_assessment(Id('repository.Asset%3Afake-id%40ODL.MIT.EDU'))
        assert self.form._my_map['assessmentId'] == 'repository.Asset%3Afake-id%40ODL.MIT.EDU'
        self.form.clear_assessment()
        assert self.form._my_map['assessmentId'] == self.form.get_assessment_metadata().get_default_id_values()[0]

    def test_get_knowledge_category_metadata(self):
        """Tests get_knowledge_category_metadata"""
        # From test_templates/resource.py::ResourceForm::get_avatar_metadata_template
        mdata = self.form.get_knowledge_category_metadata()
        assert isinstance(mdata, Metadata)
        assert isinstance(mdata.get_element_id(), ABC_Id)
        assert isinstance(mdata.get_element_label(), ABC_DisplayText)
        assert isinstance(mdata.get_instructions(), ABC_DisplayText)
        assert mdata.get_syntax() == 'ID'
        assert not mdata.is_array()
        assert isinstance(mdata.is_required(), bool)
        assert isinstance(mdata.is_read_only(), bool)
        assert isinstance(mdata.is_linked(), bool)

    def test_set_knowledge_category(self):
        """Tests set_knowledge_category"""
        # From test_templates/resource.py::ResourceForm::set_avatar_template
        assert self.form._my_map['knowledgeCategoryId'] == ''
        self.form.set_knowledge_category(Id('repository.Asset%3Afake-id%40ODL.MIT.EDU'))
        assert self.form._my_map['knowledgeCategoryId'] == 'repository.Asset%3Afake-id%40ODL.MIT.EDU'
        with pytest.raises(errors.InvalidArgument):
            self.form.set_knowledge_category(True)

    def test_clear_knowledge_category(self):
        """Tests clear_knowledge_category"""
        # From test_templates/resource.py::ResourceForm::clear_avatar_template
        self.form.set_knowledge_category(Id('repository.Asset%3Afake-id%40ODL.MIT.EDU'))
        assert self.form._my_map['knowledgeCategoryId'] == 'repository.Asset%3Afake-id%40ODL.MIT.EDU'
        self.form.clear_knowledge_category()
        assert self.form._my_map['knowledgeCategoryId'] == self.form.get_knowledge_category_metadata().get_default_id_values()[0]

    def test_get_cognitive_process_metadata(self):
        """Tests get_cognitive_process_metadata"""
        # From test_templates/resource.py::ResourceForm::get_avatar_metadata_template
        mdata = self.form.get_cognitive_process_metadata()
        assert isinstance(mdata, Metadata)
        assert isinstance(mdata.get_element_id(), ABC_Id)
        assert isinstance(mdata.get_element_label(), ABC_DisplayText)
        assert isinstance(mdata.get_instructions(), ABC_DisplayText)
        assert mdata.get_syntax() == 'ID'
        assert not mdata.is_array()
        assert isinstance(mdata.is_required(), bool)
        assert isinstance(mdata.is_read_only(), bool)
        assert isinstance(mdata.is_linked(), bool)

    def test_set_cognitive_process(self):
        """Tests set_cognitive_process"""
        # From test_templates/resource.py::ResourceForm::set_avatar_template
        assert self.form._my_map['cognitiveProcessId'] == ''
        self.form.set_cognitive_process(Id('repository.Asset%3Afake-id%40ODL.MIT.EDU'))
        assert self.form._my_map['cognitiveProcessId'] == 'repository.Asset%3Afake-id%40ODL.MIT.EDU'
        with pytest.raises(errors.InvalidArgument):
            self.form.set_cognitive_process(True)

    def test_clear_cognitive_process(self):
        """Tests clear_cognitive_process"""
        # From test_templates/resource.py::ResourceForm::clear_avatar_template
        self.form.set_cognitive_process(Id('repository.Asset%3Afake-id%40ODL.MIT.EDU'))
        assert self.form._my_map['cognitiveProcessId'] == 'repository.Asset%3Afake-id%40ODL.MIT.EDU'
        self.form.clear_cognitive_process()
        assert self.form._my_map['cognitiveProcessId'] == self.form.get_cognitive_process_metadata().get_default_id_values()[0]

    def test_get_objective_form_record(self):
        """Tests get_objective_form_record"""
        with pytest.raises(errors.Unsupported):
            self.form.get_objective_form_record(Type('osid.Osid%3Afake-record%40ODL.MIT.EDU'))
        # Here check for a real record?


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def objective_list_class_fixture(request):
    # Implemented from init template for ResourceList
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'LEARNING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_objective_bank_form_for_create([])
        create_form.display_name = 'Test ObjectiveBank'
        create_form.description = 'Test ObjectiveBank for ObjectiveList tests'
        request.cls.catalog = request.cls.svc_mgr.create_objective_bank(create_form)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_objectives():
                request.cls.catalog.delete_objective(obj.ident)
            request.cls.svc_mgr.delete_objective_bank(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def objective_list_test_fixture(request):
    # Implemented from init template for ResourceList
    from dlkit.json_.learning.objects import ObjectiveList
    request.cls.objective_list = list()
    request.cls.objective_ids = list()
    if not is_never_authz(request.cls.service_config):
        for num in [0, 1]:
            create_form = request.cls.catalog.get_objective_form_for_create([])
            create_form.display_name = 'Test Objective ' + str(num)
            create_form.description = 'Test Objective for ObjectiveList tests'
            obj = request.cls.catalog.create_objective(create_form)
            request.cls.objective_list.append(obj)
            request.cls.objective_ids.append(obj.ident)
    request.cls.objective_list = ObjectiveList(request.cls.objective_list)
    request.cls.object = request.cls.objective_list


@pytest.mark.usefixtures("objective_list_class_fixture", "objective_list_test_fixture")
class TestObjectiveList(object):
    """Tests for ObjectiveList"""
    def test_get_next_objective(self):
        """Tests get_next_objective"""
        # From test_templates/resource.py::ResourceList::get_next_resource_template
        from dlkit.abstract_osid.learning.objects import Objective
        if not is_never_authz(self.service_config):
            assert isinstance(self.objective_list.get_next_objective(), Objective)

    def test_get_next_objectives(self):
        """Tests get_next_objectives"""
        # From test_templates/resource.py::ResourceList::get_next_resources_template
        from dlkit.abstract_osid.learning.objects import ObjectiveList, Objective
        if not is_never_authz(self.service_config):
            new_list = self.objective_list.get_next_objectives(2)
            assert isinstance(new_list, ObjectiveList)
            for item in new_list:
                assert isinstance(item, Objective)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def objective_node_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'LEARNING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_objective_bank_form_for_create([])
        create_form.display_name = 'Test ObjectiveBank'
        create_form.description = 'Test ObjectiveBank for ObjectiveNode tests'
        request.cls.catalog = request.cls.svc_mgr.create_objective_bank(create_form)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_objectives():
                request.cls.catalog.delete_objective(obj.ident)
            request.cls.svc_mgr.delete_objective_bank(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def objective_node_test_fixture(request):
    from dlkit.json_.learning.objects import ObjectiveNode
    request.cls.objective_node_list = list()
    if not is_never_authz(request.cls.service_config):
        for num in [0, 1]:
            create_form = request.cls.catalog.get_objective_form_for_create([])
            create_form.display_name = 'Test Objective ' + str(num)
            create_form.description = 'Test Objective for ObjectiveNodeList tests'
            obj = request.cls.catalog.create_objective(create_form)
            request.cls.objective_node_list.append(ObjectiveNode(obj.object_map))
        # Now put the objectives in a hierarchy
        request.cls.catalog.add_root_objective(request.cls.objective_node_list[0].ident)
        request.cls.catalog.add_child_objective(
            request.cls.objective_node_list[0].ident,
            request.cls.objective_node_list[1].ident)
        request.cls.object = ObjectiveNode(request.cls.objective_node_list[0])


@pytest.mark.usefixtures("objective_node_class_fixture", "objective_node_test_fixture")
class TestObjectiveNode(object):
    """Tests for ObjectiveNode"""
    def test_get_objective(self):
        """Tests get_objective"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.object.get_objective()

    def test_get_parent_objective_nodes(self):
        """Tests get_parent_objective_nodes"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.object.get_parent_objective_nodes()

    def test_get_child_objective_nodes(self):
        """Tests get_child_objective_nodes"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.object.get_child_objective_nodes()


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def objective_node_list_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'LEARNING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_objective_bank_form_for_create([])
        create_form.display_name = 'Test ObjectiveBank'
        create_form.description = 'Test ObjectiveBank for ObjectiveNodeList tests'
        request.cls.catalog = request.cls.svc_mgr.create_objective_bank(create_form)

    request.cls.objective_node_ids = list()

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_objectives():
                request.cls.catalog.delete_objective(obj.ident)
            request.cls.svc_mgr.delete_objective_bank(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def objective_node_list_test_fixture(request):
    from dlkit.json_.learning.objects import ObjectiveNodeList, ObjectiveNode
    request.cls.objective_node_list = list()
    if not is_never_authz(request.cls.service_config):
        for num in [0, 1]:
            create_form = request.cls.catalog.get_objective_form_for_create([])
            create_form.display_name = 'Test Objective ' + str(num)
            create_form.description = 'Test Objective for ObjectiveNodeList tests'
            obj = request.cls.catalog.create_objective(create_form)
            request.cls.objective_node_list.append(ObjectiveNode(obj.object_map))
            request.cls.objective_node_ids.append(obj.ident)
        # Not put the objectives in a hierarchy
        request.cls.catalog.add_root_objective(request.cls.objective_node_list[0].ident)
        request.cls.catalog.add_child_objective(
            request.cls.objective_node_list[0].ident,
            request.cls.objective_node_list[1].ident)
    request.cls.objective_node_list = ObjectiveNodeList(request.cls.objective_node_list)


@pytest.mark.usefixtures("objective_node_list_class_fixture", "objective_node_list_test_fixture")
class TestObjectiveNodeList(object):
    """Tests for ObjectiveNodeList"""
    def test_get_next_objective_node(self):
        """Tests get_next_objective_node"""
        # From test_templates/resource.py::ResourceList::get_next_resource_template
        from dlkit.abstract_osid.learning.objects import ObjectiveNode
        if not is_never_authz(self.service_config):
            assert isinstance(self.objective_node_list.get_next_objective_node(), ObjectiveNode)

    def test_get_next_objective_nodes(self):
        """Tests get_next_objective_nodes"""
        # From test_templates/resource.py::ResourceList::get_next_resources_template
        from dlkit.abstract_osid.learning.objects import ObjectiveNodeList, ObjectiveNode
        if not is_never_authz(self.service_config):
            new_list = self.objective_node_list.get_next_objective_nodes(2)
            assert isinstance(new_list, ObjectiveNodeList)
            for item in new_list:
                assert isinstance(item, ObjectiveNode)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def activity_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'LEARNING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_objective_bank_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        request.cls.catalog = request.cls.svc_mgr.create_objective_bank(create_form)

        form = request.cls.catalog.get_objective_form_for_create([])
        form.display_name = 'Objective'
        request.cls.objective = request.cls.catalog.create_objective(form)

        form = request.cls.catalog.get_activity_form_for_create(request.cls.objective.ident,
                                                                [])
        form.display_name = 'Test activity'
        request.cls.object = request.cls.catalog.create_activity(form)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_activities():
                request.cls.catalog.delete_activity(obj.ident)
            request.cls.catalog.delete_objective(request.cls.objective.ident)
            request.cls.svc_mgr.delete_objective_bank(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def activity_test_fixture(request):
    pass


@pytest.mark.usefixtures("activity_class_fixture", "activity_test_fixture")
class TestActivity(object):
    """Tests for Activity"""
    def test_get_objective_id(self):
        """Tests get_objective_id"""
        # From test_templates/learning.py::Activity::get_objective_id_template
        if not is_never_authz(self.service_config):
            result = self.object.get_objective_id()
            assert isinstance(result, Id)
            assert str(result) == str(self.objective.ident)

    def test_get_objective(self):
        """Tests get_objective"""
        # From test_templates/learning.py::Activity::get_objective_template
        if not is_never_authz(self.service_config):
            result = self.object.get_objective()
            assert isinstance(result, ABCObjects.Objective)
            assert str(result.ident) == str(self.objective.ident)

    def test_is_asset_based_activity(self):
        """Tests is_asset_based_activity"""
        # From test_templates/resources.py::Resource::is_group_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.object.is_asset_based_activity(), bool)

    def test_get_asset_ids(self):
        """Tests get_asset_ids"""
        # From test_templates/learning.py::Activity::get_asset_ids_template
        if not is_never_authz(self.service_config):
            result = self.object.get_asset_ids()
            assert isinstance(result, IdList)
            assert result.available() == 0

    def test_get_assets(self):
        """Tests get_assets"""
        # From test_templates/learning.py::Activity::get_assets_template
        if not is_never_authz(self.service_config):
            with pytest.raises(errors.IllegalState):
                self.object.get_assets()

    def test_is_course_based_activity(self):
        """Tests is_course_based_activity"""
        # From test_templates/resources.py::Resource::is_group_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.object.is_course_based_activity(), bool)

    def test_get_course_ids(self):
        """Tests get_course_ids"""
        if not is_never_authz(self.service_config):
            result = self.object.get_course_ids()
            assert isinstance(result, IdList)
            assert result.available() == 0

    def test_get_courses(self):
        """Tests get_courses"""
        if not is_never_authz(self.service_config):
            # We don't have the course service yet
            with pytest.raises(errors.IllegalState):
                self.object.get_courses()

    def test_is_assessment_based_activity(self):
        """Tests is_assessment_based_activity"""
        # From test_templates/resources.py::Resource::is_group_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.object.is_assessment_based_activity(), bool)

    def test_get_assessment_ids(self):
        """Tests get_assessment_ids"""
        if not is_never_authz(self.service_config):
            result = self.object.get_assessment_ids()
            assert isinstance(result, IdList)
            assert result.available() == 0

    def test_get_assessments(self):
        """Tests get_assessments"""
        if not is_never_authz(self.service_config):
            with pytest.raises(errors.IllegalState):
                self.object.get_assessments()

    def test_get_activity_record(self):
        """Tests get_activity_record"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unsupported):
                self.object.get_activity_record(True)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def activity_form_class_fixture(request):
    # From test_templates/learning.py::ActivityForm::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'LEARNING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_objective_bank_form_for_create([])
        create_form.display_name = 'Test ObjectiveBank'
        create_form.description = 'Test ObjectiveBank for ActivityForm tests'
        request.cls.catalog = request.cls.svc_mgr.create_objective_bank(create_form)
        create_form = request.cls.catalog.get_objective_form_for_create([])
        create_form.display_name = 'Test Objective for Activity Lookup'
        create_form.description = 'Test Objective for ActivityForm tests'
        request.cls.objective = request.cls.catalog.create_objective(create_form)

        request.cls.form = request.cls.catalog.get_activity_form_for_create(request.cls.objective.ident, [])

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for catalog in request.cls.svc_mgr.get_objective_banks():
                for obj in catalog.get_activities():
                    catalog.delete_activity(obj.ident)
                for obj in catalog.get_objectives():
                    catalog.delete_objective(obj.ident)
                request.cls.svc_mgr.delete_objective_bank(catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def activity_form_test_fixture(request):
    pass


@pytest.mark.usefixtures("activity_form_class_fixture", "activity_form_test_fixture")
class TestActivityForm(object):
    """Tests for ActivityForm"""
    def test_get_assets_metadata(self):
        """Tests get_assets_metadata"""
        # From test_templates/learning.py::ActivityForm::get_assets_metadata_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.form.get_assets_metadata(), Metadata)

    def test_set_assets(self):
        """Tests set_assets"""
        # From test_templates/learning.py::ActivityForm::set_assets_template
        if not is_never_authz(self.service_config):
            test_id = Id('osid.Osid%3A1%40ODL.MIT.EDU')
            self.form.set_assets([test_id])
            assert len(self.form._my_map['assetIds']) == 1
            assert self.form._my_map['assetIds'][0] == str(test_id)
            with pytest.raises(errors.InvalidArgument):
                self.form.set_assets('this is not a list')
            # reset this for other tests
            self.form._my_map['assetIds'] = list()

    def test_clear_assets(self):
        """Tests clear_assets"""
        # From test_templates/learning.py::ActivityForm::clear_assets_template
        if not is_never_authz(self.service_config):
            test_id = Id('osid.Osid%3A1%40ODL.MIT.EDU')
            self.form.set_assets([test_id])
            assert len(self.form._my_map['assetIds']) == 1
            assert self.form._my_map['assetIds'][0] == str(test_id)
            self.form.clear_assets()
            assert self.form._my_map['assetIds'] == []

    def test_get_courses_metadata(self):
        """Tests get_courses_metadata"""
        # From test_templates/learning.py::ActivityForm::get_assets_metadata_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.form.get_courses_metadata(), Metadata)

    def test_set_courses(self):
        """Tests set_courses"""
        # From test_templates/learning.py::ActivityForm::set_assets_template
        if not is_never_authz(self.service_config):
            test_id = Id('osid.Osid%3A1%40ODL.MIT.EDU')
            self.form.set_courses([test_id])
            assert len(self.form._my_map['courseIds']) == 1
            assert self.form._my_map['courseIds'][0] == str(test_id)
            with pytest.raises(errors.InvalidArgument):
                self.form.set_courses('this is not a list')
            # reset this for other tests
            self.form._my_map['courseIds'] = list()

    def test_clear_courses(self):
        """Tests clear_courses"""
        # From test_templates/learning.py::ActivityForm::clear_assets_template
        if not is_never_authz(self.service_config):
            test_id = Id('osid.Osid%3A1%40ODL.MIT.EDU')
            self.form.set_courses([test_id])
            assert len(self.form._my_map['courseIds']) == 1
            assert self.form._my_map['courseIds'][0] == str(test_id)
            self.form.clear_courses()
            assert self.form._my_map['courseIds'] == []

    def test_get_assessments_metadata(self):
        """Tests get_assessments_metadata"""
        # From test_templates/learning.py::ActivityForm::get_assets_metadata_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.form.get_assessments_metadata(), Metadata)

    def test_set_assessments(self):
        """Tests set_assessments"""
        # From test_templates/learning.py::ActivityForm::set_assets_template
        if not is_never_authz(self.service_config):
            test_id = Id('osid.Osid%3A1%40ODL.MIT.EDU')
            self.form.set_assessments([test_id])
            assert len(self.form._my_map['assessmentIds']) == 1
            assert self.form._my_map['assessmentIds'][0] == str(test_id)
            with pytest.raises(errors.InvalidArgument):
                self.form.set_assessments('this is not a list')
            # reset this for other tests
            self.form._my_map['assessmentIds'] = list()

    def test_clear_assessments(self):
        """Tests clear_assessments"""
        # From test_templates/learning.py::ActivityForm::clear_assets_template
        if not is_never_authz(self.service_config):
            test_id = Id('osid.Osid%3A1%40ODL.MIT.EDU')
            self.form.set_assessments([test_id])
            assert len(self.form._my_map['assessmentIds']) == 1
            assert self.form._my_map['assessmentIds'][0] == str(test_id)
            self.form.clear_assessments()
            assert self.form._my_map['assessmentIds'] == []

    def test_get_activity_form_record(self):
        """Tests get_activity_form_record"""
        with pytest.raises(errors.Unsupported):
            self.form.get_activity_form_record(Type('osid.Osid%3Afake-record%40ODL.MIT.EDU'))
        # Here check for a real record?


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def activity_list_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'LEARNING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_objective_bank_form_for_create([])
        create_form.display_name = 'Test ObjectiveBank'
        create_form.description = 'Test ObjectiveBank for ActivityList tests'
        request.cls.catalog = request.cls.svc_mgr.create_objective_bank(create_form)
        create_form = request.cls.catalog.get_objective_form_for_create([])
        create_form.display_name = 'Test Objective for Activity Lookup'
        create_form.description = 'Test Objective for ActivityList tests'
        request.cls.objective = request.cls.catalog.create_objective(create_form)

        request.cls.form = request.cls.catalog.get_activity_form_for_create(request.cls.objective.ident, [])

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for catalog in request.cls.svc_mgr.get_objective_banks():
                for obj in catalog.get_activities():
                    catalog.delete_activity(obj.ident)
                for obj in catalog.get_objectives():
                    catalog.delete_objective(obj.ident)
                request.cls.svc_mgr.delete_objective_bank(catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def activity_list_test_fixture(request):
    from dlkit.json_.learning.objects import ActivityList
    request.cls.activity_list = list()
    request.cls.activity_ids = list()
    if not is_never_authz(request.cls.service_config):
        for num in [0, 1]:
            form = request.cls.catalog.get_activity_form_for_create(request.cls.objective.ident, [])
            form.display_name = 'Test Activity ' + str(num)
            form.description = 'Test Activity for ActivityList tests'
            obj = request.cls.catalog.create_activity(form)

            request.cls.activity_list.append(obj)
            request.cls.activity_ids.append(obj.ident)
    request.cls.activity_list = ActivityList(request.cls.activity_list)


@pytest.mark.usefixtures("activity_list_class_fixture", "activity_list_test_fixture")
class TestActivityList(object):
    """Tests for ActivityList"""
    def test_get_next_activity(self):
        """Tests get_next_activity"""
        # From test_templates/resource.py::ResourceList::get_next_resource_template
        from dlkit.abstract_osid.learning.objects import Activity
        if not is_never_authz(self.service_config):
            assert isinstance(self.activity_list.get_next_activity(), Activity)

    def test_get_next_activities(self):
        """Tests get_next_activities"""
        # From test_templates/resource.py::ResourceList::get_next_resources_template
        from dlkit.abstract_osid.learning.objects import ActivityList, Activity
        if not is_never_authz(self.service_config):
            new_list = self.activity_list.get_next_activities(2)
            assert isinstance(new_list, ActivityList)
            for item in new_list:
                assert isinstance(item, Activity)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def proficiency_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'LEARNING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_objective_bank_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        request.cls.catalog = request.cls.svc_mgr.create_objective_bank(create_form)

        form = request.cls.catalog.get_objective_form_for_create([])
        form.display_name = 'Objective'
        request.cls.objective = request.cls.catalog.create_objective(form)

        form = request.cls.catalog.get_proficiency_form_for_create(request.cls.objective.ident,
                                                                   AGENT_ID,
                                                                   [])
        form.display_name = 'Test proficiency'
        request.cls.object = request.cls.catalog.create_proficiency(form)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_proficiencies():
                request.cls.catalog.delete_proficiency(obj.ident)
            request.cls.catalog.delete_objective(request.cls.objective.ident)
            request.cls.svc_mgr.delete_objective_bank(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def proficiency_test_fixture(request):
    pass


@pytest.mark.usefixtures("proficiency_class_fixture", "proficiency_test_fixture")
class TestProficiency(object):
    """Tests for Proficiency"""
    @pytest.mark.skip('unimplemented test')
    def test_get_resource_id(self):
        """Tests get_resource_id"""
        pass

    def test_get_resource(self):
        """Tests get_resource"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.object.get_resource()

    @pytest.mark.skip('unimplemented test')
    def test_get_objective_id(self):
        """Tests get_objective_id"""
        pass

    def test_get_objective(self):
        """Tests get_objective"""
        if not is_never_authz(self.service_config):
            result = self.object.get_objective()
            assert isinstance(result, Objective)
            assert str(result.ident) == str(self.objective.ident)

    def test_get_completion(self):
        """Tests get_completion"""
        if not is_never_authz(self.service_config):
            score = self.object.get_completion()
            assert score is None

            # if this is set, should be a Decimal
            form = self.catalog.get_proficiency_form_for_create(self.objective.ident,
                                                                AGENT_ID,
                                                                [])
            form.set_completion(0.0)
            new_proficiency = self.catalog.create_proficiency(form)

            assert new_proficiency.get_completion() == 0.0

    def test_has_level(self):
        """Tests has_level"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.object.has_level()

    def test_get_level_id(self):
        """Tests get_level_id"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.object.get_level_id()

    def test_get_level(self):
        """Tests get_level"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.object.get_level()

    def test_get_proficiency_record(self):
        """Tests get_proficiency_record"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unsupported):
                self.object.get_proficiency_record(True)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def proficiency_form_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'LEARNING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_objective_bank_form_for_create([])
        create_form.display_name = 'Test ObjectiveBank'
        create_form.description = 'Test ObjectiveBank for ProficiencyForm tests'
        request.cls.catalog = request.cls.svc_mgr.create_objective_bank(create_form)

        form = request.cls.catalog.get_objective_form_for_create([])
        form.display_name = "Test LO"
        request.cls.objective = request.cls.catalog.create_objective(form)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for catalog in request.cls.svc_mgr.get_objective_banks():
                for obj in catalog.get_proficiencies():
                    catalog.delete_proficiency(obj.ident)
                for obj in catalog.get_objectives():
                    catalog.delete_objective(obj.ident)
                request.cls.svc_mgr.delete_objective_bank(catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def proficiency_form_test_fixture(request):
    if not is_never_authz(request.cls.service_config):
        request.cls.form = request.cls.catalog.get_proficiency_form_for_create(request.cls.objective.ident, AGENT_ID, [])
        request.cls.object = request.cls.form


@pytest.mark.usefixtures("proficiency_form_class_fixture", "proficiency_form_test_fixture")
class TestProficiencyForm(object):
    """Tests for ProficiencyForm"""
    def test_get_completion_metadata(self):
        """Tests get_completion_metadata"""
        # From test_templates/resource.py::ResourceForm::get_group_metadata_template
        mdata = self.form.get_completion_metadata()
        assert isinstance(mdata, Metadata)
        assert isinstance(mdata.get_element_id(), ABC_Id)
        assert isinstance(mdata.get_element_label(), ABC_DisplayText)
        assert isinstance(mdata.get_instructions(), ABC_DisplayText)
        assert mdata.get_syntax() == 'DECIMAL'
        assert not mdata.is_array()
        assert isinstance(mdata.is_required(), bool)
        assert isinstance(mdata.is_read_only(), bool)
        assert isinstance(mdata.is_linked(), bool)

    def test_set_completion(self):
        """Tests set_completion"""
        if not is_never_authz(self.service_config):
            assert self.form._my_map['completion'] is None
            self.form.set_completion(50.0)
            assert self.form._my_map['completion'] is not None

    def test_clear_completion(self):
        """Tests clear_completion"""
        if not is_never_authz(self.service_config):
            self.form.set_completion(50.0)
            assert self.form._my_map['completion'] is not None
            self.form.clear_completion()
            assert self.form._my_map['completion'] is None

    def test_get_level_metadata(self):
        """Tests get_level_metadata"""
        # From test_templates/resource.py::ResourceForm::get_avatar_metadata_template
        mdata = self.form.get_level_metadata()
        assert isinstance(mdata, Metadata)
        assert isinstance(mdata.get_element_id(), ABC_Id)
        assert isinstance(mdata.get_element_label(), ABC_DisplayText)
        assert isinstance(mdata.get_instructions(), ABC_DisplayText)
        assert mdata.get_syntax() == 'ID'
        assert not mdata.is_array()
        assert isinstance(mdata.is_required(), bool)
        assert isinstance(mdata.is_read_only(), bool)
        assert isinstance(mdata.is_linked(), bool)

    def test_set_level(self):
        """Tests set_level"""
        # This is a slightly hokey test, because the spec seems to have a typo
        if not is_never_authz(self.service_config):
            assert self.form._my_map['levelId'] == ''
            self.form.set_level(Id('grading.Grade%3Afake%40ODL.MIT.EDU'))
            assert self.form._my_map['level'] is not None

    def test_clear_level(self):
        """Tests clear_level"""
        if not is_never_authz(self.service_config):
            self.form.set_level(Id('grading.Grade%3Afake%40ODL.MIT.EDU'))
            assert self.form._my_map['level'] is not None
            self.form.clear_level()
            assert self.form._my_map['level'] == ''

    def test_get_proficiency_form_record(self):
        """Tests get_proficiency_form_record"""
        with pytest.raises(errors.Unsupported):
            self.form.get_proficiency_form_record(Type('osid.Osid%3Afake-record%40ODL.MIT.EDU'))
        # Here check for a real record?


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def proficiency_list_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'LEARNING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_objective_bank_form_for_create([])
        create_form.display_name = 'Test ObjectiveBank'
        create_form.description = 'Test ObjectiveBank for ProficiencyList tests'
        request.cls.catalog = request.cls.svc_mgr.create_objective_bank(create_form)

        form = request.cls.catalog.get_objective_form_for_create([])
        form.display_name = "Test LO"
        request.cls.objective = request.cls.catalog.create_objective(form)

        request.cls.form = request.cls.catalog.get_proficiency_form_for_create(request.cls.objective.ident, AGENT_ID, [])

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for catalog in request.cls.svc_mgr.get_objective_banks():
                for obj in catalog.get_proficiencies():
                    catalog.delete_proficiency(obj.ident)
                for obj in catalog.get_objectives():
                    catalog.delete_objective(obj.ident)
                request.cls.svc_mgr.delete_objective_bank(catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def proficiency_list_test_fixture(request):
    from dlkit.json_.learning.objects import ProficiencyList
    request.cls.proficiency_list = list()
    request.cls.proficiency_ids = list()
    if not is_never_authz(request.cls.service_config):
        for num in [0, 1]:
            form = request.cls.catalog.get_proficiency_form_for_create(request.cls.objective.ident, AGENT_ID, [])
            form.display_name = 'Test Proficiency ' + str(num)
            form.description = 'Test Proficiency for ProficiencyList tests'
            obj = request.cls.catalog.create_proficiency(form)

            request.cls.proficiency_list.append(obj)
            request.cls.proficiency_ids.append(obj.ident)
    request.cls.proficiency_list = ProficiencyList(request.cls.proficiency_list)


@pytest.mark.usefixtures("proficiency_list_class_fixture", "proficiency_list_test_fixture")
class TestProficiencyList(object):
    """Tests for ProficiencyList"""
    def test_get_next_proficiency(self):
        """Tests get_next_proficiency"""
        # From test_templates/resource.py::ResourceList::get_next_resource_template
        from dlkit.abstract_osid.learning.objects import Proficiency
        if not is_never_authz(self.service_config):
            assert isinstance(self.proficiency_list.get_next_proficiency(), Proficiency)

    def test_get_next_proficiencies(self):
        """Tests get_next_proficiencies"""
        # From test_templates/resource.py::ResourceList::get_next_resources_template
        from dlkit.abstract_osid.learning.objects import ProficiencyList, Proficiency
        if not is_never_authz(self.service_config):
            new_list = self.proficiency_list.get_next_proficiencies(2)
            assert isinstance(new_list, ProficiencyList)
            for item in new_list:
                assert isinstance(item, Proficiency)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def objective_bank_class_fixture(request):
    # From test_templates/resource.py::Bin::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'LEARNING',
        proxy=PROXY,
        implementation=request.cls.service_config)

    def class_tear_down():
        pass

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def objective_bank_test_fixture(request):
    # From test_templates/resource.py::Bin::init_template
    if not is_never_authz(request.cls.service_config):
        form = request.cls.svc_mgr.get_objective_bank_form_for_create([])
        form.display_name = 'for testing'
        request.cls.object = request.cls.svc_mgr.create_objective_bank(form)

    def test_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.svc_mgr.delete_objective_bank(request.cls.object.ident)

    request.addfinalizer(test_tear_down)


@pytest.mark.usefixtures("objective_bank_class_fixture", "objective_bank_test_fixture")
class TestObjectiveBank(object):
    """Tests for ObjectiveBank"""
    def test_get_objective_bank_record(self):
        """Tests get_objective_bank_record"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.object.get_objective_bank_record(True)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def objective_bank_form_class_fixture(request):
    # From test_templates/resource.py::BinForm::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'LEARNING',
        proxy=PROXY,
        implementation=request.cls.service_config)

    def class_tear_down():
        pass

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def objective_bank_form_test_fixture(request):
    # From test_templates/resource.py::BinForm::init_template
    if not is_never_authz(request.cls.service_config):
        request.cls.object = request.cls.svc_mgr.get_objective_bank_form_for_create([])

    def test_tear_down():
        pass

    request.addfinalizer(test_tear_down)


@pytest.mark.usefixtures("objective_bank_form_class_fixture", "objective_bank_form_test_fixture")
class TestObjectiveBankForm(object):
    """Tests for ObjectiveBankForm"""
    def test_get_objective_bank_form_record(self):
        """Tests get_objective_bank_form_record"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.object.get_objective_bank_form_record(True)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def objective_bank_list_class_fixture(request):
    # Implemented from init template for BinList
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'LEARNING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_objective_bank_form_for_create([])
        create_form.display_name = 'Test ObjectiveBank'
        create_form.description = 'Test ObjectiveBank for ObjectiveBankList tests'
        request.cls.catalog = request.cls.svc_mgr.create_objective_bank(create_form)
        request.cls.objective_bank_ids = list()

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.objective_bank_ids:
                request.cls.svc_mgr.delete_objective_bank(obj)
            request.cls.svc_mgr.delete_objective_bank(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def objective_bank_list_test_fixture(request):
    # Implemented from init template for BinList
    from dlkit.json_.learning.objects import ObjectiveBankList
    request.cls.objective_bank_list = list()
    if not is_never_authz(request.cls.service_config):
        for num in [0, 1]:
            create_form = request.cls.svc_mgr.get_objective_bank_form_for_create([])
            create_form.display_name = 'Test ObjectiveBank ' + str(num)
            create_form.description = 'Test ObjectiveBank for ObjectiveBankList tests'
            obj = request.cls.svc_mgr.create_objective_bank(create_form)
            request.cls.objective_bank_list.append(obj)
            request.cls.objective_bank_ids.append(obj.ident)
    request.cls.objective_bank_list = ObjectiveBankList(request.cls.objective_bank_list)


@pytest.mark.usefixtures("objective_bank_list_class_fixture", "objective_bank_list_test_fixture")
class TestObjectiveBankList(object):
    """Tests for ObjectiveBankList"""
    def test_get_next_objective_bank(self):
        """Tests get_next_objective_bank"""
        # From test_templates/resource.py::ResourceList::get_next_resource_template
        from dlkit.abstract_osid.learning.objects import ObjectiveBank
        if not is_never_authz(self.service_config):
            assert isinstance(self.objective_bank_list.get_next_objective_bank(), ObjectiveBank)

    def test_get_next_objective_banks(self):
        """Tests get_next_objective_banks"""
        # From test_templates/resource.py::ResourceList::get_next_resources_template
        from dlkit.abstract_osid.learning.objects import ObjectiveBankList, ObjectiveBank
        if not is_never_authz(self.service_config):
            new_list = self.objective_bank_list.get_next_objective_banks(2)
            assert isinstance(new_list, ObjectiveBankList)
            for item in new_list:
                assert isinstance(item, ObjectiveBank)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def objective_bank_node_class_fixture(request):
    # Implemented from init template for BinNode
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'LEARNING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_objective_bank_form_for_create([])
        create_form.display_name = 'Test ObjectiveBank'
        create_form.description = 'Test ObjectiveBank for ObjectiveBankNode tests'
        request.cls.catalog = request.cls.svc_mgr.create_objective_bank(create_form)
        request.cls.objective_bank_ids = list()

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.svc_mgr.delete_objective_bank(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def objective_bank_node_test_fixture(request):
    # Implemented from init template for BinNode
    from dlkit.json_.learning.objects import ObjectiveBankNode
    request.cls.objective_bank_list = list()
    if not is_never_authz(request.cls.service_config):
        for num in [0, 1]:
            create_form = request.cls.svc_mgr.get_objective_bank_form_for_create([])
            create_form.display_name = 'Test ObjectiveBank ' + str(num)
            create_form.description = 'Test ObjectiveBank for ObjectiveBankNode tests'
            obj = request.cls.svc_mgr.create_objective_bank(create_form)
            request.cls.objective_bank_list.append(ObjectiveBankNode(
                obj.object_map,
                runtime=request.cls.svc_mgr._runtime,
                proxy=request.cls.svc_mgr._proxy))
            request.cls.objective_bank_ids.append(obj.ident)
        # Not put the catalogs in a hierarchy
        request.cls.svc_mgr.add_root_objective_bank(request.cls.objective_bank_list[0].ident)
        request.cls.svc_mgr.add_child_objective_bank(
            request.cls.objective_bank_list[0].ident,
            request.cls.objective_bank_list[1].ident)

        request.cls.object = request.cls.svc_mgr.get_objective_bank_nodes(
            request.cls.objective_bank_list[0].ident, 0, 5, False)

    def test_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.svc_mgr.remove_child_objective_bank(
                request.cls.objective_bank_list[0].ident,
                request.cls.objective_bank_list[1].ident)
            request.cls.svc_mgr.remove_root_objective_bank(request.cls.objective_bank_list[0].ident)
            for node in request.cls.objective_bank_list:
                request.cls.svc_mgr.delete_objective_bank(node.ident)

    request.addfinalizer(test_tear_down)


@pytest.mark.usefixtures("objective_bank_node_class_fixture", "objective_bank_node_test_fixture")
class TestObjectiveBankNode(object):
    """Tests for ObjectiveBankNode"""
    def test_get_objective_bank(self):
        """Tests get_objective_bank"""
        # from test_templates/resource.py::BinNode::get_bin_template
        from dlkit.abstract_osid.learning.objects import ObjectiveBank
        if not is_never_authz(self.service_config):
            assert isinstance(self.objective_bank_list[0].get_objective_bank(), OsidCatalog)
            assert str(self.objective_bank_list[0].get_objective_bank().ident) == str(self.objective_bank_list[0].ident)

    def test_get_parent_objective_bank_nodes(self):
        """Tests get_parent_objective_bank_nodes"""
        # from test_templates/resource.py::BinNode::get_parent_bin_nodes
        from dlkit.abstract_osid.learning.objects import ObjectiveBankNodeList
        if not is_never_authz(self.service_config):
            node = self.svc_mgr.get_objective_bank_nodes(
                self.objective_bank_list[1].ident,
                1,
                0,
                False)
            assert isinstance(node.get_parent_objective_bank_nodes(), ObjectiveBankNodeList)
            assert node.get_parent_objective_bank_nodes().available() == 1
            assert str(node.get_parent_objective_bank_nodes().next().ident) == str(self.objective_bank_list[0].ident)

    def test_get_child_objective_bank_nodes(self):
        """Tests get_child_objective_bank_nodes"""
        # from test_templates/resource.py::BinNode::get_child_bin_nodes_template
        from dlkit.abstract_osid.learning.objects import ObjectiveBankNodeList
        if not is_never_authz(self.service_config):
            node = self.svc_mgr.get_objective_bank_nodes(
                self.objective_bank_list[0].ident,
                0,
                1,
                False)
            assert isinstance(node.get_child_objective_bank_nodes(), ObjectiveBankNodeList)
            assert node.get_child_objective_bank_nodes().available() == 1
            assert str(node.get_child_objective_bank_nodes().next().ident) == str(self.objective_bank_list[1].ident)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def objective_bank_node_list_class_fixture(request):
    # Implemented from init template for BinNodeList
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'LEARNING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_objective_bank_form_for_create([])
        create_form.display_name = 'Test ObjectiveBank'
        create_form.description = 'Test ObjectiveBank for ObjectiveBankNodeList tests'
        request.cls.catalog = request.cls.svc_mgr.create_objective_bank(create_form)
        request.cls.objective_bank_node_ids = list()

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.objective_bank_node_ids:
                request.cls.svc_mgr.delete_objective_bank(obj)
            request.cls.svc_mgr.delete_objective_bank(request.cls.catalog.ident)


@pytest.fixture(scope="function")
def objective_bank_node_list_test_fixture(request):
    # Implemented from init template for BinNodeList
    from dlkit.json_.learning.objects import ObjectiveBankNodeList, ObjectiveBankNode
    request.cls.objective_bank_node_list = list()
    if not is_never_authz(request.cls.service_config):
        for num in [0, 1]:
            create_form = request.cls.svc_mgr.get_objective_bank_form_for_create([])
            create_form.display_name = 'Test ObjectiveBankNode ' + str(num)
            create_form.description = 'Test ObjectiveBankNode for ObjectiveBankNodeList tests'
            obj = request.cls.svc_mgr.create_objective_bank(create_form)
            request.cls.objective_bank_node_list.append(ObjectiveBankNode(obj.object_map))
            request.cls.objective_bank_node_ids.append(obj.ident)
        # Not put the catalogs in a hierarchy
        request.cls.svc_mgr.add_root_objective_bank(request.cls.objective_bank_node_list[0].ident)
        request.cls.svc_mgr.add_child_objective_bank(
            request.cls.objective_bank_node_list[0].ident,
            request.cls.objective_bank_node_list[1].ident)
    request.cls.objective_bank_node_list = ObjectiveBankNodeList(request.cls.objective_bank_node_list)


@pytest.mark.usefixtures("objective_bank_node_list_class_fixture", "objective_bank_node_list_test_fixture")
class TestObjectiveBankNodeList(object):
    """Tests for ObjectiveBankNodeList"""
    def test_get_next_objective_bank_node(self):
        """Tests get_next_objective_bank_node"""
        # From test_templates/resource.py::ResourceList::get_next_resource_template
        from dlkit.abstract_osid.learning.objects import ObjectiveBankNode
        if not is_never_authz(self.service_config):
            assert isinstance(self.objective_bank_node_list.get_next_objective_bank_node(), ObjectiveBankNode)

    def test_get_next_objective_bank_nodes(self):
        """Tests get_next_objective_bank_nodes"""
        # From test_templates/resource.py::ResourceList::get_next_resources_template
        from dlkit.abstract_osid.learning.objects import ObjectiveBankNodeList, ObjectiveBankNode
        if not is_never_authz(self.service_config):
            new_list = self.objective_bank_node_list.get_next_objective_bank_nodes(2)
            assert isinstance(new_list, ObjectiveBankNodeList)
            for item in new_list:
                assert isinstance(item, ObjectiveBankNode)
