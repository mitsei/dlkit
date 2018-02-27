"""Unit tests of commenting objects."""


import pytest


from ..utilities.general import is_never_authz, is_no_authz, uses_cataloging, uses_filesystem_only
from dlkit.abstract_osid.commenting import objects as ABCObjects
from dlkit.abstract_osid.id.primitives import Id as ABC_Id
from dlkit.abstract_osid.locale.primitives import DisplayText as ABC_DisplayText
from dlkit.abstract_osid.osid import errors
from dlkit.abstract_osid.osid.objects import OsidCatalog
from dlkit.json_.id.objects import IdList
from dlkit.json_.osid.metadata import Metadata
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
AGENT_ID = Id(**{'identifier': 'jane_doe', 'namespace': 'osid.agent.Agent', 'authority': 'MIT-ODL'})


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def comment_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'COMMENTING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_book_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        request.cls.catalog = request.cls.svc_mgr.create_book(create_form)

        form = request.cls.catalog.get_comment_form_for_create(
            Id('resource.Resource%3A1%40ODL.MIT.EDU'),
            [])
        form.display_name = 'Test object'
        request.cls.object = request.cls.catalog.create_comment(form)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_comments():
                request.cls.catalog.delete_comment(obj.ident)
            request.cls.svc_mgr.delete_book(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def comment_test_fixture(request):
    pass


@pytest.mark.usefixtures("comment_class_fixture", "comment_test_fixture")
class TestComment(object):
    """Tests for Comment"""
    @pytest.mark.skip('unimplemented test')
    def test_get_reference_id(self):
        """Tests get_reference_id"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_commentor_id(self):
        """Tests get_commentor_id"""
        pass

    def test_get_commentor(self):
        """Tests get_commentor"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.object.get_commentor()

    def test_get_commenting_agent_id(self):
        """Tests get_commenting_agent_id"""
        if not is_never_authz(self.service_config):
            result = self.object.get_commenting_agent_id()
            assert isinstance(result, Id)
            assert str(result) == str(self.catalog._proxy.get_effective_agent_id())

    def test_get_commenting_agent(self):
        """Tests get_commenting_agent"""
        if not is_never_authz(self.service_config):
            # because the resource doesn't actually exist
            with pytest.raises(errors.OperationFailed):
                self.object.get_commenting_agent()

    def test_get_text(self):
        """Tests get_text"""
        if not is_never_authz(self.service_config):
            result = self.object.get_text()
            assert isinstance(result, DisplayText)
            assert result.text == ''

    def test_has_rating(self):
        """Tests has_rating"""
        # From test_templates/resources.py::Resource::has_avatar_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.object.has_rating(), bool)

    def test_get_rating_id(self):
        """Tests get_rating_id"""
        # From test_templates/resources.py::Resource::get_avatar_id_template
        if not is_never_authz(self.service_config):
            pytest.raises(errors.IllegalState,
                          self.object.get_rating_id)

    def test_get_rating(self):
        """Tests get_rating"""
        # From test_templates/resources.py::Resource::get_avatar_template
        if not is_never_authz(self.service_config):
            pytest.raises(errors.IllegalState,
                          self.object.get_rating)

    def test_get_comment_record(self):
        """Tests get_comment_record"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unsupported):
                self.object.get_comment_record(True)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def comment_form_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'COMMENTING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_book_form_for_create([])
        create_form.display_name = 'Test Book'
        create_form.description = 'Test Book for CommentForm tests'
        request.cls.catalog = request.cls.svc_mgr.create_book(create_form)
        request.cls.form = request.cls.catalog.get_comment_form_for_create(AGENT_ID, [])

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for catalog in request.cls.svc_mgr.get_books():
                request.cls.svc_mgr.delete_book(catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def comment_form_test_fixture(request):
    pass


@pytest.mark.usefixtures("comment_form_class_fixture", "comment_form_test_fixture")
class TestCommentForm(object):
    """Tests for CommentForm"""
    def test_get_text_metadata(self):
        """Tests get_text_metadata"""
        # From test_templates/resource.py::ResourceForm::get_group_metadata_template
        mdata = self.form.get_text_metadata()
        assert isinstance(mdata, Metadata)
        assert isinstance(mdata.get_element_id(), ABC_Id)
        assert isinstance(mdata.get_element_label(), ABC_DisplayText)
        assert isinstance(mdata.get_instructions(), ABC_DisplayText)
        assert mdata.get_syntax() == 'STRING'
        assert not mdata.is_array()
        assert isinstance(mdata.is_required(), bool)
        assert isinstance(mdata.is_read_only(), bool)
        assert isinstance(mdata.is_linked(), bool)

    def test_set_text(self):
        """Tests set_text"""
        # From test_templates/repository.py::AssetForm::set_title_template
        default_value = self.form.get_text_metadata().get_default_string_values()[0]
        assert self.form._my_map['text'] == default_value
        self.form.set_text('String')
        assert self.form._my_map['text']['text'] == 'String'
        with pytest.raises(errors.InvalidArgument):
            self.form.set_text(42)

    def test_clear_text(self):
        """Tests clear_text"""
        # From test_templates/repository.py::AssetForm::clear_title_template
        self.form.set_text('A String to Clear')
        assert self.form._my_map['text']['text'] == 'A String to Clear'
        self.form.clear_text()
        assert self.form._my_map['text'] == self.form.get_text_metadata().get_default_string_values()[0]

    def test_get_rating_metadata(self):
        """Tests get_rating_metadata"""
        # From test_templates/resource.py::ResourceForm::get_avatar_metadata_template
        mdata = self.form.get_rating_metadata()
        assert isinstance(mdata, Metadata)
        assert isinstance(mdata.get_element_id(), ABC_Id)
        assert isinstance(mdata.get_element_label(), ABC_DisplayText)
        assert isinstance(mdata.get_instructions(), ABC_DisplayText)
        assert mdata.get_syntax() == 'ID'
        assert not mdata.is_array()
        assert isinstance(mdata.is_required(), bool)
        assert isinstance(mdata.is_read_only(), bool)
        assert isinstance(mdata.is_linked(), bool)

    def test_set_rating(self):
        """Tests set_rating"""
        # From test_templates/resource.py::ResourceForm::set_avatar_template
        assert self.form._my_map['ratingId'] == ''
        self.form.set_rating(Id('repository.Asset%3Afake-id%40ODL.MIT.EDU'))
        assert self.form._my_map['ratingId'] == 'repository.Asset%3Afake-id%40ODL.MIT.EDU'
        with pytest.raises(errors.InvalidArgument):
            self.form.set_rating(True)

    def test_clear_rating(self):
        """Tests clear_rating"""
        # From test_templates/resource.py::ResourceForm::clear_avatar_template
        self.form.set_rating(Id('repository.Asset%3Afake-id%40ODL.MIT.EDU'))
        assert self.form._my_map['ratingId'] == 'repository.Asset%3Afake-id%40ODL.MIT.EDU'
        self.form.clear_rating()
        assert self.form._my_map['ratingId'] == self.form.get_rating_metadata().get_default_id_values()[0]

    def test_get_comment_form_record(self):
        """Tests get_comment_form_record"""
        with pytest.raises(errors.Unsupported):
            self.form.get_comment_form_record(Type('osid.Osid%3Afake-record%40ODL.MIT.EDU'))
        # Here check for a real record?


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def comment_list_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'COMMENTING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_book_form_for_create([])
        create_form.display_name = 'Test Book'
        create_form.description = 'Test Book for CommentForm tests'
        request.cls.catalog = request.cls.svc_mgr.create_book(create_form)
        request.cls.form = request.cls.catalog.get_comment_form_for_create(AGENT_ID, [])

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for catalog in request.cls.svc_mgr.get_books():
                for comment in catalog.get_comments():
                    catalog.delete_comment(comment.ident)
                request.cls.svc_mgr.delete_book(catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def comment_list_test_fixture(request):
    from dlkit.json_.commenting.objects import CommentList
    request.cls.comment_list = list()
    request.cls.comment_ids = list()

    if not is_never_authz(request.cls.service_config):
        for num in [0, 1]:
            form = request.cls.catalog.get_comment_form_for_create(AGENT_ID, [])

            obj = request.cls.catalog.create_comment(form)

            request.cls.comment_list.append(obj)
            request.cls.comment_ids.append(obj.ident)
        request.cls.comment_list = CommentList(request.cls.comment_list)


@pytest.mark.usefixtures("comment_list_class_fixture", "comment_list_test_fixture")
class TestCommentList(object):
    """Tests for CommentList"""
    def test_get_next_comment(self):
        """Tests get_next_comment"""
        # From test_templates/resource.py::ResourceList::get_next_resource_template
        from dlkit.abstract_osid.commenting.objects import Comment
        if not is_never_authz(self.service_config):
            assert isinstance(self.comment_list.get_next_comment(), Comment)

    def test_get_next_comments(self):
        """Tests get_next_comments"""
        # From test_templates/resource.py::ResourceList::get_next_resources_template
        from dlkit.abstract_osid.commenting.objects import CommentList, Comment
        if not is_never_authz(self.service_config):
            new_list = self.comment_list.get_next_comments(2)
            assert isinstance(new_list, CommentList)
            for item in new_list:
                assert isinstance(item, Comment)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def book_class_fixture(request):
    # From test_templates/resource.py::Bin::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'COMMENTING',
        proxy=PROXY,
        implementation=request.cls.service_config)

    def class_tear_down():
        pass

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def book_test_fixture(request):
    # From test_templates/resource.py::Bin::init_template
    if not is_never_authz(request.cls.service_config):
        form = request.cls.svc_mgr.get_book_form_for_create([])
        form.display_name = 'for testing'
        request.cls.object = request.cls.svc_mgr.create_book(form)

    def test_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.svc_mgr.delete_book(request.cls.object.ident)

    request.addfinalizer(test_tear_down)


@pytest.mark.usefixtures("book_class_fixture", "book_test_fixture")
class TestBook(object):
    """Tests for Book"""
    def test_get_book_record(self):
        """Tests get_book_record"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.object.get_book_record(True)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def book_form_class_fixture(request):
    # From test_templates/resource.py::BinForm::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'COMMENTING',
        proxy=PROXY,
        implementation=request.cls.service_config)

    def class_tear_down():
        pass

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def book_form_test_fixture(request):
    # From test_templates/resource.py::BinForm::init_template
    if not is_never_authz(request.cls.service_config):
        request.cls.object = request.cls.svc_mgr.get_book_form_for_create([])

    def test_tear_down():
        pass

    request.addfinalizer(test_tear_down)


