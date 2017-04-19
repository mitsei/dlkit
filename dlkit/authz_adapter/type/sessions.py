"""AuthZ Adapter implementations of type sessions."""
# pylint: disable=no-init
#     Numerous classes don't require __init__.
# pylint: disable=too-many-public-methods
#     Number of methods are defined in specification
# pylint: disable=too-many-ancestors
#     Inheritance defined in specification


from ..osid import sessions as osid_sessions
from ..osid.osid_errors import PermissionDenied, NullArgument, Unimplemented
from ..primitives import Id
from ..utilities import raise_null_argument
from dlkit.abstract_osid.type import sessions as abc_type_sessions


class TypeLookupSession(abc_type_sessions.TypeLookupSession, osid_sessions.OsidSession):
    """Adapts underlying TypeLookupSession methodswith authorization checks."""

    def can_lookup_types(self):
        raise Unimplemented()

    @raise_null_argument
    def get_type(self, namespace, identifier, authority):
        raise Unimplemented()

    @raise_null_argument
    def has_type(self, type_):
        raise Unimplemented()

    @raise_null_argument
    def get_types_by_domain(self, domain):
        raise Unimplemented()

    @raise_null_argument
    def get_types_by_authority(self, authority):
        raise Unimplemented()

    @raise_null_argument
    def get_types_by_domain_and_authority(self, domain, authority):
        raise Unimplemented()

    def get_types(self):
        raise Unimplemented()

    types = property(fget=get_types)

    @raise_null_argument
    def is_equivalent(self, type_, equivalent_type):
        raise Unimplemented()

    @raise_null_argument
    def implies_support(self, type_, base_type):
        raise Unimplemented()

    @raise_null_argument
    def has_base_type(self, type_):
        raise Unimplemented()

    @raise_null_argument
    def get_base_types(self, type_):
        raise Unimplemented()

    def get_relation_types(self):
        raise Unimplemented()

    relation_types = property(fget=get_relation_types)

    @raise_null_argument
    def get_source_types_by_relation_type(self, relation_type):
        raise Unimplemented()

    @raise_null_argument
    def get_destination_types_by_source(self, source_type):
        raise Unimplemented()

    @raise_null_argument
    def get_destination_types_by_source_and_relation_type(self, source_type, relation_type):
        raise Unimplemented()

    @raise_null_argument
    def get_destination_types_by_relation_type(self, relation_type):
        raise Unimplemented()

    @raise_null_argument
    def get_source_types_by_destination(self, destination_type):
        raise Unimplemented()

    @raise_null_argument
    def get_source_types_by_destination_and_relation_type(self, destination_type, relation_type):
        raise Unimplemented()


class TypeAdminSession(abc_type_sessions.TypeAdminSession, osid_sessions.OsidSession):
    """Adapts underlying TypeAdminSession methodswith authorization checks."""

    def can_create_types(self):
        raise Unimplemented()

    @raise_null_argument
    def get_type_form_for_create(self, type_):
        raise Unimplemented()

    @raise_null_argument
    def create_type(self, type_form):
        raise Unimplemented()

    def can_update_types(self):
        raise Unimplemented()

    @raise_null_argument
    def get_type_form_for_update(self, type_):
        raise Unimplemented()

    @raise_null_argument
    def update_type(self, type_form):
        raise Unimplemented()

    def can_delete_types(self):
        raise Unimplemented()

    @raise_null_argument
    def can_delete_type(self, type_):
        raise Unimplemented()

    @raise_null_argument
    def delete_type(self, type_):
        raise Unimplemented()

    @raise_null_argument
    def make_equivalent(self, primary_type, equivalent_type):
        raise Unimplemented()

    @raise_null_argument
    def add_base_type(self, type_, base_type):
        raise Unimplemented()

    @raise_null_argument
    def remove_base_type(self, type_, base_type):
        raise Unimplemented()

    @raise_null_argument
    def add_type_relation(self, source_type, destination_type, relation_type):
        raise Unimplemented()

    @raise_null_argument
    def remove_type_relation(self, source_type, destination_type, relation_type):
        raise Unimplemented()
