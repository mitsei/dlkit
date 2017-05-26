# -*- coding: utf-8 -*-

# This module contains all the Object classes used by the MIT Core Concept
# Catalog (MC3) Handcar based implementation of the OSID  Service.

import json
import requests

from ...abstract_osid.osid import objects as abc_osid_objects
from ...abstract_osid.id.primitives import Id as AbstractId
from ...abstract_osid.type.primitives import Type as AbstractType
from .. import settings
from ..primitives import Id, Type, DisplayText
from .osid_errors import NullArgument, InvalidArgument,\
    NotFound, NoAccess, IllegalState, OperationFailed,\
    Unimplemented, Unsupported, PermissionDenied
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
    _base_url = settings.HANDCAR + '/services/learning'
    _base_path = '/handcar/services/learning'
    _host = settings.HOST

    def __init__(self, osid_object_map, **kwargs):
        self._my_map = osid_object_map
        self._my_genus_type_map = None
        self._my_record_types = None
        self.kwargs = kwargs
        self._host = settings.HOST

    def set_host(self, mc3_host):
        """
        Hack to get copy from server to server
        :param mc3_host:
        :return:
        """
        self._host = mc3_host

    def get_host(self):
        if self._host:
            return self._host
        else:
            return None

# These two may want to be in handcar.osid.markers.browsable or
# handcar.osid.markers.extensible:

    def __iter__(self):
        for attr in dir(self):
            if not attr.startswith('__'):
                yield attr

    # def __getitem__(self, item):
    #     # can we make this work with the Handcar record extensions?
    #     # if the getattr() doesn't find the item, then search
    #     # the record extensions on Handcar...
    #     # return getattr(self, item)
    #     try:
    #         result = getattr(self, item)
    #     except:
    #         result = self.search_record_extensions(item)
    #     finally:
    #         return result
    #
    # def __setitem__(self, key, value):
    #     # also tie this to Handcar record extensions?
    #     if key in self.__dict__:
    #         self[key] = value
    #     else:
    #         self.set_record_extension(key, value)

    def _record_extension(self, key, value):
        """
        To structure a record extension property bean
        """
        record_bean = {
            'value': value,
            'displayName': self._text_bean(key),
            'description': self._text_bean(key),
            'displayLabel': self._text_bean(key),
            'associatedId': str(self.ident)
        }
        return record_bean

    def _text_bean(self, text):
        """
        To structure a text bean for MC3 with language specifications
        """
        bean = {
            'text': text,
            'scriptTypeId': '15924%3ALatin%40ISO',
            'languageTypeId': '639-2%3AEnglish%40ISO',
            'formatTypeId': 'Text+Formats%3Aplain%40okapia.net'
        }
        return bean

    def extension_url(self):
        from ..utilities import construct_url
        self_type = self.object_map['type'].lower()
        if self_type == 'objectivebank':
            extension_url = construct_url('extension_record',
                                          bank_id=self.ident)
        elif self_type == 'objective' or self_type == 'objectivenode':
            extension_url = construct_url('extension_record',
                                          bank_id=self._my_map['objectiveBankId'],
                                          obj_id=self.ident)
        elif self_type == 'activity':
            extension_url = construct_url('extension_record',
                                          bank_id=self._my_map['objectiveBankId'],
                                          act_id=self.ident)
        elif self_type == 'asset':
            extension_url = construct_url('extension_record',
                                          bank_id=self._my_map['objectiveBankId'],
                                          asset_id=self.ident)
        else:
            raise LookupError
        return extension_url

    def extensions(self):
        extension_url = self.extension_url()
        return self._get_request(extension_url)['recordProperties']

    def search_record_extensions(self, item):
        extensions = self.extensions()
        results = []
        for ext in extensions:
            if ext['displayName']['text'] == item:
                results.append(ext['value'])
        return results

    def set_record_extension(self, key, value, proxyname=None):
        # yes, hackish
        import json
        self._proxyname = proxyname
        extension_url = self.extension_url()
        current_extensions = self.extensions()
        current_keys = [e['displayName']['text'] for e in current_extensions]
        if key not in current_keys:
            current_extensions.append(self._record_extension(key, value))
        updated_extensions = {
            'associatedId': str(self.ident),
            'recordProperties': current_extensions
        }
        return self._put_request(extension_url, json.dumps(updated_extensions))
