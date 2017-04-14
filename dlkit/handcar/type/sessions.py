# -*- coding: utf-8 -*-

# This module contains all the Session classes used by the MIT Core Concept
# Catalog (MC3) Handcar based implementation of the OSID Learning Service
# specifically to manage Types.

from ...abstract_osid.type import sessions as abc_type_sessions
from ..osid import sessions as osid_sessions
from .. import settings
from ..primitives import Id, Type, DisplayText
from ..osid.osid_errors import AlreadyExists, NullArgument, InvalidArgument, NotFound, IllegalState, OperationFailed, PermissionDenied, Unsupported, Unimplemented
from . import objects
SERVICE_STRING = 'type'
CATALOGS_STRING = None


class TypeLookupSession(abc_type_sessions.TypeLookupSession, osid_sessions.OsidSession):
    """This session retrieves Types.

    A single Type can be retrieved using get_type() and all types known
    to this service can be accessed via get_types() .

    """
    def __init__(self, proxy=None, runtime=None, **kwargs):
        self._service_string = SERVICE_STRING
        self._catalogs_string = CATALOGS_STRING
        osid_sessions.OsidSession.__init__(self)
        osid_sessions.OsidSession._init_catalog(
            self,
            proxy,
            runtime
        )
        self._kwargs = kwargs

    def can_lookup_types(self):
        """Tests if this user can perform Type lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a PermissionDenied. This is intended as a
        hint to an application that may opt not to offer lookup
        operations.

        return: (boolean) - false if lookup methods are not authorized,
                true otherwise
        compliance: mandatory - This method must be implemented.

        """
        return True

    def get_type(self, namespace=None, identifier=None, authority=None):
        """Gets a Type by its string representation which is a combination
        of the authority and identifier.

        This method only returns the Type if it is known by the given
        identification components.

        arg:    namespace (string): the identifier namespace
        arg:    identifier (string): the identifier
        arg:    authority (string): the authority
        return: (osid.type.Type) - the Type
        raise:  NotFound - the type is not found
        raise:  NullArgument - null argument provided
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method must be implemented.

        """
        from . import types
        from ..osid.osid_errors import NotFound, NullArgument
        if namespace is None or identifier is None or authority is None:
            raise NullArgument()
        type_identifier = namespace + '%3A' + identifier + '%40' + authority
        url_path = '/handcar/services/learning/types/' + type_identifier
        try:
            result = self._get_request(url_path)
        except NotFound:
            result = None
            for t in types.TYPES:
                if t['id'] == type_identifier:
                    result = t
            if result is None:
                raise NotFound()
        return Type(result)

    def has_type(self, type_=None):
        """Tests if the given Type is known.

        arg:    type (osid.type.Type): the Type to look for
        return: (boolean) - true if the given Type is known, false
                otherwise
        raise:  NullArgument - type is null
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method must be implemented.

        """
        # This seems silly :)
        return bool(self.get_type(namespace=type_.get_namespace(),
                                  identifier=type_.get_identifier(),
                                  authority=type_.get_authority()))

    def get_types_by_domain(self, domain=None):
        """Gets all the known Types by domain.

        arg:    domain (string): the domain
        return: (osid.type.TypeList) - the list of Types with the given
                domain
        raise:  NullArgument - domain is null
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method must be implemented.

        """
        raise Unimplemented()

    def get_types_by_authority(self, authority=None):
        """Gets all the known Types by authority.

        arg:    authority (string): the authority
        return: (osid.type.TypeList) - the list of Types with the given
                authority
        raise:  NullArgument - authority is null
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - respect my authoritay
        compliance: mandatory - This method must be implemented.

        """
        raise Unimplemented()

    def get_types_by_domain_and_authority(self, domain=None, authority=None):
        """Gets all the known Types by domain and authority.

        arg:    domain (string): the domain
        arg:    authority (string): the authority
        return: (osid.type.TypeList) - the list of Types with the given
                domain and authority
        raise:  NullArgument - domain or authority is null
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method must be implemented.

        """
        raise Unimplemented()

    def get_types(self):
        """Gets all the known Types.

        return: (osid.type.TypeList) - the list of all known Types
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method must be implemented.

        """
        from . import types
        url_path = '/handcar/services/learning/types/'
        type_list = self._get_request(url_path)
        type_list += types.TYPES
        return objects.TypeList(type_list)

    types = property(fget=get_types)

    def is_equivalent(self, type_=None, equivalent_type=None):
        """Tests if the given types are equivalent.

        arg:    type (osid.type.Type): a type
        arg:    equivalent_type (osid.type.Type): another type
        return: (boolean) - true if both types are equivalent, false
                otherwise
        raise:  NullArgument - type is null
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method must be implemented.

        """
        raise Unimplemented()

    def implies_support(self, type_=None, base_type=None):
        """Tests if the given type is implies support of a base type.

        arg:    type (osid.type.Type): a type
        arg:    base_type (osid.type.Type): another type
        return: (boolean) - true if base_type if supported by type,
                false otherwise
        raise:  NullArgument - type or base_type is null
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method must be implemented.

        """
        raise Unimplemented()

    def has_base_type(self, type_=None):
        """Tests if the given type is derived from a base type.

        arg:    type (osid.type.Type): a type
        return: (boolean) - true is the given type is derived from a
                base type, false otherwise
        raise:  NullArgument - type is null
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method must be implemented.

        """
        raise Unimplemented()

    def get_base_types(self, type_=None):
        """Gets the immediate base types of this type.

        arg:    type (osid.type.Type): a type
        return: (osid.type.TypeList) - the base types
        raise:  NullArgument - type is null
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method must be implemented.

        """
        raise Unimplemented()

    def get_relation_types(self):
        """Gets all known relation ``Types``.

        A relation Types relates two ``Types``.

        return: (osid.type.TypeList) - known relation types
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

    relation_types = property(fget=get_relation_types)

    def get_source_types_by_relation_type(self, relation_type=None):
        """Gets all source ``Types`` related by the given type.

        arg:    relation_type (osid.type.Type): a relation type
        return: (osid.type.TypeList) - the source types
        raise:  NullArgument - ``relation_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

    def get_destination_types_by_source(self, source_type=None):
        """Gets all destination Types related to the given source ``Type``.

        arg:    source_type (osid.type.Type): a source type
        return: (osid.type.TypeList) - the related types
        raise:  NullArgument - ``source_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

    def get_destination_types_by_source_and_relation_type(self, source_type=None, relation_type=None):
        """Gets all destination Types related to the given source ``Type`` and relation ``Type``.

        arg:    source_type (osid.type.Type): a source type
        arg:    relation_type (osid.type.Type): a relation type
        return: (osid.type.TypeList) - the related types
        raise:  NullArgument - ``source_type`` or ``relation_type`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

    def get_destination_types_by_relation_type(self, relation_type=None):
        """Gets all destination ``Types`` related by the given type.

        arg:    relation_type (osid.type.Type): a relation type
        return: (osid.type.TypeList) - the destination types
        raise:  NullArgument - ``relation_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

    def get_source_types_by_destination(self, destination_type=None):
        """Gets all source Types related to the given destination ``Type``.

        arg:    destination_type (osid.type.Type): a destination type
        return: (osid.type.TypeList) - the source types
        raise:  NullArgument - ``destination_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

    def get_source_types_by_destination_and_relation_type(self, destination_type=None, relation_type=None):
        """Gets all source Types related to the given destination ``Type`` and relation ``Type``.

        arg:    destination_type (osid.type.Type): a destination type
        arg:    relation_type (osid.type.Type): a relation type
        return: (osid.type.TypeList) - the related types
        raise:  NullArgument - ``destination_type`` or ``relation_type``
                is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()
