# -*- coding: utf-8 -*-

# This module contains all the Object classes used by the MIT Core Concept
# Catalog (MC3) Handcar based implementation of the OSID Learning Service.

import json
from ...abstract_osid.relationship import objects as abc_relationship_objects
from ..osid import objects as osid_objects
from ..osid import markers
from ..osid.metadata import Metadata
from .. import settings
from ..primitives import Id, Type, DisplayText
from ..id.objects import IdList
from ..osid.osid_errors import NullArgument, InvalidArgument, NotFound, NoAccess, IllegalState, OperationFailed, Unimplemented, Unsupported

INVALID = 0
VALID = 1


class Relationship(abc_relationship_objects.Relationship, osid_objects.OsidRelationship):
    """A ``Relationship`` is an object between two peers.

    The genus type indicates the relationship between the peer and the
    related peer.

    """
    _namespace = 'relationship.Relationship'

    def get_source_id(self):
        """Gets the from peer ``Id`` in this relationship.

        return: (osid.id.Id) - the peer
        *compliance: mandatory -- This method must be implemented.*

        """
        return Id(self._my_map['sourceId'])

    def get_destination_id(self):
        """Gets the to peer ``Id`` in this relationship.

        return: (osid.id.Id) - the related peer
        *compliance: mandatory -- This method must be implemented.*

        """
        return Id(self._my_map['destinationId'])

    def get_genus_type(self):
        """
        Patched in by cjshaw@mit.edu, Aug 6, 2014
        :return:
        """
        return Id(self._my_map['genusTypeId'])

    def get_relationship_record(self, relationship_record_type=None):
        """Gets the relationshop record corresponding to the given ``Relationship`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``relationship_record_type`` may be the
        ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(relationship_record_type)`` is ``true`` .

        arg:    relationship_record_type (osid.type.Type): the type of
                relationship record to retrieve
        return: (osid.relationship.records.RelationshipRecord) - the
                relationship record
        raise:  NullArgument - ``relationship_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        raise:  Unsupported -
                ``has_record_type(relationship_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()


class RelationshipForm(abc_relationship_objects.RelationshipForm, osid_objects.OsidRelationshipForm):
    """This is the form for creating and updating ``Relationships``.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``RelationshipAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.

    """
    _namespace = 'relationship.Relationship'

    def _init_map(self):
        osid_objects.OsidObjectForm._init_map(self)
        self._my_map['sourceId'] = str(self.kwargs['source_id'])
        self._my_map['destinationId'] = str(self.kwargs['destination_id'])

    def _init_validity_map(self):
        osid_objects.OsidObjectForm._init_validity_map(self)

    def get_relationship_form_record(self, relationship_record_type=None):
        """Gets the ``RelationshipFormRecord`` corresponding to the given relationship record ``Type``.

        arg:    relationship_record_type (osid.type.Type): a
                relationship record type
        return: (osid.relationship.records.RelationshipFormRecord) - the
                relationship form record
        raise:  NullArgument - ``relationship_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        raise:  Unsupported -
                ``has_record_type(relationship_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

    def set_genus_type(self, genus_type=None):
        """
        Patched in by cjshaw@mit.edu, Aug 6, 2014. For Crosslinks copying...
        :param genus_type:
        :return:
        """
        self._my_map['genusTypeId'] = str(genus_type)


class RelationshipList(abc_relationship_objects.RelationshipList, osid_objects.OsidList):
    """Like all ``OsidLists,``  ``Relationship`` provides a means for accessing ``Relationship`` elements sequentially either one at a time or many at a time.

    Examples: while (rl.hasNext()) { Relationship relationship =
    rl.getNextRelationship(); }

    or
      while (rl.hasNext()) {
           Relationship[] relationships = rl.getNextRelationships(rl.available());
      }

    """

    def get_next_relationship(self):
        """Gets the next ``Relationship`` in this list.

        return: (osid.relationship.Relationship) - the next
                ``Relationship`` in this list. The ``has_next()`` method
                should be used to test that a next ``Relationship`` is
                available before calling this method.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        try:
            next_object = next(self)
        except StopIteration:
            raise IllegalState('no more elements available in this list')
        except Exception:  # Need to specify exceptions here!
            raise OperationFailed()
        else:
            return next_object

    def next(self):
        try:
            next_object = osid_objects.OsidList.next(self)
        except StopIteration:
            raise
        except Exception:  # Need to specify exceptions here!
            raise OperationFailed
        if isinstance(next_object, dict):
            next_object = Relationship(next_object)
        return next_object

    __next__ = next

    def get_next_relationships(self, n=None):
        """Gets the next set of ``Relationships`` elements in this list.

        The specified amount must be less than or equal to the return
        from ``available()``.

        arg:    n (cardinal): the number of ``Relationship`` elements
                requested which must be less than or equal to
                ``available()``
        return: (osid.relationship.Relationship) - an array of
                ``Relationship`` elements.The length of the array is
                less than or equal to the number specified.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        if n > self.available():
            # !!! This is not quite as specified (see method docs) !!!
            raise IllegalState('not enough elements available in this list')
        else:
            next_list = []
            x = 0
            while x < n:
                try:
                    next_list.append(next(self))
                except Exception:  # Need to specify exceptions here!
                    raise  # OperationFailed()
                x = x + 1
            return next_list

    next_relationship = property(get_next_relationship)


class Family(abc_relationship_objects.Family, osid_objects.OsidCatalog):
    """A ``Family`` represents a collection of relationships.

    Like all OSID objects, a ``Family`` is identified by its ``Id`` and
    any persisted references should use the ``Id``.

    """

    _namespace = 'relationship.Family'

    def get_family_record(self, family_record_type=None):
        """Gets the famly record corresponding to the given ``Family`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``family_record_type`` may be the ``Type``
        returned in ``get_record_types()`` or any of its parents in a
        ``Type`` hierarchy where ``has_record_type(family_record_type)``
        is ``true`` .

        arg:    family_record_type (osid.type.Type): the type of family
                record to retrieve
        return: (osid.relationship.records.FamilyRecord) - the family
                record
        raise:  NullArgument - ``family_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        raise:  Unsupported - ``has_record_type(family_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        if not self.has_record_type():
            raise IllegalState()
        else:  # This should never get called.
            raise Unimplemented()


class FamilyForm(abc_relationship_objects.FamilyForm, osid_objects.OsidCatalogForm):
    """This is the form for creating and updating ``Family`` objects.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``FamilyAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.

    """

    _namespace = 'relationship.Family'

    def _init_map(self):
        osid_objects.OsidObjectForm._init_map(self)

    def _init_validity_map(self):
        osid_objects.OsidObjectForm._init_validity_map(self)

    def __init__(self, osid_catalog_model=None):
        if osid_catalog_model:
            self.my_model = osid_catalog_model
        else:
            from .models import Family as FamilyModel
            self.my_model = FamilyModel()
        self._init_metadata()

    def _init_metadata(self):
        from ..osid.objects import OsidObjectForm
        OsidObjectForm._init_metadata(self)

    def get_family_form_record(self, family_record_type=None):
        """Gets the ``FamilyFormRecord`` corresponding to the given family record ``Type``.

        arg:    family_record_type (osid.type.Type): the family record
                type
        return: (osid.relationship.records.FamilyFormRecord) - the
                family form record
        raise:  NullArgument - ``family_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        raise:  Unsupported - ``has_record_type(family_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class FamilyList(abc_relationship_objects.FamilyList, osid_objects.OsidList):
    """Like all ``OsidLists,``  ``FamilyList`` provides a means for accessing ``Family`` elements sequentially either one at a time or many at a time.

    Examples: while (fl.hasNext()) { Family family = fl.getNextFamily();
    }

    or
      while (fl.hasNext()) {
           Family[] families = fl.getNextFamilies(fl.available());
      }



    """

    def get_next_family(self):
        """Gets the next ``Family`` in this list.

        return: (osid.relationship.Family) - the next ``Family`` in this
                list. The ``has_next()`` method should be used to test
                that a next ``Family`` is available before calling this
                method.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        try:
            next_object = next(self)
        except StopIteration:
            raise IllegalState('no more elements available in this list')
        except Exception:  # Need to specify exceptions here!
            raise OperationFailed()
        else:
            return next_object

    def next(self):
        try:
            next_object = osid_objects.OsidList.next(self)
        except StopIteration:
            raise
        except Exception:  # Need to specify exceptions here!
            raise OperationFailed()
        if isinstance(next_object, dict):
            next_object = Family(next_object)
        return next_object

    __next__ = next

    def get_next_families(self, n=None):
        """Gets the next set of ``Family elements`` in this list.

        The specified amount must be less than or equal to the return
        from ``available()``.

        arg:    n (cardinal): the number of ``Family`` elements
                requested which must be less than or equal to
                ``available()``
        return: (osid.relationship.Family) - an array of ``Family``
                elements.The length of the array is less than or equal
                to the number specified.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        if n > self.available():
            # !!! This is not quite as specified (see method docs) !!!
            raise IllegalState('not enough elements available in this list')
        else:
            next_list = []
            x = 0
            while x < n:
                try:
                    next_list.append(next(self))
                except Exception:  # Need to specify exceptions here!
                    raise OperationFailed()
                x = x + 1
            return next_list

    next_family = property(get_next_family)