# ----------------------------------

    def _error_check(self, response):
        if response.status_code == 200:
            return
        elif response.status_code == 404:
            raise NotFound(response.text)
        elif response.status_code == 403:
            raise PermissionDenied(response.text)
        else:
            print(response.text)
            raise OperationFailed(str(response.status_code) + ' Error: ' + response.text)

    def _full_url(self, url_path):
        return 'https://{0}{1}'.format(self._host, url_path)

    # This is where the work gets done to process GET requests with handcar.
    # Here you can experiment with different libraries, etc.
    def _get_request(self, url_path):
        response = requests.get(self._full_url(url_path))
        self._error_check(response)
        return response.json()

    def _load_json(self, url_string):
        response = requests.get(url_string)
        try:
            return response.json()
        except Exception:
            raise OperationFailed()

    # This is where the work gets done to process PUT requests with handcar.
    # Here you can experiment with different libraries, etc.
    def _put_request(self, url_path, data):
        if self._proxyname is not None:
            url_path += '?proxyname=' + self._proxyname
        response = requests.put(self._full_url(url_path),
                                data=data,
                                headers={'Content-Type': 'application/json'})
        self._error_check(response)
        return response.json()

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
        return DisplayText(self._my_map['displayName'])

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
        return DisplayText(self._my_map['description'])

    def get_genus_type(self):
        """Gets the genus type of this object.

        return: (osid.type.Type) - the genus type of this object
        compliance: mandatory - This method must be implemented.

        """
        if self._my_genus_type_map is None:
            url_path = '/handcar/services/learning/types/' + self._my_map['genusTypeId']
#            url_str = self._base_url + '/types/' + self._my_map['genusTypeId']
#            self._my_genus_type_map = self._load_json(url_str)
            self._my_genus_type_map = self._get_request(url_path)
        return Type(self._my_genus_type_map)

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

    def get_object_map(self):
        return self._my_map

    object_map = property(get_object_map)


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


class OsidCatalog(abc_osid_objects.OsidCatalog, OsidObject, markers.Sourceable, markers.Federateable):
    """OsidCatalog is the top level interface for all OSID catalog-like
    objects."""
    _namespace = 'osid.OsidCatalog'


