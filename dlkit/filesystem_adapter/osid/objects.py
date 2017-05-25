"""AWS Adapter osid objects implementations."""
# pylint: disable=too-many-ancestors
#    number of ancestors defined in spec


from ...abstract_osid.osid import objects as abc_osid_objects
from ..osid import markers as osid_markers
from .osid_errors import OperationFailed, IllegalState


class OsidObject(abc_osid_objects.OsidObject,
                 osid_markers.Identifiable,
                 osid_markers.Extensible,
                 osid_markers.Browsable):
    """``OsidObject`` is the top level interface for all OSID Objects.

    An OSID Object is an object identified by an OSID ``Id`` and may
    implements optional interfaces. OSID Objects also contain a display
    name and a description. These fields are required but may be used
    for a variety of purposes ranging from a primary name and
    description of the object to a more user friendly display of various
    attributes.

    Creation of OSID Objects and the modification of their data is
    managed through the associated ``OsidSession`` which removes the
    dependency of updating data elements upon object retrieval.The
    ``OsidManager`` should be used to test if updates are available and
    determine what ``PropertyTypes`` are supported. The ``OsidManager``
    is also used to create the appropriate ``OsidSession`` for object
    creation, updates and deletes.

    All ``OsidObjects`` are identified by an immutable ``Id``. An ``Id``
    is assigned to an object upon creation of the object and cannot be
    changed once assigned.

    An ``OsidObject`` may support one or more supplementary records
    which are expressed in the form of interfaces. Each record interface
    is identified by a Type. A record interface may extend another
    record interface where support of the parent record interface is
    implied. In this case of interface inheritance, support of the
    parent record type may be implied through ``has_record_type()`` and
    not explicit in ``getRecordTypes()``.

    For example, if recordB extends recordA, typeB is a child of typeA.
    If a record implements typeB, than it also implements typeA. An
    application that only knows about typeA retrieves recordA. An
    application that knows about typeB, retrieves recordB which is the
    union of methods specified in typeA and typeB. If an application
    requests typeA, it may not attempt to access methods defined in
    typeB as they may not exist until explicitly requested. The
    mechanics of this polymorphism is defined by the language binder.
    One mechanism might be the use of casting.

    In addition to the record ``Types,`` OSID Objects also have a genus
    ``Type``. A genus ``Type`` indicates a classification or kind of the
    object where an "is a" relationship exists. The purpose of of the
    genus ``Type`` is to avoid the creation of unnecessary record types
    that may needlessly complicate an interface hierarchy or introduce
    interoperability issues. For example, an OSID object may have a
    record ``Type`` of ``Publication`` that defines methods pertinent to
    publications, such as an ISBN number. A provider may wish to
    distinguish between books and journals without having the need of
    new record interfaces. In this case, the genus ``Type`` may be one
    of ``Book`` or ``Journal``. While this distinction can aid a search,
    these genres should be treated in such a way that do not introduce
    interoperability problems.

    Like record Types, the genus Types may also exist in an implicit
    type hierarchy. An OSID object always has at least one genus. Genus
    types should not be confused with subject tagging, which is managed
    externally to the object. Unlike record ``Types,`` an object's genus
    may be modified. However, once an object's record is created with a
    record ``Type,`` it cannot be changed.

    Methods that return values are not permitted to return nulls. If a
    value is not set, it is indicated in the ``Metadata`` of the update
    form.

    """

    def __init__(self, payload, config_map):
        super(OsidObject, self).__init__()
        self._payload = payload
        self._config_map = config_map

    def get_display_name(self):
        """Gets the preferred display name associated with this instance of
        this OSID object appropriate for display to the user.

        return: (osid.locale.DisplayText) - the display name
        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: A display name is a string used for
        identifying an object in human terms. A provider may wish to
        initialize the display name based on one or more object
        attributes. In some cases, the display name may not map to a
        specific or significant object attribute but simply be used as a
        preferred display name that can be modified. A provider may also
        wish to translate the display name into a specific locale using
        the Locale service. Some OSIDs define methods for more detailed
        naming.

        """
        return self._payload.get_display_name()

    display_name = property(fget=get_display_name)

    def get_description(self):
        """Gets the description associated with this instance of this OSID object.

        return: (osid.locale.DisplayText) - the description
        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: A description is a string used for
        describing an object in human terms and may not have
        significance in the underlying system. A provider may wish to
        initialize the description based on one or more object
        attributes and/or treat it as an auxiliary piece of data that
        can be modified. A provider may also wish to translate the
        description into a specific locale using the Locale service.

        """
        return self._payload.get_description()

    description = property(fget=get_description)

    def get_genus_type(self):
        """Gets the genus type of this object.

        return: (osid.type.Type) - the genus type of this object
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._payload.get_genus_type()

    genus_type = property(fget=get_genus_type)

    def is_of_genus_type(self, genus_type=None):
        """Tests if this object is of the given genus ``Type``.

        The given genus type may be supported by the object through the
        type hierarchy.

        arg:    genus_type (osid.type.Type): a genus type
        return: (boolean) - ``true`` if this object is of the given
                genus ``Type,``  ``false`` otherwise
        raise:  NullArgument - ``genus_type`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._payload.is_of_genus_type(genus_type)


class OsidCatalog(abc_osid_objects.OsidCatalog,
                  OsidObject,
                  osid_markers.Sourceable,
                  osid_markers.Federateable):
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
    def __init__(self):
        super(OsidCatalog, self).__init__()


class OsidForm(abc_osid_objects.OsidForm,
               osid_markers.Identifiable,
               osid_markers.Suppliable):
    """The ``OsidForm`` is the vehicle used to create and update objects.

    The form is a container for data to be sent to an update or create
    method of a session. Applications should persist their own data
    until a form is successfully submitted in an update or create
    transaction.

    The form may provide some feedback as to the validity of certain
    data updates before the update transaction is issued to the
    correspodning session but a successful modification of the form is
    not a guarantee of success for the update transaction. A consumer
    may elect to perform all updates within a single update transaction
    or break up a large update intio smaller units. The tradeoff is the
    granularity of error feedback vs. the performance gain of a single
    transaction.

    ``OsidForms`` are ``Identifiable``. The ``Id`` of the ``OsidForm``
    is used to uniquely identify the update or create transaction and
    not that of the object being updated. Currently, it is not necessary
    to have these ``Ids`` persisted.

    As with all aspects of the OSIDs, nulls cannot be used. Methods to
    clear values are also defined in the form.

    A new ``OsidForm`` should be acquired for each transaction upon an
    ``OsidObject``. Forms should not be reused from one object to
    another even if the supplied data is the same as the forms may
    encapsulate data specific to the object requested. Example of
    changing a display name and a color defined in a color interface
    extension:
      ObjectForm form = session.getObjectFormForUpdate(objectId);
      form.setDisplayName("new name");
      ColorForm recordForm = form.getFormRecord(colorRecordType);
      recordForm.setColor("green");
      session.updateObject(objectId, form);

    """

    def __init__(self, payload, config_map, repository_id):
        super(OsidForm, self).__init__()
        self._payload = payload
        self._config_map = config_map
        # This should probably go in the AssetContentForm initter:
        self._repository_id = repository_id

    def is_for_update(self):
        """Tests if this form is for an update operation.

        return: (boolean) - ``true`` if this form is for an update
                operation, ``false`` if for a create operation
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._payload.is_for_update()

    def get_default_locale(self):
        """Gets a default locale for ``DisplayTexts`` when a locale is not specified.

        return: (osid.locale.Locale) - the default locale
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._payload.get_default_locale()

    default_locale = property(fget=get_default_locale)

    def get_locales(self):
        """Gets a list of locales for available ``DisplayText`` translations
        that can be performed using this form.

        return: (osid.locale.LocaleList) - a list of available locales
                or an empty list if no translation operations are
                available
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._payload.get_locales()

    locales = property(fget=get_locales)

    def set_locale(self, language_type=None, script_type=None):
        """Specifies a language and script type for ``DisplayText``
        fields in this form.

        Setting a locale to something other than the default locale may
        affect the ``Metadata`` in this form.

        If multiple locales are available for managing translations, the
        ``Metadata`` indicates the fields are unset as they may be
        returning a defeult value based on the default locale.

        arg:    language_type (osid.type.Type): the language type
        arg:    script_type (osid.type.Type): the script type
        raise:  NullArgument - ``language_type`` or ``script_type`` is
                null
        raise:  Unsupported - ``language_type`` and ``script_type`` not
                available from ``get_locales()``
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._payload.set_locale(language_type, script_type)

    def get_journal_comment_metadata(self):
        """Gets the metadata for the comment corresponding to this form submission.

        The comment is used for describing the nature of the change to
        the corresponding object for the purposes of logging and
        auditing.

        return: (osid.Metadata) - metadata for the comment
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._payload.get_journal_comment_metadata()

    journal_comment_metadata = property(fget=get_journal_comment_metadata)

    def set_journal_comment(self, comment=None):
        """Sets a comment.

        arg:    comment (string): the new comment
        raise:  InvalidArgument - ``comment`` is invalid
        raise:  NoAccess - ``Metadata.isReadonly()`` is ``true``
        raise:  NullArgument - ``comment`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._payload.set_comment(comment)

    journal_comment = property(fset=set_journal_comment)

    def is_valid(self):
        """Tests if ths form is in a valid state for submission.

        A form is valid if all required data has been supplied compliant
        with any constraints.

        return: (boolean) - ``false`` if there is a known error in this
                form, ``true`` otherwise
        raise:  OperationFailed - attempt to perform validation failed
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._payload.is_valid()

    def get_validation_messages(self):
        """Gets text messages corresponding to additional instructions to
        pass form validation.

        return: (osid.locale.DisplayText) - a list of messages
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._payload.get_validation_messages()

    validation_messages = property(fget=get_validation_messages)

    def get_invalid_metadata(self):
        """Gets a list of metadata for the elements in this form which are not valid.

        return: (osid.Metadata) - invalid metadata
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._payload.get_invalid_metadata()

    invalid_metadata = property(fget=get_invalid_metadata)


class OsidIdentifiableForm(abc_osid_objects.OsidIdentifiableForm, OsidForm):
    """The ``OsidIdentifiableForm`` is used to create and update identifiable objects.

    The form is a container for data to be sent to an update or create
    method of a session.

    """


class OsidExtensibleForm(abc_osid_objects.OsidExtensibleForm,
                         OsidForm,
                         osid_markers.Extensible):
    """The ``OsidExtensibleForm`` is used to create and update extensible objects.

    The form is a container for data to be sent to an update or create
    method of a session.

    """

    def get_required_record_types(self):
        """Gets the required record types for this form.

        The required records may change as a result of other data in
        this form and should be checked before submission.

        return: (osid.type.TypeList) - a list of required record types
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    required_record_types = property(fget=get_required_record_types)


