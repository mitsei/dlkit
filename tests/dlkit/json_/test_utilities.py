import unittest

from dlkit.json_.utilities import MyIterator, query_is_match


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
