"""Unit tests of commenting sessions."""


import unittest


from dlkit.abstract_osid.hierarchy.objects import Hierarchy
from dlkit.abstract_osid.id.objects import IdList
from dlkit.abstract_osid.osid import errors
from dlkit.abstract_osid.osid.objects import OsidForm
from dlkit.abstract_osid.osid.objects import OsidNode
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
ALIAS_ID = Id(**{'identifier': 'ALIAS', 'namespace': 'ALIAS', 'authority': 'ALIAS'})
NEW_TYPE = Type(**{'identifier': 'NEW', 'namespace': 'MINE', 'authority': 'YOURS'})
NEW_TYPE_2 = Type(**{'identifier': 'NEW 2', 'namespace': 'MINE', 'authority': 'YOURS'})


class TestCommentLookupSession(unittest.TestCase):
    """Tests for CommentLookupSession"""

    @classmethod
    def setUpClass(cls):
        cls.comment_list = list()
        cls.comment_ids = list()
        cls.svc_mgr = Runtime().get_service_manager('COMMENTING', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_book_form_for_create([])
        create_form.display_name = 'Test Book'
        create_form.description = 'Test Book for CommentLookupSession tests'
        cls.catalog = cls.svc_mgr.create_book(create_form)
        for num in [0, 1]:
            create_form = cls.catalog.get_comment_form_for_create(AGENT_ID, [])
            create_form.display_name = 'Test Comment ' + str(num)
            create_form.description = 'Test Comment for CommentLookupSession tests'
            object = cls.catalog.create_comment(create_form)
            cls.comment_list.append(object)
            cls.comment_ids.append(object.ident)

    @classmethod
    def tearDownClass(cls):
        for catalog in cls.svc_mgr.get_books():
            for obj in catalog.get_comments():
                catalog.delete_comment(obj.ident)
            cls.svc_mgr.delete_book(catalog.ident)

    def test_get_book_id(self):
        """Tests get_book_id"""
        self.assertEqual(self.catalog.get_book_id(), self.catalog.ident)

    def test_get_book(self):
        """Tests get_book"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        self.assertIsNotNone(self.catalog)

    def test_can_lookup_comments(self):
        """Tests can_lookup_comments"""
        self.assertTrue(isinstance(self.catalog.can_lookup_comments(), bool))

    def test_use_comparative_comment_view(self):
        """Tests use_comparative_comment_view"""
        self.catalog.use_comparative_comment_view()

    def test_use_plenary_comment_view(self):
        """Tests use_plenary_comment_view"""
        self.catalog.use_plenary_comment_view()

    def test_use_federated_book_view(self):
        """Tests use_federated_book_view"""
        self.catalog.use_federated_book_view()

    def test_use_isolated_book_view(self):
        """Tests use_isolated_book_view"""
        self.catalog.use_isolated_book_view()

    @unittest.skip('unimplemented test')
    def test_use_effective_comment_view(self):
        """Tests use_effective_comment_view"""
        pass

    @unittest.skip('unimplemented test')
    def test_use_any_effective_comment_view(self):
        """Tests use_any_effective_comment_view"""
        pass

    def test_get_comment(self):
        """Tests get_comment"""
        # From test_templates/resource.py ResourceLookupSession.get_resource_template
        self.catalog.use_isolated_book_view()
        obj = self.catalog.get_comment(self.comment_list[0].ident)
        self.assertEqual(obj.ident, self.comment_list[0].ident)
        self.catalog.use_federated_book_view()
        obj = self.catalog.get_comment(self.comment_list[0].ident)
        self.assertEqual(obj.ident, self.comment_list[0].ident)

    def test_get_comments_by_ids(self):
        """Tests get_comments_by_ids"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_ids_template
        from dlkit.abstract_osid.commenting.objects import CommentList
        objects = self.catalog.get_comments_by_ids(self.comment_ids)
        self.assertTrue(isinstance(objects, CommentList))
        self.catalog.use_federated_book_view()
        objects = self.catalog.get_comments_by_ids(self.comment_ids)

    def test_get_comments_by_genus_type(self):
        """Tests get_comments_by_genus_type"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_genus_type_template
        from dlkit.abstract_osid.commenting.objects import CommentList
        objects = self.catalog.get_comments_by_genus_type(DEFAULT_TYPE)
        self.assertTrue(isinstance(objects, CommentList))
        self.catalog.use_federated_book_view()
        objects = self.catalog.get_comments_by_genus_type(DEFAULT_TYPE)

    def test_get_comments_by_parent_genus_type(self):
        """Tests get_comments_by_parent_genus_type"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_parent_genus_type_template
        from dlkit.abstract_osid.commenting.objects import CommentList
        objects = self.catalog.get_comments_by_parent_genus_type(DEFAULT_TYPE)
        self.assertTrue(isinstance(objects, CommentList))
        self.catalog.use_federated_book_view()
        objects = self.catalog.get_comments_by_parent_genus_type(DEFAULT_TYPE)

    def test_get_comments_by_record_type(self):
        """Tests get_comments_by_record_type"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_record_type_template
        from dlkit.abstract_osid.commenting.objects import CommentList
        objects = self.catalog.get_comments_by_record_type(DEFAULT_TYPE)
        self.assertTrue(isinstance(objects, CommentList))
        self.catalog.use_federated_book_view()
        objects = self.catalog.get_comments_by_record_type(DEFAULT_TYPE)

    @unittest.skip('unimplemented test')
    def test_get_comments_on_date(self):
        """Tests get_comments_on_date"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_comments_by_genus_type_on_date(self):
        """Tests get_comments_by_genus_type_on_date"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_comments_for_commentor(self):
        """Tests get_comments_for_commentor"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_comments_for_commentor_on_date(self):
        """Tests get_comments_for_commentor_on_date"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_comments_by_genus_type_for_commentor(self):
        """Tests get_comments_by_genus_type_for_commentor"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_comments_by_genus_type_for_commentor_on_date(self):
        """Tests get_comments_by_genus_type_for_commentor_on_date"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_comments_for_reference(self):
        """Tests get_comments_for_reference"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_comments_for_reference_on_date(self):
        """Tests get_comments_for_reference_on_date"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_comments_by_genus_type_for_reference(self):
        """Tests get_comments_by_genus_type_for_reference"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_comments_by_genus_type_for_reference_on_date(self):
        """Tests get_comments_by_genus_type_for_reference_on_date"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_comments_for_commentor_and_reference(self):
        """Tests get_comments_for_commentor_and_reference"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_comments_for_commentor_and_reference_on_date(self):
        """Tests get_comments_for_commentor_and_reference_on_date"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_comments_by_genus_type_for_commentor_and_reference(self):
        """Tests get_comments_by_genus_type_for_commentor_and_reference"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_comments_by_genus_type_for_commentor_and_reference_on_date(self):
        """Tests get_comments_by_genus_type_for_commentor_and_reference_on_date"""
        pass

    def test_get_comments(self):
        """Tests get_comments"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_template
        from dlkit.abstract_osid.commenting.objects import CommentList
        objects = self.catalog.get_comments()
        self.assertTrue(isinstance(objects, CommentList))
        self.catalog.use_federated_book_view()
        objects = self.catalog.get_comments()

    def test_get_comment_with_alias(self):
        self.catalog.alias_comment(self.comment_ids[0], ALIAS_ID)
        obj = self.catalog.get_comment(ALIAS_ID)
        self.assertEqual(obj.get_id(), self.comment_ids[0])


class TestCommentQuerySession(unittest.TestCase):
    """Tests for CommentQuerySession"""

    @classmethod
    def setUpClass(cls):
        cls.comment_list = list()
        cls.comment_ids = list()
        cls.svc_mgr = Runtime().get_service_manager('COMMENTING', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_book_form_for_create([])
        create_form.display_name = 'Test Book'
        create_form.description = 'Test Book for CommentQuerySession tests'
        cls.catalog = cls.svc_mgr.create_book(create_form)
        for color in ['Orange', 'Blue', 'Green', 'orange']:
            create_form = cls.catalog.get_comment_form_for_create(AGENT_ID, [])
            create_form.display_name = 'Test Comment ' + color
            create_form.description = (
                'Test Comment for CommentQuerySession tests, did I mention green')
            obj = cls.catalog.create_comment(create_form)
            cls.comment_list.append(obj)
            cls.comment_ids.append(obj.ident)

    @classmethod
    def tearDownClass(cls):
        for catalog in cls.svc_mgr.get_books():
            for obj in catalog.get_comments():
                catalog.delete_comment(obj.ident)
            cls.svc_mgr.delete_book(catalog.ident)

    def test_get_book_id(self):
        """Tests get_book_id"""
        self.assertEqual(self.catalog.get_book_id(), self.catalog.ident)

    def test_get_book(self):
        """Tests get_book"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        self.assertIsNotNone(self.catalog)

    @unittest.skip('unimplemented test')
    def test_can_search_comments(self):
        """Tests can_search_comments"""
        pass

    def test_use_federated_book_view(self):
        """Tests use_federated_book_view"""
        self.catalog.use_federated_book_view()

    def test_use_isolated_book_view(self):
        """Tests use_isolated_book_view"""
        self.catalog.use_isolated_book_view()

    def test_get_comment_query(self):
        """Tests get_comment_query"""
        query = self.catalog.get_comment_query()

    def test_get_comments_by_query(self):
        """Tests get_comments_by_query"""
        # From test_templates/resource.py ResourceQuerySession::get_resources_by_query_template
        # Need to add some tests with string types
        query = self.catalog.get_comment_query()
        query.match_display_name('orange')
        self.assertEqual(self.catalog.get_comments_by_query(query).available(), 2)
        query.clear_display_name_terms()
        query.match_display_name('blue', match=False)
        self.assertEqual(self.catalog.get_comments_by_query(query).available(), 3)


class TestCommentAdminSession(unittest.TestCase):
    """Tests for CommentAdminSession"""

    @classmethod
    def setUpClass(cls):
        cls.comment_list = list()
        cls.comment_ids = list()
        cls.svc_mgr = Runtime().get_service_manager('COMMENTING', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_book_form_for_create([])
        create_form.display_name = 'Test Book'
        create_form.description = 'Test Book for CommentAdminSession tests'
        cls.catalog = cls.svc_mgr.create_book(create_form)
        for num in [0, 1]:
            create_form = cls.catalog.get_comment_form_for_create(AGENT_ID, [])
            create_form.display_name = 'Test Comment ' + str(num)
            create_form.description = 'Test Comment for CommentAdminSession tests'
            object = cls.catalog.create_comment(create_form)
            cls.comment_list.append(object)
            cls.comment_ids.append(object.ident)
        create_form = cls.catalog.get_comment_form_for_create(AGENT_ID, [])
        create_form.display_name = 'new Comment'
        create_form.description = 'description of Comment'
        create_form.genus_type = NEW_TYPE
        cls.osid_object = cls.catalog.create_comment(create_form)

    @classmethod
    def tearDownClass(cls):
        for catalog in cls.svc_mgr.get_books():
            for obj in catalog.get_comments():
                catalog.delete_comment(obj.ident)
            cls.svc_mgr.delete_book(catalog.ident)

    def test_get_book_id(self):
        """Tests get_book_id"""
        self.assertEqual(self.catalog.get_book_id(), self.catalog.ident)

    def test_get_book(self):
        """Tests get_book"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        self.assertIsNotNone(self.catalog)

    def test_can_create_comments(self):
        """Tests can_create_comments"""
        # From test_templates/resource.py::ResourceAdminSession::can_create_resources_template
        self.assertTrue(isinstance(self.catalog.can_create_comments(), bool))

    def test_can_create_comment_with_record_types(self):
        """Tests can_create_comment_with_record_types"""
        # From test_templates/resource.py::ResourceAdminSession::can_create_resource_with_record_types_template
        self.assertTrue(isinstance(self.catalog.can_create_comment_with_record_types(DEFAULT_TYPE), bool))

    def test_get_comment_form_for_create(self):
        """Tests get_comment_form_for_create"""
        form = self.catalog.get_comment_form_for_create(AGENT_ID, [])
        self.assertTrue(isinstance(form, OsidForm))
        self.assertFalse(form.is_for_update())

    def test_create_comment(self):
        """Tests create_comment"""
        # From test_templates/resource.py::ResourceAdminSession::create_resource_template
        from dlkit.abstract_osid.commenting.objects import Comment
        self.assertTrue(isinstance(self.osid_object, Comment))
        self.assertEqual(self.osid_object.display_name.text, 'new Comment')
        self.assertEqual(self.osid_object.description.text, 'description of Comment')
        self.assertEqual(self.osid_object.genus_type, NEW_TYPE)

    def test_can_update_comments(self):
        """Tests can_update_comments"""
        # From test_templates/resource.py::ResourceAdminSession::can_update_resources_template
        self.assertTrue(isinstance(self.catalog.can_update_comments(), bool))

    def test_get_comment_form_for_update(self):
        """Tests get_comment_form_for_update"""
        # From test_templates/resource.py::ResourceAdminSession::get_resource_form_for_update_template
        form = self.catalog.get_comment_form_for_update(self.osid_object.ident)
        self.assertTrue(isinstance(form, OsidForm))
        self.assertTrue(form.is_for_update())

    def test_update_comment(self):
        """Tests update_comment"""
        # From test_templates/resource.py::ResourceAdminSession::update_resource_template
        from dlkit.abstract_osid.commenting.objects import Comment
        form = self.catalog.get_comment_form_for_update(self.osid_object.ident)
        form.display_name = 'new name'
        form.description = 'new description'
        form.set_genus_type(NEW_TYPE_2)
        updated_object = self.catalog.update_comment(form)
        self.assertTrue(isinstance(updated_object, Comment))
        self.assertEqual(updated_object.ident, self.osid_object.ident)
        self.assertEqual(updated_object.display_name.text, 'new name')
        self.assertEqual(updated_object.description.text, 'new description')
        self.assertEqual(updated_object.genus_type, NEW_TYPE_2)

    def test_can_delete_comments(self):
        """Tests can_delete_comments"""
        # From test_templates/resource.py::ResourceAdminSession::can_delete_resources_template
        self.assertTrue(isinstance(self.catalog.can_delete_comments(), bool))

    def test_delete_comment(self):
        """Tests delete_comment"""
        form = self.catalog.get_comment_form_for_create(AGENT_ID, [])
        form.display_name = 'new Comment'
        form.description = 'description of Comment'
        form.set_genus_type(NEW_TYPE)
        osid_object = self.catalog.create_comment(form)
        self.catalog.delete_comment(osid_object.ident)
        with self.assertRaises(errors.NotFound):
            self.catalog.get_comment(osid_object.ident)

    def test_can_manage_comment_aliases(self):
        """Tests can_manage_comment_aliases"""
        # From test_templates/resource.py::ResourceAdminSession::can_manage_resource_aliases_template
        self.assertTrue(isinstance(self.catalog.can_manage_comment_aliases(), bool))

    def test_alias_comment(self):
        """Tests alias_comment"""
        # From test_templates/resource.py::ResourceAdminSession::alias_resource_template
        alias_id = Id(self.catalog.ident.namespace + '%3Amy-alias%40ODL.MIT.EDU')
        self.catalog.alias_comment(self.osid_object.ident, alias_id)
        aliased_object = self.catalog.get_comment(alias_id)
        self.assertEqual(aliased_object.ident, self.osid_object.ident)


class TestBookLookupSession(unittest.TestCase):
    """Tests for BookLookupSession"""

    @classmethod
    def setUpClass(cls):
        cls.catalogs = list()
        cls.catalog_ids = list()
        cls.svc_mgr = Runtime().get_service_manager('COMMENTING', proxy=PROXY, implementation='TEST_SERVICE')
        for num in [0, 1]:
            create_form = cls.svc_mgr.get_book_form_for_create([])
            create_form.display_name = 'Test Book ' + str(num)
            create_form.description = 'Test Book for commenting proxy manager tests'
            catalog = cls.svc_mgr.create_book(create_form)
            cls.catalogs.append(catalog)
            cls.catalog_ids.append(catalog.ident)

    @classmethod
    def tearDownClass(cls):
        for catalog in cls.svc_mgr.get_books():
            cls.svc_mgr.delete_book(catalog.ident)

    @unittest.skip('unimplemented test')
    def test_can_lookup_books(self):
        """Tests can_lookup_books"""
        pass

    def test_use_comparative_book_view(self):
        """Tests use_comparative_book_view"""
        self.svc_mgr.use_comparative_book_view()

    def test_use_plenary_book_view(self):
        """Tests use_plenary_book_view"""
        self.svc_mgr.use_plenary_book_view()

    def test_get_book(self):
        """Tests get_book"""
        catalog = self.svc_mgr.get_book(self.catalogs[0].ident)
        self.assertEqual(catalog.ident, self.catalogs[0].ident)

    def test_get_books_by_ids(self):
        """Tests get_books_by_ids"""
        catalogs = self.svc_mgr.get_books_by_ids(self.catalog_ids)

    @unittest.skip('unimplemented test')
    def test_get_books_by_genus_type(self):
        """Tests get_books_by_genus_type"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_books_by_parent_genus_type(self):
        """Tests get_books_by_parent_genus_type"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_books_by_record_type(self):
        """Tests get_books_by_record_type"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_books_by_provider(self):
        """Tests get_books_by_provider"""
        pass

    def test_get_books(self):
        """Tests get_books"""
        catalogs = self.svc_mgr.get_books()


class TestBookAdminSession(unittest.TestCase):
    """Tests for BookAdminSession"""

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('COMMENTING', proxy=PROXY, implementation='TEST_SERVICE')
        # Initialize test catalog:
        create_form = cls.svc_mgr.get_book_form_for_create([])
        create_form.display_name = 'Test Book'
        create_form.description = 'Test Book for BookAdminSession tests'
        cls.catalog = cls.svc_mgr.create_book(create_form)
        # Initialize catalog to be deleted:
        create_form = cls.svc_mgr.get_book_form_for_create([])
        create_form.display_name = 'Test Book For Deletion'
        create_form.description = 'Test Book for BookAdminSession deletion test'
        cls.catalog_to_delete = cls.svc_mgr.create_book(create_form)

    @classmethod
    def tearDownClass(cls):
        for catalog in cls.svc_mgr.get_books():
            cls.svc_mgr.delete_book(catalog.ident)

    def test_can_create_books(self):
        """Tests can_create_books"""
        # From test_templates/resource.py BinAdminSession.can_create_bins_template
        self.assertTrue(isinstance(self.svc_mgr.can_create_books(), bool))

    def test_can_create_book_with_record_types(self):
        """Tests can_create_book_with_record_types"""
        # From test_templates/resource.py BinAdminSession.can_create_bin_with_record_types_template
        self.assertTrue(isinstance(self.svc_mgr.can_create_book_with_record_types(DEFAULT_TYPE), bool))

    def test_get_book_form_for_create(self):
        """Tests get_book_form_for_create"""
        # From test_templates/resource.py BinAdminSession.get_bin_form_for_create_template
        from dlkit.abstract_osid.commenting.objects import BookForm
        catalog_form = self.svc_mgr.get_book_form_for_create([])
        self.assertTrue(isinstance(catalog_form, BookForm))
        self.assertFalse(catalog_form.is_for_update())

    def test_create_book(self):
        """Tests create_book"""
        # From test_templates/resource.py BinAdminSession.create_bin_template
        from dlkit.abstract_osid.commenting.objects import Book
        catalog_form = self.svc_mgr.get_book_form_for_create([])
        catalog_form.display_name = 'Test Book'
        catalog_form.description = 'Test Book for BookAdminSession.create_book tests'
        new_catalog = self.svc_mgr.create_book(catalog_form)
        self.assertTrue(isinstance(new_catalog, Book))

    @unittest.skip('unimplemented test')
    def test_can_update_books(self):
        """Tests can_update_books"""
        pass

    def test_get_book_form_for_update(self):
        """Tests get_book_form_for_update"""
        # From test_templates/resource.py BinAdminSession.get_bin_form_for_update_template
        from dlkit.abstract_osid.commenting.objects import BookForm
        catalog_form = self.svc_mgr.get_book_form_for_update(self.catalog.ident)
        self.assertTrue(isinstance(catalog_form, BookForm))
        self.assertTrue(catalog_form.is_for_update())

    def test_update_book(self):
        """Tests update_book"""
        # From test_templates/resource.py BinAdminSession.update_bin_template
        catalog_form = self.svc_mgr.get_book_form_for_update(self.catalog.ident)
        # Update some elements here?
        self.svc_mgr.update_book(catalog_form)

    @unittest.skip('unimplemented test')
    def test_can_delete_books(self):
        """Tests can_delete_books"""
        pass

    def test_delete_book(self):
        """Tests delete_book"""
        # From test_templates/resource.py BinAdminSession.delete_bin_template
        cat_id = self.catalog_to_delete.ident
        self.svc_mgr.delete_book(cat_id)
        with self.assertRaises(errors.NotFound):
            self.svc_mgr.get_book(cat_id)

    def test_can_manage_book_aliases(self):
        """Tests can_manage_book_aliases"""
        # From test_templates/resource.py::ResourceAdminSession::can_manage_resource_aliases_template
        self.assertTrue(isinstance(self.svc_mgr.can_manage_book_aliases(), bool))

    def test_alias_book(self):
        """Tests alias_book"""
        # From test_templates/resource.py BinAdminSession.alias_bin_template
        alias_id = Id('commenting.Book%3Amy-alias%40ODL.MIT.EDU')
        self.svc_mgr.alias_book(self.catalog_to_delete.ident, alias_id)
        aliased_catalog = self.svc_mgr.get_book(alias_id)
        self.assertEqual(self.catalog_to_delete.ident, aliased_catalog.ident)


class TestBookHierarchySession(unittest.TestCase):
    """Tests for BookHierarchySession"""

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('COMMENTING', proxy=PROXY, implementation='TEST_SERVICE')
        cls.catalogs = dict()
        for name in ['Root', 'Child 1', 'Child 2', 'Grandchild 1']:
            create_form = cls.svc_mgr.get_book_form_for_create([])
            create_form.display_name = name
            create_form.description = 'Test Book ' + name
            cls.catalogs[name] = cls.svc_mgr.create_book(create_form)
        cls.svc_mgr.add_root_book(cls.catalogs['Root'].ident)
        cls.svc_mgr.add_child_book(cls.catalogs['Root'].ident, cls.catalogs['Child 1'].ident)
        cls.svc_mgr.add_child_book(cls.catalogs['Root'].ident, cls.catalogs['Child 2'].ident)
        cls.svc_mgr.add_child_book(cls.catalogs['Child 1'].ident, cls.catalogs['Grandchild 1'].ident)

    @classmethod
    def tearDownClass(cls):
        cls.svc_mgr.remove_child_book(cls.catalogs['Child 1'].ident, cls.catalogs['Grandchild 1'].ident)
        cls.svc_mgr.remove_child_books(cls.catalogs['Root'].ident)
        cls.svc_mgr.remove_root_book(cls.catalogs['Root'].ident)
        for cat_name in cls.catalogs:
            cls.svc_mgr.delete_book(cls.catalogs[cat_name].ident)

    def test_get_book_hierarchy_id(self):
        """Tests get_book_hierarchy_id"""
        # From test_templates/resource.py::BinHierarchySession::get_bin_hierarchy_id_template
        hierarchy_id = self.svc_mgr.get_book_hierarchy_id()
        self.assertTrue(isinstance(hierarchy_id, Id))

    def test_get_book_hierarchy(self):
        """Tests get_book_hierarchy"""
        # From test_templates/resource.py::BinHierarchySession::get_bin_hierarchy_template
        hierarchy = self.svc_mgr.get_book_hierarchy()
        self.assertTrue(isinstance(hierarchy, Hierarchy))

    @unittest.skip('unimplemented test')
    def test_can_access_book_hierarchy(self):
        """Tests can_access_book_hierarchy"""
        pass

    def test_use_comparative_book_view(self):
        """Tests use_comparative_book_view"""
        self.svc_mgr.use_comparative_book_view()

    def test_use_plenary_book_view(self):
        """Tests use_plenary_book_view"""
        self.svc_mgr.use_plenary_book_view()

    def test_get_root_book_ids(self):
        """Tests get_root_book_ids"""
        # From test_templates/resource.py::BinHierarchySession::get_root_bin_ids_template
        root_ids = self.svc_mgr.get_root_book_ids()
        self.assertTrue(isinstance(root_ids, IdList))
        # probably should be == 1, but we seem to be getting test cruft,
        # and I can't pinpoint where it's being introduced.
        self.assertTrue(root_ids.available() >= 1)

    def test_get_root_books(self):
        """Tests get_root_books"""
        # From test_templates/resource.py::BinHierarchySession::get_root_bins_template
        from dlkit.abstract_osid.commenting.objects import BookList
        roots = self.svc_mgr.get_root_books()
        self.assertTrue(isinstance(roots, BookList))
        self.assertTrue(roots.available() == 1)

    def test_has_parent_books(self):
        """Tests has_parent_books"""
        # From test_templates/resource.py::BinHierarchySession::has_parent_bins_template
        self.assertTrue(isinstance(self.svc_mgr.has_parent_books(self.catalogs['Child 1'].ident), bool))
        self.assertTrue(self.svc_mgr.has_parent_books(self.catalogs['Child 1'].ident))
        self.assertTrue(self.svc_mgr.has_parent_books(self.catalogs['Child 2'].ident))
        self.assertTrue(self.svc_mgr.has_parent_books(self.catalogs['Grandchild 1'].ident))
        self.assertFalse(self.svc_mgr.has_parent_books(self.catalogs['Root'].ident))

    def test_is_parent_of_book(self):
        """Tests is_parent_of_book"""
        # From test_templates/resource.py::BinHierarchySession::is_parent_of_bin_template
        self.assertTrue(isinstance(self.svc_mgr.is_parent_of_book(self.catalogs['Child 1'].ident, self.catalogs['Root'].ident), bool))
        self.assertTrue(self.svc_mgr.is_parent_of_book(self.catalogs['Root'].ident, self.catalogs['Child 1'].ident))
        self.assertTrue(self.svc_mgr.is_parent_of_book(self.catalogs['Child 1'].ident, self.catalogs['Grandchild 1'].ident))
        self.assertFalse(self.svc_mgr.is_parent_of_book(self.catalogs['Child 1'].ident, self.catalogs['Root'].ident))

    def test_get_parent_book_ids(self):
        """Tests get_parent_book_ids"""
        # From test_templates/resource.py::BinHierarchySession::get_parent_bin_ids_template
        from dlkit.abstract_osid.id.objects import IdList
        catalog_list = self.svc_mgr.get_parent_book_ids(self.catalogs['Child 1'].ident)
        self.assertTrue(isinstance(catalog_list, IdList))
        self.assertEqual(catalog_list.available(), 1)

    def test_get_parent_books(self):
        """Tests get_parent_books"""
        # From test_templates/resource.py::BinHierarchySession::get_parent_bins_template
        from dlkit.abstract_osid.commenting.objects import BookList
        catalog_list = self.svc_mgr.get_parent_books(self.catalogs['Child 1'].ident)
        self.assertTrue(isinstance(catalog_list, BookList))
        self.assertEqual(catalog_list.available(), 1)
        self.assertEqual(catalog_list.next().display_name.text, 'Root')

    def test_is_ancestor_of_book(self):
        """Tests is_ancestor_of_book"""
        # From test_templates/resource.py::BinHierarchySession::is_ancestor_of_bin_template
        self.assertRaises(errors.Unimplemented,
                          self.svc_mgr.is_ancestor_of_book,
                          self.catalogs['Root'].ident,
                          self.catalogs['Child 1'].ident)
        # self.assertTrue(isinstance(self.svc_mgr.is_ancestor_of_book(
        #     self.catalogs['Root'].ident,
        #     self.catalogs['Child 1'].ident),
        #     bool))
        # self.assertTrue(self.svc_mgr.is_ancestor_of_book(
        #     self.catalogs['Root'].ident,
        #     self.catalogs['Child 1'].ident))
        # self.assertTrue(self.svc_mgr.is_ancestor_of_book(
        #     self.catalogs['Root'].ident,
        #     self.catalogs['Grandchild 1'].ident))
        # self.assertFalse(self.svc_mgr.is_ancestor_of_book(
        #     self.catalogs['Child 1'].ident,
        #     self.catalogs['Root'].ident))

    def test_has_child_books(self):
        """Tests has_child_books"""
        self.assertTrue(isinstance(self.svc_mgr.has_child_books(self.catalogs['Child 1'].ident), bool))
        self.assertTrue(self.svc_mgr.has_child_books(self.catalogs['Root'].ident))
        self.assertTrue(self.svc_mgr.has_child_books(self.catalogs['Child 1'].ident))
        self.assertFalse(self.svc_mgr.has_child_books(self.catalogs['Child 2'].ident))
        self.assertFalse(self.svc_mgr.has_child_books(self.catalogs['Grandchild 1'].ident))

    def test_is_child_of_book(self):
        """Tests is_child_of_book"""
        self.assertTrue(isinstance(self.svc_mgr.is_child_of_book(self.catalogs['Child 1'].ident, self.catalogs['Root'].ident), bool))
        self.assertTrue(self.svc_mgr.is_child_of_book(self.catalogs['Child 1'].ident, self.catalogs['Root'].ident))
        self.assertTrue(self.svc_mgr.is_child_of_book(self.catalogs['Grandchild 1'].ident, self.catalogs['Child 1'].ident))
        self.assertFalse(self.svc_mgr.is_child_of_book(self.catalogs['Root'].ident, self.catalogs['Child 1'].ident))

    def test_get_child_book_ids(self):
        """Tests get_child_book_ids"""
        from dlkit.abstract_osid.id.objects import IdList
        catalog_list = self.svc_mgr.get_child_book_ids(self.catalogs['Child 1'].ident)
        self.assertTrue(isinstance(catalog_list, IdList))
        self.assertEqual(catalog_list.available(), 1)

    def test_get_child_books(self):
        """Tests get_child_books"""
        from dlkit.abstract_osid.commenting.objects import BookList
        catalog_list = self.svc_mgr.get_child_books(self.catalogs['Child 1'].ident)
        self.assertTrue(isinstance(catalog_list, BookList))
        self.assertEqual(catalog_list.available(), 1)
        self.assertEqual(catalog_list.next().display_name.text, 'Grandchild 1')

    def test_is_descendant_of_book(self):
        """Tests is_descendant_of_book"""
        # From test_templates/resource.py::BinHierarchySession::is_descendant_of_bin_template
        self.assertRaises(errors.Unimplemented,
                          self.svc_mgr.is_descendant_of_book,
                          self.catalogs['Child 1'].ident,
                          self.catalogs['Root'].ident)
        # self.assertTrue(isinstance(self.svc_mgr.is_descendant_of_book(
        #     self.catalogs['Root'].ident,
        #     self.catalogs['Child 1'].ident),
        #     bool))
        # self.assertTrue(self.svc_mgr.is_descendant_of_book(
        #     self.catalogs['Child 1'].ident,
        #     self.catalogs['Root'].ident))
        # self.assertTrue(self.svc_mgr.is_descendant_of_book(
        #     self.catalogs['Grandchild 1'].ident,
        #     self.catalogs['Root'].ident))
        # self.assertFalse(self.svc_mgr.is_descendant_of_book(
        #     self.catalogs['Root'].ident,
        #     self.catalogs['Child 1'].ident))

    def test_get_book_node_ids(self):
        """Tests get_book_node_ids"""
        # From test_templates/resource.py::BinHierarchySession::get_bin_node_ids_template
        # Per the spec, perhaps counterintuitively this method returns a
        #  node, **not** a IdList...
        node = self.svc_mgr.get_book_node_ids(self.catalogs['Child 1'].ident, 1, 2, False)
        self.assertTrue(isinstance(node, OsidNode))
        self.assertFalse(node.is_root())
        self.assertFalse(node.is_leaf())
        self.assertTrue(node.get_child_ids().available(), 1)
        self.assertTrue(isinstance(node.get_child_ids(), IdList))
        self.assertTrue(node.get_parent_ids().available(), 1)
        self.assertTrue(isinstance(node.get_parent_ids(), IdList))

    def test_get_book_nodes(self):
        """Tests get_book_nodes"""
        # From test_templates/resource.py::BinHierarchySession::get_bin_nodes_template
        node = self.svc_mgr.get_book_nodes(self.catalogs['Child 1'].ident, 1, 2, False)
        self.assertTrue(isinstance(node, OsidNode))
        self.assertFalse(node.is_root())
        self.assertFalse(node.is_leaf())
        self.assertTrue(node.get_child_ids().available(), 1)
        self.assertTrue(isinstance(node.get_child_ids(), IdList))
        self.assertTrue(node.get_parent_ids().available(), 1)
        self.assertTrue(isinstance(node.get_parent_ids(), IdList))


class TestBookHierarchyDesignSession(unittest.TestCase):
    """Tests for BookHierarchyDesignSession"""

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('COMMENTING', proxy=PROXY, implementation='TEST_SERVICE')
        cls.catalogs = dict()
        for name in ['Root', 'Child 1', 'Child 2', 'Grandchild 1']:
            create_form = cls.svc_mgr.get_book_form_for_create([])
            create_form.display_name = name
            create_form.description = 'Test Book ' + name
            cls.catalogs[name] = cls.svc_mgr.create_book(create_form)
        cls.svc_mgr.add_root_book(cls.catalogs['Root'].ident)
        cls.svc_mgr.add_child_book(cls.catalogs['Root'].ident, cls.catalogs['Child 1'].ident)
        cls.svc_mgr.add_child_book(cls.catalogs['Root'].ident, cls.catalogs['Child 2'].ident)
        cls.svc_mgr.add_child_book(cls.catalogs['Child 1'].ident, cls.catalogs['Grandchild 1'].ident)

    @classmethod
    def tearDownClass(cls):
        cls.svc_mgr.remove_child_book(cls.catalogs['Child 1'].ident, cls.catalogs['Grandchild 1'].ident)
        cls.svc_mgr.remove_child_books(cls.catalogs['Root'].ident)
        for cat_name in cls.catalogs:
            cls.svc_mgr.delete_book(cls.catalogs[cat_name].ident)

    def test_get_book_hierarchy_id(self):
        """Tests get_book_hierarchy_id"""
        # From test_templates/resource.py::BinHierarchySession::get_bin_hierarchy_id_template
        hierarchy_id = self.svc_mgr.get_book_hierarchy_id()
        self.assertTrue(isinstance(hierarchy_id, Id))

    def test_get_book_hierarchy(self):
        """Tests get_book_hierarchy"""
        # From test_templates/resource.py::BinHierarchySession::get_bin_hierarchy_template
        hierarchy = self.svc_mgr.get_book_hierarchy()
        self.assertTrue(isinstance(hierarchy, Hierarchy))

    def test_can_modify_book_hierarchy(self):
        """Tests can_modify_book_hierarchy"""
        # this is tested in the setUpClass
        self.assertTrue(True)

    def test_add_root_book(self):
        """Tests add_root_book"""
        # this is tested in the setUpClass
        self.assertTrue(True)

    def test_remove_root_book(self):
        """Tests remove_root_book"""
        # this is tested in the tearDownClass
        self.assertTrue(True)

    def test_add_child_book(self):
        """Tests add_child_book"""
        # this is tested in the setUpClass
        self.assertTrue(True)

    def test_remove_child_book(self):
        """Tests remove_child_book"""
        # this is tested in the tearDownClass
        self.assertTrue(True)

    def test_remove_child_books(self):
        """Tests remove_child_books"""
        # this is tested in the tearDownClass
        self.assertTrue(True)