class OsidBrowsableForm(abc_osid_objects.OsidBrowsableForm, OsidForm):
    """The ``OsidBrowsableForm`` is used to create and update browsable objects.

    The form is a container for data to be sent to an update or create
    method of a session.

    """


class OsidSubjugateableForm(abc_osid_objects.OsidSubjugateableForm, OsidForm):
    """This form is used to create and update dependent objects."""


class OsidAggregateableForm(abc_osid_objects.OsidAggregateableForm, OsidForm):
    """This form is used to create and update assemblages."""


class OsidSourceableForm(abc_osid_objects.OsidSourceableForm, OsidForm):
    """This form is used to create and update sourceables."""

    def get_provider_metadata(self):
        """Gets the metadata for a provider.

        return: (osid.Metadata) - metadata for the provider
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    provider_metadata = property(fget=get_provider_metadata)

    def set_provider(self, provider_id=None):
        """Sets a provider.

        arg:    provider_id (osid.id.Id): the new provider
        raise:  InvalidArgument - ``provider_id`` is invalid
        raise:  NoAccess - ``Metadata.isReadOnly()`` is ``true``
        raise:  NullArgument - ``provider_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def clear_provider(self):
        """Removes the provider.

        raise:  NoAccess - ``Metadata.isRequired()`` is ``true`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    provider = property(fset=set_provider, fdel=clear_provider)

    def get_branding_metadata(self):
        """Gets the metadata for the asset branding.

        return: (osid.Metadata) - metadata for the asset branding.
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    branding_metadata = property(fget=get_branding_metadata)

    def set_branding(self, asset_ids=None):
        """Sets the branding.

        arg:    asset_ids (osid.id.Id[]): the new assets
        raise:  InvalidArgument - ``asset_ids`` is invalid
        raise:  NoAccess - ``Metadata.isReadOnly()`` is ``true``
        raise:  NullArgument - ``asset_ids`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def clear_branding(self):
        """Removes the branding.

        raise:  NoAccess - ``Metadata.isRequired()`` is ``true`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    branding = property(fset=set_branding, fdel=clear_branding)

    def get_license_metadata(self):
        """Gets the metadata for the license.

        return: (osid.Metadata) - metadata for the license
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    license_metadata = property(fget=get_license_metadata)

    def set_license(self, license_=None):
        """Sets the license.

        arg:    license (string): the new license
        raise:  InvalidArgument - ``license`` is invalid
        raise:  NoAccess - ``Metadata.isReadOnly()`` is ``true``
        raise:  NullArgument - ``license`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def clear_license(self):
        """Removes the license.

        raise:  NoAccess - ``Metadata.isRequired()`` is ``true`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    license_ = property(fset=set_license, fdel=clear_license)


class OsidFederateableForm(abc_osid_objects.OsidFederateableForm, OsidForm):
    """This form is used to create and update federateables."""


class OsidObjectForm(abc_osid_objects.OsidObjectForm,
                     OsidIdentifiableForm,
                     OsidExtensibleForm,
                     OsidBrowsableForm):
    """The ``OsidObjectForm`` is used to create and update ``OsidObjects``.

    The form is not an ``OsidObject`` but merely a container for data to
    be sent to an update or create method of a session. A provider may
    or may not combine the ``OsidObject`` and ``OsidObjectForm``
    interfaces into a single object.

    Generally, a set method parallels each get method of an
    ``OsidObject``. Additionally, ``Metadata`` may be examined for each
    data element to assist in understanding particular rules concerning
    acceptable data.

    The form may provide some feedback as to the validity of certain
    data updates before the update transaction is issued to the
    correspodning session but a successful modification of the form is
    not a guarantee of success for the update transaction. A consumer
    may elect to perform all updates within a single update transaction
    or break up a large update intio smaller units. The tradeoff is the
    granularity of error feedback vs. the performance gain of a single
    transaction.

    As with all aspects of the OSIDs, nulls cannot be used. Methods to
    clear values are also defined in the form.

    A new ``OsidForm`` should be acquired for each transaction upon an
    ``OsidObject``. Forms should not be reused from one object to
    another even if the supplied data is the same as the forms may
    encapsulate data specific to the object requested. Example of
    changing a display name and a color defined in a color interface
    extension:
      ObjectForm form = session.getObjectFormForUpdate(objectId);
      form.setDisplayName("new name");
      ColorForm recordForm = form.getFormRecord(colorRecordType);
      recordForm.setColor("green");
      session.updateObject(objectId, form);

    """

    def get_display_name_metadata(self):
        """Gets the metadata for a display name.

        return: (osid.Metadata) - metadata for the display name
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._payload.get_display_name_metadata()

    display_name_metadata = property(fget=get_display_name_metadata)

    def set_display_name(self, display_name=None):
        """Sets a display name.

        A display name is required and if not set, will be set by the
        provider.

        arg:    display_name (string): the new display name
        raise:  InvalidArgument - ``display_name`` is invalid
        raise:  NoAccess - ``Metadata.isReadonly()`` is ``true``
        raise:  NullArgument - ``display_name`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        self._payload.set_display_name(display_name)

    def clear_display_name(self):
        """Clears the display name.

        raise:  NoAccess - ``Metadata.isRequired()`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        self._payload.clear_display_name()

    display_name = property(fset=set_display_name, fdel=clear_display_name)

    def get_description_metadata(self):
        """Gets the metadata for a description.

        return: (osid.Metadata) - metadata for the description
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._payload.get_description_metadata()

    description_metadata = property(fget=get_description_metadata)

    def set_description(self, description=None):
        """Sets a description.

        arg:    description (string): the new description
        raise:  InvalidArgument - ``description`` is invalid
        raise:  NoAccess - ``Metadata.isReadonly()`` is ``true``
        raise:  NullArgument - ``description`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._payload.set_description(description)

    def clear_description(self):
        """Clears the description.

        raise:  NoAccess - ``Metadata.isRequired()`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        self._payload.clear_description()

    description = property(fset=set_description, fdel=clear_description)

    def get_genus_type_metadata(self):
        """Gets the metadata for a genus type.

        return: (osid.Metadata) - metadata for the genus
        *compliance: mandatory -- This method must be implemented.*

        """
        self._payload.get_genus_type_metadata()

    genus_type_metadata = property(fget=get_genus_type_metadata)

    def set_genus_type(self, genus_type=None):
        """Sets a genus.

        A genus cannot be cleared because all objects have at minimum a
        root genus.

        arg:    genus_type (osid.type.Type): the new genus
        raise:  InvalidArgument - ``genus_type`` is invalid
        raise:  NoAccess - ``Metadata.isReadonly()`` is ``true``
        raise:  NullArgument - ``genus_type`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        self._payload.set_genus_type(genus_type)

    def clear_genus_type(self):
        """Clears the genus type.

        raise:  NoAccess - ``Metadata.isRequired()`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        self._payload.clear_genus_type()

    genus_type = property(fset=set_genus_type, fdel=clear_genus_type)


