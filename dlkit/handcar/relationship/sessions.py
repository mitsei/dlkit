# -*- coding: utf-8 -*-

# This module contains all the Session classes used by the MIT Core Concept
# Catalog (MC3) Handcar based implementation of the OSID Relationship Service.

import json
from ...abstract_osid.relationship import sessions as abc_relationship_sessions
from ...abstract_osid.relationship import objects as abc_relationship_objects
from ..osid.osid_errors import AlreadyExists, NullArgument, InvalidArgument, NotFound, IllegalState, OperationFailed, PermissionDenied, Unsupported, Unimplemented
from ..osid import sessions as osid_sessions
from ..osid import sessions as osid_sessions
from .. import settings
from . import objects
from ..id import objects as id_objects
from ..primitives import Id, Type, DisplayText
from .managers import RelationshipManager, RelationshipProxyManager

COMPARATIVE = 0
PLENARY = 1
ISOLATED = 0
FEDERATED = 1
EFFECTIVE = 0
ANY_EFFECTIVE = 1
CREATED = True
UPDATED = True
SERVICE_STRING = 'relationship'
CATALOGS_STRING = 'relationships'


class RelationshipLookupSession(abc_relationship_sessions.RelationshipLookupSession, osid_sessions.OsidSession):
    """This session defines methods for retrieving relationships.

    A ``Relationship`` is mapped to two OSID ``Ids``.

    This lookup session defines several views:

      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete result set or is an error
        condition
      * federated family view: includes relationships in families which
        are children of this family in the family hierarchy
      * isolated family view: restricts lookups to this family only
      * effective relationship view: Relationship methods return only
        relationships currently in effect.
      * any effective relationship view: Relationship methods return
        both effective and ineffective relationships.


    Relationships may have an additional records indicated by their
    respective record types. The record may not be accessed through a
    cast of the ``Relationship``.

    """

    def __init__(self, family_id=None, proxy=None, runtime=None, **kwargs):
        self._service_string = SERVICE_STRING
        self._catalogs_string = CATALOGS_STRING
        osid_sessions.OsidSession.__init__(self)
        osid_sessions.OsidSession._init_catalog(
            self,
            proxy,
            runtime
        )
        self._relationship_view = COMPARATIVE
        self._effective_relationship_view = EFFECTIVE
        self._family_view = FEDERATED
        if family_id is None:
            # For now we are just going to find the first objective bank
            # This needs to change!
            url_path = '/handcar/services/relationship/families'
            family = objects.Family(self._get_request(url_path)[0])
            self._family_id = family.get_id()
        else:
            self._family_id = family_id
        self._catalog_idstr = str(self._family_id)

    def get_family_id(self):
        """Gets the ``Family``  ``Id`` associated with this session.

        return: (osid.id.Id) - the ``Family Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._family_id

    def get_family(self):
        """Gets the ``Family`` associated with this session.

        return: (osid.relationship.Family) - the family
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        return FamilyLookupSession(proxy=self._proxy,
                                   runtime=self._runtime).get_family(self._family_id)

    def can_lookup_relationships(self):
        """Tests if this user can perform ``Relationship`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may not offer lookup operations
        to unauthorized users.

        return: (boolean) - ``false`` if lookup methods are not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # There is now a handcar call for this. Must implement
        return True

    def use_comparative_relationship_view(self):
        """The returns from the lookup methods may omit or translate elements based on this
        session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*

        """
        self._relationship_view = COMPARATIVE

    def use_plenary_relationship_view(self):
        """A complete view of the ``Relationship`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*

        """
        self._relationship_view = PLENARY

    def use_federated_family_view(self):
        """Federates the view for methods in this session.

        A federated view will include relationships in families which
        are children of this family in the family hierarchy.

        *compliance: mandatory -- This method is must be implemented.*

        """
        self._family_view = FEDERATED

    def use_isolated_family_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts retrievals to this family only.

        *compliance: mandatory -- This method is must be implemented.*

        """
        self._family_view = ISOLATED

    def use_effective_relationship_view(self):
        """Only relationships whose effective dates are current are returned by methods in this session.

        *compliance: mandatory -- This method is must be implemented.*

        """
        self._effective_relationship_view = EFFECTIVE

    def use_any_effective_relationship_view(self):
        """All relationships of any effective dates are returned by all methods in this session.

        *compliance: mandatory -- This method is must be implemented.*

        """
        self._effective_relationship_view = ANY_EFFECTIVE

    def get_relationship(self, relationship_id=None):
        """Gets the ``Relationship`` specified by its ``Id``.

        arg:    relationship_id (osid.id.Id): the ``Id`` of the
                ``Relationship`` to retrieve
        return: (osid.relationship.Relationship) - the returned
                ``Relationship``
        raise:  NotFound - no ``Relationship`` found with the given
                ``Id``
        raise:  NullArgument - ``relationship_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        if relationship_id is None:
            raise NullArgument()
        url_path = ('/handcar/services/relationship/families/' +
                    self._catalog_idstr +
                    '/relationships/' + str(relationship_id))
        return objects.Relationship(self._get_request(url_path))

    def get_relationships_by_ids(self, relationship_ids=None):
        """Gets a ``RelationshipList`` corresponding to the given ``IdList``.

        arg:    relationship_ids (osid.id.IdList): the list of ``Ids``
                to retrieve
        return: (osid.relationship.RelationshipList) - the returned
                ``Relationship list``
        raise:  NotFound - an ``Id`` was not found
        raise:  NullArgument - ``relationship_ids`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        if relationship_ids is None:
            raise NullArgument()
        relationships = []
        for i in relationship_ids:
            relationship = None
            url_path = ('/handcar/services/relationship/families/' +
                        self._catalog_idstr +
                        '/relatioships/' + str(i))
            try:
                relationship = self._get_request(url_path)
            except (NotFound, OperationFailed):
                if self._relationship_view == PLENARY:
                    raise
                else:
                    pass
            if relationship:
                if not (self._relationship_view == COMPARATIVE and
                        relationship in relationships):
                    relationships.append(relationship)
        return objects.RelationshipList(relationships)

    def get_relationships_by_genus_type(self, relationship_genus_type=None):
        """Gets a ``RelationshipList`` corresponding to the given relationship genus ``Type``
            which does not include relationships of types derived from the specified ``Type``.

        arg:    relationship_genus_type (osid.type.Type): a relationship
                genus type
        return: (osid.relationship.RelationshipList) - the returned
                ``Relationship list``
        raise:  NullArgument - ``relationship_genus_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        if relationship_genus_type is None:
            raise NullArgument()
        url_path = ('/handcar/services/relationship/families/' +
                    self._catalog_idstr + '/relationships?genustypeid=' +
                    relationship_genus_type.get_identifier())
        return objects.RelationshipList(self._get_request(url_path))

    def get_relationships_by_parent_genus_type(self, relationship_genus_type=None):
        """Gets a ``RelationshipList`` corresponding to the given relationship genus ``Type``
            and include any additional relationships with genus types derived from the specified ``Type``.

        arg:    relationship_genus_type (osid.type.Type): a relationship
                genus type
        return: (osid.relationship.RelationshipList) - the returned
                ``Relationship list``
        raise:  NullArgument - ``relationship_genus_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

    def get_relationships_by_record_type(self, relationship_record_type=None):
        """Gets a ``RelationshipList`` containing the given relationship record ``Type``.

        arg:    relationship_record_type (osid.type.Type): a
                relationship record type
        return: (osid.relationship.RelationshipList) - the returned
                ``RelationshipList``
        raise:  NullArgument - ``relationship_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

    def get_relationships_on_date(self, from_=None, to=None):
        """Gets a ``RelationshipList`` effective during the entire given date range inclusive
            but not confined to the date range.

        arg:    from (osid.calendaring.DateTime): starting date
        arg:    to (osid.calendaring.DateTime): ending date
        return: (osid.relationship.RelationshipList) - the relationships
        raise:  InvalidArgument - ``from is greater than to``
        raise:  NullArgument - ``from`` or ``to`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

    def get_relationships_for_source(self, source_id=None):
        """Gets a ``RelationshipList`` corresponding to the given peer ``Id``.

        arg:    source_id (osid.id.Id): a peer ``Id``
        return: (osid.relationship.RelationshipList) - the relationships
        raise:  NullArgument - ``source_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        if source_id is None:
            raise NullArgument()
        url_path = ('/handcar/services/relationship/families/' +
                    self._catalog_idstr + '/relationships?sourceid=' +
                    str(source_id))
        return objects.RelationshipList(self._get_request(url_path))

    def get_relationships_for_source_on_date(self, source_id=None, from_=None, to=None):
        """Gets a ``RelationshipList`` corresponding to the given peer ``Id`` and effective
            during the entire given date range inclusive but not confined to the date range.

        arg:    source_id (osid.id.Id): a peer ``Id``
        arg:    from (osid.calendaring.DateTime): starting date
        arg:    to (osid.calendaring.DateTime): ending date
        return: (osid.relationship.RelationshipList) - the relationships
        raise:  InvalidArgument - ``from is greater than to``
        raise:  NullArgument - ``source_id, from`` ,or ``to`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

    def get_relationships_by_genus_type_for_source(self, source_id=None, relationship_genus_type=None):
        """Gets a ``RelationshipList`` corresponding to the given peer ``Id`` and relationship genus ``Type.

        Relationships`` of any genus derived from the given genus are
        returned.

        In plenary mode, the returned list contains all of the
        relationships corresponding to the given peer, including
        duplicates, or an error results if a relationship is
        inaccessible. Otherwise, inaccessible ``Relationships`` may be
        omitted from the list and may present the elements in any order
        including returning a unique set.

        In effective mode, relationships are returned that are currently
        effective. In any effective mode, effective relationships and
        those currently expired are returned.

        arg:    source_id (osid.id.Id): a peer ``Id``
        arg:    relationship_genus_type (osid.type.Type): a relationship
                genus type
        return: (osid.relationship.RelationshipList) - the relationships
        raise:  NullArgument - ``source_id`` or
                ``relationship_genus_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*
        """
        if source_id is None or relationship_genus_type is None:
            raise NullArgument()
        url_path = ('/handcar/services/relationship/families/' +
                    self._catalog_idstr + '/relationships?genustypeid=' +
                    relationship_genus_type.get_identifier + '?sourceid=' +
                    str(source_id))
        return objects.RelationshipList(self._get_request(url_path))

    def get_relationships_by_genus_type_for_source_on_date(self,
                                                           source_id=None,
                                                           relationship_genus_type=None,
                                                           from_=None,
                                                           to=None):
        """Gets a ``RelationshipList`` corresponding to the given peer ``Id`` and relationship genus
            ``Type`` and effective during the entire given date range inclusive but not confined
            to the date range.

        arg:    source_id (osid.id.Id): a peer ``Id``
        arg:    relationship_genus_type (osid.type.Type): a relationship
                genus type
        arg:    from (osid.calendaring.DateTime): starting date
        arg:    to (osid.calendaring.DateTime): ending date
        return: (osid.relationship.RelationshipList) - the relationships
        raise:  InvalidArgument - ``from is greater than to``
        raise:  NullArgument - ``source_id, relationship_genus_type,
                from`` or ``to`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

    def get_relationships_for_destination(self, destination_id=None):
        """Gets a ``RelationshipList`` corresponding to the given peer ``Id``.

        arg:    destination_id (osid.id.Id): a peer ``Id``
        return: (osid.relationship.RelationshipList) - the relationships
        raise:  NullArgument - ``destination_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        if destination_id is None:
            raise NullArgument()
        url_path = ('/handcar/services/relationship/families/' +
                    self._catalog_idstr + '/relationships?sourceid=' +
                    str(destination_id))
        return objects.RelationshipList(self._get_request(url_path))

    def get_relationships_for_destination_on_date(self, destination_id=None, from_=None, to=None):
        """Gets a ``RelationshipList`` corresponding to the given peer ``Id`` with a starting effective
            date in the given range inclusive.

        arg:    destination_id (osid.id.Id): a peer ``Id``
        arg:    from (osid.calendaring.DateTime): starting date
        arg:    to (osid.calendaring.DateTime): ending date
        return: (osid.relationship.RelationshipList) - the relationships
        raise:  InvalidArgument - ``from is greater than to``
        raise:  NullArgument - ``destination_id, from`` ,or ``to`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

    def get_relationships_by_genus_type_for_destination(self, destination_id=None, relationship_genus_type=None):
        """Gets a ``RelationshipList`` corresponding to the given peer ``Id`` and relationship genus ``Type.

        Relationships`` of any genus derived from the given genus are
        returned.

        In plenary mode, the returned list contains all of the
        relationships corresponding to the given peer, including
        duplicates, or an error results if a relationship is
        inaccessible. Otherwise, inaccessible ``Relationships`` may be
        omitted from the list and may present the elements in any order
        including returning a unique set.

        In effective mode, relationships are returned that are currently
        effective. In any effective mode, effective relationships and
        those currently expired are returned.

        arg:    destination_id (osid.id.Id): a peer ``Id``
        arg:    relationship_genus_type (osid.type.Type): a relationship
                genus type
        return: (osid.relationship.RelationshipList) - the relationships
        raise:  NullArgument - ``destination_id`` or
                ``relationship_genus_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        if destination_id is None or relationship_genus_type is None:
            raise NullArgument()
        url_path = ('/handcar/services/relationship/families/' +
                    self._catalog_idstr + '/relationships?genustypeid=' +
                    relationship_genus_type.get_identifier + '?sourceid=' +
                    str(destination_id))
        return objects.RelationshipList(self._get_request(url_path))

    def get_relationships_by_genus_type_for_destination_on_date(self,
                                                                destination_id=None,
                                                                relationship_genus_type=None,
                                                                from_=None,
                                                                to=None):
        """Gets a ``RelationshipList`` corresponding to the given peer ``Id`` and relationship genus
            ``Type`` and effective during the entire given date range inclusive but not confined
            to the date range.

        arg:    destination_id (osid.id.Id): a peer ``Id``
        arg:    relationship_genus_type (osid.type.Type): a relationship
                genus type
        arg:    from (osid.calendaring.DateTime): starting date
        arg:    to (osid.calendaring.DateTime): ending date
        return: (osid.relationship.RelationshipList) - the relationships
        raise:  InvalidArgument - ``from is greater than to``
        raise:  NullArgument - ``destination_id,
                relationship_genus_type, from`` or ``to`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

    def get_relationships_for_peers(self, source_id=None, destination_id=None):
        """Gets a ``RelationshipList`` corresponding to the given peer ``Ids``.

        arg:    source_id (osid.id.Id): a peer ``Id``
        arg:    destination_id (osid.id.Id): a related peer ``Id``
        return: (osid.relationship.RelationshipList) - the relationships
        raise:  NullArgument - ``source_id`` or ``destination_id`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

    def get_relationships_for_peers_on_date(self, source_id=None, destination_id=None, from_=None, to=None):
        """Gets a ``RelationshipList`` corresponding to the given peer ``Ids`` and effective during
            the entire given date range inclusive but not confined to the date range.

        arg:    source_id (osid.id.Id): a peer ``Id``
        arg:    destination_id (osid.id.Id): a related peer ``Id``
        arg:    from (osid.calendaring.DateTime): starting date
        arg:    to (osid.calendaring.DateTime): ending date
        return: (osid.relationship.RelationshipList) - the relationships
        raise:  InvalidArgument - ``from`` is greater than ``to``
        raise:  NullArgument - ``source_id, destination_id, from`` or
                ``to`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

    def get_relationships_by_genus_type_for_peers(self,
                                                  source_id=None,
                                                  destination_id=None,
                                                  relationship_genus_type=None):
        """Gets a ``RelationshipList`` corresponding between the given peer ``Ids`` and relationship genus ``Type.

        Relationships`` of any genus derived from the given genus are
        returned.

        In plenary mode, the returned list contains all of the
        relationships corresponding to the given peer or an error
        results if a relationship is inaccessible. Otherwise,
        inaccessible ``Relationships`` may be omitted from the list.

        In effective mode, relationships are returned that are currently
        effective. In any effective mode, effective relationships and
        those currently expired are returned.

        arg:    source_id (osid.id.Id): a peer ``Id``
        arg:    destination_id (osid.id.Id): a related peer ``Id``
        arg:    relationship_genus_type (osid.type.Type): a relationship
                genus type
        return: (osid.relationship.RelationshipList) - the relationships
        raise:  NullArgument - ``source_id, destination_id,`` or
                ``relationship_genus_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

    def get_relationships_by_genus_type_for_peers_on_date(self,
                                                          source_id=None,
                                                          destination_id=None,
                                                          relationship_genus_type=None,
                                                          from_=None,
                                                          to=None):
        """Gets a ``RelationshipList`` effective during the entire given date range inclusive
            but not confined to the date range.

        arg:    source_id (osid.id.Id): a peer ``Id``
        arg:    destination_id (osid.id.Id): a related peer ``Id``
        arg:    relationship_genus_type (osid.type.Type): a relationship
                genus type
        arg:    from (osid.calendaring.DateTime): starting date
        arg:    to (osid.calendaring.DateTime): ending date
        return: (osid.relationship.RelationshipList) - the relationships
        raise:  InvalidArgument - ``from is greater than to``
        raise:  NullArgument - ``source_id, destination_id,
                relationship_genus_type, from`` or ``to`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

    def get_relationships(self):
        """Gets all ``Relationships``.

        return: (osid.relationship.RelationshipList) - a list of
                ``Relationships``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        url_path = ('/handcar/services/relationship/families/' +
                    self._catalog_idstr + '/relationships')
        return objects.RelationshipList(self._get_request(url_path))

    family_id = property(get_family_id)
    family = property(get_family)
    relationships = property(get_relationships)


class RelationshipQuerySession(abc_relationship_sessions.RelationshipQuerySession, osid_sessions.OsidSession):
    """This session provides methods for searching among ``Relationship`` objects.

    The search query is constructed using the ``Relationship``.

    Relationships may have a query record indicated by their respective
    record types. The query record is accessed via the
    ``RelationshipQuery``.

    """
    def get_family_id(self):
        """Gets the ``Family``  ``Id`` associated with this session.

        return: (osid.id.Id) - the ``Family Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin_id
        return self._catalog_id

    def get_family(self):
        """Gets the ``Family`` associated with this session.

        return: (osid.relationship.Family) - the family
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin
        from ..osid.osid_errors import OperationFailed, PermissionDenied
        from .objects import Family
        try:
            return Family(self.my_catalog_model)
        except:
            raise OperationFailed()

    def use_federated_family_view(self):
        """Federates the view for methods in this session.

        A federated view will include relationships in families which
        are children of this family in the family hierarchy.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_federated_bin_view
        self._catalog_view = self.FEDERATED

    def use_isolated_family_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts retrievals to this family only.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_isolated_bin_view
        self._catalog_view = self.ISOLATED

    def can_search_relationships(self):
        """Tests if this user can perform ``Relationship`` searches.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.

        return: (boolean) - ``false`` if search methods are not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def get_relationship_query(self):
        """Gets a relationship query.

        return: (osid.relationship.RelationshipQuery) - the relationship
                query
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def get_relationships_by_query(self, relationship_query=None):
        """Gets a list of ``Relationships`` matching the given relationship query.

        arg:    relationship_query
                (osid.relationship.RelationshipQuery): the relationship
                query
        return: (osid.relationship.RelationshipList) - the returned
                ``RelationshipList``
        raise:  NullArgument - ``relationship_query`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - ``relationship_query`` is not of this
                service
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class RelationshipSearchSession(abc_relationship_sessions.RelationshipSearchSession, RelationshipQuerySession):
    """This session provides methods for searching among ``Relationship`` objects.

    The search query is constructed using the ``Relationship``.

    ``get_relationships_by_query()`` is the basic search method and
    returns a list of ``Relationships``. A more advanced search may be
    performed with ``getRelationshipsBySearch()``. It accepts a
    ``RelationshipSearch`` in addition to the query for the purpose of
    specifying additional options affecting the entire search, such as
    ordering. ``get_relationships_by_search()`` returns a
    ``RelationshipSearchResults`` that can be used to access the
    resulting ``RelationshipList`` or be used to perform a search within
    the result set through ``RelationshipSearch``.

    Relationships may have a query record indicated by their respective
    record types. The query record is accessed via the
    ``RelationshipQuery``.

    """
    def get_relationship_search(self):
        """Gets a relationship search.

        return: (osid.relationship.RelationshipSearch) - the
                relationship search
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def get_relationship_search_order(self):
        """Gets a relationship search order.

        The ``RelationshipSearchOrder`` is supplied to a
        ``RelationshipSearch`` to specify the ordering of results.

        return: (osid.relationship.RelationshipSearchOrder) - the
                relationship search order
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def get_relationships_by_search(self, relationship_query=None, relationship_search=None):
        """Gets the search results matching the given search query using the given search.

        arg:    relationship_query
                (osid.relationship.RelationshipQuery): the relationship
                query
        arg:    relationship_search
                (osid.relationship.RelationshipSearch): the relationship
                search
        return: (osid.relationship.RelationshipSearchResults) - the
                returned search results
        raise:  NullArgument - ``relationship_query`` or
                ``relationship_search`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - ``relationship_query`` or
                ``relationship_search`` is not of this service
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def get_relationship_query_from_inspector(self, relationship_query_inspector=None):
        """Gets a relationship query from an inspector.

        The inspector is available from a ``RelationshipSearchResults``.

        arg:    relationship_query_inspector
                (osid.relationship.RelationshipQueryInspector): a
                relationship query inspector
        return: (osid.relationship.RelationshipQuery) - the relationship
                query
        raise:  NullArgument - ``relationship_query_inspector`` is
                ``null``
        raise:  Unsupported - ``relationship_query_inspector`` is not of
                this service
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class RelationshipAdminSession(abc_relationship_sessions.RelationshipAdminSession, osid_sessions.OsidSession):
    """This session creates, updates, and deletes ``Relationships``.

    The data for create and update is provided by the consumer via the
    form object. ``OsidForms`` are requested for each create or update
    and may not be reused.

    Create and update operations differ in their usage. To create a
    ``Relationship,`` a ``RelationshipForm`` is requested using
    ``get_relationship_form_for_create()`` specifying the desired peers
    and record ``Types`` or none if no record ``Types`` are needed. The
    returned ``RelationshipForm`` will indicate that it is to be used
    with a create operation and can be used to examine metdata or
    validate data prior to creation. Once the ``RelationshipForm`` is
    submiited to a create operation, it cannot be reused with another
    create operation unless the first operation was unsuccessful. Each
    ``RelationshipForm`` corresponds to an attempted transaction.

    For updates, ``RelationshipForms`` are requested to the
    ``Relationship``  ``Id`` that is to be updated using
    ``getRelationshipFormForUpdate()``. Similarly, the
    ``RelationshipForm`` has metadata about the data that can be updated
    and it can perform validation before submitting the update. The
    ``RelationshipForm`` can only be used once for a successful update
    and cannot be reused.

    The delete operations delete ``Relationships``. To unmap a
    ``Relationship`` from the current ``Family,`` the
    ``RelationshipFamilyAssignmentSession`` should be used. These delete
    operations attempt to remove the ``Relationship`` itself thus
    removing it from all known ``Family`` catalogs.

    This session includes an ``Id`` aliasing mechanism to assign an
    external ``Id`` to an internally assigned Id.

    """
    def __init__(self, family_id=None, proxy=None, runtime=None, **kwargs):
        self._service_string = SERVICE_STRING
        self._catalogs_string = CATALOGS_STRING
        osid_sessions.OsidSession.__init__(self)
        osid_sessions.OsidSession._init_catalog(
            self,
            proxy,
            runtime
        )
        if family_id is None:
            # For now we are just going to find the first objective bank
            # This needs to change!
            url_path = '/handcar/services/relationship/families'
            family = objects.Family(self._get_request(url_path)[0])
            self._family_id = family.get_id()
        else:
            self._family_id = family_id
        self._catalog_idstr = str(self._family_id)
        self._forms = dict()

    def get_family_id(self):
        """Gets the ``Familt``  ``Id`` associated with this session.

        return: (osid.id.Id) - the ``Family Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._family_id

    def get_family(self):
        """Gets the ``Family`` associated with this session.

        return: (osid.relationship.Family) - the family
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        return FamilyLookupSession().get_family(self._family_id)

    def can_create_relationships(self):
        """Tests if this user can create ``Relationships`` A return of true does not
            guarantee successful authorization.

        A return of false indicates that it is known creating a
        ``Relationship`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        create operations to an unauthorized user.

        return: (boolean) - ``false`` if ``Relationship`` creation is
                not authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return True

    def can_create_relationship_with_record_types(self, relationship_record_types=None):
        """Tests if this user can create a single ``Relationship`` using the desired record types.

        While ``RelationshipManager.getRelationshipRecordTypes()`` can
        be used to examine which records are supported, this method
        tests which record(s) are required for creating a specific
        ``Relationship``. Providing an empty array tests if a
        ``Relationship`` can be created with no records.

        arg:    relationship_record_types (osid.type.Type[]): array of
                relationship record types
        return: (boolean) - ``true`` if ``Relationship`` creation using
                the specified record ``Types`` is supported, ``false``
                otherwise
        raise:  NullArgument - ``relationship_record_types`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        return True

    def get_relationship_form_for_create(self, source_id=None, destination_id=None, relationship_record_types=None):
        """Gets the relationship form for creating new relationships.

        A new form should be requested for each create transaction.

        arg:    source_id (osid.id.Id): ``Id`` of a peer
        arg:    destination_id (osid.id.Id): ``Id`` of the related peer
        arg:    relationship_record_types (osid.type.Type[]): array of
                relationship record types
        return: (osid.relationship.RelationshipForm) - the relationship
                form
        raise:  NotFound - ``source_id`` or ``destination_id`` is not
                found
        raise:  NullArgument - ``source_id`` or ``destination_id`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - unable to get form for requested recod
                types
        *compliance: mandatory -- This method must be implemented.*

        """
        if source_id is None or destination_id is None:
            raise NullArgument()
        if relationship_record_types is None:
            pass  # Still need to deal with the record_types argument
        relationship_form = objects.RelationshipForm(osid_object_map=None,
                                                     source_id=source_id,
                                                     destination_id=destination_id)
        self._forms[relationship_form.get_id().get_identifier()] = not CREATED
        return relationship_form

    def create_relationship(self, relationship_form=None):
        """Creates a new ``Relationship``.

        arg:    relationship_form (osid.relationship.RelationshipForm):
                the form for this ``Relationship``
        return: (osid.relationship.Relationship) - the new
                ``Relationship``
        raise:  IllegalState - ``relationship_form`` already used in a
                create transaction
        raise:  InvalidArgument - one or more of the form elements is
                invalid
        raise:  NullArgument - ``relationship_form`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - ``relationship_form`` did not originate
                from ``get_relationship_form_for_create()``
        *compliance: mandatory -- This method must be implemented.*

        """
        if relationship_form is None:
            raise NullArgument()
        if not isinstance(relationship_form, abc_relationship_objects.RelationshipForm):
            raise InvalidArgument('argument type is not a RelationshipForm')
        if relationship_form.is_for_update():
            raise InvalidArgument('form is for update only, not create')
        try:
            if self._forms[relationship_form.get_id().get_identifier()] == CREATED:
                raise IllegalState('form already used in a create transaction')
        except KeyError:
            raise Unsupported('form did not originate from this session')
        if not relationship_form.is_valid():
            raise InvalidArgument('one or more of the form elements is invalid')

        url_path = ('/handcar/services/relationship/families/' +
                    self._catalog_idstr + '/relationships')
        try:
            result = self._post_request(url_path, relationship_form._my_map)
        except Exception:
            raise  # OperationFailed
        self._forms[relationship_form.get_id().get_identifier()] = CREATED
        return objects.Relationship(result)

    def can_update_relationships(self):
        """Tests if this user can update ``Relationships``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a
        ``Relationship`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        update operations to an unauthorized user.

        return: (boolean) - ``false`` if ``Relationship`` modification
                is not authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return True

    def get_relationship_form_for_update(self, relationship_id=None):
        """Gets the relationship form for updating an existing relationship.

        A new relationship form should be requested for each update
        transaction.

        arg:    relationship_id (osid.id.Id): the ``Id`` of the
                ``Relationship``
        return: (osid.relationship.RelationshipForm) - the relationship
                form
        raise:  NotFound - ``relationship_id`` is not found
        raise:  NullArgument - ``relationship_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        if relationship_id is None:
            raise NullArgument()
        try:
            url_path = ('/handcar/services/relationship/families/' +
                        self._catalog_idstr + '/relationships/' + str(relationship_id))
            relationship = objects.Relationship(self._get_request(url_path))
        except Exception:
            raise
        relationship_form = objects.RelationshipForm(relationship._my_map)
        self._forms[relationship_form.get_id().get_identifier()] = not UPDATED
        return relationship_form

    def update_relationship(self, relationship_id=None, relationship_form=None):
        """Updates an existing relationship.

        arg:    relationship_id (osid.id.Id): the ``Id`` of the
                ``Relationship``
        arg:    relationship_form (osid.relationship.RelationshipForm):
                the form containing the elements to be updated
        raise:  IllegalState - ``relationship_form`` already used in an
                update transaction
        raise:  InvalidArgument - the form contains an invalid value
        raise:  NullArgument - ``relationship_form`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - ``relationship_form`` did not originate
                from ``get_relationship_form_for_update()``
        *compliance: mandatory -- This method must be implemented.*

        """
        if relationship_id is None or relationship_form is None:
            raise NullArgument()
        if not isinstance(relationship_form, objects.RelationshipForm):
            raise InvalidArgument('argument type is not an RelationshipForm')
        if not relationship_form.is_for_update():
            raise InvalidArgument('form is for create only, not update')
        try:
            if self._forms[relationship_form.get_id().get_identifier()] == UPDATED:
                raise IllegalState('form already used in an update transaction')
        except KeyError:
            raise Unsupported('form did not originate from this session')
        if not relationship_form.is_valid():
            raise InvalidArgument('one or more of the form elements is invalid')

        url_path = ('/handcar/services/relationship/families/' +
                    self._catalog_idstr + '/relationships')
        try:
            result = self._put_request(url_path, relationship_form._my_map)
        except Exception:
            raise  # OperationFailed
        self._forms[relationship_form.get_id().get_identifier()] = UPDATED
        return objects.Relationship(result)  # Not expected to return anything

    def can_delete_relationships(self):
        """Tests if this user can delete ``Relationships``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a
        ``Relationship`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        delete operations to an unauthorized user.

        return: (boolean) - ``false`` if ``Relationship`` deletion is
                not authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return True

    def delete_relationship(self, relationship_id=None):
        """Deletes a ``Relationship``.

        arg:    relationship_id (osid.id.Id): the ``Id`` of the
                ``Relationship`` to remove
        raise:  NotFound - ``relationship_id`` not found
        raise:  NullArgument - ``relationship_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        if relationship_id is None:
            raise NullArgument()
        if not isinstance(relationship_id, Id):
            raise InvalidArgument('argument type is not an osid Id')

        url_path = ('/handcar/services/relationship/families/' +
                    self._catalog_idstr + '/relationships/' +
                    str(relationship_id))
        result = self._delete_request(url_path)
        return objects.Relationship(result)  # Not expected to return anything

    def can_manage_relationship_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Relationships``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        return: (boolean) - ``false`` if ``Relationship`` aliasing is
                not authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False  # Not yet implemented

    def alias_relationship(self, relationship_id=None, alias_id=None):
        """Adds an ``Id`` to a ``Relationship`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``Relationship`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another relationship, it is
        reassigned to the given relationship ``Id``.

        arg:    relationship_id (osid.id.Id): the ``Id`` of a
                ``Relationship``
        arg:    alias_id (osid.id.Id): the alias ``Id``
        raise:  AlreadyExists - ``alias_id`` is already assigned
        raise:  NotFound - ``relationship`` not found
        raise:  NullArgument - ``relationship_id`` or ``alias_id`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

    family_id = property(get_family_id)
    family = property(get_family)


class RelationshipNotificationSession(abc_relationship_sessions.RelationshipNotificationSession,
                                      osid_sessions.OsidSession):
    """This session defines methods to receive notifications on adds/changes to ``Relationship``
        objects in this ``Family``.

    This also includes existing relationships that may appear or
    disappear due to changes in the ``Family`` hierarchy, This session
    is intended for consumers needing to synchronize their state with
    this service without the use of polling. Notifications are cancelled
    when this session is closed.

    The two views defined in this session correspond to the views in the
    ``RelationshipLookupSession``.

    """

    def get_family_id(self):
        """Gets the ``Family``  ``Id`` associated with this session.

        return: (osid.id.Id) - the ``Family Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin_id
        return self._catalog_id

    def get_family(self):
        """Gets the ``Family`` associated with this session.

        return: (osid.relationship.Family) - the family
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin
        from ..osid.osid_errors import OperationFailed, PermissionDenied
        from .objects import Family
        try:
            return Family(self.my_catalog_model)
        except:
            raise OperationFailed()

    def can_register_for_relationship_notifications(self):
        """Tests if this user can register for ``Relationship`` notifications.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.

        return: (boolean) - ``false`` if notification methods are not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def use_federated_family_view(self):
        """Federates the view for methods in this session.

        A federated view will include relationships in families which
        are children of this family in the family hierarchy.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_federated_bin_view
        self._catalog_view = self.FEDERATED

    def use_isolated_family_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts notifications to this family only.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_isolated_bin_view
        self._catalog_view = self.ISOLATED

    def register_for_new_relationships(self):
        """Register for notifications of new relationships.

        ``RelationshipReceiver.newRelationship()`` is invoked when a new
        ``Relationship`` appears in this family.

        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def register_for_new_relationships_for_peer(self, peer_id=None):
        """Register for notifications of new relationships.

        ``RelationshipReceiver.newRelationship()`` is invoked when a new
        ``Relationship`` appears for the given peer.

        arg:    peer_id (osid.id.Id): the ``Id`` of a peer to monitor
        raise:  NullArgument - ``peer_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def register_for_new_relationships_by_genus_type(self, relationship_genus_type=None):
        """Register for notifications of new relationships.

        ``RelationshipReceiver.newRelationship()`` is invoked when a new
        ``Relationship`` appears for the given peer.

        arg:    relationship_genus_type (osid.type.Type): the genus type
                of the ``Relationship`` to monitor
        raise:  NullArgument - ``relationship_genus_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def register_for_changed_relationships(self):
        """Registers for notification of updated relationships.

        ``RelationshipReceiver.changedRelationship()`` is invoked when a
        relationship in this family is changed.

        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def register_for_changed_relationships_for_peer(self, peer_id=None):
        """Register for notifications of updated relationships.

        ``RelationshipReceiver.changedRelationship()`` is invoked when a
        ``Relationship`` if changed for the given peer.

        arg:    peer_id (osid.id.Id): the ``Id`` of a peer to monitor
        raise:  NullArgument - ``peer_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def register_for_changed_relationships_by_genus_type(self, relationship_genus_type=None):
        """Register for notifications of updated relationships.

        ``RelationshipReceiver.changedRelationship()`` is invoked when a
        ``Relationship`` if changed for the given peer.

        arg:    relationship_genus_type (osid.type.Type): the genus type
                of the ``Relationship`` to monitor
        raise:  NullArgument - ``relationship_genus_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def register_for_changed_relationship(self, relationship_id=None):
        """Registers for notification of an updated relationship.

        ``RelationshipReceiver.changedRelationship()`` is invoked when
        the specified relationship in this family is changed.

        arg:    relationship_id (osid.id.Id): the ``Id`` of the
                ``Relationship`` to monitor
        raise:  NullArgument - ``relationship_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def register_for_deleted_relationships(self):
        """Registers for notification of deleted relationships.

        ``RelationshipReceiver.deletedRelationship()`` is invoked when a
        relationship is deleted or removed from this family.

        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def register_for_deleted_relationships_for_peer(self, peer_id=None):
        """Register for notifications of deleted relationships.

        ``RelationshipReceiver.deletedRelationship()`` is invoked when a
        ``Relationship`` if removed for the given peer.

        arg:    peer_id (osid.id.Id): the ``Id`` of a peer to monitor
        raise:  NullArgument - ``peer_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def register_for_deleted_relationships_by_genus_type(self, relationship_genus_type=None):
        """Register for notifications of deleted relationships.

        ``RelationshipReceiver.deletedRelationship()`` is invoked when a
        ``Relationship`` if removed for the given peer.

        arg:    relationship_genus_type (osid.type.Type): the genus type
                of the ``Relationship`` to monitor
        raise:  NullArgument - ``relationship_genus_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def register_for_deleted_relationship(self, relationship_id=None):
        """Registers for notification of a deleted relationship.

        ``RelationshipReceiver.deletedRelationship()`` is invoked when
        the specified relationship is deleted or removed from this
        family.

        arg:    relationship_id (osid.id.Id): the ``Id`` of the
                ``Relationship`` to monitor
        raise:  NullArgument - ``relationship_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class RelationshipFamilySession(abc_relationship_sessions.RelationshipFamilySession, osid_sessions.OsidSession):
    """This session provides methods to retrieve ``Relationship`` to ``Family`` mappings.

    A ``Relationship`` may appear in multiple ``Family`` objects. Each
    catalog may have its own authorizations governing who is allowed to
    look at it.

    This lookup session defines several views:

      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete result set or is an error
        condition


    """

    def can_lookup_relationship_family_mappings(self):
        """Tests if this user can perform lookups of relationship/family mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known lookup methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        return: (boolean) - ``false`` if looking up mappings is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def use_comparative_family_view(self):
        """The returns from the lookup methods may omit or translate elements based on this
            session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_plenary_family_view(self):
        """A complete view of the ``Relationship`` and ``Family`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def get_relationship_ids_by_family(self, family_id=None):
        """Gets the list of ``Relationship Ids`` associated with a ``Family``.

        arg:    family_id (osid.id.Id): ``Id`` of the ``Family``
        return: (osid.id.IdList) - list of related relationship ``Ids``
        raise:  NotFound - ``family_id`` is not found
        raise:  NullArgument - ``family_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def get_relationships_by_family(self, family_id=None):
        """Gets the list of ``Relationships`` associated with a ``Family``.

        arg:    family_id (osid.id.Id): ``Id`` of the ``Family``
        return: (osid.relationship.RelationshipList) - list of related
                relationships
        raise:  NotFound - ``family_id`` is not found
        raise:  NullArgument - ``family_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def get_relationship_ids_by_families(self, family_ids=None):
        """Gets the list of ``Relationship Ids`` corresponding to a list of ``Family`` objects.

        arg:    family_ids (osid.id.IdList): list of family ``Ids``
        return: (osid.id.IdList) - list of relationship ``Ids``
        raise:  NullArgument - ``family_ids`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def get_relationships_by_families(self, family_ids=None):
        """Gets the list of ``Relationships`` corresponding to a list of ``Family`` objects.

        arg:    family_ids (osid.id.IdList): list of family ``Ids``
        return: (osid.relationship.RelationshipList) - list of
                relationships
        raise:  NullArgument - ``family_ids`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def get_family_ids_by_relationship(self, relationship_id=None):
        """Gets the ``Family``  ``Ids`` mapped to a ``Relationship``.

        arg:    relationship_id (osid.id.Id): ``Id`` of a
                ``Relationship``
        return: (osid.id.IdList) - list of family ``Ids``
        raise:  NotFound - ``relationship_id`` is not found
        raise:  NullArgument - ``relationship_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def get_families_by_relationship(self, relationship_id=None):
        """Gets the ``Family`` objects mapped to a ``Relationship``.

        arg:    relationship_id (osid.id.Id): ``Id`` of a
                ``Relationship``
        return: (osid.relationship.FamilyList) - list of family ``Ids``
        raise:  NotFound - ``relationship_id`` is not found
        raise:  NullArgument - ``relationship_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class RelationshipFamilyAssignmentSession(abc_relationship_sessions.RelationshipFamilyAssignmentSession,
                                          osid_sessions.OsidSession):
    """This session provides methods to re-assign ``Relationships`` to ``Family`` objects A
        ``Relationship`` may appear in multiple ``Family`` objects and removing the last reference
        to a ``Relationship`` is the equivalent of deleting it.

    Each ``Family`` may have its own authorizations governing who is
    allowed to operate on it.

    Moving or adding a reference of a ``Relationship`` to another
    ``Family`` is not a copy operation (eg: does not change its ``Id``
    ).

    """

    def can_assign_relationships(self):
        """Tests if this user can alter relationship/family mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        return: (boolean) - ``false`` if mapping is not authorized,
                ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def can_assign_relationships_to_family(self, family_id=None):
        """Tests if this user can alter relationship/family mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        arg:    family_id (osid.id.Id): the ``Id`` of the ``Family``
        return: (boolean) - ``false`` if mapping is not authorized,
                ``true`` otherwise
        raise:  NullArgument - ``family_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def get_assignable_family_ids(self, family_id=None):
        """Gets a list of families including and under the given family node in which any
            relationship can be assigned.

        arg:    family_id (osid.id.Id): the ``Id`` of the ``Family``
        return: (osid.id.IdList) - list of assignable family ``Ids``
        raise:  NullArgument - ``family_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def get_assignable_family_ids_for_relationship(self, family_id=None, relationship_id=None):
        """Gets a list of families including and under the given family node in which a specific
            relationship can be assigned.

        arg:    family_id (osid.id.Id): the ``Id`` of the ``Family``
        arg:    relationship_id (osid.id.Id): the ``Id`` of the
                ``Relationship``
        return: (osid.id.IdList) - list of assignable family ``Ids``
        raise:  NullArgument - ``family_id`` or ``relationship_id`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def assign_relationship_to_family(self, relationship_id=None, family_id=None):
        """Adds an existing ``Relationship`` to a ``Family``.

        arg:    relationship_id (osid.id.Id): the ``Id`` of the
                ``Relationship``
        arg:    family_id (osid.id.Id): the ``Id`` of the ``Family``
        raise:  AlreadyExists - ``relationship_id`` is already assigned
                to ``family_id``
        raise:  NotFound - ``relationship_id`` or ``family_id`` not
                found
        raise:  NullArgument - ``relationship_id`` or ``family_id`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def unassign_relationship_from_family(self, relationship_id=None, family_id=None):
        """Removes a ``Relationship`` from a ``Family``.

        arg:    relationship_id (osid.id.Id): the ``Id`` of the
                ``Relationship``
        arg:    family_id (osid.id.Id): the ``Id`` of the ``Family``
        raise:  NotFound - ``relationship_id`` or ``family_id`` not
                found or ``relationship_id`` not assigned to
                ``family_id``
        raise:  NullArgument - ``relationship_id`` or ``family_id`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class RelationshipSmartFamilySession(abc_relationship_sessions.RelationshipSmartFamilySession,
                                     osid_sessions.OsidSession):
    """This session manages queries and sequencing to create "smart" dynamic catalogs.

    A ``RelationshipQuery`` can be retrieved from this session and
    mapped to this ``Family`` to create a virtual collection of
    ``Relationships``. The entries may be sequenced using the
    ``RelationshipSearchOrder`` from this session.

    This ``Family`` has a default query that matches any relationship
    and a default search order that specifies no sequencing. The queries
    may be examined using a ``RelationshipQueryInspector``. The query
    may be modified by converting the inspector back to a
    ``RelationshipQuery``.

    """

    def get_family_id(self):
        """Gets the ``Family``  ``Id`` associated with this session.

        return: (osid.id.Id) - the ``Family Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin_id
        return self._catalog_id

    def get_family(self):
        """Gets the ``Family`` associated with this session.

        return: (osid.relationship.Family) - the family
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin
        from ..osid.osid_errors import OperationFailed, PermissionDenied
        from .objects import Family
        try:
            return Family(self.my_catalog_model)
        except:
            raise OperationFailed()

    def can_manage_smart_families(self):
        """Tests if this user can manage smart families.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer smart
        operations.

        return: (boolean) - ``false`` if smart family methods are not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def get_relationship_query(self):
        """Gets a relationship query.

        return: (osid.relationship.RelationshipQuery) - the relationship
                query
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def get_relationship_search_order(self):
        """Gets a relationship search order.

        return: (osid.relationship.RelationshipSearchOrder) - the
                relationship search order
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def apply_relationship_query(self, relationship_query=None):
        """Applies a relationship query to this family.

        arg:    relationship_query
                (osid.relationship.RelationshipQuery): the relationship
                query
        raise:  NullArgument - ``relationship_query`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        raise:  Unsupported - ``relationship_query`` not of this service
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def inspect_relationship_query(self):
        """Gets a relationship query inspector for this family.

        return: (osid.relationship.RelationshipQueryInspector) - the
                relationship query inspector
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def apply_relationship_sequencing(self, relationship_search_order=None):
        """Applies a relationship search order to this family.

        arg:    relationship_search_order
                (osid.relationship.RelationshipSearchOrder): the
                relationship search order
        raise:  NullArgument - ``relationship_search_order`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        raise:  Unsupported - ``relationship_search_order`` not of this
                service
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def get_relationship_query_from_inspector(self, relationship_query_inspector=None):
        """Gets a relationship query from an inspector.

        arg:    relationship_query_inspector
                (osid.relationship.RelationshipQueryInspector): a
                relationship query inspector
        return: (osid.relationship.RelationshipQuery) - the relationship
                query
        raise:  NullArgument - ``relatinship_query_inspector`` is
                ``null``
        raise:  Unsupported - ``relationship_query_inspector`` is not of
                this service
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class FamilyLookupSession(abc_relationship_sessions.FamilyLookupSession, osid_sessions.OsidSession):
    """This session provides methods for retrieving ``Family`` objects.

    The ``Family`` represents a collection of relationships.

    This session defines views that offer differing behaviors when
    retrieving multiple objects.

      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete set or is an error condition


    Generally, the comparative view should be used for most applications
    as it permits operation even if there is data that cannot be
    accessed. For example, a browsing application may only need to
    examine the ``Families`` it can access, without breaking execution.
    However, an assessment may only be useful if all ``Families``
    referenced by it are available, and a test-taking applicationmay
    sacrifice some interoperability for the sake of precision.

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
        self._family_view = COMPARATIVE

    def can_lookup_families(self):
        """Tests if this user can perform ``Family`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may not offer lookup operations
        to unauthorized users.

        return: (boolean) - ``false`` if lookup methods are not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return True

    def use_comparative_family_view(self):
        """The returns from the lookup methods may omit or translate elements based on this
            session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*

        """
        self.family_view = COMPARATIVE

    def use_plenary_family_view(self):
        """A complete view of the ``Family`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*

        """
        self.family_view = PLENARY

    def get_family(self, family_id=None):
        """Gets the ``Family`` specified by its ``Id``.

        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Family`` may have a different
        ``Id`` than requested, such as the case where a duplicate ``Id``
        was assigned to a ``Family`` and retained for compatibil

        arg:    family_id (osid.id.Id): ``Id`` of the ``Family``
        return: (osid.relationship.Family) - the family
        raise:  NotFound - ``family_id`` not found
        raise:  NullArgument - ``family_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method is must be implemented.*

        """
        if family_id is None:
            raise NullArgument()
        url_path = '/handcar/services/relationship/families/' + str(family_id)
        return objects.Family(self._get_request(url_path))

    def get_families_by_ids(self, family_ids=None):
        """Gets a ``FamilyList`` corresponding to the given ``IdList``.

        In plenary mode, the returned list contains all of the families
        specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if an ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible families may be omitted from the list and may
        present the elements in any order including returning a unique
        set.

        arg:    family_ids (osid.id.IdList): the list of ``Ids`` to
                retrieve
        return: (osid.relationship.FamilyList) - the returned ``Family
                list``
        raise:  NotFound - an ``Id was`` not found
        raise:  NullArgument - ``family_ids`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        if family_ids is None:
            raise NullArgument()
        families = []
        for i in family_ids:
            family = None
            url_path = '/handcar/services/relationship/families/' + str(i)
            try:
                family = self._get_request(url_path)
            except (NotFound, OperationFailed):
                if self._family_view == PLENARY:
                    raise
                else:
                    pass
            if family:
                if not (self._family_view == COMPARATIVE and
                        family in families):
                    families.append(family)
        return objects.FamilykList(families)

    def get_families_by_genus_type(self, family_genus_type=None):
        """Gets a ``FamilyList`` corresponding to the given family genus ``Type`` which
            does not include families of genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known families
        or an error results. Otherwise, the returned list may contain
        only those families that are accessible through this session.

        arg:    family_genus_type (osid.type.Type): a family genus type
        return: (osid.relationship.FamilyList) - the returned ``Family
                list``
        raise:  NullArgument - ``family_genus_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        if family_genus_type is None:
            raise NullArgument()
        url_path = '/handcar/services/relationship/families'
        families_of_type = []
        all_families = self._get_request(url_path)
        for family in all_families:
            # DO WE NEED TO CHECK ALL THREE ATRIBUTES OF THE Id HERE?
            if family['genusTypeId'] == str(family_genus_type):
                families_of_type.append(family)
        return objects.FamilyList(families_of_type)

    def get_families_by_parent_genus_type(self, family_genus_type=None):
        """Gets a ``FamilyList`` corresponding to the given family genus ``Type`` and
            include any additional families with genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known families
        or an error results. Otherwise, the returned list may contain
        only those families that are accessible through this session.

        arg:    family_genus_type (osid.type.Type): a family genus type
        return: (osid.relationship.FamilyList) - the returned ``Family
                list``
        raise:  NullArgument - ``family_genus_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

    def get_families_by_record_type(self, family_record_type=None):
        """Gets a ``FamilyList`` containing the given family record ``Type``.

        In plenary mode, the returned list contains all known families
        or an error results. Otherwise, the returned list may contain
        only those families that are accessible through this session.

        arg:    family_record_type (osid.type.Type): a family record
                type
        return: (osid.relationship.FamilyList) - the returned ``Family
                list``
        raise:  NullArgument - ``family_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

    def get_families_by_provider(self, resource_id=None):
        """Gets a ``FamilyList`` from the given provider.

        In plenary mode, the returned list contains all known families
        or an error results. Otherwise, the returned list may contain
        only those families that are accessible through this session.

        arg:    resource_id (osid.id.Id): a resource ``Id``
        return: (osid.relationship.FamilyList) - the returned ``Family
                list``
        raise:  NullArgument - ``resource_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

    def get_families(self):
        """Gets all families.

        In plenary mode, the returned list contains all known families
        or an error results. Otherwise, the returned list may contain
        only those families that are accessible through this session.

        return: (osid.relationship.FamilyList) - a list of families
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        url_path = '/handcar/services/relationship/families'
        return objects.FamilyList(self._get_request(url_path))

    families = property(get_families)


