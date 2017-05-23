"""Unit tests of commenting objects."""


import unittest


from dlkit.abstract_osid.osid import errors
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


class TestComment(unittest.TestCase):
    """Tests for Comment"""

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('COMMENTING', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_book_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        cls.catalog = cls.svc_mgr.create_book(create_form)

        form = cls.catalog.get_comment_form_for_create(
            Id('resource.Resource%3A1%40ODL.MIT.EDU'),
            [])
        form.display_name = 'Test object'
        cls.object = cls.catalog.create_comment(form)

    @classmethod
    def tearDownClass(cls):
        for obj in cls.catalog.get_comments():
            cls.catalog.delete_comment(obj.ident)
        cls.svc_mgr.delete_book(cls.catalog.ident)

    @unittest.skip('unimplemented test')
    def test_get_reference_id(self):
        """Tests get_reference_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_commentor_id(self):
        """Tests get_commentor_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_commentor(self):
        """Tests get_commentor"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_commenting_agent_id(self):
        """Tests get_commenting_agent_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_commenting_agent(self):
        """Tests get_commenting_agent"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_text(self):
        """Tests get_text"""
        pass

    @unittest.skip('unimplemented test')
    def test_has_rating(self):
        """Tests has_rating"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_rating_id(self):
        """Tests get_rating_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_rating(self):
        """Tests get_rating"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_comment_record(self):
        """Tests get_comment_record"""
        pass


class TestCommentForm(unittest.TestCase):
    """Tests for CommentForm"""

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('COMMENTING', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_book_form_for_create([])
        create_form.display_name = 'Test Book'
        create_form.description = 'Test Book for CommentForm tests'
        cls.catalog = cls.svc_mgr.create_book(create_form)
        cls.form = cls.catalog.get_comment_form_for_create(AGENT_ID, [])

    @classmethod
    def tearDownClass(cls):
        for catalog in cls.svc_mgr.get_books():
            cls.svc_mgr.delete_book(catalog.ident)

    def test_get_text_metadata(self):
        """Tests get_text_metadata"""
        # From test_templates/resource.py::ResourceForm::get_group_metadata_template
        self.assertTrue(isinstance(self.form.get_text_metadata(), Metadata))

    @unittest.skip('unimplemented test')
    def test_set_text(self):
        """Tests set_text"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_text(self):
        """Tests clear_text"""
        pass

    def test_get_rating_metadata(self):
        """Tests get_rating_metadata"""
        # From test_templates/resource.py::ResourceForm::get_avatar_metadata_template
        self.assertTrue(isinstance(self.form.get_rating_metadata(), Metadata))

    def test_set_rating(self):
        """Tests set_rating"""
        # From test_templates/resource.py::ResourceForm::set_avatar_template
        self.assertEqual(self.form._my_map['ratingId'], '')
        self.form.set_rating(Id('repository.Asset%3Afake-id%40ODL.MIT.EDU'))
        self.assertEqual(self.form._my_map['ratingId'],
                         'repository.Asset%3Afake-id%40ODL.MIT.EDU')

    def test_clear_rating(self):
        """Tests clear_rating"""
        # From test_templates/resource.py::ResourceForm::clear_avatar_template
        self.form.set_rating(Id('repository.Asset%3Afake-id%40ODL.MIT.EDU'))
        self.assertEqual(self.form._my_map['ratingId'],
                         'repository.Asset%3Afake-id%40ODL.MIT.EDU')
        self.form.clear_rating()
        self.assertEqual(self.form._my_map['ratingId'], '')

    def test_get_comment_form_record(self):
        """Tests get_comment_form_record"""
        with self.assertRaises(errors.Unsupported):
            self.form.get_comment_form_record(Type('osid.Osid%3Afake-record%40ODL.MIT.EDU'))
        # Here check for a real record?


class TestCommentList(unittest.TestCase):
    """Tests for CommentList"""

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('COMMENTING', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_book_form_for_create([])
        create_form.display_name = 'Test Book'
        create_form.description = 'Test Book for CommentForm tests'
        cls.catalog = cls.svc_mgr.create_book(create_form)
        cls.form = cls.catalog.get_comment_form_for_create(AGENT_ID, [])

    def setUp(self):
        from dlkit.json_.commenting.objects import CommentList
        self.comment_list = list()
        self.comment_ids = list()

        for num in [0, 1]:
            form = self.catalog.get_comment_form_for_create(AGENT_ID, [])

            obj = self.catalog.create_comment(form)

            self.comment_list.append(obj)
            self.comment_ids.append(obj.ident)
        self.comment_list = CommentList(self.comment_list)

    @classmethod
    def tearDownClass(cls):
        for catalog in cls.svc_mgr.get_books():
            for comment in catalog.get_comments():
                catalog.delete_comment(comment.ident)
            cls.svc_mgr.delete_book(catalog.ident)

    def test_get_next_comment(self):
        """Tests get_next_comment"""
        # From test_templates/resource.py::ResourceList::get_next_resource_template
        from dlkit.abstract_osid.commenting.objects import Comment
        self.assertTrue(isinstance(self.comment_list.get_next_comment(), Comment))

    def test_get_next_comments(self):
        """Tests get_next_comments"""
        # From test_templates/resource.py::ResourceList::get_next_resources_template
        from dlkit.abstract_osid.commenting.objects import CommentList, Comment
        new_list = self.comment_list.get_next_comments(2)
        self.assertTrue(isinstance(new_list, CommentList))
        for item in new_list:
            self.assertTrue(isinstance(item, Comment))


class TestBook(unittest.TestCase):
    """Tests for Book"""

    @unittest.skip('unimplemented test')
    def test_get_book_record(self):
        """Tests get_book_record"""
        pass


class TestBookForm(unittest.TestCase):
    """Tests for BookForm"""

    @unittest.skip('unimplemented test')
    def test_get_book_form_record(self):
        """Tests get_book_form_record"""
        pass


class TestBookList(unittest.TestCase):
    """Tests for BookList"""

    @classmethod
    def setUpClass(cls):
        # Implemented from init template for BinList
        cls.svc_mgr = Runtime().get_service_manager('COMMENTING', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_book_form_for_create([])
        create_form.display_name = 'Test Book'
        create_form.description = 'Test Book for BookList tests'
        cls.catalog = cls.svc_mgr.create_book(create_form)
        cls.book_ids = list()

    def setUp(self):
        # Implemented from init template for BinList
        from dlkit.json_.commenting.objects import BookList
        self.book_list = list()
        for num in [0, 1]:
            create_form = self.svc_mgr.get_book_form_for_create([])
            create_form.display_name = 'Test Book ' + str(num)
            create_form.description = 'Test Book for BookList tests'
            obj = self.svc_mgr.create_book(create_form)
            self.book_list.append(obj)
            self.book_ids.append(obj.ident)
        self.book_list = BookList(self.book_list)

    @classmethod
    def tearDownClass(cls):
        # Implemented from init template for BinList
        for obj in cls.book_ids:
            cls.svc_mgr.delete_book(obj)
        cls.svc_mgr.delete_book(cls.catalog.ident)

    def test_get_next_book(self):
        """Tests get_next_book"""
        # From test_templates/resource.py::ResourceList::get_next_resource_template
        from dlkit.abstract_osid.commenting.objects import Book
        self.assertTrue(isinstance(self.book_list.get_next_book(), Book))

    def test_get_next_books(self):
        """Tests get_next_books"""
        # From test_templates/resource.py::ResourceList::get_next_resources_template
        from dlkit.abstract_osid.commenting.objects import BookList, Book
        new_list = self.book_list.get_next_books(2)
        self.assertTrue(isinstance(new_list, BookList))
        for item in new_list:
            self.assertTrue(isinstance(item, Book))


class TestBookNode(unittest.TestCase):
    """Tests for BookNode"""

    @classmethod
    def setUpClass(cls):
        # Implemented from init template for BinNode
        cls.svc_mgr = Runtime().get_service_manager('COMMENTING', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_book_form_for_create([])
        create_form.display_name = 'Test Book'
        create_form.description = 'Test Book for BookNode tests'
        cls.catalog = cls.svc_mgr.create_book(create_form)
        cls.book_ids = list()

    def setUp(self):
        # Implemented from init template for BinNode
        from dlkit.json_.commenting.objects import BookNode
        self.book_list = list()
        for num in [0, 1]:
            create_form = self.svc_mgr.get_book_form_for_create([])
            create_form.display_name = 'Test Book ' + str(num)
            create_form.description = 'Test Book for BookNode tests'
            obj = self.svc_mgr.create_book(create_form)
            self.book_list.append(BookNode(
                obj.object_map,
                runtime=self.svc_mgr._runtime,
                proxy=self.svc_mgr._proxy))
            self.book_ids.append(obj.ident)
        # Not put the catalogs in a hierarchy
        self.svc_mgr.add_root_book(self.book_list[0].ident)
        self.svc_mgr.add_child_book(
            self.book_list[0].ident,
            self.book_list[1].ident)

    @classmethod
    def tearDownClass(cls):
        # Implemented from init template for BinNode
        for obj in cls.book_ids:
            cls.svc_mgr.delete_book(obj)
        cls.svc_mgr.delete_book(cls.catalog.ident)

    def test_get_book(self):
        """Tests get_book"""
        # from test_templates/resource.py::BinNode::get_bin_template
        from dlkit.abstract_osid.commenting.objects import Book
        self.assertTrue(isinstance(self.book_list[0].get_book(), Book))
        self.assertEqual(str(self.book_list[0].get_book().ident),
                         str(self.book_list[0].ident))

    def test_get_parent_book_nodes(self):
        """Tests get_parent_book_nodes"""
        # from test_templates/resource.py::BinNode::get_parent_bin_nodes
        from dlkit.abstract_osid.commenting.objects import BookNodeList
        node = self.svc_mgr.get_book_nodes(
            self.book_list[1].ident,
            1,
            0,
            False)
        self.assertTrue(isinstance(node.get_parent_book_nodes(), BookNodeList))
        self.assertEqual(node.get_parent_book_nodes().available(),
                         1)
        self.assertEqual(str(node.get_parent_book_nodes().next().ident),
                         str(self.book_list[0].ident))

    def test_get_child_book_nodes(self):
        """Tests get_child_book_nodes"""
        # from test_templates/resource.py::BinNode::get_child_bin_nodes_template
        from dlkit.abstract_osid.commenting.objects import BookNodeList
        node = self.svc_mgr.get_book_nodes(
            self.book_list[0].ident,
            0,
            1,
            False)
        self.assertTrue(isinstance(node.get_child_book_nodes(), BookNodeList))
        self.assertEqual(node.get_child_book_nodes().available(),
                         1)
        self.assertEqual(str(node.get_child_book_nodes().next().ident),
                         str(self.book_list[1].ident))


class TestBookNodeList(unittest.TestCase):
    """Tests for BookNodeList"""

    @classmethod
    def setUpClass(cls):
        # Implemented from init template for BinNodeList
        cls.svc_mgr = Runtime().get_service_manager('COMMENTING', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_book_form_for_create([])
        create_form.display_name = 'Test Book'
        create_form.description = 'Test Book for BookNodeList tests'
        cls.catalog = cls.svc_mgr.create_book(create_form)
        cls.book_node_ids = list()

    def setUp(self):
        # Implemented from init template for BinNodeList
        from dlkit.json_.commenting.objects import BookNodeList, BookNode
        self.book_node_list = list()
        for num in [0, 1]:
            create_form = self.svc_mgr.get_book_form_for_create([])
            create_form.display_name = 'Test BookNode ' + str(num)
            create_form.description = 'Test BookNode for BookNodeList tests'
            obj = self.svc_mgr.create_book(create_form)
            self.book_node_list.append(BookNode(obj.object_map))
            self.book_node_ids.append(obj.ident)
        # Not put the catalogs in a hierarchy
        self.svc_mgr.add_root_book(self.book_node_list[0].ident)
        self.svc_mgr.add_child_book(
            self.book_node_list[0].ident,
            self.book_node_list[1].ident)
        self.book_node_list = BookNodeList(self.book_node_list)

    @classmethod
    def tearDownClass(cls):
        # Implemented from init template for BinNodeList
        for obj in cls.book_node_ids:
            cls.svc_mgr.delete_book(obj)
        cls.svc_mgr.delete_book(cls.catalog.ident)

    def test_get_next_book_node(self):
        """Tests get_next_book_node"""
        # From test_templates/resource.py::ResourceList::get_next_resource_template
        from dlkit.abstract_osid.commenting.objects import BookNode
        self.assertTrue(isinstance(self.book_node_list.get_next_book_node(), BookNode))

    def test_get_next_book_nodes(self):
        """Tests get_next_book_nodes"""
        # From test_templates/resource.py::ResourceList::get_next_resources_template
        from dlkit.abstract_osid.commenting.objects import BookNodeList, BookNode
        new_list = self.book_node_list.get_next_book_nodes(2)
        self.assertTrue(isinstance(new_list, BookNodeList))
        for item in new_list:
            self.assertTrue(isinstance(item, BookNode))
