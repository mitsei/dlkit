from __future__ import unicode_literals

import codecs
import glob
import json
import os
import shutil
import unittest

from dlkit.json_.utilities import MyIterator,\
    query_is_match, JSONClientValidated
from dlkit.runtime import RUNTIME, PROXY_SESSION
from dlkit.runtime.errors import NotFound
from dlkit.runtime.primitives import Id
from dlkit.runtime.proxy_example import SimpleRequest


def get_assessment_manager():
    request = SimpleRequest(username='tester')
    condition = PROXY_SESSION.get_proxy_condition()
    condition.set_http_request(request)
    proxy = PROXY_SESSION.get_proxy(condition)
    return RUNTIME.get_service_manager('ASSESSMENT',
                                       implementation='TEST_SERVICE_FILESYSTEM',
                                       proxy=proxy)


class TestMyIterator(unittest.TestCase):
    """Tests for MyIterator"""

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_can_use_list_as_data(self):
        """makes sure that lists passed in to MyIterator are converted to iterators"""
        test_list = [1, 2, 3]
        test_iterator = MyIterator(test_list)
        self.assertEqual(next(test_iterator), 1)
        self.assertEqual(next(test_iterator), 2)
        self.assertEqual(next(test_iterator), 3)


class TestQueryHelper(unittest.TestCase):
    """Check that the query method catches the right terms"""

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_query_with_in_returns_correct_value(self):
        """make sure the $in key is properly considered"""
        query = {
            'foo': {'$in': ['bar', 'bim']}
        }
        content_1 = {
            'foo': 'bar'
        }
        content_2 = {
            'foo': 'baz'
        }
        self.assertTrue(query_is_match(query, content_1))
        self.assertFalse(query_is_match(query, content_2))


class TestJSONClientValidated(unittest.TestCase):
    """Check various filesystem methods for save / find"""

    @staticmethod
    def _get_test_store_path(runtime):
        try:
            full_path_param_id = Id('parameter:dataStoreFullPath@json')
            full_path = runtime.get_configuration().get_value_by_parameter(full_path_param_id).get_string_value()

            path_param_id = Id('parameter:dataStorePath@json')
            rel_path = runtime.get_configuration().get_value_by_parameter(path_param_id).get_string_value()

            return os.path.join(full_path, rel_path)
        except (AttributeError, KeyError, NotFound):
            pass
        return None

    def remove_files(self):
        test_datastore = self._get_test_store_path(self.mgr._provider_manager._runtime)
        if test_datastore is not None:
            for file_ in glob.iglob(os.path.join(test_datastore, self.db, self.collection, '*')):
                os.remove(file_)

    @classmethod
    def setUpClass(cls):
        cls.mgr = get_assessment_manager()
        cls.db = 'testing'
        cls.collection = 'json_client'
        cls.client = JSONClientValidated(cls.db,
                                         collection=cls.collection,
                                         runtime=cls.mgr._provider_manager._runtime)

    def setUp(self):
        # make sure there are no json files in the test_datastore/test_json_client directory
        self.remove_files()

    def tearDown(self):
        # make sure there are no json files in the test_datastore/test_json_client directory
        self.remove_files()

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls._get_test_store_path(cls.mgr._provider_manager._runtime))

    def test_can_save_json_file(self):
        test_doc = {'_id': '123', 'foo': 'bar'}
        self.client.save(test_doc)
        # assert the file exists
        test_datastore = self._get_test_store_path(self.mgr._provider_manager._runtime)
        json_file_path = os.path.join(test_datastore,
                                      self.db,
                                      self.collection,
                                      '123.json')
        self.assertTrue(os.path.isfile(json_file_path))
        with codecs.open(json_file_path, 'rb', encoding='utf-8') as test_file:
            result = json.loads(test_file.read())
            self.assertEqual(result, test_doc)

    def test_can_search_json_files(self):
        test_doc = {'_id': '123', 'foo': 'bar'}
        self.client.save(test_doc)

        result = self.client.find({'foo': 'bar'})
        self.assertEqual(result.count(), 1)
        self.assertEqual(next(iter(result)), test_doc)

        result = self.client.find({'foo': 'bim'})
        self.assertEqual(result.count(), 0)

        result = self.client.find_one({'foo': 'bar'})
        self.assertEqual(result, test_doc)

        with self.assertRaises(NotFound):
            self.client.find_one({'foo': 'bim'})