class FamilyQuerySession(abc_relationship_sessions.FamilyQuerySession, osid_sessions.OsidSession):
    """This session provides methods for searching ``Family`` objects.

    The search query is constructed using the ``FamilyQuery``. The
    family record ``Type`` also specifies the record for the family
    query.

    Families may have a query record indicated by their respective
    record types. The query record is accessed via the ``FamilyQuery``.
    The returns in this session may not be cast directly to these
    interfaces.

    """

    def can_search_families(self):
        """Tests if this user can perform ``Family`` searches.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.

        return: (boolean) - ``false`` if search methods are not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def get_family_query(self):
        """Gets a family query.

        return: (osid.relationship.FamilyQuery) - the family query
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def get_families_by_query(self, family_query=None):
        """Gets a list of ``Family`` objects matching the given family query.

        arg:    family_query (osid.relationship.FamilyQuery): the family
                query
        return: (osid.relationship.FamilyList) - the returned
                ``FamilyList``
        raise:  NullArgument - ``family_query`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - ``family_query`` is not of this service
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class FamilySearchSession(abc_relationship_sessions.FamilySearchSession, FamilyQuerySession):
    """This session provides methods for searching ``Family`` objects.

    The search query is constructed using the ``FamilyQuery``. The
    family record ``Type`` also specifies the record for the family
    query.

    ``get_families_by_query()`` is the basic search method and returns a
    list of ``Family`` elements. A more advanced search may be performed
    with ``getFamiliesBySearch()``. It accepts a ``FamilySearch`` in
    addition to the query for the purpose of specifying additional
    options affecting the entire search, such as ordering.
    ``get_families_by_search()`` returns a ``FamilySearchResults`` that
    can be used to access the resulting ``FamilyList`` or be used to
    perform a search within the result set through ``FamilySearch``.

    Families may have a query record indicated by their respective
    record types. The query record is accessed via the ``FamilyQuery``.
    The returns in this session may not be cast directly to these
    interfaces.

    """

    def get_family_search(self):
        """Gets a family search.

        return: (osid.relationship.FamilySearch) - the family search
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def get_family_search_order(self):
        """Gets a family search order.

        The ``FamilySearchOrder`` is supplied to a ``FamilySearch`` to
        specify the ordering of results.

        return: (osid.relationship.FamilySearchOrder) - the family
                search order
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def get_families_by_search(self, family_query=None, family_search=None):
        """Gets the search results matching the given search.

        arg:    family_query (osid.relationship.FamilyQuery): the family
                query
        arg:    family_search (osid.relationship.FamilySearch): the
                family search
        return: (osid.relationship.FamilySearchResults) - the search
                results
        raise:  NullArgument - ``family_query`` or ``family_search`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - ``family_query`` or ``family_search`` is
                not of this service
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def get_family_query_from_inspector(self, family_query_inspector=None):
        """Gets a family query from an inspector.

        The inspector is available from an ``FamilySearchResults``.

        arg:    family_query_inspector
                (osid.relationship.FamilyQueryInspector): a family query
                inspector
        return: (osid.relationship.FamilyQuery) - the familyh query
        raise:  NullArgument - ``family_query_inspector`` is ``null``
        raise:  Unsupported - ``family_query_inspector`` is not of this
                service
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class FamilyAdminSession(abc_relationship_sessions.FamilyAdminSession, osid_sessions.OsidSession):
    """This session creates, updates, and deletes ``Families``.

    The data for create and update is provided by the consumer via the
    form object. ``OsidForms`` are requested for each create or update
    and may not be reused.

    Create and update operations differ in their usage. To create a
    ``Family,`` a ``FamilyForm`` is requested using
    ``get_family_form_for_create()`` specifying the desired record
    ``Types`` or none if no record ``Types`` are needed. The returned
    ``FamilyForm`` will indicate that it is to be used with a create
    operation and can be used to examine metdata or validate data prior
    to creation. Once the ``FamilyForm`` is submiited to a create
    operation, it cannot be reused with another create operation unless
    the first operation was unsuccessful. Each ``FamilyForm``
    corresponds to an attempted transaction.

    For updates, ``FamilyForms`` are requested to the ``Family``  ``Id``
    that is to be updated using ``getFamilyFormForUpdate()``. Similarly,
    the ``FamilyForm`` has metadata about the data that can be updated
    and it can perform validation before submitting the update. The
    ``FamilyForm`` can only be used once for a successful update and
    cannot be reused.

    The delete operations delete ``Families``.

    This session includes an ``Id`` aliasing mechanism to assign an
    external ``Id`` to an internally assigned Id.

    """

    def can_create_families(self):
        """Tests if this user can create families.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a ``Family``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer create
        operations to unauthorized users.

        return: (boolean) - ``false`` if ``Family`` creation is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.can_create_resources
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    def can_create_family_with_record_types(self, family_record_types=None):
        """Tests if this user can create a single ``Family`` using the desired record types.

        While ``RelationshipManager.getFamilyRecordTypes()`` can be used
        to examine which records are supported, this method tests which
        record(s) are required for creating a specific ``Family``.
        Providing an empty array tests if a ``Family`` can be created
        with no records.

        arg:    family_record_types (osid.type.Type[]): array of family
                record types
        return: (boolean) - ``true`` if ``Family`` creation using the
                specified record ``Types`` is supported, ``false``
                otherwise
        raise:  NullArgument - ``family_record_types is null``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.can_create_resource_with_record_types
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    def get_family_form_for_create(self, family_record_types=None):
        """Gets the family form for creating new families.

        . A new form should be requested for each create transaction.

        arg:    family_record_types (osid.type.Type[]): array of family
                record types
        return: (osid.relationship.FamilyForm) - the family form
        raise:  NullArgument - ``family_record_types is null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - unable to get form for requested record
                types
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def create_family(self, family_form=None):
        """Creates a new ``Family``.

        arg:    family_form (osid.relationship.FamilyForm): the form for
                this ``Family``.
        return: (osid.relationship.Family) - the new ``Family``
        raise:  IllegalState - ``family_form`` already used in a create
                transaction
        raise:  InvalidArgument - one or more of the form elements is
                invalid
        raise:  NullArgument - ``family_form`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - ``family_form`` did not originate from
                ``get_family_form_for_create()``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def can_update_families(self):
        """Tests if this user can update families.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a ``Family``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer update
        operations to unauthorized users.

        return: (boolean) - ``false`` if ``Family`` modification is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.can_create_resources
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    def get_family_form_for_update(self, family_id=None):
        """Gets the family form for updating an existing family.

        A new family form should be requested for each update
        transaction.

        arg:    family_id (osid.id.Id): the ``Id`` of the ``Family``
        return: (osid.relationship.FamilyForm) - the family form
        raise:  NotFound - ``family_id`` is not found
        raise:  NullArgument - ``family_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def update_family(self, family_form=None):
        """Updates an existing family.

        arg:    family_form (osid.relationship.FamilyForm): the form
                containing the elements to be updated
        raise:  IllegalState - ``family_form`` already used in an update
                transaction
        raise:  InvalidArgument - the form contains an invalid value
        raise:  NullArgument - ``family_id`` or ``family_form`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - ``family_form`` did not originate from
                ``get_family_form_for_update()``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def can_delete_families(self):
        """Tests if this user can delete families.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a ``Family``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer delete
        operations to unauthorized users.

        return: (boolean) - ``false`` if ``Family`` deletion is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.can_create_resources
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    def delete_family(self, family_id=None):
        """Deletes a ``Family``.

        arg:    family_id (osid.id.Id): the ``Id`` of the ``Family`` to
                remove
        raise:  NotFound - ``family_id`` not found
        raise:  NullArgument - ``family_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def can_manage_family_aliases(self):
        """Tests if this user can manage ``Id`` aliases for families.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        return: (boolean) - ``false`` if ``Family`` aliasing is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def alias_family(self, family_id=None, alias_id=None):
        """Adds an ``Id`` to a ``Family`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``Family`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another family, it is
        reassigned to the given family ``Id``.

        arg:    family_id (osid.id.Id): the ``Id`` of a ``Family``
        arg:    alias_id (osid.id.Id): the alias ``Id``
        raise:  AlreadyExists - ``alias_id`` is already assigned
        raise:  NotFound - ``family_id`` not found
        raise:  NullArgument - ``family_id`` or ``alias_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class FamilyNotificationSession(abc_relationship_sessions.FamilyNotificationSession, osid_sessions.OsidSession):
    """This session defines methods to receive notifications on adds/changes to ``Family`` objects.

    This session is intended for consumers needing to synchronize their
    state with this service without the use of polling. Notifications
    are cancelled when this session is closed.

    Notifications are triggered with changes to the ``Family`` object
    itself. Adding and removing relationships result in notifications
    available from the notification session for rules.

    """

    def can_register_for_family_notifications(self):
        """Tests if this user can register for ``Family`` notifications.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.

        return: (boolean) - ``false`` if notification methods are not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def register_for_new_families(self):
        """Register for notifications of new families.

        ``FamilyReceiver.newFamily()`` is invoked when a new ``Family``
        is created.

        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def register_for_new_family_ancestors(self, family_id=None):
        """Registers for notification of an updated hierarchy structure that introduces
            a new ancestor of the specified family.

        ``FamilyReceiver.newAncestorFamily()`` is invoked when the
        specified family node gets a new ancestor.

        arg:    family_id (osid.id.Id): the ``Id`` of the ``Family``
                node to monitor
        raise:  NullArgument - ``family_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def register_for_new_family_descendants(self, family_id=None):
        """Registers for notification of an updated hierarchy structure that introduces
            a new descendant of the specified family.

        ``FamilyReceiver.newDescendantFamily()`` is invoked when the
        specified family node gets a new descendant.

        arg:    family_id (osid.id.Id): the ``Id`` of the ``Family``
                node to monitor
        raise:  NullArgument - ``family_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def register_for_changed_families(self):
        """Registers for notification of updated families.

        ``FamilyReceiver.changedFamily()`` is invoked when a family is
        changed.

        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def register_for_changed_family(self, family_id=None):
        """Registers for notification of an updated family.

        ``FamilyReceiver.changedFamily()`` is invoked when the specified
        family is changed.

        arg:    family_id (osid.id.Id): the ``Id`` of the ``Family`` to
                monitor
        raise:  NullArgument - ``family_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def register_for_deleted_families(self):
        """Registers for notification of deleted families.

        ``FamilyReceiver.deletedFamily()`` is invoked when a family is
        deleted.

        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def register_for_deleted_family(self, family_id=None):
        """Registers for notification of a deleted family.

        ``FamilyReceiver.deletedFamily()`` is invoked when the specified
        family is deleted.

        arg:    family_id (osid.id.Id): the ``Id`` of the ``Family`` to
                monitor
        raise:  NullArgument - ``family_id is null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def register_for_deleted_family_ancestors(self, family_id=None):
        """Registers for notification of an updated hierarchy structure that removes
            an ancestor of the specified family.

        ``FamilyReceiver.deletedAncestor()`` is invoked when the
        specified family node loses an ancestor.

        arg:    family_id (osid.id.Id): the ``Id`` of the ``Family`` to
                monitor
        raise:  NullArgument - ``family_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def register_for_deleted_family_descendants(self, family_id=None):
        """Registers for notification of an updated hierarchy structure that removes
            a descendant of the specified family.

        ``FamilyReceiver.deletedDescendant()`` is invoked when the
        specified family node loses a descendant.

        arg:    family_id (osid.id.Id): the ``Id`` of the ``Family`` to
                monitor
        raise:  NullArgument - ``family_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class FamilyHierarchySession(abc_relationship_sessions.FamilyHierarchySession, osid_sessions.OsidSession):
    """This session defines methods for traversing a hierarchy of ``Family`` objects.

    Each node in the hierarchy is a unique ``Family``. The hierarchy may
    be traversed recursively to establish the tree structure through
    ``get_parent_families()`` and ``getChildFamilies()``. To relate
    these ``Ids`` to another OSID, ``get_family_nodes()`` can be used
    for retrievals that can be used for bulk lookups in other OSIDs. Any
    ``Family`` available in the Relationship OSID is known to this
    hierarchy but does not appear in the hierarchy traversal until added
    as a root node or a child of another node.

    A user may not be authorized to traverse the entire hierarchy. Parts
    of the hierarchy may be made invisible through omission from the
    returns of ``get_parent_families()`` or ``get_child_families()`` in
    lieu of a ``PermissionDenied`` error that may disrupt the traversal
    through authorized pathways.

    This session defines views that offer differing behaviors when
    retrieving multiple objects.

      * comparative view: family elements may be silently omitted or re-
        ordered
      * plenary view: provides a complete set or is an error condition
    """

    def get_family_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        return: (osid.id.Id) - the hierarchy ``Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def get_family_hierarchy(self):
        """Gets the hierarchy associated with this session.

        return: (osid.hierarchy.Hierarchy) - the hierarchy associated
                with this session
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def can_access_family_hierarchy(self):
        """Tests if this user can perform hierarchy queries.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an an application that may not offer hierrachy
        traversal operations to unauthorized users.

        return: (boolean) - ``false`` if hierarchy traversal methods are
                not authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def use_comparative_family_view(self):
        """The returns from the family methods may omit or translate elements based on
            this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_plenary_family_view(self):
        """A complete view of the ``Family`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def get_root_family_ids(self):
        """Gets the root family ``Ids`` in this hierarchy.

        return: (osid.id.IdList) - the root family ``Ids``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def get_root_families(self):
        """Gets the root families in the family hierarchy.

        A node with no parents is an orphan. While all family ``Ids``
        are known to the hierarchy, an orphan does not appear in the
        hierarchy unless explicitly added as a root node or child of
        another node.

        return: (osid.relationship.FamilyList) - the root families
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def has_parent_families(self, family_id=None):
        """Tests if the ``Family`` has any parents.

        arg:    family_id (osid.id.Id): the ``Id`` of a family
        return: (boolean) - ``true`` if the family has parents,
                ``false`` otherwise
        raise:  NotFound - ``family_id`` is not found
        raise:  NullArgument - ``family_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def is_parent_of_family(self, id_=None, family_id=None):
        """Tests if an ``Id`` is a direct parent of a family.

        arg:    id (osid.id.Id): an ``Id``
        arg:    family_id (osid.id.Id): the ``Id`` of a family
        return: (boolean) - ``true`` if this ``id`` is a parent of
                ``family_id,``  ``false`` otherwise
        raise:  NotFound - ``family_id`` is not found
        raise:  NullArgument - ``id`` or ``family_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.

        """
        pass

    def get_parent_family_ids(self, family_id=None):
        """Gets the parent ``Ids`` of the given family.

        arg:    family_id (osid.id.Id): the ``Id`` of a family
        return: (osid.id.IdList) - the parent ``Ids`` of the family
        raise:  NotFound - ``family_id`` is not found
        raise:  NullArgument - ``family_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def get_parent_families(self, family_id=None):
        """Gets the parent families of the given ``id``.

        arg:    family_id (osid.id.Id): the ``Id`` of the ``Family`` to
                query
        return: (osid.relationship.FamilyList) - the parent families of
                the ``id``
        raise:  NotFound - a ``Family`` identified by ``Id is`` not
                found
        raise:  NullArgument - ``family_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def is_ancestor_of_family(self, id_=None, family_id=None):
        """Tests if an ``Id`` is an ancestor of a family.

        arg:    id (osid.id.Id): an ``Id``
        arg:    family_id (osid.id.Id): the ``Id`` of a family
        return: (boolean) - ``true`` if this ``id`` is an ancestor of
                ``family_id,``  ``false`` otherwise
        raise:  NotFound - ``family_id`` is not found
        raise:  NullArgument - ``id`` or ``family_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.

        """
        pass

    def has_child_families(self, family_id=None):
        """Tests if a family has any children.

        arg:    family_id (osid.id.Id): the ``Id`` of a family
        return: (boolean) - ``true`` if the ``family_id`` has children,
                ``false`` otherwise
        raise:  NotFound - ``family_id`` is not found
        raise:  NullArgument - ``family_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def is_child_of_family(self, id_=None, family_id=None):
        """Tests if a family is a direct child of another.

        arg:    id (osid.id.Id): an ``Id``
        arg:    family_id (osid.id.Id): the ``Id`` of a family
        return: (boolean) - ``true`` if the ``id`` is a child of
                ``family_id,``  ``false`` otherwise
        raise:  NotFound - ``family_id`` is not found
        raise:  NullArgument - ``id`` or ``family_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.

        """
        pass

    def get_child_family_ids(self, family_id=None):
        """Gets the child ``Ids`` of the given family.

        arg:    family_id (osid.id.Id): the ``Id`` to query
        return: (osid.id.IdList) - the children of the family
        raise:  NotFound - ``family_id`` is not found
        raise:  NullArgument - ``family_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def get_child_families(self, family_id=None):
        """Gets the child families of the given ``id``.

        arg:    family_id (osid.id.Id): the ``Id`` of the ``Family`` to
                query
        return: (osid.relationship.FamilyList) - the child families of
                the ``id``
        raise:  NotFound - a ``Family`` identified by ``Id is`` not
                found
        raise:  NullArgument - ``family_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def is_descendant_of_family(self, id_=None, family_id=None):
        """Tests if an ``Id`` is a descendant of a family.

        arg:    id (osid.id.Id): an ``Id``
        arg:    family_id (osid.id.Id): the ``Id`` of a family
        return: (boolean) - ``true`` if the ``id`` is a descendant of
                the ``family_id,``  ``false`` otherwise
        raise:  NotFound - ``family_id`` is not found
        raise:  NullArgument - ``id`` or ``family_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` is not found return ``false``.

        """
        pass

    def get_family_node_ids(self, family_id=None, ancestor_levels=None, descendant_levels=None, include_siblings=None):
        """Gets a portion of the hierarchy for the given family.

        arg:    family_id (osid.id.Id): the ``Id`` to query
        arg:    ancestor_levels (cardinal): the maximum number of
                ancestor levels to include. A value of 0 returns no
                parents in the node.
        arg:    descendant_levels (cardinal): the maximum number of
                descendant levels to include. A value of 0 returns no
                children in the node.
        arg:    include_siblings (boolean): ``true`` to include the
                siblings of the given node, ``false`` to omit the
                siblings
        return: (osid.hierarchy.Node) - a family node
        raise:  NotFound - ``family_id`` is not found
        raise:  NullArgument - ``family_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def get_family_nodes(self, family_id=None, ancestor_levels=None, descendant_levels=None, include_siblings=None):
        """Gets a portion of the hierarchy for the given family.

        arg:    family_id (osid.id.Id): the ``Id`` to query
        arg:    ancestor_levels (cardinal): the maximum number of
                ancestor levels to include. A value of 0 returns no
                parents in the node.
        arg:    descendant_levels (cardinal): the maximum number of
                descendant levels to include. A value of 0 returns no
                children in the node.
        arg:    include_siblings (boolean): ``true`` to include the
                siblings of the given node, ``false`` to omit the
                siblings
        return: (osid.relationship.FamilyNode) - a family node
        raise:  NotFound - ``family_id`` is not found
        raise:  NullArgument - ``family_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class FamilyHierarchyDesignSession(abc_relationship_sessions.FamilyHierarchyDesignSession, osid_sessions.OsidSession):
    """This session manages a hierarchy of families may be organized into a hierarchy for organizing or federating.

    A parent ``Family`` includes all of the relationships of its
    children such that a single root node contains all of the
    relationships of the federation.

    """

    def get_family_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        return: (osid.id.Id) - the hierarchy ``Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def get_family_hierarchy(self):
        """Gets the hierarchy associated with this session.

        return: (osid.hierarchy.Hierarchy) - the hierarchy associated
                with this session
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def can_modify_family_hierarchy(self):
        """Tests if this user can change the hierarchy.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known performing any update
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer these
        operations to an unauthorized user.

        return: (boolean) - ``false`` if changing this hierarchy is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def add_root_family(self, family_id=None):
        """Adds a root family.

        arg:    family_id (osid.id.Id): the ``Id`` of a family
        raise:  AlreadyExists - ``family_id`` is already in hierarchy
        raise:  NotFound - ``family_id`` not found
        raise:  NullArgument - ``family_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def remove_root_family(self, family_id=None):
        """Removes a root family.

        arg:    family_id (osid.id.Id): the ``Id`` of a family
        raise:  NotFound - ``family_id`` not a root
        raise:  NullArgument - ``family_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def add_child_family(self, family_id=None, child_id=None):
        """Adds a child to a family.

        arg:    family_id (osid.id.Id): the ``Id`` of a family
        arg:    child_id (osid.id.Id): the ``Id`` of the new child
        raise:  AlreadyExists - ``family_id`` is already a parent of
                ``child_id``
        raise:  NotFound - ``family_id`` or ``child_id`` not found
        raise:  NullArgument - ``family_id`` or ``child_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def remove_child_family(self, family_id=None, child_id=None):
        """Removes a child from a family.

        arg:    family_id (osid.id.Id): the ``Id`` of a family
        arg:    child_id (osid.id.Id): the ``Id`` of the new child
        raise:  NotFound - ``family_id`` not a parent of ``child_id``
        raise:  NullArgument - ``family_id`` or ``child_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def remove_child_families(self, family_id=None):
        """Removes all children from a family.

        arg:    family_id (osid.id.Id): the ``Id`` of a family
        raise:  NotFound - ``family_id`` not in hierarchy
        raise:  NullArgument - ``family_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        pass