@pytest.mark.usefixtures("book_form_class_fixture", "book_form_test_fixture")
class TestBookForm(object):
    """Tests for BookForm"""
    def test_get_book_form_record(self):
        """Tests get_book_form_record"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.object.get_book_form_record(True)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def book_list_class_fixture(request):
    # Implemented from init template for BinList
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'COMMENTING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_book_form_for_create([])
        create_form.display_name = 'Test Book'
        create_form.description = 'Test Book for BookList tests'
        request.cls.catalog = request.cls.svc_mgr.create_book(create_form)
        request.cls.book_ids = list()

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.book_ids:
                request.cls.svc_mgr.delete_book(obj)
            request.cls.svc_mgr.delete_book(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def book_list_test_fixture(request):
    # Implemented from init template for BinList
    from dlkit.json_.commenting.objects import BookList
    request.cls.book_list = list()
    if not is_never_authz(request.cls.service_config):
        for num in [0, 1]:
            create_form = request.cls.svc_mgr.get_book_form_for_create([])
            create_form.display_name = 'Test Book ' + str(num)
            create_form.description = 'Test Book for BookList tests'
            obj = request.cls.svc_mgr.create_book(create_form)
            request.cls.book_list.append(obj)
            request.cls.book_ids.append(obj.ident)
    request.cls.book_list = BookList(request.cls.book_list)


@pytest.mark.usefixtures("book_list_class_fixture", "book_list_test_fixture")
class TestBookList(object):
    """Tests for BookList"""
    def test_get_next_book(self):
        """Tests get_next_book"""
        # From test_templates/resource.py::ResourceList::get_next_resource_template
        from dlkit.abstract_osid.commenting.objects import Book
        if not is_never_authz(self.service_config):
            assert isinstance(self.book_list.get_next_book(), Book)

    def test_get_next_books(self):
        """Tests get_next_books"""
        # From test_templates/resource.py::ResourceList::get_next_resources_template
        from dlkit.abstract_osid.commenting.objects import BookList, Book
        if not is_never_authz(self.service_config):
            new_list = self.book_list.get_next_books(2)
            assert isinstance(new_list, BookList)
            for item in new_list:
                assert isinstance(item, Book)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def book_node_class_fixture(request):
    # Implemented from init template for BinNode
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'COMMENTING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_book_form_for_create([])
        create_form.display_name = 'Test Book'
        create_form.description = 'Test Book for BookNode tests'
        request.cls.catalog = request.cls.svc_mgr.create_book(create_form)
        request.cls.book_ids = list()

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.svc_mgr.delete_book(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def book_node_test_fixture(request):
    # Implemented from init template for BinNode
    from dlkit.json_.commenting.objects import BookNode
    request.cls.book_list = list()
    if not is_never_authz(request.cls.service_config):
        for num in [0, 1]:
            create_form = request.cls.svc_mgr.get_book_form_for_create([])
            create_form.display_name = 'Test Book ' + str(num)
            create_form.description = 'Test Book for BookNode tests'
            obj = request.cls.svc_mgr.create_book(create_form)
            request.cls.book_list.append(BookNode(
                obj.object_map,
                runtime=request.cls.svc_mgr._runtime,
                proxy=request.cls.svc_mgr._proxy))
            request.cls.book_ids.append(obj.ident)
        # Not put the catalogs in a hierarchy
        request.cls.svc_mgr.add_root_book(request.cls.book_list[0].ident)
        request.cls.svc_mgr.add_child_book(
            request.cls.book_list[0].ident,
            request.cls.book_list[1].ident)

        request.cls.object = request.cls.svc_mgr.get_book_nodes(
            request.cls.book_list[0].ident, 0, 5, False)

    def test_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.svc_mgr.remove_child_book(
                request.cls.book_list[0].ident,
                request.cls.book_list[1].ident)
            request.cls.svc_mgr.remove_root_book(request.cls.book_list[0].ident)
            for node in request.cls.book_list:
                request.cls.svc_mgr.delete_book(node.ident)

    request.addfinalizer(test_tear_down)


@pytest.mark.usefixtures("book_node_class_fixture", "book_node_test_fixture")
class TestBookNode(object):
    """Tests for BookNode"""
    def test_get_book(self):
        """Tests get_book"""
        # from test_templates/resource.py::BinNode::get_bin_template
        from dlkit.abstract_osid.commenting.objects import Book
        if not is_never_authz(self.service_config):
            assert isinstance(self.book_list[0].get_book(), OsidCatalog)
            assert str(self.book_list[0].get_book().ident) == str(self.book_list[0].ident)

    def test_get_parent_book_nodes(self):
        """Tests get_parent_book_nodes"""
        # from test_templates/resource.py::BinNode::get_parent_bin_nodes
        from dlkit.abstract_osid.commenting.objects import BookNodeList
        if not is_never_authz(self.service_config):
            node = self.svc_mgr.get_book_nodes(
                self.book_list[1].ident,
                1,
                0,
                False)
            assert isinstance(node.get_parent_book_nodes(), BookNodeList)
            assert node.get_parent_book_nodes().available() == 1
            assert str(node.get_parent_book_nodes().next().ident) == str(self.book_list[0].ident)

    def test_get_child_book_nodes(self):
        """Tests get_child_book_nodes"""
        # from test_templates/resource.py::BinNode::get_child_bin_nodes_template
        from dlkit.abstract_osid.commenting.objects import BookNodeList
        if not is_never_authz(self.service_config):
            node = self.svc_mgr.get_book_nodes(
                self.book_list[0].ident,
                0,
                1,
                False)
            assert isinstance(node.get_child_book_nodes(), BookNodeList)
            assert node.get_child_book_nodes().available() == 1
            assert str(node.get_child_book_nodes().next().ident) == str(self.book_list[1].ident)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def book_node_list_class_fixture(request):
    # Implemented from init template for BinNodeList
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'COMMENTING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_book_form_for_create([])
        create_form.display_name = 'Test Book'
        create_form.description = 'Test Book for BookNodeList tests'
        request.cls.catalog = request.cls.svc_mgr.create_book(create_form)
        request.cls.book_node_ids = list()

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.book_node_ids:
                request.cls.svc_mgr.delete_book(obj)
            request.cls.svc_mgr.delete_book(request.cls.catalog.ident)


@pytest.fixture(scope="function")
def book_node_list_test_fixture(request):
    # Implemented from init template for BinNodeList
    from dlkit.json_.commenting.objects import BookNodeList, BookNode
    request.cls.book_node_list = list()
    if not is_never_authz(request.cls.service_config):
        for num in [0, 1]:
            create_form = request.cls.svc_mgr.get_book_form_for_create([])
            create_form.display_name = 'Test BookNode ' + str(num)
            create_form.description = 'Test BookNode for BookNodeList tests'
            obj = request.cls.svc_mgr.create_book(create_form)
            request.cls.book_node_list.append(BookNode(obj.object_map))
            request.cls.book_node_ids.append(obj.ident)
        # Not put the catalogs in a hierarchy
        request.cls.svc_mgr.add_root_book(request.cls.book_node_list[0].ident)
        request.cls.svc_mgr.add_child_book(
            request.cls.book_node_list[0].ident,
            request.cls.book_node_list[1].ident)
    request.cls.book_node_list = BookNodeList(request.cls.book_node_list)


@pytest.mark.usefixtures("book_node_list_class_fixture", "book_node_list_test_fixture")
class TestBookNodeList(object):
    """Tests for BookNodeList"""
    def test_get_next_book_node(self):
        """Tests get_next_book_node"""
        # From test_templates/resource.py::ResourceList::get_next_resource_template
        from dlkit.abstract_osid.commenting.objects import BookNode
        if not is_never_authz(self.service_config):
            assert isinstance(self.book_node_list.get_next_book_node(), BookNode)

    def test_get_next_book_nodes(self):
        """Tests get_next_book_nodes"""
        # From test_templates/resource.py::ResourceList::get_next_resources_template
        from dlkit.abstract_osid.commenting.objects import BookNodeList, BookNode
        if not is_never_authz(self.service_config):
            new_list = self.book_node_list.get_next_book_nodes(2)
            assert isinstance(new_list, BookNodeList)
            for item in new_list:
                assert isinstance(item, BookNode)
