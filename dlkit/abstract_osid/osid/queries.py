"""Implementations of osid abstract base class queries."""
# pylint: disable=invalid-name
#     Method names comply with OSID specification.
# pylint: disable=no-init
#     Abstract classes do not define __init__.
# pylint: disable=too-few-public-methods
#     Some interfaces are specified as 'markers' and include no methods.
# pylint: disable=too-many-public-methods
#     Number of methods are defined in specification
# pylint: disable=too-many-ancestors
#     Inheritance defined in specification
# pylint: disable=too-many-arguments
#     Argument signature defined in specification.
# pylint: disable=duplicate-code
#     All apparent duplicates have been inspected. They aren't.
import abc


class OsidQuery:
    """The ``OsidQuery`` is used to assemble search queries.

    An ``OsidQuery`` is available from an ``OsidQuerySession`` and
    defines methods to match objects. Once the desired parameters are
    set, the ``OsidQuery`` is given to the designated search method. The
    same ``OsidQuery`` returned from the session must be used in the
    search as the provider may utilize implementation-specific data
    wiithin the object.

    If multiple data elements are set in this interface, the results
    matching all the given data (eg: AND) are returned.

    Any match method inside an ``OsidQuery`` may be invoked multiple
    times. In the case of a match method, each invocation adds an
    element to an ``OR`` expression. Any of these terms may also be
    negated through the ``match`` flag.
      OsidQuery { OsidQuery.matchDisplayName AND (OsidQuery.matchDescription OR OsidQuery.matchDescription)}



    ``OsidObjects`` allow for the definition of an additonal records and
    the ``OsidQuery`` parallels this mechanism. An interface type of an
    ``OsidObject`` record must also define the corresponding
    ``OsidQuery`` record which is available through query interfaces.
    Multiple requests of these typed interfaces may return the same
    underlying object and thus it is only useful to request once.

    An ``OsidQuery`` may be used to query for set or unset values using
    the "match any" methods. A field that has not bee explicitly
    assigned may default to a value. If multiple language translations
    exist and the query session is placed in a non-default locale,
    fields that have not been explicitly assigned in the non-default
    locale are considered unset even if the values from the default
    locale appear in the objects.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_string_match_types(self):
        """Gets the string matching types supported.

        A string match type specifies the syntax of the string query,
        such as matching a word or including a wildcard or regular
        expression.

        :return: a list containing the supported string match types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    string_match_types = property(fget=get_string_match_types)

    @abc.abstractmethod
    def supports_string_match_type(self, string_match_type):
        """Tests if the given string matching type is supported.

        :param string_match_type: a ``Type`` indicating a string match type
        :type string_match_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``string_match_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def match_keyword(self, keyword, string_match_type, match):
        """Adds a keyword to match.

        Multiple keywords can be added to perform a boolean ``OR`` among
        them. A keyword may be applied to any of the elements defined in
        this object such as the display name, description or any method
        defined in an interface implemented by this object.

        :param keyword: keyword to match
        :type keyword: ``string``
        :param string_match_type: the string match type
        :type string_match_type: ``osid.type.Type``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``keyword`` is not of ``string_match_type``
        :raise: ``NullArgument`` -- ``keyword`` or ``string_match_type`` is ``null``
        :raise: ``Unsupported`` -- ``supports_string_match_type(string_match_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_keyword_terms(self):
        """Clears all keyword terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    keyword_terms = property(fdel=clear_keyword_terms)

    @abc.abstractmethod
    def match_any(self, match):
        """Matches any object.

        :param match: ``true`` to match any object ``,``  ``false`` to match no objects
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_any_terms(self):
        """Clears the match any terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    any_terms = property(fdel=clear_any_terms)


class OsidIdentifiableQuery:
    """The ``OsidIdentiableQuery`` is used to assemble search queries for ``Identifiable`` objects.

    An ``OsidIdentifiableQuery`` is available from an
    ``OsidQuerySession`` and defines methods to match objects. Once the
    desired parameters are set, the ``OsidIdentifiableQuery`` is given
    to the designated search method. The same ``OsidIdentifiableQuery``
    returned from the session must be used in the search as the provider
    may utilize implementation-specific data wiithin the object.

    If multiple data elements are set in this interface, the results
    matching all the given data (eg: AND) are returned.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def match_id(self, id_, match):
        """Adds an ``Id`` to match.

        Multiple ``Ids`` can be added to perform a boolean ``OR`` among
        them.

        :param id: ``Id`` to match
        :type id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_id_terms(self):
        """Clears all ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    id_terms = property(fdel=clear_id_terms)


class OsidExtensibleQuery:
    """The ``OsidExtensibleQuery`` is used to assemble search queries for ``Extensible`` objects.

    An ``OsidExtensibleQuery`` is available from an ``OsidQuerySession``
    and defines methods to match objects. Once the desired parameters
    are set, the ``OsidExtensibleQuery`` is given to the designated
    search method. The same ``OsidExtensibleQuery`` returned from the
    session must be used in the search as the provider may utilize
    implementation-specific data wiithin the object.

    If multiple data elements are set in this interface, the results
    matching all the given data (eg: AND) are returned.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def match_record_type(self, record_type, match):
        """Sets a ``Type`` for querying objects having records implementing a given record type.

        :param record_type: a record type
        :type record_type: ``osid.type.Type``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def match_any_record(self, match):
        """Matches an object that has any record.

        :param match: ``true`` to match any record, ``false`` to match objects with no records
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_record_terms(self):
        """Clears all record ``Type`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    record_terms = property(fdel=clear_record_terms)


class OsidBrowsableQuery:
    """The ``OsidBrowsableQuery`` is used to assemble search queries for ``Browsable`` objects.

    An ``OsidBrowsableQuery`` is available from an ``OsidQuerySession``
    and defines methods to match objects. Once the desired parameters
    are set, the ``OsidBrowsableQuery`` is given to the designated
    search method. The same ``OsidBrowsableQuery`` returned from the
    session must be used in the search as the provider may utilize
    implementation-specific data wiithin the object.

    If multiple data elements are set in this interface, the results
    matching all the given data (eg: AND) are returned.

    """
    __metaclass__ = abc.ABCMeta


class OsidTemporalQuery:
    """This is the query interface for searching temporal objects.

    Each method specifies an ``AND`` term while multiple invocations of
    the same method produce a nested ``OR``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def match_effective(self, match):
        """Match effective objects where the current date falls within the start and end dates inclusive.

        :param match: ``true`` to match any effective, ``false`` to match ineffective
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_effective_terms(self):
        """Clears the effective query terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    effective_terms = property(fdel=clear_effective_terms)

    @abc.abstractmethod
    def match_start_date(self, start, end, match):
        """Matches temporals whose start date falls in between the given dates inclusive.

        :param start: start of date range
        :type start: ``osid.calendaring.DateTime``
        :param end: end of date range
        :type end: ``osid.calendaring.DateTime``
        :param match: ``true`` if a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``start`` is less than ``end``
        :raise: ``NullArgument`` -- ``start`` or ``end`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def match_any_start_date(self, match):
        """Matches temporals with any start date set.

        :param match: ``true`` to match any start date, ``false`` to match no start date
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_start_date_terms(self):
        """Clears the start date query terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    start_date_terms = property(fdel=clear_start_date_terms)

    @abc.abstractmethod
    def match_end_date(self, start, end, match):
        """Matches temporals whose effective end date falls in between the given dates inclusive.

        :param start: start of date range
        :type start: ``osid.calendaring.DateTime``
        :param end: end of date range
        :type end: ``osid.calendaring.DateTime``
        :param match: ``true`` if a positive match, ``false`` for negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``start`` is less than ``end``
        :raise: ``NullArgument`` -- ``start`` or ``end`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def match_any_end_date(self, match):
        """Matches temporals with any end date set.

        :param match: ``true`` to match any end date, ``false`` to match no start date
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_end_date_terms(self):
        """Clears the end date query terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    end_date_terms = property(fdel=clear_end_date_terms)

    @abc.abstractmethod
    def match_date(self, from_, to, match):
        """Matches temporals where the given date range falls entirely between the start and end dates inclusive.

        :param from: start date
        :type from: ``osid.calendaring.DateTime``
        :param to: end date
        :type to: ``osid.calendaring.DateTime``
        :param match: ``true`` if a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``from`` is less than ``to``
        :raise: ``NullArgument`` -- ``from`` or ``to`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_date_terms(self):
        """Clears the date query terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    date_terms = property(fdel=clear_date_terms)


class OsidSubjugateableQuery:
    """The ``OsidSubjugateableQuery`` is used to assemble search queries for dependent objects."""
    __metaclass__ = abc.ABCMeta


class OsidAggregateableQuery:
    """The ``OsidAggregateableQuery`` is used to assemble search queries for assemblages."""
    __metaclass__ = abc.ABCMeta


class OsidContainableQuery:
    """This is the query interface for searching containers.

    Each method specifies an ``AND`` term while multiple invocations of
    the same method produce a nested ``OR``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def match_sequestered(self, match):
        """Match containables that are sequestered.

        :param match: ``true`` to match any sequestered containables, ``false`` to match non-sequestered containables
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_sequestered_terms(self):
        """Clears the sequestered query terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    sequestered_terms = property(fdel=clear_sequestered_terms)


class OsidSourceableQuery:
    """The ``OsidSourceableQuery`` is used to assemble search queries for sourceables."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def match_provider_id(self, resource_id, match):
        """Match the ``Id`` of the provider resource.

        :param resource_id: ``Id`` to match
        :type resource_id: ``osid.id.Id``
        :param match: ``true`` if for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_provider_id_terms(self):
        """Clears all provider ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    provider_id_terms = property(fdel=clear_provider_id_terms)

    @abc.abstractmethod
    def supports_provider_query(self):
        """Tests if a ``ResourceQuery`` for the provider is available.

        :return: ``true`` if a resource query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_provider_query(self, match):
        """Gets the query for the provider.

        Each retrieval performs a boolean ``OR``.

        :param match: ``true`` if for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :return: the provider query
        :rtype: ``osid.resource.ResourceQuery``
        :raise: ``Unimplemented`` -- ``supports_provider_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_provider_query()`` is ``true``.*

        """
        return  # osid.resource.ResourceQuery

    @abc.abstractmethod
    def match_any_provider(self, match):
        """Match sourceables with a provider value.

        :param match: ``true`` to match sourceables with any provider, ``false`` to match sourceables with no providers
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_provider_terms(self):
        """Clears all provider terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    provider_terms = property(fdel=clear_provider_terms)

    @abc.abstractmethod
    def match_branding_id(self, asset_id, match):
        """Match the ``Id`` of an asset used for branding.

        :param asset_id: ``Id`` to match
        :type asset_id: ``osid.id.Id``
        :param match: ``true`` if for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``asset_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_branding_id_terms(self):
        """Clears all asset ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    branding_id_terms = property(fdel=clear_branding_id_terms)

    @abc.abstractmethod
    def supports_branding_query(self):
        """Tests if an ``AssetQuery`` for the branding is available.

        :return: ``true`` if a asset query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_branding_query(self, match):
        """Gets the query for an asset.

        Each retrieval performs a boolean ``OR``.

        :param match: ``true`` if for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :return: the asset query
        :rtype: ``osid.repository.AssetQuery``
        :raise: ``Unimplemented`` -- ``supports_branding_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_branding_query()`` is ``true``.*

        """
        return  # osid.repository.AssetQuery

    @abc.abstractmethod
    def match_any_branding(self, match):
        """Match sourceables with any branding.

        :param match: ``true`` to match any asset, ``false`` to match no assets
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_branding_terms(self):
        """Clears all branding terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    branding_terms = property(fdel=clear_branding_terms)

    @abc.abstractmethod
    def match_license(self, license_, string_match_type, match):
        """Adds a license to match.

        Multiple license matches can be added to perform a boolean
        ``OR`` among them.

        :param license: a string to match
        :type license: ``string``
        :param string_match_type: the string match type
        :type string_match_type: ``osid.type.Type``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``license`` is not of ``string_match_type``
        :raise: ``NullArgument`` -- ``license`` or ``string_match_type`` is ``null``
        :raise: ``Unsupported`` -- ``supports_string_match_type(string_match_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def match_any_license(self, match):
        """Matches any object with a license.

        :param match: ``true`` to match any license, ``false`` to match objects with no license
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_license_terms(self):
        """Clears all license terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    license_terms = property(fdel=clear_license_terms)


class OsidFederateableQuery:
    """The ``OsidFederateableQuery`` is used to assemble search queries for federated objects."""
    __metaclass__ = abc.ABCMeta


class OsidOperableQuery:
    """This is the query interface for searching operables.

    Each method specifies an ``AND`` term while multiple invocations of
    the same method produce a nested ``OR``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def match_active(self, match):
        """Matches active.

        :param match: ``true`` to match active, ``false`` to match inactive
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_active_terms(self):
        """Clears the active query terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    active_terms = property(fdel=clear_active_terms)

    @abc.abstractmethod
    def match_enabled(self, match):
        """Matches administratively enabled.

        :param match: ``true`` to match administratively enabled, ``false`` otherwise
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_enabled_terms(self):
        """Clears the administratively enabled query terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    enabled_terms = property(fdel=clear_enabled_terms)

    @abc.abstractmethod
    def match_disabled(self, match):
        """Matches administratively disabled.

        :param match: ``true`` to match administratively disabled, ``false`` otherwise
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_disabled_terms(self):
        """Clears the administratively disabled query terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    disabled_terms = property(fdel=clear_disabled_terms)

    @abc.abstractmethod
    def match_operational(self, match):
        """Matches operational operables.

        :param match: ``true`` to match operational, ``false`` to match not operational
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_operational_terms(self):
        """Clears the operational query terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    operational_terms = property(fdel=clear_operational_terms)


class OsidObjectQuery:
    """The ``OsidObjectQuery`` is used to assemble search queries.

    An ``OsidObjectQuery`` is available from an ``OsidSession`` and
    defines methods to query for an ``OsidObject`` that includes setting
    a display name and a description. Once the desired parameters are
    set, the ``OsidQuery`` is given to the designated search method. The
    same ``OsidQuery`` returned from the session must be used in the
    search as the provider may utilize implementation-specific data
    wiithin the object.

    If multiple data elements are set in this interface, the results
    matching all the given data (eg: AND) are returned.

    Any match method inside an ``OsidObjectQuery`` may be invoked
    multiple times. In the case of a match method, each invocation adds
    an element to an ``OR`` expression. Any of these terms may also be
    negated through the ``match`` flag.
      OsidObjectQuery { OsidQuery.matchDisplayName AND (OsidQuery.matchDescription OR OsidObjectQuery.matchDescription)}



    ``OsidObjects`` allow for the definition of an additonal records and
    the ``OsidQuery`` parallels this mechanism. An interface type of an
    ``OsidObject`` record must also define the corresponding
    ``OsidQuery`` record which is available through query interfaces.
    Multiple requests of these typed interfaces may return the same
    underlying object and thus it is only useful to request once.

    String searches are described using a string search ``Type`` that
    indicates the type of regular expression or wildcarding encoding.
    Compatibility with a strings search ``Type`` can be tested within
    this interface.

    As with all aspects of OSIDs, nulls cannot be used. Separate tests
    are available for querying for unset values except for required
    fields.

    An example to find all objects whose name starts with "Fred" or
    whose name starts with "Barney", but the word "dinosaur" does not
    appear in the description and not the color is not purple.
    ``ColorQuery`` is a record of the object that defines a color.
      ObjectObjectQuery query;
      query = session.getObjectQuery();
      query.matchDisplayName("Fred*", wildcardStringMatchType, true);
      query.matchDisplayName("Barney*", wildcardStringMatchType, true);
      query.matchDescriptionMatch("dinosaur", wordStringMatchType, false);

      ColorQuery recordQuery;
      recordQuery = query.getObjectRecord(colorRecordType);
      recordQuery.matchColor("purple", false);
      ObjectList list = session.getObjectsByQuery(query);

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def match_display_name(self, display_name, string_match_type, match):
        """Adds a display name to match.

        Multiple display name matches can be added to perform a boolean
        ``OR`` among them.

        :param display_name: display name to match
        :type display_name: ``string``
        :param string_match_type: the string match type
        :type string_match_type: ``osid.type.Type``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``display_name`` is not of ``string_match_type``
        :raise: ``NullArgument`` -- ``display_name`` or ``string_match_type`` is ``null``
        :raise: ``Unsupported`` -- ``supports_string_match_type(string_match_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def match_any_display_name(self, match):
        """Matches any object with a display name.

        :param match: ``true`` to match any display name, ``false`` to match objects with no display name
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_display_name_terms(self):
        """Clears all display name terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    display_name_terms = property(fdel=clear_display_name_terms)

    @abc.abstractmethod
    def match_description(self, description, string_match_type, match):
        """Adds a description name to match.

        Multiple description matches can be added to perform a boolean
        ``OR`` among them.

        :param description: description to match
        :type description: ``string``
        :param string_match_type: the string match type
        :type string_match_type: ``osid.type.Type``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``description`` is not of ``string_match_type``
        :raise: ``NullArgument`` -- ``description`` or ``string_match_type`` is ``null``
        :raise: ``Unsupported`` -- ``supports_string_match_type(string_match_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def match_any_description(self, match):
        """Matches a description that has any value.

        :param match: ``true`` to match any description, ``false`` to match descriptions with no values
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_description_terms(self):
        """Clears all description terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    description_terms = property(fdel=clear_description_terms)

    @abc.abstractmethod
    def match_genus_type(self, genus_type, match):
        """Sets a ``Type`` for querying objects of a given genus.

        A genus type matches if the specified type is the same genus as
        the object genus type.

        :param genus_type: the object genus type
        :type genus_type: ``osid.type.Type``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``genus_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def match_any_genus_type(self, match):
        """Matches an object that has any genus type.

        :param match: ``true`` to match any genus type, ``false`` to match objects with no genus type
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_genus_type_terms(self):
        """Clears all genus type terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    genus_type_terms = property(fdel=clear_genus_type_terms)

    @abc.abstractmethod
    def match_parent_genus_type(self, genus_type, match):
        """Sets a ``Type`` for querying objects of a given genus.

        A genus type matches if the specified type is the same genus as
        the object or if the specified type is an ancestor of the object
        genus in a type hierarchy.

        :param genus_type: the object genus type
        :type genus_type: ``osid.type.Type``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``genus_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_parent_genus_type_terms(self):
        """Clears all genus type terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    parent_genus_type_terms = property(fdel=clear_parent_genus_type_terms)

    @abc.abstractmethod
    def match_subject_id(self, subject_id, match):
        """Matches an object with a relationship to the given subject.

        :param subject_id: a subject ``Id``
        :type subject_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``subject_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_subject_id_terms(self):
        """Clears all subject ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    subject_id_terms = property(fdel=clear_subject_id_terms)

    @abc.abstractmethod
    def supports_subject_query(self):
        """Tests if a ``SubjectQuery`` is available.

        :return: ``true`` if a subject query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_subject_query(self):
        """Gets the query for a subject.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the subject query
        :rtype: ``osid.ontology.SubjectQuery``
        :raise: ``Unimplemented`` -- ``supports_subject_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_subject_query()`` is ``true``.*

        """
        return  # osid.ontology.SubjectQuery

    subject_query = property(fget=get_subject_query)

    @abc.abstractmethod
    def match_any_subject(self, match):
        """Matches an object that has any relationship to a ``Subject``.

        :param match: ``true`` to match any subject, ``false`` to match objects with no subjects
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_subject_terms(self):
        """Clears all subject terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    subject_terms = property(fdel=clear_subject_terms)

    @abc.abstractmethod
    def supports_subject_relevancy_query(self):
        """Tests if a ``RelevancyQuery`` is available to provide queries about the relationships to ``Subjects``.

        :return: ``true`` if a relevancy entry query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_subject_relevancy_query(self):
        """Gets the query for a subject relevancy.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the relevancy query
        :rtype: ``osid.ontology.RelevancyQuery``
        :raise: ``Unimplemented`` -- ``supports_subject_relevancy_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_subject_relevancy_query()`` is ``true``.*

        """
        return  # osid.ontology.RelevancyQuery

    subject_relevancy_query = property(fget=get_subject_relevancy_query)

    @abc.abstractmethod
    def clear_subject_relevancy_terms(self):
        """Clears all subject relevancy terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    subject_relevancy_terms = property(fdel=clear_subject_relevancy_terms)

    @abc.abstractmethod
    def match_state_id(self, state_id, match):
        """Matches an object mapped to the given state.

        :param state_id: a state ``Id``
        :type state_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``state_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_state_id_terms(self):
        """Clears all state ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    state_id_terms = property(fdel=clear_state_id_terms)

    @abc.abstractmethod
    def supports_state_query(self):
        """Tests if a ``StateQuery`` is available to provide queries of processed objects.

        :return: ``true`` if a state query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_state_query(self):
        """Gets the query for a state.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the journal entry query
        :rtype: ``osid.process.StateQuery``
        :raise: ``Unimplemented`` -- ``supports_state_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_state_query()`` is ``true``.*

        """
        return  # osid.process.StateQuery

    state_query = property(fget=get_state_query)

    @abc.abstractmethod
    def match_any_state(self, match):
        """Matches an object that has any mapping to a ``State`` in the given ``Process``.

        :param match: ``true`` to match any state, ``false`` to match objects with no states
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_state_terms(self):
        """Clears all state terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    state_terms = property(fdel=clear_state_terms)

    @abc.abstractmethod
    def match_comment_id(self, comment_id, match):
        """Matches an object that has the given comment.

        :param comment_id: a comment ``Id``
        :type comment_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``comment_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_comment_id_terms(self):
        """Clears all comment ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    comment_id_terms = property(fdel=clear_comment_id_terms)

    @abc.abstractmethod
    def supports_comment_query(self):
        """Tests if a ``CommentQuery`` is available.

        :return: ``true`` if a comment query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_comment_query(self):
        """Gets the query for a comment.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the comment query
        :rtype: ``osid.commenting.CommentQuery``
        :raise: ``Unimplemented`` -- ``supports_comment_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_comment_query()`` is ``true``.*

        """
        return  # osid.commenting.CommentQuery

    comment_query = property(fget=get_comment_query)

    @abc.abstractmethod
    def match_any_comment(self, match):
        """Matches an object that has any ``Comment`` in the given ``Book``.

        :param match: ``true`` to match any comment, ``false`` to match objects with no comments
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_comment_terms(self):
        """Clears all comment terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    comment_terms = property(fdel=clear_comment_terms)

    @abc.abstractmethod
    def match_journal_entry_id(self, journal_entry_id, match):
        """Matches an object that has the given journal entry.

        :param journal_entry_id: a journal entry ``Id``
        :type journal_entry_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``journal_entry_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_journal_entry_id_terms(self):
        """Clears all journal entry ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    journal_entry_id_terms = property(fdel=clear_journal_entry_id_terms)

    @abc.abstractmethod
    def supports_journal_entry_query(self):
        """Tests if a ``JournalEntry`` is available to provide queries of journaled ``OsidObjects``.

        :return: ``true`` if a journal entry query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_journal_entry_query(self):
        """Gets the query for a journal entry.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the journal entry query
        :rtype: ``osid.journaling.JournalEntryQuery``
        :raise: ``Unimplemented`` -- ``supports_journal_entry_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_journal_entry_query()`` is ``true``.*

        """
        return  # osid.journaling.JournalEntryQuery

    journal_entry_query = property(fget=get_journal_entry_query)

    @abc.abstractmethod
    def match_any_journal_entry(self, match):
        """Matches an object that has any ``JournalEntry`` in the given ``Journal``.

        :param match: ``true`` to match any journal entry, ``false`` to match objects with no journal entries
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_journal_entry_terms(self):
        """Clears all journal entry terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    journal_entry_terms = property(fdel=clear_journal_entry_terms)

    @abc.abstractmethod
    def supports_statistic_query(self):
        """Tests if a ``StatisticQuery`` is available to provide statistical queries.

        :return: ``true`` if a statistic query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_statistic_query(self):
        """Gets the query for a statistic.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the statistic query
        :rtype: ``osid.metering.StatisticQuery``
        :raise: ``Unimplemented`` -- ``supports_statistic_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_statistic_query()`` is ``true``.*

        """
        return  # osid.metering.StatisticQuery

    statistic_query = property(fget=get_statistic_query)

    @abc.abstractmethod
    def match_any_statistic(self, match):
        """Matches an object that has any ``Statistic``.

        :param match: ``true`` to match any statistic, ``false`` to match objects with no statistics
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_statistic_terms(self):
        """Clears all statistic terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    statistic_terms = property(fdel=clear_statistic_terms)

    @abc.abstractmethod
    def match_credit_id(self, credit_id, match):
        """Matches an object that has the given credit.

        :param credit_id: a credit ``Id``
        :type credit_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``credit_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_credit_id_terms(self):
        """Clears all credit ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    credit_id_terms = property(fdel=clear_credit_id_terms)

    @abc.abstractmethod
    def supports_credit_query(self):
        """Tests if a ``CreditQuery`` is available to provide queries of related acknowledgements.

        :return: ``true`` if a credit query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_credit_query(self):
        """Gets the query for an ackowledgement credit.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the credit query
        :rtype: ``osid.acknowledgement.CreditQuery``
        :raise: ``Unimplemented`` -- ``supports_credit_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_credit_query()`` is ``true``.*

        """
        return  # osid.acknowledgement.CreditQuery

    credit_query = property(fget=get_credit_query)

    @abc.abstractmethod
    def match_any_credit(self, match):
        """Matches an object that has any ``Credit``.

        :param match: ``true`` to match any credit, ``false`` to match objects with no credits
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_credit_terms(self):
        """Clears all credit terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    credit_terms = property(fdel=clear_credit_terms)

    @abc.abstractmethod
    def match_relationship_id(self, relationship_id, match):
        """Matches an object that has the given relationship.

        :param relationship_id: a relationship ``Id``
        :type relationship_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``relationship_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_relationship_id_terms(self):
        """Clears all relationship ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    relationship_id_terms = property(fdel=clear_relationship_id_terms)

    @abc.abstractmethod
    def supports_relationship_query(self):
        """Tests if a ``RelationshipQuery`` is available.

        :return: ``true`` if a relationship query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_relationship_query(self):
        """Gets the query for relationship.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the relationship query
        :rtype: ``osid.relationship.RelationshipQuery``
        :raise: ``Unimplemented`` -- ``supports_relationship_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_relationship_query()`` is ``true``.*

        """
        return  # osid.relationship.RelationshipQuery

    relationship_query = property(fget=get_relationship_query)

    @abc.abstractmethod
    def match_any_relationship(self, match):
        """Matches an object that has any ``Relationship``.

        :param match: ``true`` to match any relationship, ``false`` to match objects with no relationships
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_relationship_terms(self):
        """Clears all relationship terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    relationship_terms = property(fdel=clear_relationship_terms)

    @abc.abstractmethod
    def match_relationship_peer_id(self, peer_id, match):
        """Matches an object that has a relationship to the given peer ``Id``.

        :param peer_id: a relationship peer ``Id``
        :type peer_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``peer_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_relationship_peer_id_terms(self):
        """Clears all relationship ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    relationship_peer_id_terms = property(fdel=clear_relationship_peer_id_terms)


class OsidRelationshipQuery:
    """This is the query interface for searching relationships.

    Each method specifies an ``AND`` term while multiple invocations of
    the same method produce a nested ``OR``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def match_end_reason_id(self, state_id, match):
        """Match the ``Id`` of the end reason state.

        :param state_id: ``Id`` to match
        :type state_id: ``osid.id.Id``
        :param match: ``true`` if for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``rule_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_end_reason_id_terms(self):
        """Clears all state ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    end_reason_id_terms = property(fdel=clear_end_reason_id_terms)

    @abc.abstractmethod
    def supports_end_reason_query(self):
        """Tests if a ``StateQuery`` for the end reason is available.

        :return: ``true`` if a end reason query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_end_reason_query(self, match):
        """Gets the query for the end reason state.

        Each retrieval performs a boolean ``OR``.

        :param match: ``true`` if for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :return: the state query
        :rtype: ``osid.process.StateQuery``
        :raise: ``Unimplemented`` -- ``supports_end_reason_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_end_reason_query()`` is ``true``.*

        """
        return  # osid.process.StateQuery

    @abc.abstractmethod
    def match_any_end_reason(self, match):
        """Match any end reason state.

        :param match: ``true`` to match any state, ``false`` to match no state
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_end_reason_terms(self):
        """Clears all end reason state terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    end_reason_terms = property(fdel=clear_end_reason_terms)


class OsidCatalogQuery:
    """The ``OsidCatalogQuery`` is used to assemble search queries for catalogs."""
    __metaclass__ = abc.ABCMeta


class OsidRuleQuery:
    """This is the query interface for searching rules.

    Each method specifies an ``AND`` term while multiple invocations of
    the same method produce a nested ``OR``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def match_rule_id(self, rule_id, match):
        """Match the ``Id`` of the rule.

        :param rule_id: ``Id`` to match
        :type rule_id: ``osid.id.Id``
        :param match: ``true`` if for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``rule_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_rule_id_terms(self):
        """Clears all rule ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    rule_id_terms = property(fdel=clear_rule_id_terms)

    @abc.abstractmethod
    def supports_rule_query(self):
        """Tests if a ``RuleQuery`` for the rule is available.

        :return: ``true`` if a rule query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_rule_query(self, match):
        """Gets the query for the rule.

        Each retrieval performs a boolean ``OR``.

        :param match: ``true`` if for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :return: the rule query
        :rtype: ``osid.rules.RuleQuery``
        :raise: ``Unimplemented`` -- ``supports_rule_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_rule_query()`` is ``true``.*

        """
        return  # osid.rules.RuleQuery

    @abc.abstractmethod
    def match_any_rule(self, match):
        """Match any associated rule.

        :param match: ``true`` to match any rule, ``false`` to match no rules
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_rule_terms(self):
        """Clears all rule terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    rule_terms = property(fdel=clear_rule_terms)


class OsidEnablerQuery:
    """This is the query interface for searching enablers.

    Each method specifies an ``AND`` term while multiple invocations of
    the same method produce a nested ``OR``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def match_schedule_id(self, schedule_id, match):
        """Match the ``Id`` of an associated schedule.

        :param schedule_id: ``Id`` to match
        :type schedule_id: ``osid.id.Id``
        :param match: ``true`` if for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``schedule_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_schedule_id_terms(self):
        """Clears all schedule ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    schedule_id_terms = property(fdel=clear_schedule_id_terms)

    @abc.abstractmethod
    def supports_schedule_query(self):
        """Tests if a ``ScheduleQuery`` for the rule is available.

        :return: ``true`` if a schedule query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_schedule_query(self, match):
        """Gets the query for the schedule.

        Each retrieval performs a boolean ``OR``.

        :param match: ``true`` if for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :return: the schedule query
        :rtype: ``osid.calendaring.ScheduleQuery``
        :raise: ``Unimplemented`` -- ``supports_schedule_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_schedule_query()`` is ``true``.*

        """
        return  # osid.calendaring.ScheduleQuery

    @abc.abstractmethod
    def match_any_schedule(self, match):
        """Match any associated schedule.

        :param match: ``true`` to match any schedule, ``false`` to match no schedules
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_schedule_terms(self):
        """Clears all schedule terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    schedule_terms = property(fdel=clear_schedule_terms)

    @abc.abstractmethod
    def match_event_id(self, event_id, match):
        """Match the ``Id`` of an associated event.

        :param event_id: ``Id`` to match
        :type event_id: ``osid.id.Id``
        :param match: ``true`` if for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``event_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_event_id_terms(self):
        """Clears all event ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    event_id_terms = property(fdel=clear_event_id_terms)

    @abc.abstractmethod
    def supports_event_query(self):
        """Tests if a ``EventQuery`` for the rule is available.

        :return: ``true`` if an event query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_event_query(self, match):
        """Gets the query for the event.

        Each retrieval performs a boolean ``OR``.

        :param match: ``true`` if for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :return: the event query
        :rtype: ``osid.calendaring.EventQuery``
        :raise: ``Unimplemented`` -- ``supports_event_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_event_query()`` is ``true``.*

        """
        return  # osid.calendaring.EventQuery

    @abc.abstractmethod
    def match_any_event(self, match):
        """Match any associated event.

        :param match: ``true`` to match any event, ``false`` to match no events
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_event_terms(self):
        """Clears all recurirng event terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    event_terms = property(fdel=clear_event_terms)

    @abc.abstractmethod
    def match_cyclic_event_id(self, cyclic_event_id, match):
        """Sets the cyclic event ``Id`` for this query.

        :param cyclic_event_id: the cyclic event ``Id``
        :type cyclic_event_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``cyclic_event_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_cyclic_event_id_terms(self):
        """Clears the cyclic event ``Id`` query terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    cyclic_event_id_terms = property(fdel=clear_cyclic_event_id_terms)

    @abc.abstractmethod
    def supports_cyclic_event_query(self):
        """Tests if a ``CyclicEventQuery`` is available.

        :return: ``true`` if a cyclic event query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_cyclic_event_query(self):
        """Gets the query for a cyclic event.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the cyclic event query
        :rtype: ``osid.calendaring.cycle.CyclicEventQuery``
        :raise: ``Unimplemented`` -- ``supports_cyclic_event_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_cyclic_event_query()`` is ``true``.*

        """
        return  # osid.calendaring.cycle.CyclicEventQuery

    cyclic_event_query = property(fget=get_cyclic_event_query)

    @abc.abstractmethod
    def match_any_cyclic_event(self, match):
        """Matches any enabler with a cyclic event.

        :param match: ``true`` to match any enablers with a cyclic event, ``false`` to match enablers with no cyclic events
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_cyclic_event_terms(self):
        """Clears the cyclic event query terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    cyclic_event_terms = property(fdel=clear_cyclic_event_terms)

    @abc.abstractmethod
    def match_demographic_id(self, resource_id, match):
        """Match the ``Id`` of the demographic resource.

        :param resource_id: ``Id`` to match
        :type resource_id: ``osid.id.Id``
        :param match: ``true`` if for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_demographic_id_terms(self):
        """Clears all resource ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    demographic_id_terms = property(fdel=clear_demographic_id_terms)

    @abc.abstractmethod
    def supports_demographic_query(self):
        """Tests if a ``ResourceQuery`` for the demographic is available.

        :return: ``true`` if a resource query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_demographic_query(self, match):
        """Gets the query for the resource.

        Each retrieval performs a boolean ``OR``.

        :param match: ``true`` if for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :return: the resource query
        :rtype: ``osid.resource.ResourceQuery``
        :raise: ``Unimplemented`` -- ``supports_resource_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_resource_query()`` is ``true``.*

        """
        return  # osid.resource.ResourceQuery

    @abc.abstractmethod
    def match_any_demographic(self, match):
        """Match any associated resource.

        :param match: ``true`` to match any demographic, ``false`` to match no rules
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_demographic_terms(self):
        """Clears all demographic terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    demographic_terms = property(fdel=clear_demographic_terms)


class OsidConstrainerQuery:
    """This is the query interface for searching constrainers.

    Each method specifies an ``AND`` term while multiple invocations of
    the same method produce a nested ``OR``.

    """
    __metaclass__ = abc.ABCMeta


class OsidProcessorQuery:
    """This is the query interface for searching processors.

    Each method specifies an ``AND`` term while multiple invocations of
    the same method produce a nested ``OR``.

    """
    __metaclass__ = abc.ABCMeta


class OsidGovernatorQuery:
    """This is the query interface for searching governers.

    Each method specifies an ``AND`` term while multiple invocations of
    the same method produce a nested ``OR``.

    """
    __metaclass__ = abc.ABCMeta


class OsidCompendiumQuery:
    """This is the query interface for searching reports.

    Each method specifies an ``AND`` term while multiple invocations of
    the same method produce a nested ``OR``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def match_start_date(self, start, end, match):
        """Matches reports whose start date falls in between the given dates inclusive.

        :param start: start of date range
        :type start: ``osid.calendaring.DateTime``
        :param end: end of date range
        :type end: ``osid.calendaring.DateTime``
        :param match: ``true`` if a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``start`` is less than ``end``
        :raise: ``NullArgument`` -- ``start`` or ``end`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def match_any_start_date(self, match):
        """Matches reports with any start date set.

        :param match: ``true`` to match any start date, ``false`` to match no start date
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_start_date_terms(self):
        """Clears the start date query terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    start_date_terms = property(fdel=clear_start_date_terms)

    @abc.abstractmethod
    def match_end_date(self, start, end, match):
        """Matches reports whose effective end date falls in between the given dates inclusive.

        :param start: start of date range
        :type start: ``osid.calendaring.DateTime``
        :param end: end of date range
        :type end: ``osid.calendaring.DateTime``
        :param match: ``true`` if a positive match, ``false`` for negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``start`` is less than ``end``
        :raise: ``NullArgument`` -- ``start`` or ``end`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def match_any_end_date(self, match):
        """Matches reports with any end date set.

        :param match: ``true`` to match any end date, ``false`` to match no start date
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_end_date_terms(self):
        """Clears the end date query terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    end_date_terms = property(fdel=clear_end_date_terms)

    @abc.abstractmethod
    def match_interpolated(self, match):
        """Match reports that are interpolated.

        :param match: ``true`` to match any interpolated reports, ``false`` to match non-interpolated reports
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_interpolated_terms(self):
        """Clears the interpolated query terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    interpolated_terms = property(fdel=clear_interpolated_terms)

    @abc.abstractmethod
    def match_extrapolated(self, match):
        """Match reports that are extrapolated.

        :param match: ``true`` to match any extrapolated reports, ``false`` to match non-extrapolated reports
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_extrapolated_terms(self):
        """Clears the extrapolated query terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    extrapolated_terms = property(fdel=clear_extrapolated_terms)


class OsidCapsuleQuery:
    """This is the query interface for searching capsulating interfaces.

    Each method specifies an ``AND`` term while multiple invocations of
    the same method produce a nested ``OR``.

    """
    __metaclass__ = abc.ABCMeta
