from dlkit.abstract_osid.osid import errors

from dlkit.primordium.locale.types import string as String
from dlkit.primordium.type.primitives import Type

from .utilities.testing import DLKitTestCase

WORDIGNORECASE_STRING_MATCH_TYPE = Type(**String.get_type_data('WORDIGNORECASE'))


class SearchPaginationTests(DLKitTestCase):
    def create_resource(self, name="my new resource"):
        form = self._bin.get_resource_form_for_create([])

        form.display_name = str(name)
        form.description = 'Test resource'

        return self._bin.create_resource(form)

    def setUp(self):
        super(SearchPaginationTests, self).setUp()

        self._bin = self._get_test_bin()
        for i in range(1, 20):
            self.create_resource(name=str(i))

    def tearDown(self):
        """
        Remove the test user from all groups in Membership
        Start from the smallest groupId because need to
        remove "parental" roles like for DepartmentAdmin / DepartmentOfficer
        """
        super(SearchPaginationTests, self).tearDown()

    def test_specifying_start_and_end_returns_right_objects(self):
        querier = self._bin.get_resource_query()
        querier.match_keyword('1', WORDIGNORECASE_STRING_MATCH_TYPE, True)

        searcher = self._bin.get_resource_search()
        searcher.limit_result_set(1, 5)  # should return 5 results, numbered 1, 10, 11, 12, 13

        results = self._bin.get_resources_by_search(querier, searcher)
        self.assertEqual(
            results.get_result_size(),
            5
        )
        resources_found = results.get_resources()
        self.assertEqual(
            resources_found.available(),
            5
        )

        expected_names = ['1', '10', '11', '12', '13']
        for expected_name in expected_names:
            self.assertEqual(
                resources_found.next().display_name.text,
                expected_name
            )

    def test_null_start_and_end_throws_exception(self):
        searcher = self._bin.get_resource_search()

        self.assertRaises(errors.NullArgument, searcher.limit_result_set, 1, None)
        self.assertRaises(errors.NullArgument, searcher.limit_result_set, None, 5)
        self.assertRaises(errors.NullArgument, searcher.limit_result_set, None, None)

    def test_end_less_than_start_throws_exception(self):
        searcher = self._bin.get_resource_search()

        self.assertRaises(errors.InvalidArgument, searcher.limit_result_set, 5, 1)

    def test_end_equal_to_start_throws_exception(self):
        searcher = self._bin.get_resource_search()

        self.assertRaises(errors.InvalidArgument, searcher.limit_result_set, 5, 5)

    def test_end_greater_than_total_docs_returns_everything(self):
        querier = self._bin.get_resource_query()
        querier.match_keyword('1', WORDIGNORECASE_STRING_MATCH_TYPE, True)

        searcher = self._bin.get_resource_search()
        searcher.limit_result_set(1, 25)  # should return 11 results, 1 + 10-19

        results = self._bin.get_resources_by_search(querier, searcher)
        resources_found = results.get_resources()
        self.assertEqual(
            resources_found.available(),
            11
        )

        expected_names = ['1', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19']
        for expected_name in expected_names:
            self.assertEqual(
                resources_found.next().display_name.text,
                expected_name
            )

    def test_can_search_within_an_id_list(self):
        querier = self._bin.get_resource_query()
        querier.match_keyword('1', WORDIGNORECASE_STRING_MATCH_TYPE, True)

        searcher = self._bin.get_resource_search()
        searcher.limit_result_set(1, 5)  # should return 5 results, numbered 1, 10, 11, 12, 13

        results = self._bin.get_resources_by_search(querier, searcher)
        self.assertEqual(
            results.get_result_size(),
            5
        )
        resources_found = results.get_resources()
        self.assertEqual(
            resources_found.available(),
            5
        )

        expected_names = ['1', '10', '11', '12', '13']
        new_id_to_search_on = []
        for expected_name in expected_names:
            if expected_name == '12':
                new_id_to_search_on.append(resources_found.next().ident)
            else:
                next(resources_found)

        querier = self._bin.get_resource_query()
        querier.match_keyword('2', WORDIGNORECASE_STRING_MATCH_TYPE, True)

        searcher = self._bin.get_resource_search()
        searcher.search_among_resources(new_id_to_search_on)

        results = self._bin.get_resources_by_search(querier, searcher)  # should only return "12", and not "2"
        self.assertEqual(
            results.get_result_size(),
            1
        )
        resources_found = results.get_resources()
        self.assertEqual(
            resources_found.available(),
            1
        )

        self.assertEqual(
            str(resources_found.next().ident),
            str(new_id_to_search_on[0])
        )
