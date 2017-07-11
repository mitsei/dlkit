from dlkit.abstract_osid.osid import markers as abc_osid_markers


class OsidPrimitive(abc_osid_markers.OsidPrimitive):
    """A marker interface for an interface that behaves like a language
    primitive.
    """


class Identifiable(abc_osid_markers.Identifiable):
    """A marker interface for objects uniquely identified with an OSID Id."""
    # The authority for all identifiers can be set in settings.py:
    # Disregard and delete as necessary:

    import socket
    _authority = socket.gethostname()

    def get_id(self):
        from .. import primitives
        return primitives.Id(identifier=self._identifier,
                             namespace=self._namespace,
                             authority=self._authority)

    def is_current(self):
        """Tests to see if the last method invoked retrieved up-to-date
        data."""
        return True  # I think, since this is all hard-coded anyway

    id_ = property(get_id)
    ident = property(get_id)


class Extensible(abc_osid_markers.Extensible):
    """A marker interface for objects that contain OsidRecords."""

    def __init__(self):  # This will never get called :)
        from ..type.objects import TypeList
        self._record_types = TypeList([])

    def get_record_types(self):
        """Gets the record types available in this object."""
        return self._record_types

        """
        if self._my_extension_map is None:
            self._my_extension_map = self._get_extension_map()
        type_list = []
        for type_id in self._my_extension_map['recordTypeIds']:
            url_path = '/handcar/services/learning/types/' + type_id
            type_list.append(self._get_request(url_path))
        return TypeList(type_list)"""

    def has_record_type(self, record_type=None):
        """Tests if this object supports the given record Type."""
        return record_type in self._record_types

    record_types = property(get_record_types)


class Browsable(abc_osid_markers.Browsable):
    """A marker interface for objects that offer property inspection."""

    def get_properties(self):
        """Gets a list of properties."""
        pass

    def get_properties_by_record_type(self, record_type=None):
        """Gets a list of properties corresponding to the specified record
        type."""
        pass

    properties = property(get_properties)


class Suppliable(abc_osid_markers.Suppliable):
    pass


