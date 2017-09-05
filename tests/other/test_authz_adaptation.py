"""Unit tests of authz adapter functionality."""
import pytest
import unittest

from dlkit.runtime import PROXY_SESSION, proxy_example
from dlkit.runtime.managers import Runtime
from dlkit.abstract_osid.osid import errors
from dlkit.primordium.type.primitives import Type

from ..authorization.test_sessions import TestAuthorizationSession,\
    authorization_session_class_fixture,\
    authorization_session_test_fixture
from ..utilities.general import is_never_authz, uses_filesystem_only

JANE_REQUEST = proxy_example.SimpleRequest(username='jane_doe')
JANE_CONDITION = PROXY_SESSION.get_proxy_condition()
JANE_CONDITION.set_http_request(JANE_REQUEST)
JANE_PROXY = PROXY_SESSION.get_proxy(JANE_CONDITION)

BLUE_TYPE = Type(authority='BLUE',
                 namespace='BLUE',
                 identifier='BLUE')


@pytest.fixture(scope="function")
def authz_adapter_class_fixture(request):
    request.cls.resource_id_lists = []
    count = 0
    if not is_never_authz(request.cls.service_config) and not uses_filesystem_only(request.cls.service_config):
        for bin_ in request.cls.bin_list:
            # print bin.display_name.text, "ID =", bin.ident.identifier
            request.cls.resource_id_lists.append([])
            for color in ['Red', 'Blue', 'Red']:
                create_form = bin_.get_resource_form_for_create([])
                create_form.display_name = color + ' ' + str(count) + ' Resource'
                create_form.description = color + ' resource for authz adapter tests from Bin number ' + str(count)
                if color == 'Blue':
                    create_form.genus_type = BLUE_TYPE
                resource = bin_.create_resource(create_form)
                if count == 2 and color == 'Blue':
                    request.cls.resource_mgr.assign_resource_to_bin(resource.ident,
                                                                    request.cls.bin_id_list[7])
                request.cls.resource_id_lists[count].append(resource.ident)
            count += 1

    def test_tear_down():
        if not is_never_authz(request.cls.service_config) and not uses_filesystem_only(request.cls.service_config):
            for index, bin_ in enumerate(request.cls.bin_list):
                # print bin.display_name.text, "ID =", bin.ident.identifier
                for resource_id in request.cls.resource_id_lists[index]:
                    bin_.delete_resource(resource_id)

    request.addfinalizer(test_tear_down)

    # The hierarchy should look like this. (t) indicates where lookup is
    # explicitely authorized:
    #
    #            _____ 0 _____
    #           |             |
    #        _ 1(t) _         2
    #       |        |        |     not in hierarchy:
    #       3        4       5(t)      6     7(t)   (the 'blue' resource in bin 2 is also assigned to bin 7)