class OsidForm(abc_osid_objects.OsidForm, markers.Identifiable, markers.Suppliable):
    """The OsidForm is the vehicle used to create and update objects.

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

    OsidForms are Identifiable. The Id of the OsidForm is used to
    uniquely identify the update or create transaction and not that of
    the object being updated. Currently, it is not necessary to have
    these Ids persisted.

    As with all aspects of the OSIDs, nulls cannot be used. Methods to
    clear values are also defined in the form.

    A new OsidForm should be acquired for each transaction upon an
    OsidObject. Forms should not be reused from one object to another
    even if the supplied data is the same as the forms may encapsulate
    data specific to the object requested. Example of changing a display
    name and a color defined in a color interface extension:
      ObjectForm form = session.getObjectFormForUpdate(objectId);
      form.setDisplayName("new name");
      ColorForm recordForm = form.getFormRecord(colorRecordType);
      recordForm.setColor("green");
      session.updateObject(objectId, form);



    """
    _namespace = 'osid.OsidForm'

    def __init__(self, osid_object_map=None, **kwargs):
        import uuid
        self._validity_map = dict()
        self._identifier = str(uuid.uuid4())
        self.kwargs = kwargs
        if osid_object_map is None:
            self._my_map = dict()
            self._for_update = False
            self._init_map()
        else:
            self._my_map = osid_object_map
            self._for_update = True
        self._init_validity_map()

    def _init_map(self):
        self._my_map['journalComment'] = {
            'languageTypeId': settings.LANGUAGE_TYPE_ID,
            'scriptTypeId': settings.SCRIPT_TYPE_ID,
            'formatTypeId': settings.FORMAT_TYPE_ID,
            'text': ''
        }

    def _init_validity_map(self):
        self._validity_map['journalComment'] = VALID

    # The _is_valid_input method takes three arguments, the user input to
    # be checked and the associated metadata structure (an osid.Metadata
    # object) that will store the  validation requirements.
    def _is_valid_input(self, input, metadata, array):
        syntax = metadata.get_syntax()
        valid = True

        # First check if this is a required data element
        if metadata.is_required and not input:
            return False

        # Recursively run through all the elements of an array
        if array:
            min_elements = metadata.get_minimum_elements()
            max_elements = metadata.get_maximum_elements()
            if min_elements is not None and len(input) < min_elements:
                valid = False
            elif max_elements is not None and len(input) > max_elements:
                valid = False
            else:
                for element in input:
                    valid = (valid and
                             self._is_valid_input(element, metadata, array=False))
        # Run through all the possible syntax types
        elif syntax == 'ID':
            valid = self._is_valid_id(input)
        elif syntax == 'TYPE':
            valid = self._is_valid_type(input)
        elif syntax == 'BOOLEAN':
            valid = self._is_valid_boolean(input)
        elif syntax == 'STRING':
            valid = self._is_valid_string(input, metadata)
        else:
            raise OperationFailed('no validation function available for ' + syntax)
        return valid

    def _is_valid_id(self, input):
        if isinstance(input, AbstractId):
            return True
        else:
            return False

    def _is_valid_type(self, input):
        if isinstance(input, AbstractType):
            return True
        else:
            return False

    def _is_valid_boolean(self, input):
        if isinstance(input, bool):
            return True
        else:
            return False

    def _is_valid_string(self, input_, metadata):
        from ..utilities import is_string
        if not is_string(input_):
            return False
        if len(input_) < metadata.get_minimum_string_length():
            return False
        elif len(input_) > metadata.get_maximum_string_length():
            return False
        if (metadata.get_string_set() and
                input_ not in metadata.get_string_set()):
            return False
        else:
            return True

    # Override get_id as implemented in Identifiable for the purpose of
    # returning an Id unique to this form for submission purposed as
    # recommended in the osid documentation. This implementation
    # substitutes the intialized Python uuid4 identifier, and the
    # form namespace from the calling Osid Form thing.
    def get_id(self):
        return Id(identifier=self._identifier,
                  namespace=self._namespace,
                  authority=self._authority)

    def is_for_update(self):
        """Tests if this form is for an update operation.

        return: (boolean) - true if this form is for an update
                operation, false if for a create operation
        compliance: mandatory - This method must be implemented.

        """
        return self._for_update

    def get_default_locale(self):
        """Gets a default locale for DisplayTexts when a locale is not
        specified.

        return: (osid.locale.Locale) - the default locale
        compliance: mandatory - This method must be implemented.

        """
        raise Unimplemented()

    def get_locales(self):
        """Gets a list of locales for available DisplayText translations
        that can be performed using this form.

        return: (osid.locale.LocaleList) - a list of available locales
                or an empty list if no translation operations are
                available
        compliance: mandatory - This method must be implemented.

        """
        raise Unimplemented()

    def set_locale(self, language_type=None, script_type=None):
        """Specifies a language and script type for DisplayText fields in
        this form.

        Setting a locale to something other than the default locale may
        affect the Metadata in this form.

        If multiple locales are available for managing translations, the
        Metadata indicates the fields are unset as they may be returning
        a defeult value based on the default locale.

        arg:    languageType (osid.type.Type): the language type
        arg:    scriptType (osid.type.Type): the script type
        raise:  NullArgument - languageType or scriptType is null
        raise:  Unsupported - languageType and scriptType not available
                from get_locales()
        compliance: mandatory - This method must be implemented.

        """
        raise Unsupported()

    def get_journal_comment_metadata(self):
        """Gets the metadata for the comment corresponding to this form
        submission.

        The comment is used for describing the nature of the change to
        the corresponding object for the purposes of logging and
        auditing.

        return: (osid.Metadata) - metadata for the comment
        compliance: mandatory - This method must be implemented.

        """
        return Metadata(**settings.METADATA['journalComment'])

    def set_journal_comment(self, comment=None):
        """Sets a comment.

        arg:    comment (string): the new comment
        raise:  InvalidArgument - comment is invalid
        raise:  NoAccess - metadata.is_readonly() is true
        raise:  NullArgument - comment is null
        compliance: mandatory - This method must be implemented.

        """
        if comment is None:
            raise NullArgument()
        metadata = Metadata(**settings.METADATA['comment'])
        if metadata.is_read_only():
            raise NoAccess()
        if self._is_valid_input(comment, metadata, array=False):
            self._my_map['journalComment']['text'] = comment
        else:
            raise InvalidArgument()

    def is_valid(self):
        """Tests if ths form is in a valid state for submission.

        A form is valid if all required data has been supplied compliant
        with any constraints.

        return: (boolean) - false if there is a known error in this
                form, true otherwise
        raise:  OperationFailed - attempt to perform validation failed
        compliance: mandatory - This method must be implemented.

        """
        validity = True
        for element in self._validity_map:
            if self._validity_map[element] is not VALID:
                validity = False
        return validity

    def get_validation_messages(self):
        """Gets text messages corresponding to additional instructions to
        pass form validation.

        return: (osid.locale.DisplayText) - a list of messages
        compliance: mandatory - This method must be implemented.

        """
        pass

    def get_invalid_metadata(self):
        """Gets a list of metadata for the elements in this form which are
        not valid.

        return: (osid.Metadata) - invalid metadata
        compliance: mandatory - This method must be implemented.

        """
        pass

    default_locale = property(get_default_locale)
    locales = property(get_locales)
    journal_comment_metadata = property(get_journal_comment_metadata)
    validation_messages = property(get_validation_messages)
    invalid_metadata = property(get_invalid_metadata)
    journal_comment = property(fset=set_journal_comment)


