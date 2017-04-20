# -*- coding: utf-8 -*-

# This module contains all the Object classes used by the MIT Core Concept
# Catalog (MC3) Handcar based implementation of the OSID  Service.

from dlkit.abstract_osid.osid import objects as abc_osid_objects
from dlkit.abstract_osid.id.primitives import Id as AbstractId
from dlkit.abstract_osid.type.primitives import Type as AbstractType
from .. import settings
from ..primitives import Id, Type, DisplayText
from .osid_errors import *
from .metadata import Metadata
from . import markers

INVALID = 0
VALID = 1


class OsidObject(abc_osid_objects.OsidObject, markers.Identifiable, markers.Extensible, markers.Browsable):
    """OsidObject is the top level interface for all OSID Objects.

    An OSID Object is an object identified by an OSID Id and may
    implements optional interfaces. OSID Objects also contain a display
    name and a description. These fields are required but may be used
    for a variety of purposes ranging from a primary name and
    description of the object to a more user friendly display of various
    attributes.

    Creation of OSID Objects and the modification of their data is
    managed through the associated OsidSession which removes the
    dependency of updating data elements upon object retrieval.  The
    OsidManager should be used to test if updates are available and
    determine what PropertyTypes are supported. The OsidManager is also
    used to create the appropriate OsidSession for object creation,
    updates and deletes.

    All OsidObjects are identified by an immutable Id. An Id is assigned
    to an object upon creation of the object and cannot be changed once
    assigned.

    An OsidObject may support one or more supplementary records which
    are expressed in the form of interfaces. Each record interface is
    identified by a Type. A record interface may extend another record
    interface where support of the parent record interface is implied.
    In this case of interface inheritance, support of the parent record
    type may be implied through has_record_type() and not explicit in
    get_record_types().

    For example, if recordB extends recordA, typeB is a child of typeA.
    If a record implements typeB, than it also implements typeA. An
    application that only knows about typeA retrieves recordA. An
    application that knows about typeB, retrieves recordB which is the
    union of methods specified in typeA and typeB. If an application
    requests typeA, it may not attempt to access methods defined in
    typeB as they may not exist until explicitly requested. The
    mechanics of this polymorphism is defined by the language binder.
    One mechanism might be the use of casting.

    In addition to the record Types, OSID Objects also have a genus
    Type. A genus Type indicates a classification or kind of the object
    where an "is a" relationship exists. The purpose of of the genus
    Type is to avoid the creation of unnecessary record types that may
    needlessly complicate an interface hierarchy or introduce
    interoperability issues. For example, an OSID object may have a
    record Type of Publication that defines methods pertinent to
    publications, such as an ISBN number. A provider may wish to
    distinguish between books and journals without having the need of
    new record interfaces. In this case, the genus Type may be one of
    Book or Journal. While this distinction can aid a search, these
    genres should be treated in such a way that do not introduce
    interoperability problems.

    Like record Types, the genus Types may also exist in an implicit
    type hierarchy. An OSID object always has at least one genus. Genus
    types should not be confused with subject tagging, which is managed
    externally to the object. Unlike record Types, an object's genus may
    be modified. However, once an object's record is created with a
    record Type, it cannot be changed.

    Methods that return values are not permitted to return nulls. If a
    value is not set, it is indicated in the Metadata of the update
    form.

    """
    _namespace = 'osid.OsidObject'

    def get_display_name(self):
        """Gets the preferred display name associated with this instance of this OSID object appropriate for display to the user.

        return: (osid.locale.DisplayText) - the display name
        compliance: mandatory - This method must be implemented.
        implementation notes: A display name is a string used for
        identifying an object in human terms. A provider may wish to
        initialize the display name based on one or more object
        attributes. In some cases, the display name may not map to a
        specific or significant object attribute but simply be used as a
        preferred display name that can be modified. A provider may also
        wish to translate the display name into a specific locale using
        the Locale service. Some OSIDs define methods for more detailed
        naming.

        """
        return DisplayText(self._display_name)

    def get_description(self):
        """Gets the description associated with this instance of this OSID
        object.

        return: (osid.locale.DisplayText) - the description
        compliance: mandatory - This method must be implemented.
        implementation notes: A description is a string used for
        describing an object in human terms and may not have
        significance in the underlying system. A provider may wish to
        initialize the description based on one or more object
        attributes and/or treat it as an auxiliary piece of data that
        can be modified. A provider may also wish to translate the
        description into a specific locale using the Locale service.

        """
        return DisplayText(self._description)

    def get_genus_type(self):
        """Gets the genus type of this object.

        return: (osid.type.Type) - the genus type of this object
        compliance: mandatory - This method must be implemented.

        """
        return Type(self._my_genus_type)

    def is_of_genus_type(self, genus_type=None):
        """Tests if this object is of the given genus Type.

        The given genus type may be supported by the object through the
        type hierarchy.

        | arg:    ``genus_type`` (``osid.type.Type``): a genus type
        | return: (``boolean``) - true if this object is of the given genus
                Type,  false otherwise
        | raise:  ``NullArgument`` - ``genus_type`` is null
        | *compliance: mandatory - This method must be implemented.*

        """
        if genus_type is None:
            raise NullArgument()
        else:
            my_genus_type = self.get_genus_type()
            return (genus_type.get_authority() == my_genus_type.get_authority() and
                    genus_type.get_identifier_namespace() == my_genus_type.get_identifier_namespace() and
                    genus_type.get_identifier() == my_genus_type.get_identifier())

    display_name = property(get_display_name)
    description = property(get_description)
    genus_type = property(get_genus_type)