@pytest.mark.usefixtures("authz_adapter_class_fixture")
class TestAuthzAdapter(TestAuthorizationSession):

    def test_lookup_bank_0_plenary_isolated(self):
        if not is_never_authz(self.service_config) and not uses_filesystem_only(self.service_config):
            janes_resource_mgr = Runtime().get_service_manager('RESOURCE',
                                                               proxy=JANE_PROXY,
                                                               implementation='TEST_SERVICE_JSON_AUTHZ')
            bin = janes_resource_mgr.get_bin(self.bin_id_list[0])
            bin.use_isolated_bin_view()
            bin.use_plenary_resource_view()
            # with pytest.raises(errors.NotFound):
            #     resources = bin.get_resources()
            # with pytest.raises(errors.NotFound):
            #     resources = bin.get_resources_by_genus_type(BLUE_TYPE)
            # for resource_id in self.resource_id_lists[0]:
            #     with pytest.raises(errors.NotFound):
            #         resource = bin.get_resource(resource_id)
            # with pytest.raises(errors.NotFound):
            #     resources = bin.get_resources_by_ids(self.resource_id_lists[0])

    def test_lookup_bank_0_plenary_federated(self):
        if not is_never_authz(self.service_config) and not uses_filesystem_only(self.service_config):
            janes_resource_mgr = Runtime().get_service_manager('RESOURCE',
                                                               proxy=JANE_PROXY,
                                                               implementation='TEST_SERVICE_JSON_AUTHZ')
            bin = janes_resource_mgr.get_bin(self.bin_id_list[0])
            bin.use_federated_bin_view()
            bin.use_plenary_resource_view()
            assert bin.can_lookup_resources()
            assert bin.get_resources().available() == 1
            assert bin.get_resources_by_genus_type(BLUE_TYPE).available() == 1
            assert bin.get_resources_by_genus_type(BLUE_TYPE).next().ident == self.resource_id_lists[2][1]
            bin.get_resource(self.resource_id_lists[2][1])
            for resource_num in [0, 2]:
                with pytest.raises(errors.NotFound):  # Is this right?  Perhaps PermissionDenied
                    resource = bin.get_resource(self.resource_id_lists[2][resource_num])

    def test_lookup_bank_0_comparative_federated(self):
        if not is_never_authz(self.service_config) and not uses_filesystem_only(self.service_config):
            janes_resource_mgr = Runtime().get_service_manager('RESOURCE',
                                                               proxy=JANE_PROXY,
                                                               implementation='TEST_SERVICE_JSON_AUTHZ')
            bin = janes_resource_mgr.get_bin(self.bin_id_list[0])
            bin.use_federated_bin_view()
            bin.use_comparative_resource_view()
            # print "START"
            assert bin.get_resources().available() == 13
            # print "1"
            assert bin.get_resources_by_genus_type(BLUE_TYPE).available() == 5
            # print "2"
            for resource in bin.get_resources():
                bin.get_resource(resource.ident)
            # print "3" (The previous is the long one)
            resource_ids = [resource.ident for resource in bin.get_resources()]
            bin.get_resources_by_ids(resource_ids)
            # print "4"
            for resource_id in self.resource_id_lists[0]:
                with pytest.raises(errors.NotFound):
                    resource = bin.get_resource(resource_id)
            # print "5"
            resource = bin.get_resource(self.resource_id_lists[2][1])
            # print "6"
            for resource_num in [0, 2]:
                with pytest.raises(errors.NotFound):
                    resource = bin.get_resource(self.resource_id_lists[2][resource_num])
            # print "7"
            for resource_id in self.resource_id_lists[1]:
                    resource = bin.get_resource(resource_id)
            # print "8"
            for resource_id in self.resource_id_lists[3]:
                    resource = bin.get_resource(resource_id)
            # print "9"
            for resource_id in self.resource_id_lists[4]:
                    resource = bin.get_resource(resource_id)
            # print "10"
            for resource_id in self.resource_id_lists[5]:
                    resource = bin.get_resource(resource_id)

    def test_lookup_bank_0_comparative_isolated(self):
        if not is_never_authz(self.service_config) and not uses_filesystem_only(self.service_config):
            janes_resource_mgr = Runtime().get_service_manager('RESOURCE',
                                                               proxy=JANE_PROXY,
                                                               implementation='TEST_SERVICE_JSON_AUTHZ')
            bin = janes_resource_mgr.get_bin(self.bin_id_list[0])
            bin.use_isolated_bin_view()
            bin.use_comparative_resource_view()
            assert bin.get_resources().available() == 0
            assert bin.get_resources_by_genus_type(BLUE_TYPE).available() == 0

    def test_lookup_bank_1_plenary_isolated(self):
        if not is_never_authz(self.service_config) and not uses_filesystem_only(self.service_config):
            janes_resource_mgr = Runtime().get_service_manager('RESOURCE',
                                                               proxy=JANE_PROXY,
                                                               implementation='TEST_SERVICE_JSON_AUTHZ')
            bin = janes_resource_mgr.get_bin(self.bin_id_list[1])
            bin.use_isolated_bin_view()
            bin.use_plenary_resource_view()
            assert bin.get_resources().available() == 3
            assert bin.get_resources_by_genus_type(BLUE_TYPE).available() == 1

    def test_lookup_bank_1_plenary_federated(self):
        if not is_never_authz(self.service_config) and not uses_filesystem_only(self.service_config):
            janes_resource_mgr = Runtime().get_service_manager('RESOURCE',
                                                               proxy=JANE_PROXY,
                                                               implementation='TEST_SERVICE_JSON_AUTHZ')
            bin = janes_resource_mgr.get_bin(self.bin_id_list[1])
            bin.use_federated_bin_view()
            bin.use_plenary_resource_view()
            assert bin.get_resources().available() == 9
            assert bin.get_resources_by_genus_type(BLUE_TYPE).available() == 3

    def test_lookup_bank_1_comparative_federated(self):
        if not is_never_authz(self.service_config) and not uses_filesystem_only(self.service_config):
            janes_resource_mgr = Runtime().get_service_manager('RESOURCE',
                                                               proxy=JANE_PROXY,
                                                               implementation='TEST_SERVICE_JSON_AUTHZ')
            bin = janes_resource_mgr.get_bin(self.bin_id_list[1])
            bin.use_federated_bin_view()
            bin.use_comparative_resource_view()
            assert bin.get_resources().available() == 9
            assert bin.get_resources_by_genus_type(BLUE_TYPE).available() == 3

    def test_lookup_bank_1_comparative_isolated(self):
        if not is_never_authz(self.service_config) and not uses_filesystem_only(self.service_config):
            janes_resource_mgr = Runtime().get_service_manager('RESOURCE',
                                                               proxy=JANE_PROXY,
                                                               implementation='TEST_SERVICE_JSON_AUTHZ')
            bin = janes_resource_mgr.get_bin(self.bin_id_list[1])
            bin.use_isolated_bin_view()
            bin.use_comparative_resource_view()
            assert bin.get_resources().available() == 3
            assert bin.get_resources_by_genus_type(BLUE_TYPE).available() == 1

    def test_lookup_bank_2_plenary_isolated(self):
        if not is_never_authz(self.service_config) and not uses_filesystem_only(self.service_config):
            janes_resource_mgr = Runtime().get_service_manager('RESOURCE',
                                                               proxy=JANE_PROXY,
                                                               implementation='TEST_SERVICE_JSON_AUTHZ')
            bin = janes_resource_mgr.get_bin(self.bin_id_list[2])
            bin.use_isolated_bin_view()
            bin.use_plenary_resource_view()
            assert bin.get_resources().available() == 1
            assert bin.get_resources_by_genus_type(BLUE_TYPE).available() == 1
            # with pytest.raises(errors.PermissionDenied):
            #     resources = bin.get_resources()
            # with pytest.raises(errors.PermissionDenied):
            #     resources = bin.get_resources_by_genus_type(BLUE_TYPE)

    def test_lookup_bank_2_plenary_federated(self):
        if not is_never_authz(self.service_config) and not uses_filesystem_only(self.service_config):
            janes_resource_mgr = Runtime().get_service_manager('RESOURCE',
                                                               proxy=JANE_PROXY,
                                                               implementation='TEST_SERVICE_JSON_AUTHZ')
            bin = janes_resource_mgr.get_bin(self.bin_id_list[2])
            bin.use_federated_bin_view()
            bin.use_plenary_resource_view()
            assert bin.get_resources().available() == 1
            assert bin.get_resources_by_genus_type(BLUE_TYPE).available() == 1
            # with pytest.raises(errors.PermissionDenied):
            #     resources = bin.get_resources()
            # with pytest.raises(errors.PermissionDenied):
            #     resources = bin.get_resources_by_genus_type(BLUE_TYPE)

    def test_lookup_bank_2_comparative_federated(self):
        if not is_never_authz(self.service_config) and not uses_filesystem_only(self.service_config):
            janes_resource_mgr = Runtime().get_service_manager('RESOURCE',
                                                               proxy=JANE_PROXY,
                                                               implementation='TEST_SERVICE_JSON_AUTHZ')
            bin = janes_resource_mgr.get_bin(self.bin_id_list[2])
            bin.use_federated_bin_view()
            bin.use_comparative_resource_view()
            assert bin.get_resources().available() == 4
            assert bin.get_resources_by_genus_type(BLUE_TYPE).available() == 2
            # self.assertEqual(bin.get_resources().available(), 3)
            # self.assertEqual(bin.get_resources_by_genus_type(BLUE_TYPE).available(), 1)

    def test_lookup_bank_2_comparative_isolated(self):
        if not is_never_authz(self.service_config) and not uses_filesystem_only(self.service_config):
            janes_resource_mgr = Runtime().get_service_manager('RESOURCE',
                                                               proxy=JANE_PROXY,
                                                               implementation='TEST_SERVICE_JSON_AUTHZ')
            bin = janes_resource_mgr.get_bin(self.bin_id_list[2])
            bin.use_isolated_bin_view()
            bin.use_comparative_resource_view()
            assert bin.get_resources().available() == 1
            assert bin.get_resources_by_genus_type(BLUE_TYPE).available() == 1
            # with pytest.raises(errors.PermissionDenied):
            #     resources = bin.get_resources()
            # with pytest.raises(errors.PermissionDenied):
            #     resources = bin.get_resources_by_genus_type(BLUE_TYPE)

    def test_lookup_bank_3_plenary_isolated(self):
        if not is_never_authz(self.service_config) and not uses_filesystem_only(self.service_config):
            janes_resource_mgr = Runtime().get_service_manager('RESOURCE',
                                                               proxy=JANE_PROXY,
                                                               implementation='TEST_SERVICE_JSON_AUTHZ')
            bin = janes_resource_mgr.get_bin(self.bin_id_list[3])
            bin.use_isolated_bin_view()
            bin.use_plenary_resource_view()
            assert bin.get_resources().available() == 3
            assert bin.get_resources_by_genus_type(BLUE_TYPE).available() == 1

    def test_lookup_bank_3_plenary_federated(self):
        if not is_never_authz(self.service_config) and not uses_filesystem_only(self.service_config):
            janes_resource_mgr = Runtime().get_service_manager('RESOURCE',
                                                               proxy=JANE_PROXY,
                                                               implementation='TEST_SERVICE_JSON_AUTHZ')
            bin = janes_resource_mgr.get_bin(self.bin_id_list[3])
            bin.use_federated_bin_view()
            bin.use_plenary_resource_view()
            assert bin.get_resources().available() == 3
            assert bin.get_resources_by_genus_type(BLUE_TYPE).available() == 1

    def test_lookup_bank_3_comparative_federated(self):
        if not is_never_authz(self.service_config) and not uses_filesystem_only(self.service_config):
            janes_resource_mgr = Runtime().get_service_manager('RESOURCE',
                                                               proxy=JANE_PROXY,
                                                               implementation='TEST_SERVICE_JSON_AUTHZ')
            bin = janes_resource_mgr.get_bin(self.bin_id_list[3])
            bin.use_federated_bin_view()
            bin.use_comparative_resource_view()
            assert bin.get_resources().available() == 3
            assert bin.get_resources_by_genus_type(BLUE_TYPE).available() == 1

    def test_lookup_bank_3_comparative_isolated(self):
        if not is_never_authz(self.service_config) and not uses_filesystem_only(self.service_config):
            janes_resource_mgr = Runtime().get_service_manager('RESOURCE',
                                                               proxy=JANE_PROXY,
                                                               implementation='TEST_SERVICE_JSON_AUTHZ')
            bin = janes_resource_mgr.get_bin(self.bin_id_list[3])
            bin.use_isolated_bin_view()
            bin.use_comparative_resource_view()
            assert bin.get_resources().available() == 3
            assert bin.get_resources_by_genus_type(BLUE_TYPE).available() == 1

    def test_query_bank_0_isolated(self):
        if not is_never_authz(self.service_config) and not uses_filesystem_only(self.service_config):
            janes_resource_mgr = Runtime().get_service_manager('RESOURCE',
                                                               proxy=JANE_PROXY,
                                                               implementation='TEST_SERVICE_JSON_AUTHZ')
            bin = janes_resource_mgr.get_bin(self.bin_id_list[0])
            bin.use_isolated_bin_view()
            with pytest.raises(errors.PermissionDenied):
                query = bin.get_resource_query()

    def test_query_bank_0_federated(self):
        if not is_never_authz(self.service_config) and not uses_filesystem_only(self.service_config):
            janes_resource_mgr = Runtime().get_service_manager('RESOURCE',
                                                               proxy=JANE_PROXY,
                                                               implementation='TEST_SERVICE_JSON_AUTHZ')
            bin = janes_resource_mgr.get_bin(self.bin_id_list[0])
            bin.use_federated_bin_view()
            query = bin.get_resource_query()
            query.match_display_name('red')
            assert bin.get_resources_by_query(query).available() == 8
            query.clear_display_name_terms()
            query.match_display_name('blue')
            assert bin.get_resources_by_query(query).available() == 5

    def test_query_bank_1_isolated(self):
        if not is_never_authz(self.service_config) and not uses_filesystem_only(self.service_config):
            janes_resource_mgr = Runtime().get_service_manager('RESOURCE',
                                                               proxy=JANE_PROXY,
                                                               implementation='TEST_SERVICE_JSON_AUTHZ')
            bin = janes_resource_mgr.get_bin(self.bin_id_list[1])
            bin.use_isolated_bin_view()
            query = bin.get_resource_query()
            query.match_display_name('red')
            assert bin.get_resources_by_query(query).available() == 2

    def test_query_bank_1_federated(self):
        if not is_never_authz(self.service_config) and not uses_filesystem_only(self.service_config):
            janes_resource_mgr = Runtime().get_service_manager('RESOURCE',
                                                               proxy=JANE_PROXY,
                                                               implementation='TEST_SERVICE_JSON_AUTHZ')
            bin = janes_resource_mgr.get_bin(self.bin_id_list[1])
            bin.use_federated_bin_view()
            query = bin.get_resource_query()
            query.match_display_name('red')
            assert bin.get_resources_by_query(query).available() == 6