class OsidCatalogForm(abc_osid_objects.OsidCatalogForm,
                      OsidObjectForm,
                      OsidSourceableForm,
                      OsidFederateableForm):
    """This form is used to create and update catalogs."""


class OsidList(abc_osid_objects.OsidList):
    """``OsidList`` is the top-level interface for all OSID lists.

    An OSID list provides sequential access, one at a time or many at a
    time, access to a set of elements. These elements are not required
    to be OsidObjects but generally are. The element retrieval methods
    are defined in the sub-interface of ``OsidList`` where the
    appropriate return type is defined.

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

    def __init__(self, payload_list, config_map):
        self._payload_list = payload_list
        self._config_map = config_map
        self._count = payload_list.available()

    def __iter__(self):
        return self

    def _get_next_n(self, number=None):
        """Gets the next set of "n" elements in this list.

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
        if number > self.available():
            # !!! This is not quite as specified (see method docs) !!!
            raise IllegalState('not enough elements available in this list')
        else:
            next_list = []
            counter = 0
            while counter < number:
                try:
                    next_list.append(self.next())
                except Exception:  # Need to specify exceptions here!
                    raise OperationFailed()
                counter += 1
            return next_list

    def _get_next_object(self, object_class):
        """stub"""
        try:
            next_object = OsidList.next(self)
        except StopIteration:
            raise
        except Exception:  # Need to specify exceptions here!
            raise OperationFailed()
        if isinstance(next_object, dict):
            next_object = object_class(next_object)
        return next_object

    def next(self):
        """This will be overridden by inheriting object"""
        pass

    __next__ = next

    def has_next(self):
        """Tests if there are more elements in this list.

        return: (boolean) - ``true`` if more elements are available in
                this list, ``false`` if the end of the list has been
                reached
        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: Any errors that may result from accesing
        the underlying set of elements are to be deferred until the
        consumer attempts retrieval in which case the provider must
        return ``true`` for this method.

        """
        return self._payload_list.has_next()

    def available(self):
        """Gets the number of elements available for retrieval.

        The number returned by this method may be less than or equal to
        the total number of elements in this list. To determine if the
        end of the list has been reached, the method ``has_next()``
        should be used. This method conveys what is known about the
        number of remaining elements at a point in time and can be used
        to determine a minimum size of the remaining elements, if known.
        A valid return is zero even if ``has_next()`` is true.

        This method does not imply asynchronous usage. All OSID methods
        may block.

        return: (cardinal) - the number of elements available for
                retrieval
        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: Any errors that may result from accesing
        the underlying set of elements are to be deferred until the
        consumer attempts retrieval in which case the provider must
        return a positive integer for this method so the consumer can
        continue execution to receive the error. In all other
        circumstances, the provider must not return a number greater
        than the number of elements known since this number will be fed
        as a parameter to the bulk retrieval method.

        """
        return self._payload_list.available()

    def skip(self, n=None):
        """Skip the specified number of elements in the list.

        If the number skipped is greater than the number of elements in
        the list, hasNext() becomes false and available() returns zero
        as there are no more elements to retrieve.

        arg:    n (cardinal): the number of elements to skip
        *compliance: mandatory -- This method must be implemented.*

        """
        pass