class Temporal(abc_osid_markers.Temporal):
    """``Temporal`` is used to indicate the object endures for a period of time."""

    def is_effective(self):
        """Tests if the current date is within the start end end dates inclusive.

        return: (boolean) - ``true`` if this is effective, ``false``
                otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def get_start_date(self):
        """Gets the start date.

        return: (osid.calendaring.DateTime) - the start date
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def get_end_date(self):
        """Gets the end date.

        return: (osid.calendaring.DateTime) - the end date
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class Aggregateable(abc_osid_markers.Aggregateable):
    """Aggregateable is used for an OsidObject to indicate that some or all
    of the definition is based on an included set of other OsidObjects
    which are directly accessible and do not exist outside the context
    of the parent object.

    Aggregateables allow for an OsidObject to stand alone without
    knowledge of the originating service.

    An Asset is an example of an aggregate by including the
    AssetContents. An Asset also contains a provider however in this
    case the provider is categorized as a simple data attribute of the
    Asset that can be changed by updating the Asset using an AssetForm.
    The AssetContent differs in there exists a explicit mapping to the
    Asset managed through an OsidSession but accessible directly within
    the Asset to enable its consumption outside the Repository OSID.

    This marker has little practicality other than to identify a service
    pattern that is neither a data attribute nor a separately accessible
    relationship or mapping.

    """


class Sourceable(abc_osid_markers.Sourceable):
    """Sourceble is used for OsidObjects where information about a provider
    is appropriate."""

    def get_provider_id(self):
        """Gets the Id of the provider."""
        pass

    def get_provider(self):
        """Gets the Resource representing the provider."""
        pass

    def get_branding_ids(self):
        """Gets the branding asset ``Ids``."""
        pass

    def get_branding(self):
        """Gets a branding, such as an image or logo, expressed using the
        Asset interface."""
        pass

    def get_license(self):
        """Gets the terms of usage."""
        pass

    provider_id = property(get_provider_id)
    provider = property(get_provider)
    branding_ids = property(get_branding_ids)
    branding = property(get_branding)
    license = property(get_license)


class Federateable(abc_osid_markers.Federateable):
    """Federateable is used to indicate an OsidObject can be federated
    using the OSID Hierarchy pattern."""


class Operable(abc_osid_markers.Operable):
    """``Operable`` is used to indicate an ``OsidObject`` performs operations.

    The active status indicates if the ``Operable`` is on or off. The
    active status is determined from the operational status and the
    enabling rules.

    The operational status indicates the Operable is functioning. This
    status is not set administratively but instead refelects suitable
    conditions for operation.

    Operables may be administratively turned on of off through the
    enabled and disabled administrative overrides. If there are no
    related ``OsidEnabler`` rules, then ``is_enabled()`` should be set
    to ``true`` and ``is_disabled()`` set to ``false`` for the
    ``Operable`` to be on and ``is_enabled()`` set to ``false`` and
    ``is_disabled()`` set to true for the ``Operable`` to be ``off``.
    ``is_enabled()`` and ``is_disabled()`` cannot both be ``tru`` e.

    If there are related ``OsidEnabler`` rules, the active status of at
    least one ``OsidEnabler`` results in a ``true`` value for
    ``isOperational()``. This active status can be overridden by setting
    ``is_disabled()`` to ``true``. If there are no active
    ``OsidEnabler`` rules, ``is_operational()`` is false resulting in an
    ``off``  ``Operable`` unless ``is_enabled()`` is ``true`` .

    For the active status to be completely determined by the
    ``OsidEnablers,`` both ``is_enabled()`` and ``is_disabled()`` should
    be ``false`` where the ``is_active()`` status is completely driven
    from ``isOperational()``.

    """

    def is_active(self):
        """Tests if this operable is active.

        ``is_active()`` is ``true`` if ``is_operational()`` is ``true``
        and ``is_disabled()`` is ``false,`` or ``is_enabled()`` is
        ``true``.

        return: (boolean) - ``true`` if this operable is on, ``false``
                if it is off
        *compliance: mandatory -- This method must be implemented.*

        """
        # THIS MAY NOT BE RIGHT. REVIEW LOGIC FROM OSID DOC
        return self.is_operational() and (not self.is_disabled() or self.is_enabled())

    def is_enabled(self):
        """Tests if this operable is administravely enabled.

        Administratively enabling overrides any applied ``OsidEnabler``.
        If this method returns ``true`` then ``is_disabled()`` must
        return ``false``.

        return: (boolean) - ``true`` if this operable is enabled,
                ``false`` if the active status is determined by other
                rules
        *compliance: mandatory -- This method must be implemented.*

        """
        # Someday I'll have a real implementation, but for now I just:
        return False

    def is_disabled(self):
        """Tests if this operable is administravely disabled.

        Administratively disabling overrides any applied
        ``OsidEnabler``. If this method returns ``true`` then
        ``is_enabled()`` must return ``false``.

        return: (boolean) - ``true`` if this operable is disabled,
                ``false`` if the active status is determined by other
                rules
        *compliance: mandatory -- This method must be implemented.*

        """
        # Someday I'll have a real implementation, but for now I just:
        return True

    def is_operational(self):
        """Tests if this ``Operable`` is operational.

        This Operable is operational if any of the applied
        ``OsidEnablers`` are ``true``.

        return: (boolean) - ``true`` if this operable is operational,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Someday I'll have a real implementation, but for now I just:
        return False


class Subjugateable(abc_osid_markers.Subjugateable):
    """A ``Subjugateable`` is an ``OsidObject`` dependent upon another ``OsidObject``.

    A ``Subjugateable`` is created in the context of the administering
    ``OsidObject`` that may not be reassigned.

    A ``Subjugateable`` always has a fixed Id of it administering
    ``OsidObject``.

    """
    pass