class OsidRelationship(abc_osid_objects.OsidRelationship, OsidObject, markers.Temporal):
    """A ``Relationship`` associates two OSID objects.

    Relationships are transient. They define a date range for which they
    are in effect.

    Unlike other ``OsidObjects`` that rely on the auxiliary Journaling
    OSID to track variance over time, ``OsidRelationships`` introduce a
    different concept of time independent from journaling. For example,
    in the present, a student was registered in a course and dropped it.
    The relationship between the student and the course remains
    pertinent, independent of any journaled changes that may have
    occurred to either the student or the course.

    Once the student has dropped the course, the relationship has
    expired such that ``is_effective()`` becomes false. It can be
    inferred that during the period of the effective dates, the student
    was actively registered in the course. Here is an example:

      * T1. September 1: Student registers for course for grades
      * T2. September 10: Student drops course
      * T3. September 15: Student re-registers for course pass/fail

    The relationships are:
      T1. R1 {effective,   September 1  -> end of term,  data=grades}
      T2. R1 {ineffective, September 1  -> September 10, data=grades}
      T3. R1 {ineffective, September 1  -> September 10, data=grades}
          R2 {effective,   September 10 -> end of term,  data=p/f}

    An OSID Provider may also permit dates to be set in the future in
    which case the relationship can become automatically become
    effective at a future time and later expire. More complex
    effectiveness management can be done through other rule-based
    services.

    OSID Consumer lookups and queries of relationships need to consider
    that it may be only effective relationshps are of interest.

    """
    _namespace = 'osid.OsidRelationship'

    def has_end_reason(self):
        """Tests if a reason this relationship came to an end is known.

        return: (boolean) - ``true`` if an end reason is available,
                ``false`` otherwise
        raise:  IllegalState - ``is_effective()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Someday I will have real end reasons
        return False

    def get_end_reason_id(self):
        """Gets a state ``Id`` indicating why this relationship has ended.

        return: (osid.id.Id) - a state ``Id``
        raise:  IllegalState - ``has_end_reason()`` is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Someday I will have real end reasons
        raise IllegalState()

    def get_end_reason(self):
        """Gets a state indicating why this relationship has ended.

        return: (osid.process.State) - a state
        raise:  IllegalState - ``has_end_reason()`` is ``false``
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Someday I will have real end reasons
        raise IllegalState()


class OsidList(abc_osid_objects.OsidList):
    """OsidList is the top-level interface for all OSID lists.

    An OSID list provides sequential access, one at a time or many at a
    time, access to a set of elements. These elements are not required
    to be OsidObjects but generally are. The element retrieval methods
    are defined in the sub-interface of OsidList where the appropriate
    return type is defined.

    Osid lists are a once pass through iteration of elements. The size
    of the object set and the means in which the element set is
    generated or stored is not known. Assumptions based on the length of
    the element set by copying the entire contents of the list into a
    fixed buffer should be done with caution a awareness that an
    implementation may return a number of elements ranging from zero to
    infinity.

    Lists are returned by methods when multiple return values are
    possible. There is no guarantee that successive calls to the same
    method will return the same set of elements in a list. Unless an
    order is specified in an interface definition, the order of the
    elements is not known.

    """

    def __init__(self, iter_object=[], count=None):
        if count is not None:
            self._count = count
        elif isinstance(iter_object, dict) or isinstance(iter_object, list):
            self._count = len(iter_object)
        self._iter_object = iter(iter_object)

    def __iter__(self):
        return self

    def __len__(self):
        return self.available()

    def next(self):
        try:
            next_object = self._iter_object.next()
        except StopIteration:
            raise
        except Exception:  # Need to specify exceptions here!
            raise OperationFailed()
        if self._count is not None:
            self._count -= 1
        return next_object

    def has_next(self):
        """Tests if there are more elements in this list.

        return: (boolean) - true if more elements are available in this
                list, false if the end of the list has been reached
        compliance: mandatory - This method must be implemented.
        implementation notes: Any errors that may result from accesing
        the underlying set of elements are to be deferred until the
        consumer attempts retrieval in which case the provider must
        return true for this method.

        """
        if self._count is not None:
            # If count is available, use it
            return bool(self._count)
        else:
            # otherwise we have no idea
            return True

    def available(self):
        """Gets the number of elements available for retrieval.
        The number returned by this method may be less than or equal to
        the total number of elements in this list. To determine if the
        end of the list has been reached, the method has_next() should
        be used. This method conveys what is known about the number of
        remaining elements at a point in time and can be used to
        determine a minimum size of the remaining elements, if known. A
        valid return is zero even if has_next() is true.

        This method does not imply asynchronous usage. All OSID methods
        may block.
        return: (cardinal) - the number of elements available for
                retrieval
        compliance: mandatory - This method must be implemented.
        implementation notes: Any errors that may result from accesing
        the underlying set of elements are to be deferred until the
        consumer attempts retrieval in which case the provider must
        return a positive integer for this method so the consumer can
        continue execution to receive the error. In all other
        circumstances, the provider must not return a number greater
        than the number of elements known since this number will be fed
        as a parameter to the bulk retrieval method.

        """
        if self._count is not None:
            # If count is available, use it
            return self._count
        else:
            # We really have no idea.
            # Don't know what do do here, but for this
            # impl, which should only be constructed with
            # python lists, self._count should never be none.
            return 0

    def skip(self, n=None):
        """Skip the specified number of elements in the list.
        If the number skipped is greater than the number of elements in
        the list, hasNext() becomes false and available() returns zero
        as there are no more elements to retrieve.
        arg:    n (cardinal): the number of elements to skip
        compliance: mandatory - This method must be implemented.

        """
        while n > 0:
            try:
                self.next()
            except StopIteration:
                break
            n -= 1


class OsidCatalog(abc_osid_objects.OsidCatalog, OsidObject, markers.Sourceable, markers.Federateable):
    """``OsidCatalog`` is the top level interface for all OSID catalog-like objects.

    A catalog relates to other OSID objects for the purpose of
    organization and federation and almost always are hierarchical. An
    example catalog is a ``Repository`` that relates to a collection of
    ``Assets``.

    ``OsidCatalogs`` allow for the retrieval of a provider identity and
    branding.

    Collections visible through an ``OsidCatalog`` may be the output of
    a dynamic query or some other rules-based evaluation. The facts
    surrounding the evaluation are the ``OsidObjects`` visible to the
    ``OsidCatalog`` from its position in the federated hierarchy. The
    input conditions may satisifed on a service-wide basis using an
    ``OsidQuery`` or environmental conditions supplied to the services
    via a ``Proxy`` .

    Often, the selection of an ``OsidCatalog`` in instantiating an
    ``OsidSession`` provides access to a set of ``OsidObjects`` .
    Because the view inside an ``OsidCatalog`` can also be produced
    behaviorally using a rules evaluation, the ``Id`` (or well-known
    alias) of the ``OsidCatalog`` may be used as an abstract means of
    requesting a predefined set of behaviors or data constraints from an
    OSID Provider.

    The flexibility of interpretation together with its central role in
    federation to build a rich and complex service from a set of
    individual OSID Providers makes cataloging an essential pattern to
    achieve abstraction from implementations in the OSIDs without loss
    of functionality. Most OSIDs include a cataloging pattern.

    """
    pass


class OsidRule(abc_osid_objects.OsidRule, OsidObject, markers.Operable):
    """An ``OsidRule`` identifies an explicit or implicit rule evaluation.

    An associated ``Rule`` may be available in cases where the behavior
    of the object can be explicitly modified using a defined rule. In
    many cases, an ``OsidObject`` may define specific methods to manage
    certain common behavioral aspects and delegate anything above and
    beyond what has been defined to a rule evaluation.

    Rules are defined to be operable. In the case of a statement
    evaluation, an enabled rule overrides any evaluation to return
    ``true`` and a disabled rule overrides any evaluation to return
    ``false``.

    ``Rules`` are never required to consume or implement. They serve as
    a mechanism to offer a level of management not attainable in the
    immediate service definition. Each Rule implies evaluating a set of
    facts known to the service to produce a resulting beavior. Rule
    evaluations may also accept input data or conditions, however,
    ``OsidRules`` as they appear in throughout the services may or may
    not provide a means of supplying ``OsidConditions`` directly. In the
    services where an explicit ``OsidCondition`` is absent they may be
    masquerading as another interface such as a ``Proxy`` or an
    ``OsidQuery`` .

    """

    def has_rule(self):
        """Tests if an explicit rule is available.

        return: (boolean) - ``true`` if an explicit rule is available,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Someday I'll have a real implementation, but for now I just:
        return False

    def get_rule_id(self):
        """Gets the explicit rule ``Id``.

        return: (osid.id.Id) - the rule ``Id``
        raise:  IllegalState - ``has_rule()`` is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        from .osid_errors import IllegalState
        # Someday I'll have a real implementation, but for now I just:
        raise IllegalState()

    rule_id = property(fget=get_rule_id)

    def get_rule(self):
        """Gets the explicit rule.

        return: (osid.rules.Rule) - the rule
        raise:  IllegalState - ``has_rule()`` is ``false``
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        from .osid_errors import IllegalState
        # Someday I'll have a real implementation, but for now I just:
        raise IllegalState()

    rule = property(fget=get_rule)