class OsidIdentifiableForm(abc_osid_objects.OsidIdentifiableForm, OsidForm):
    """The OsidIdentifiableForm is used to create and update identifiable
    objects.

    The form is a container for data to be sent to an update or create
    method of a session.

    """


class OsidExtensibleForm(abc_osid_objects.OsidExtensibleForm, OsidForm, markers.Extensible):
    """The OsidExtensibleForm is used to create and update extensible
    objects.

    The form is a container for data to be sent to an update or create
    method of a session.

    """

    def get_required_record_types(self):
        """Gets the required record types for this form.

        The required records may change as a result of other data in
        this form and should be checked before submission.

        return: (osid.type.TypeList) - a list of required record types
        compliance: mandatory - This method must be implemented.

        """
        pass

    required_record_types = property(get_required_record_types)


class OsidBrowsableForm(abc_osid_objects.OsidBrowsableForm, OsidForm):
    """The OsidBrowsableForm is used to create and update browsable
    objects.

    The form is a container for data to be sent to an update or create
    method of a session.

    """


class OsidTemporalForm(abc_osid_objects.OsidTemporalForm, OsidForm):
    """This form is used to create and update temporals."""

    def get_start_date_metadata(self):
        """Gets the metadata for a start date.

        return: (osid.Metadata) - metadata for the date
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    start_date_metadata = property(get_start_date_metadata)

    def set_start_date(self, date=None):
        """Sets the start date.

        arg:    date (osid.calendaring.DateTime): the new date
        raise:  InvalidArgument - ``date`` is invalid
        raise:  NoAccess - ``Metadata.isReadOnly()`` is ``true``
        raise:  NullArgument - ``date`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def clear_start_date(self):
        """Clears the start date.

        raise:  NoAccess - ``Metadata.isRequired()`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def get_end_date_metadata(self):
        """Gets the metadata for an end date.

        return: (osid.Metadata) - metadata for the date
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def set_end_date(self, date=None):
        """Sets the end date.

        arg:    date (osid.calendaring.DateTime): the new date
        raise:  InvalidArgument - ``date`` is invalid
        raise:  NoAccess - ``Metadata.isReadOnly()`` is ``true``
        raise:  NullArgument - ``date`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def clear_end_date(self):
        """Clears the end date.

        raise:  NoAccess - ``Metadata.isRequired()`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class OsidAggregateableForm(OsidForm):
    """This form is used to create and update assemblages."""


