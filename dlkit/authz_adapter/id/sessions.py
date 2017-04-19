"""AuthZ Adapter implementations of id sessions."""
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
from dlkit.abstract_osid.id import sessions as abc_id_sessions


class IdLookupSession(abc_id_sessions.IdLookupSession, osid_sessions.OsidSession):
    """Adapts underlying IdLookupSession methodswith authorization checks."""

    def can_lookup_ids(self):
        raise Unimplemented()

    @raise_null_argument
    def get_id(self, id_):
        raise Unimplemented()

    ident = property(fget=get_id)

    @raise_null_argument
    def get_ids_by_ids(self, ids):
        raise Unimplemented()

    @raise_null_argument
    def get_ids_by_authority(self, authority):
        raise Unimplemented()

    @raise_null_argument
    def get_ids_by_authority_and_namespace(self, authority, namespace):
        raise Unimplemented()

    def get_ids(self):
        raise Unimplemented()

    ids = property(fget=get_ids)

    @raise_null_argument
    def is_equivalent(self, id_, equivalent_id):
        raise Unimplemented()

    @raise_null_argument
    def get_id_aliases(self, id_):
        raise Unimplemented()

    @raise_null_argument
    def get_id_aliases_by_authority(self, id_, authority):
        raise Unimplemented()

    @raise_null_argument
    def get_id_aliases_by_authority_and_namespace(self, id_, authority, namespace):
        raise Unimplemented()


class IdIssueSession(abc_id_sessions.IdIssueSession, osid_sessions.OsidSession):
    """Adapts underlying IdIssueSession methodswith authorization checks."""

    def can_issue_ids(self):
        raise Unimplemented()

    def issue_id(self):
        raise Unimplemented()


class IdAdminSession(abc_id_sessions.IdAdminSession, osid_sessions.OsidSession):
    """Adapts underlying IdAdminSession methodswith authorization checks."""

    def can_create_ids(self):
        raise Unimplemented()

    def get_id_form_for_create(self):
        raise Unimplemented()

    id_form_for_create = property(fget=get_id_form_for_create)

    @raise_null_argument
    def create_id(self, id_form):
        raise Unimplemented()

    def can_alias_ids(self):
        raise Unimplemented()

    @raise_null_argument
    def alias_id(self, primary_id, equivalent_id):
        raise Unimplemented()

    @raise_null_argument
    def remove_alias(self, primary_id, equivalent_id):
        raise Unimplemented()