class OsidSourceableForm(abc_osid_objects.OsidSourceableForm, OsidForm):
    """This form is used to create and update sourceables."""

    def get_provider_metadata(self):
        """Gets the metadata for a provider.

        return: (osid.Metadata) - metadata for the provider
        compliance: mandatory - This method must be implemented.

        """
        pass

    def set_provider(self, provider_id=None):
        """Sets a provider.

        arg:    providerId (osid.id.Id): the new provider
        raise:  INVALID_ARGUMENT - providerId is invalid
        raise:  NO_ACCESS - metadata.is_read_only() is true
        raise:  NULL_ARGUMENT - providerId is null
        compliance: mandatory - This method must be implemented.

        """
        pass

    def clear_provider(self):
        """Removes the provider.

        raise:  NO_ACCESS - metadata.is_required() is true or
                metadata.is_read_only() is true
        compliance: mandatory - This method must be implemented.

        """
        pass

    def get_branding_metadata(self):
        """Gets the metadata for the asset branding.

        return: (osid.Metadata) - metadata for the asset branding.
        compliance: mandatory - This method must be implemented.

        """
        pass

    def set_branding(self, asset_ids=None):
        """Sets the branding.

        arg:    assetIds (osid.id.Id): the new assets
        raise:  INVALID_ARGUMENT - assetIds is invalid
        raise:  NO_ACCESS - metadata.is_read_only() is true
        raise:  NULL_ARGUMENT - assetIds is null
        compliance: mandatory - This method must be implemented.

        """
        pass

    def clear_branding(self):
        """Removes the branding.

        raise:  NO_ACCESS - metadata.is_required() is true or
                metadata.is_read_only() is true
        compliance: mandatory - This method must be implemented.

        """
        pass

    def get_license_metadata(self):
        """Gets the metadata for the license.

        return: (osid.Metadata) - metadata for the license
        compliance: mandatory - This method must be implemented.

        """
        pass

    def set_license(self, license=None):
        """Sets the license.

        arg:    license (string): the new license
        raise:  INVALID_ARGUMENT - license is invalid
        raise:  NO_ACCESS - metadata.is_read_only() is true
        raise:  NULL_ARGUMENT - license is null
        compliance: mandatory - This method must be implemented.

        """
        pass

    def clear_license(self):
        """Removes the license.

        raise:  NO_ACCESS - metadata.is_required() is true or
                metadata.is_read_only() is true
        compliance: mandatory - This method must be implemented.

        """
        pass


class OsidFederateableForm(abc_osid_objects.OsidFederateableForm, OsidForm):
    """This form is used to create and update federateables."""


class OsidObjectForm(abc_osid_objects.OsidObjectForm, OsidIdentifiableForm, OsidExtensibleForm, OsidBrowsableForm):
    """The OsidObjectForm is used to create and update OsidObjects.

    The form is not an OsidObject but merely a container for data to be
    sent to an update or create method of a session. A provider may or
    may not combine the OsidObject and OsidObjectForm interfaces into a
    single object.

    Generally, a set method parallels each get method of an OsidObject.
    Additionally, Metadata may be examined for each data element to
    assist in understanding particular rules concerning acceptable data.

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

    A new OsidForm should be acquired for each transaction upon an
    OsidObject. Forms should not be reused from one object to another
    even if the supplied data is the same as the forms may encapsulate
    data specific to the object requested. Example of changing a display
    name and a color defined in a color interface extension:
      ObjectForm form = session.getObjectFormForUpdate(objectId);
      form.setDisplayName("new name");
      ColorForm recordForm = form.getFormRecord(colorRecordType);
      recordForm.setColor("green");
      session.updateObject(objectId, form);

    """
    _namespace = "osid.OsidObject"

    def _init_map(self):
        OsidForm._init_map(self)
        self._my_map['displayName'] = {
            'languageTypeId': settings.LANGUAGE_TYPE_ID,
            'scriptTypeId': settings.SCRIPT_TYPE_ID,
            'formatTypeId': settings.FORMAT_TYPE_ID,
            'text': ''
        }
        self._my_map['description'] = {
            'languageTypeId': settings.LANGUAGE_TYPE_ID,
            'scriptTypeId': settings.SCRIPT_TYPE_ID,
            'formatTypeId': settings.FORMAT_TYPE_ID,
            'text': ''
        }
        self._my_map['genusTypeId'] = settings.DEFAULT_GENUS_TYPES[self._namespace]

    def _init_validity_map(self):
        OsidForm._init_validity_map(self)
        self._validity_map['display_name'] = VALID
        self._validity_map['description'] = VALID
        self._validity_map['genus_type'] = VALID

    def get_display_name_metadata(self):
        """Gets the metadata for a display name.

        return: (osid.Metadata) - metadata for the display name
        compliance: mandatory - This method must be implemented.

        """
        return Metadata(**settings.METADATA['display_name'])

    def set_display_name(self, display_name=None):
        """Sets a display name.

        A display name is required and if not set, will be set by the
        provider.

        arg:    displayName (string): the new display name
        raise:  InvalidArgument - displayName is invalid
        raise:  NoAccess - metadata.is_readonly() is true
        raise:  NullArgument - displayName is null
        compliance: mandatory - This method must be implemented.

        """
        if display_name is None:
            raise NullArgument()
        metadata = Metadata(**settings.METADATA['display_name'])
        if metadata.is_read_only():
            raise NoAccess()
        if self._is_valid_input(display_name, metadata, array=False):
            self._my_map['displayName']['text'] = display_name
        else:
            raise InvalidArgument

    def clear_display_name(self):
        """Clears the display name.

        raise:  NoAccess - metadata.is_required() or
                metadata.is_read_only() is true
        compliance: mandatory - This method must be implemented.

        """
        metadata = Metadata(**settings.METADATA['display_name'])
        if metadata.is_read_only() or metadata.is_required():
            raise NoAccess()
        self._my_map['displayName'] = ''

    def get_description_metadata(self):
        """Gets the metadata for a description.

        return: (osid.Metadata) - metadata for the description
        compliance: mandatory - This method must be implemented.

        """
        return Metadata(**settings.METADATA['description'])

    def set_description(self, description=None):
        """Sets a description.

        arg:    description (string): the new description
        raise:  InvalidArgument - description is invalid
        raise:  NoAccess - metadata.is_readonly() is true
        raise:  NullArgument - description is null
        compliance: mandatory - This method must be implemented.

        """
        if description is None:
            raise NullArgument()
        metadata = Metadata(**settings.METADATA['description'])
        if metadata.is_read_only():
            raise NoAccess()
        if self._is_valid_input(description, metadata, array=False):
            self._my_map['description']['text'] = description
        else:
            raise InvalidArgument

    def clear_description(self):
        """Clears the description.

        raise:  NoAccess - metadata.is_required() or
                metadata.is_read_only() is true
        compliance: mandatory - This method must be implemented.

        """
        metadata = Metadata(**settings.METADATA['description'])
        if metadata.is_read_only() or metadata.is_required():
            raise NoAccess()
        self._my_map['description'] = ''

    def get_genus_type_metadata(self):
        """Gets the metadata for a genus type.

        return: (osid.Metadata) - metadata for the genus
        compliance: mandatory - This method must be implemented.

        """
        return Metadata(**settings.METADATA['genus_type'])

    def set_genus_type(self, genus_type=None):
        """Sets a genus.

        A genus cannot be cleared because all objects have at minimum a
        root genus.

        arg:    genusType (osid.type.Type): the new genus
        raise:  InvalidArgument - genusType is invalid
        raise:  NoAccess - metadata.is_readonly() is true
        raise:  NullArgument - genusType is null
        compliance: mandatory - This method must be implemented.

        """
        if genus_type is None:
            raise NullArgument()
        metadata = Metadata(**settings.METADATA['genus_type'])
        metadata_id = Metadata(**settings.METADATA['genus_type_id'])
        if metadata.is_read_only():
            raise NoAccess()
        if self._is_valid_input(genus_type, metadata, array=False):
            self._my_map['genusTypeId'] = str(genus_type)
            # REALLY?  This assumes that all genus_type arguments
            # will be Types that have come from Hancar.  Perhaps?
        elif self._is_valid_input(genus_type, metadata_id, array=False):
            self._my_map['genusTypeId'] = str(genus_type)
        else:
            raise InvalidArgument

    def clear_genus_type(self):
        """Clears the genus type.

        raise:  NoAccess - metadata.is_required() or
                metadata.is_read_only() is true
        compliance: mandatory - This method must be implemented.

        """
        metadata = Metadata(**settings.METADATA['genus_type'])
        if metadata.is_read_only() or metadata.is_required():
            raise NoAccess()
        # This may never get called, as
        # is_required will likely always
        # be True for genus types.
        self._my_map['genus_type'] = ''

    display_name_metadata = property(get_display_name_metadata)
    description_metadata = property(get_description_metadata)
    genus_type_metadata = property(get_genus_type_metadata)
    display_name = property(fset=set_display_name, fdel=clear_display_name)
    description = property(fset=set_description, fdel=clear_description)
    genus_type = property(fset=set_genus_type, fdel=clear_genus_type)


class OsidRelationshipForm(abc_osid_objects.OsidRelationshipForm, OsidObjectForm, OsidTemporalForm):
    """This form is used to create and update relationshps."""


class OsidCatalogForm(abc_osid_objects.OsidCatalogForm, OsidObjectForm, OsidSourceableForm, OsidFederateableForm):
    """This form is used to create and update catalogs."""


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
            next_object = next(self._iter_object)
        except StopIteration:
            raise
        except Exception:  # Need to specify exceptions here!
            raise OperationFailed()
        if self._count is not None:
            self._count -= 1
        return next_object

    __next__ = next

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
                next(self)
            except StopIteration:
                break
            n -= 1
