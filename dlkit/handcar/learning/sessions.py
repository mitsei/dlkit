# -*- coding: utf-8 -*-

# This module contains all the Session classes used by the MIT Core Concept
# Catalog (MC3) Handcar based implementation of the OSID Learning Service.
# This includes the learning package sessions for Objective, Activities
# and ObjectiveBanks.

import json
import re
from ...abstract_osid.learning import sessions as abc_learning_sessions
from ...abstract_osid.learning import objects as abc_learning_objects
from ...abstract_osid.id.primitives import Id as abc_id
from ..osid.osid_errors import AlreadyExists, NullArgument, InvalidArgument, NotFound, IllegalState, OperationFailed, PermissionDenied, Unsupported, Unimplemented
from ..osid import sessions as osid_sessions
from .. import settings, profile
from . import objects
from . import queries
from ..id import objects as id_objects
from ..primitives import Id, Type, DisplayText
from .managers import LearningManager, LearningProxyManager
from ..type import objects as typeObjects

from ..utilities import construct_url, BankHierarchyUrls

COMPARATIVE = 0
PLENARY = 1
ISOLATED = 0
FEDERATED = 1
CREATED = True
UPDATED = True
SERVICE_STRING = 'learning'
CATALOGS_STRING = 'objectivebanks'


class ObjectiveLookupSession(abc_learning_sessions.ObjectiveLookupSession, osid_sessions.OsidSession):
    """This session provides methods for retrieving Objectives."""

    def __init__(self, objective_bank_id=None, proxy=None, runtime=None, **kwargs):
        self._service_string = SERVICE_STRING
        self._catalogs_string = CATALOGS_STRING
        osid_sessions.OsidSession.__init__(self)
        osid_sessions.OsidSession._init_catalog(
            self,
            proxy,
            runtime
        )
        self._objective_view = COMPARATIVE
        self._objective_bank_view = FEDERATED
        if objective_bank_id is None:
            self._objective_bank_id = Id(**profile.ROOT_BANK_ID)
        else:
            self._objective_bank_id = objective_bank_id
        self._catalog_idstr = str(self._objective_bank_id)
        self._kwargs = kwargs

    def _get_viewable_bank_idstrs(self):
        if self._objective_bank_view == FEDERATED:
            if self._objective_bank_id == Id(**profile.ROOT_BANK_ID):
                url_path = construct_url('objective_banks')
                banks = self._get_request(url_path)
                bank_idstrs = []
                for bank in banks:
                    bank_idstrs.append(bank['id'])
                return bank_idstrs
            else:
                # Eventually this may want to return from a node list of child banks:
                return [self._catalog_idstr]
        else:
            if self._objective_bank_id == Id(**profile.ROOT_BANK_ID):
                raise NotFound()
            else:
                return [self._catalog_idstr]

    def get_objective_bank_id(self):
        """Gets the ObjectiveBank  Id associated with this session.

        return: (osid.id.Id) - the ObjectiveBank Id associated with this
                session
        compliance: mandatory - This method must be implemented.

        """
        return self._objective_bank_id

    def get_objective_bank(self):
        """Gets the ObjectiveBank associated with this session.

        return: (osid.learning.ObjectiveBank) - the ObjectiveBank
                associated with this session
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method must be implemented.

        """
        # This should probably be accomplished via a handcar call instead of OSID
        url_path = construct_url('objective_banks',
                                 bank_id=self._catalog_idstr)
        return objects.ObjectiveBank(self._get_request(url_path))

    def can_lookup_objectives(self):
        """Tests if this user can perform Objective lookups.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a PermissionDenied. This is intended as
        a hint to an application that may opt not to offer lookup
        operations to unauthorized users.
        return: (boolean) - false if lookup methods are not authorized,
                true otherwise
        compliance: mandatory - This method must be implemented.

        """
        url_path = construct_url('authorization',
                                 bank_id=self._catalog_idstr)
        return self._get_request(url_path)['objectiveHints']['canLookup']

    def use_comparative_objective_view(self):
        """The returns from the lookup methods may omit or translate
        elements based on this session, such as authorization, and not
        result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.
        compliance: mandatory - This method is must be implemented.

        """
        self._objective_view = COMPARATIVE

    def use_plenary_objective_view(self):
        """A complete view of the Objective returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.
        compliance: mandatory - This method is must be implemented.

        """
        self._objective_view = PLENARY

    def use_federated_objective_bank_view(self):
        """Federates the view for methods in this session.
        A federated view will include objectives in objective banks
        which are children of this objective bank in the objective bank
        hierarchy.
        compliance: mandatory - This method is must be implemented.

        """
        self._objective_bank_view = FEDERATED

    def use_isolated_objective_bank_view(self):
        """Isolates the view for methods in this session.
        An isolated view restricts lookups to this objective bank only.
        compliance: mandatory - This method is must be implemented.

        """
        self._objective_bank_view = ISOLATED

    def get_objective(self, objective_id=None):
        """Gets the Objective specified by its Id.
        In plenary mode, the exact Id is found or a NotFound results.
        Otherwise, the returned Objective may have a different Id than
        requested, such as the case where a duplicate Id was assigned to
        an Objective and retained for compatibility.
        arg:    objectiveId (osid.id.Id): Id of the Objective
        return: (osid.learning.Objective) - the objective
        raise:  NotFound - objectiveId not found
        raise:  NullArgument - objectiveId is null
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method is must be implemented.

        """
        if objective_id is None:
            raise NullArgument()
        url_path = construct_url('objectives', obj_id=objective_id)
        return objects.Objective(self._get_request(url_path))

    def get_objectives_by_ids(self, objective_ids=None):
        """Gets an ObjectiveList corresponding to the given IdList.
        In plenary mode, the returned list contains all of the
        objectives specified in the Id list, in the order of the list,
        including duplicates, or an error results if an Id in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible Objectives may be omitted from the list and may
        present the elements in any order including returning a unique
        set.
        arg:    objectiveIds (osid.id.IdList): the list of Ids to
                retrieve
        return: (osid.learning.ObjectiveList) - the returned Objective
                list
        raise:  NotFound - an Id was not found
        raise:  NullArgument - objectiveIds is null
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method must be implemented.

        """
        if objective_ids is None:
            raise NullArgument()

        url_path = construct_url('objectives_by_ids',
                                 obj_ids=objective_ids)
        objectives = self._get_request(url_path)

        # for i in objective_ids:
        #     objective = None
        #     url_path = construct_url('objectives',
        #                              obj_id=i)
        #     try:
        #         objective = self._get_request(url_path)
        #     except (NotFound, OperationFailed):
        #         if self._objective_view == PLENARY:
        #             raise
        #         else:
        #             pass
        #     if objective:
        #         if not (self._objective_view == COMPARATIVE and
        #                 objective in objectives):
        #             objectives.append(objective)
        return objects.ObjectiveList(objectives)

    def get_objectives_by_genus_type(self, objective_genus_type=None):
        """Gets an ObjectiveList corresponding to the given objective genus
        Type which does not include objectives of genus types derived
        from the specified Type.
        In plenary mode, the returned list contains all known objectives
        or an error results. Otherwise, the returned list may contain
        only those objectives that are accessible through this session.
        arg:    objectiveGenusType (osid.type.Type): an objective genus
                type
        return: (osid.learning.ObjectiveList) - the returned Objective
                list
        raise:  NullArgument - objectiveGenusType is null
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method must be implemented.

        """
        if objective_genus_type is None:
            raise NullArgument()
        url_path = construct_url('objectives_by_genus',
                                 bank_id=self._catalog_idstr,
                                 genus_type=str(objective_genus_type))
        return objects.ObjectiveList(self._get_request(url_path))

    def get_objectives_by_parent_genus_type(self, objective_genus_type=None):
        """Gets an ObjectiveList corresponding to the given objective genus
        Type and include any additional objective with genus types
        derived from the specified Type.
        In plenary mode, the returned list contains all known objectives
        or an error results. Otherwise, the returned list may contain
        only those objectives that are accessible through this session
        arg:    objectiveGenusType (osid.type.Type): an objective genus
                type
        return: (osid.learning.ObjectiveList) - the returned Objective
                list
        raise:  NullArgument - objectiveGenusType is null
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method must be implemented.

        """
        raise Unimplemented()

    def get_objectives_by_record_type(self, objective_record_type=None):
        """Gets an ObjectiveList containing the given objective record
        Type.
        In plenary mode, the returned list contains all known objectives
        or an error results. Otherwise, the returned list may contain
        only those objectives that are accessible through this session.
        arg:    objectiveRecordType (osid.type.Type): an objective
                record type
        return: (osid.learning.ObjectiveList) - the returned Objective
                list
        raise:  NullArgument - objectiveRecordType is null
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method must be implemented.

        """
        raise Unimplemented()

    def get_objectives(self):
        """Gets all Objectives.
        In plenary mode, the returned list contains all known objectives
        or an error results. Otherwise, the returned list may contain
        only those objectives that are accessible through this session.
        return: (osid.learning.ObjectiveList) - an ObjectiveList
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method must be implemented.

        """
        url_path = construct_url('objectives',
                                 bank_id=self._catalog_idstr)
        return objects.ObjectiveList(self._get_request(url_path))

    objective_bank_id = property(get_objective_bank_id)
    objective_bank = property(get_objective_bank)
    objectives = property(get_objectives)


class ObjectiveObjectiveBankAssignmentSession(abc_learning_sessions.ObjectiveObjectiveBankAssignmentSession,
                                              osid_sessions.OsidSession):
    """This session provides methods to re-assign Objectives to ObjectiveBanks.

    An Objective may map to multiple ObjectiveBanks and removing the last reference to an
    Objective is the equivalent of deleting it. Each ObjectiveBank may have its own
    authorizations governing who is allowed to operate on it.

    Moving or adding a reference of an Objective to another ObjectiveBank is not a
    copy operation (eg: does not change its Id ).

    """
    def __init__(self, objective_bank_id, proxy=None, runtime=None, **kwargs):
        self._service_string = SERVICE_STRING
        self._catalogs_string = CATALOGS_STRING
        osid_sessions.OsidSession.__init__(self)
        osid_sessions.OsidSession._init_catalog(
            self,
            proxy,
            runtime
        )
        self._objective_view = COMPARATIVE
        self._objective_bank_view = FEDERATED
        self._objective_bank_id = objective_bank_id
        self._catalog_idstr = str(objective_bank_id)
        self._kwargs = kwargs

    def can_assign_objectives(self):
        return True

    def assign_objective_to_objective_bank(self, objective_id, objective_bank_id):
        if not objective_bank_id or not objective_id:
            raise NullArgument('must provide both objective_id and objective_bank_id')
        if not isinstance(objective_id, Id):
            raise InvalidArgument('objective_id needs to be an Id object')
        if not isinstance(objective_bank_id, Id):
            raise InvalidArgument('objective_bank_id needs to be an Id object')
        url_path = construct_url('objective_objective_bank_assignment',
                                 bank_id=objective_bank_id,
                                 obj_id=objective_id)
        return self._post_request(url_path, {})


class ObjectiveQuerySession(abc_learning_sessions.ObjectiveQuerySession, osid_sessions.OsidSession):
    """This session provides methods for searching Objective objects.

    The search query is constructed using the ObjectiveQuery. The
    objective record Type also specifies the record for the objective
    query.

    This session defines views that offer differing behaviors for
    searching.
      > federated objective bank view: searches include objectives in
        objective banks of which this objective bank is a ancestor in
        the objective bank hierarchy
      > isolated objective bank view: searches are restricted to
        objectives in this objective bank


    Objectives may have a query record indicated by their respective
    record types. The query record is accessed via the ObjectiveQuery.

    """
    def __init__(self, objective_bank_id, proxy=None, runtime=None, **kwargs):
        self._service_string = SERVICE_STRING
        self._catalogs_string = CATALOGS_STRING
        osid_sessions.OsidSession.__init__(self)
        osid_sessions.OsidSession._init_catalog(
            self,
            proxy,
            runtime
        )
        self._objective_view = COMPARATIVE
        self._objective_bank_view = FEDERATED
        self._objective_bank_id = objective_bank_id
        self._catalog_idstr = str(objective_bank_id)
        self._kwargs = kwargs

    def get_objective_bank_id(self):
        """Gets the ObjectiveBank  Id associated with this session.

        return: (osid.id.Id) - the ObjectiveBank Id associated with this
                session
        compliance: mandatory - This method must be implemented.

        """
        return self._objective_bank_id

    def get_objective_bank(self):
        """Gets the ObjectiveBank associated with this session.

        return: (osid.learning.ObjectiveBank) - the ObjectiveBank
                associated with this session
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method must be implemented.

        """
        return ObjectiveBankLookupSession().get_objective_bank(self._objective_bank_id)

    def can_search_objectives(self):
        """Tests if this user can perform Objectives searches.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a PermissionDenied. This is intended as
        a hint to an application that may opt not to offer search
        operations to unauthorized users.
        return: (boolean) - false if search methods are not authorized,
                true otherwise
        compliance: mandatory - This method must be implemented.

        """
        pass

    def use_federated_objective_bank_view(self):
        """Federates the view for methods in this session.
        A federated view will include objectives in objective banks
        which are children of this objective bank in the objective bank
        hierarchy.
        compliance: mandatory - This method is must be implemented.

        """
        self._objective_bank_view = FEDERATED

    def use_isolated_objective_bank_view(self):
        """Isolates the view for methods in this session.
        An isolated view restricts searches to this objective bank only.
        compliance: mandatory - This method is must be implemented.

        """
        self._objective_bank_view = ISOLATED

    def get_objective_query(self):
        """Gets an objective query.

        return: (osid.learning.ObjectiveQuery) - the objective query
        compliance: mandatory - This method must be implemented.

        """
        return queries.ObjectiveQuery()

    def get_objectives_by_query(self, objective_query=None):
        """Gets a list of Objectives matching the given objective query.

        arg:    objectiveQuery (osid.learning.ObjectiveQuery): the
                objective query
        return: (osid.learning.ObjectiveList) - the returned
                ObjectiveList
        raise:  NullArgument - objectiveQuery is null
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - objectiveQuery is not of this service
        compliance: mandatory - This method must be implemented.

        """
        if objective_query is None:
            raise NullArgument()
        if 'ancestorObjectiveId' in objective_query._query_terms:
            url_path = construct_url('objectives',
                                     bank_id=self._objective_bank_id,
                                     obj_id=objective_query._query_terms['ancestorObjectiveId'].split('=')[1])
            url_path += '/children'
        elif 'descendantObjectiveId' in objective_query._query_terms:
            url_path = construct_url('objectives',
                                     bank_id=self._objective_bank_id,
                                     obj_id=objective_query._query_terms['descendantObjectiveId'].split('=')[1])
            url_path += '/parents'
        else:
            url_path = construct_url('objectives', obj_id=None)

        for term in objective_query._query_terms:
            if term not in ['ancestorObjectiveId', 'descendantObjectiveId']:
                url_path += '&{0}'.format(objective_query._query_terms[term])

        url_path = url_path.replace('&', '?', 1)
        return objects.ObjectiveList(self._get_request(url_path))

    objective_bank_id = property(get_objective_bank_id)
    objective_bank = property(get_objective_bank)
    objective_query = property(get_objective_query)


class ObjectiveSearchSession(abc_learning_sessions.ObjectiveSearchSession, ObjectiveQuerySession):
    """This session provides methods for searching Objective objects.

    The search query is constructed using the ObjectiveQuery. The
    objective record Type also specifies the record for the objective
    query.

    get_objectives_by_query() is the basic search method and returns a
    list of Objectives. A more advanced search may be performed with
    get_objectives_by_search(). It accepts a ObjectiveSearch in addition
    to the query for the purpose of specifying additional options
    affecting the entire search, such as ordering.
    get_objectives_by_search() returns an ObjectiveSearchResults that
    can be used to access the resulting ObjectiveList or be used to
    perform a search within the result set through ObjectiveSearch.

    This session defines views that offer differing behaviors for
    searching.
      > federated objective bank view: searches include objectives in
        objective banks of which this objective bank is a ancestor in
        the objective bank hierarchy
      > isolated objective bank view: searches are restricted to
        objectives in this objective bank


    Objectives may have a query record indicated by their respective
    record types. The query record is accessed via the ObjectiveQuery.

    """

    def get_objective_search(self):
        """Gets an objective search.

        return: (osid.learning.ObjectiveSearch) - the objective search
        compliance: mandatory - This method must be implemented.

        """
        pass

    def get_objective_search_order(self):
        """Gets a n objective search order.
        The ObjectiveSearchOrder is supplied to an ObjectiveSearch to
        specify the ordering of results.
        return: (osid.learning.ObjectiveSearchOrder) - the objective
                search order
        compliance: mandatory - This method must be implemented.

        """
        pass

    def get_objectives_by_search(self, objective_query=None, objective_search=None):
        """Gets the search results matching the given search query using
        the given search.

        arg:    objectiveSearch (osid.learning.ObjectiveSearch): the
                objective search
        return: (osid.learning.ObjectiveSearchResults) - the returned
                search results
        raise:  NullArgument - objectiveQuery or objectiveSearch is
                null
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - objectiveSearch or objectiveQuery is not
                of this service
        compliance: mandatory - This method must be implemented.

        """
        pass

    def get_objective_query_from_inspector(self, objective_query_inspector=None):
        """Gets an objective query from an inspector.
        The inspector is available from an ObjectiveSearchResults.
        arg:    objectiveQueryInspector
                (osid.learning.ObjectiveQueryInspector): an objective
                bank query inspector
        return: (osid.learning.ObjectiveQuery) - the objective query
        raise:  NullArgument - objectiveQueryInspector is null
        raise:  Unsupported - objectiveQueryInspector is not of this
                service
        compliance: mandatory - This method must be implemented.

        """
        pass

    objective_search = property(get_objective_search)
    objective_search_order = property(get_objective_search_order)


class ObjectiveAdminSession(abc_learning_sessions.ObjectiveAdminSession, osid_sessions.OsidSession):
    """This session creates, updates, and deletes Objectives.

    The data for create and update is provided by the consumer via the
    form object. OsidForms are requested for each create or update and
    may not be reused.

    Create and update operations differ in their usage. To create an
    Objective, a ObjectiveForm is requested using
    get_objective_form_for_create() specifying the desired record Types
    or none if no record Types are needed. The returned ObjectiveForm
    will indicate that it is to be used with a create operation and can
    be used to examine metdata or validate data prior to creation. Once
    the ObjectiveForm is submiited to a create operation, it cannot be
    reused with another create operation unless the first operation was
    unsuccessful. Each ObjectiveForm corresponds to an attempted
    transaction.

    For updates, ObjectiveForms are requested to the Objective  Id that
    is to be updated using get_objective_form_for_update(). Similarly,
    the ObjectiveForm has metadata about the data that can be updated
    and it can perform validation before submitting the update. The
    ObjectiveForm can only be used once for a successful update and
    cannot be reused.

    The delete operations delete Objectives. To unmap an Objective from
    the current ObjectiveBank, the
    ObjectiveObjectiveBankAssignmentSession should be used. These delete
    operations attempt to remove the Objective itself thus removing it
    from all known ObjectiveBank catalogs.

    This session includes an Id aliasing mechanism to assign an external
    Id to an internally assigned Id.

    """
    def __init__(self, objective_bank_id=None, proxy=None, runtime=None, **kwargs):
        self._service_string = SERVICE_STRING
        self._catalogs_string = CATALOGS_STRING
        osid_sessions.OsidSession.__init__(self)
        osid_sessions.OsidSession._init_catalog(
            self,
            proxy,
            runtime
        )
        if objective_bank_id is None:
            # For now we are just going to find the first objective bank
            # This needs to change!
            url_path = construct_url('objective_banks')
            objective_bank = objects.ObjectiveBank(self._get_request(url_path)[0])
            self._objective_bank_id = objective_bank.get_id()
        else:
            self._objective_bank_id = objective_bank_id
        self._catalog_idstr = str(self._objective_bank_id)
        self._forms = dict()
        self._kwargs = kwargs

    # to support record extensions

    def _record_extension(self, objective_id, key, value):
        """
        To structure a record extension property bean
        """
        record_bean = {
            'value': value,
            'displayName': self._text_bean(key),
            'description': self._text_bean(key),
            'displayLabel': self._text_bean(key),
            'associatedId': str(objective_id)
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

    def extension_url(self, objective_id):
        from ..utilities import construct_url
        extension_url = construct_url('extension_record',
                                      bank_id=str(self._objective_bank_id),
                                      obj_id=str(objective_id))
        return extension_url

    def extensions(self, objective_id):
        extension_url = self.extension_url(objective_id)
        return self._get_request(extension_url)['recordProperties']

    def clear_objective_record_extension(self, objective_id, key):
        extensions = self.extensions(objective_id)
        extension_url = self.extension_url(objective_id)
        results = []
        for ext in extensions:
            if ext['displayName']['text'] != key:
                results.append(self._record_extension(objective_id,
                                                      ext['displayName']['text'],
                                                      ext['value']))
        updated_extensions = {
            'associatedId': str(objective_id),
            'recordProperties': results
        }
        return self._put_request(extension_url, updated_extensions)

    def get_objective_record_extensions(self, objective_id, item):
        extensions = self.extensions(objective_id)
        results = []
        for ext in extensions:
            if ext['displayName']['text'] == item:
                results.append(ext['value'])
        return results

    def set_objective_record_extension(self, objective_id, key, value):
        extension_url = self.extension_url(objective_id)
        current_extensions = self.extensions(objective_id)
        current_extensions.append(self._record_extension(objective_id, key, value))
        updated_extensions = {
            'associatedId': str(objective_id),
            'recordProperties': current_extensions
        }
        return self._put_request(extension_url, updated_extensions)
# ==================

    def get_objective_bank_id(self):
        """Gets the ObjectiveBank  Id associated with this session.

        return: (osid.id.Id) - the ObjectiveBank Id associated with this
                session
        compliance: mandatory - This method must be implemented.

        """
        return self._objective_bank_id

    def get_objective_bank(self):
        """Gets the ObjectiveBank associated with this session.

        return: (osid.learning.ObjectiveBank) - the ObjectiveBank
                associated with this session
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method must be implemented.

        """
        return ObjectiveBankLookupSession().get_objective_bank(self._objective_bank_id)

    def can_create_objectives(self):
        """Tests if this user can create Objectives.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating an Objective
        will result in a PermissionDenied. This is intended as a hint
        to an application that may opt not to offer create operations to
        an unauthorized user.
        return: (boolean) - false if Objective creation is not
                authorized, true otherwise
        compliance: mandatory - This method must be implemented.

        """
        url_path = construct_url('authorization',
                                 bank_id=self._catalog_idstr)
        return self._get_request(url_path)['objectiveHints']['canCreate']

    def can_create_objective_with_record_types(self, objective_record_types=None):
        """Tests if this user can create a single Objective using the
        desired record types.
        While learning_manager.get_objective_record_types() can be used
        to examine which records are supported, this method tests which
        record(s) are required for creating a specific Objective.
        Providing an empty array tests if an Objective can be created
        with no records.
        arg:    objectiveRecordTypes (osid.type.Type): array of
                objective record types
        return: (boolean) - true if Objective creation using the
                specified record Types is supported, false otherwise
        raise:  NullArgument - objectiveRecordTypes is null
        compliance: mandatory - This method must be implemented.

        """
        return True

    def get_objective_form_for_create(self, objective_record_types=None):
        """Gets the objective form for creating new objectives.
        A new form should be requested for each create transaction.
        arg:    objectiveRecordTypes (osid.type.Type): array of
                objective record types
        return: (osid.learning.ObjectiveForm) - the objective form
        raise:  NullArgument - objectiveRecordTypes is null
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - unable to get form for requested record
                types
        compliance: mandatory - This method must be implemented.

        """
        if objective_record_types is None:
            pass  # Still need to deal with the record_types argument
        objective_form = objects.ObjectiveForm()
        self._forms[objective_form.get_id().get_identifier()] = not CREATED
        return objective_form

    def create_objective(self, objective_form=None):
        """Creates a new Objective.

        arg:    objectiveForm (osid.learning.ObjectiveForm): the form
                for this Objective
        return: (osid.learning.Objective) - the new Objective
        raise:  IllegalState - objectiveForm already used in a create
                transaction
        raise:  InvalidArgument - one or more of the form elements is
                invalid
        raise:  NullArgument - objectiveForm is null
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - objectiveForm did not originate from
                get_objective_form_for_create()
        compliance: mandatory - This method must be implemented.

        """
        if objective_form is None:
            raise NullArgument()
        if not isinstance(objective_form, abc_learning_objects.ObjectiveForm):
            raise InvalidArgument('argument type is not an ObjectiveForm')
        if objective_form.is_for_update():
            raise InvalidArgument('form is for update only, not create')
        try:
            if self._forms[objective_form.get_id().get_identifier()] == CREATED:
                raise IllegalState('form already used in a create transaction')
        except KeyError:
            raise Unsupported('form did not originate from this session')
        if not objective_form.is_valid():
            raise InvalidArgument('one or more of the form elements is invalid')

        url_path = construct_url('objectives',
                                 bank_id=self._catalog_idstr)
        try:
            result = self._post_request(url_path, objective_form._my_map)
        except Exception:
            raise  # OperationFailed
        self._forms[objective_form.get_id().get_identifier()] = CREATED
        return objects.Objective(result)

    def can_update_objectives(self):
        """Tests if this user can update Objectives.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating an Objective
        will result in a PermissionDenied. This is intended as a hint
        to an application that may opt not to offer update operations to
        an unauthorized user.
        return: (boolean) - false if objective modification is not
                authorized, true otherwise
        compliance: mandatory - This method must be implemented.

        """
        url_path = construct_url('authorization',
                                 self._catalog_idstr)
        return self._get_request(url_path)['objectiveHints']['canUpdate']

    def get_objective_form_for_update(self, objective_id=None):
        """Gets the objective form for updating an existing objective.
        A new objective form should be requested for each update
        transaction.
        arg:    objectiveId (osid.id.Id): the Id of the Objective
        return: (osid.learning.ObjectiveForm) - the objective form
        raise:  NotFound - objectiveId is not found
        raise:  NullArgument - objectiveId is null
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method must be implemented.

        """
        if objective_id is None:
            raise NullArgument()
        try:
            url_path = construct_url('objectives',
                                     bank_id=self._catalog_idstr,
                                     obj_id=objective_id)
            objective = objects.Objective(self._get_request(url_path))
        except Exception:
            raise
        objective_form = objects.ObjectiveForm(objective._my_map)
        self._forms[objective_form.get_id().get_identifier()] = not UPDATED
        return objective_form

    def update_objective(self, objective_form=None):
        """Updates an existing objective.

        arg:    objectiveForm (osid.learning.ObjectiveForm): the form
                containing the elements to be updated
        raise:  IllegalState - objectiveForm already used in an update
                transaction
        raise:  InvalidArgument - the form contains an invalid value
        raise:  NullArgument - objectiveForm is null
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - objectiveForm did not originate from
                get_objective_form_for_update()
        compliance: mandatory - This method must be implemented.

        """
        if objective_form is None:
            raise NullArgument()
        if not isinstance(objective_form, abc_learning_objects.ObjectiveForm):
            raise InvalidArgument('argument type is not an ObjectiveForm')
        if not objective_form.is_for_update():
            raise InvalidArgument('form is for create only, not update')
        try:
            if self._forms[objective_form.get_id().get_identifier()] == UPDATED:
                raise IllegalState('form already used in an update transaction')
        except KeyError:
            raise Unsupported('form did not originate from this session')
        if not objective_form.is_valid():
            raise InvalidArgument('one or more of the form elements is invalid')

        url_path = construct_url('objectives',
                                 bank_id=self._catalog_idstr)
        try:
            # print url_path
            # print objective_form._my_map
            result = self._put_request(url_path, objective_form._my_map)
        except Exception:
            raise  # OperationFailed
        self._forms[objective_form.get_id().get_identifier()] = UPDATED
        return objects.Objective(result)  # Not expected to return anything

    def can_delete_objectives(self):
        """Tests if this user can delete Objectives.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting an Objective
        will result in a PermissionDenied. This is intended as a hint
        to an application that may opt not to offer delete operations to
        an unauthorized user.
        return: (boolean) - false if Objective deletion is not
                authorized, true otherwise
        compliance: mandatory - This method must be implemented.

        """
        url_path = construct_url('authorization',
                                 bank_id=self._catalog_idstr)
        return self._get_request(url_path)['objectiveHints']['canDelete']

    def delete_objective(self, objective_id=None):
        """Deletes the Objective identified by the given Id.

        arg:    objectiveId (osid.id.Id): the Id of the Objective to
                delete
        raise:  NotFound - an Objective was not found identified by the
                given Id
        raise:  NullArgument - objectiveId is null
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method must be implemented.

        """
        if objective_id is None:
            raise NullArgument()
        if not isinstance(objective_id, abc_id):
            raise InvalidArgument('argument type is not an osid Id')

        url_path = construct_url('objectives',
                                 bank_id=self._catalog_idstr,
                                 obj_id=objective_id)
        result = self._delete_request(url_path)
        return objects.Objective(result)  # Not expected to return anything

    def can_manage_objective_aliases(self):
        """Tests if this user can manage Id aliases for Objectives.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a PermissionDenied. This is intended as a hint
        to an application that may opt not to offer alias operations to
        an unauthorized user.
        return: (boolean) - false if Objective aliasing is not
                authorized, true otherwise
        compliance: mandatory - This method must be implemented.

        """
        return False  # Not yet implemented

    def alias_objective(self, objective_id=None, alias_id=None):
        """Adds an Id to an Objective for the purpose of creating
        compatibility.
        The primary Id of the Objective is determined by the provider.
        The new Id performs as an alias to the primary Id. If the alias
        is a pointer to another objective, it is reassigned to the given
        objective Id.
        arg:    aliasId (osid.id.Id): the alias Id
        raise:  AlreadyExists - aliasId is already assigned
        raise:  NotFound - objectiveId not found
        raise:  NullArgument - objectiveId or aliasId is null
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method must be implemented.

        """
        raise Unimplemented()

    objective_bank_id = property(get_objective_bank_id)
    objective_bank = property(get_objective_bank)


class ObjectiveHierarchySession(abc_learning_sessions.ObjectiveHierarchySession,
                                osid_sessions.OsidSession):
    """This session defines methods for traversing a hierarchy of Objective
    objects.

    Each node in the hierarchy is a unique Objective that contains its
    child objectives. The hierarchy may be traversed recursively to
    establish the tree structure through get_parent_objectives() and
    getChildObjectives(). To relate these Ids to another OSID,
    get_objective_nodes() can be used for retrievals that can be used
    for bulk lookups in other OSIDs. Any Objective available in the
    Learning OSID is known to this hierarchy but does not appear in the
    hierarchy traversal until added as a root node or a child of another
    node.

    A user may not be authorized to traverse the entire hierarchy. Parts
    of the hierarchy may be made invisible through omission from the
    returns of get_parent_objectives() or get_child_objectives() in lieu
    of a PermissionDenied error that may disrupt the traversal through
    authorized pathways.

    This session defines views that offer differing behaviors when
    retrieving multiple objects.

      > comparative view: objective elements may be silently omitted or
        re-ordered
      > plenary view: provides a complete set or is an error condition


    """

    def __init__(self, objective_bank_id=None, proxy=None, runtime=None, **kwargs):
        self._service_string = SERVICE_STRING
        self._catalogs_string = CATALOGS_STRING
        osid_sessions.OsidSession.__init__(self)
        osid_sessions.OsidSession._init_catalog(
            self,
            proxy,
            runtime
        )
        self._objective_view = COMPARATIVE
        if objective_bank_id is None:
            # For now we are just going to find the first objective bank
            # This needs to change!
            url_path = construct_url('objective_banks')
            objective_bank = objects.ObjectiveBank(self._get_request(url_path)[0])
            self._objective_bank_id = objective_bank.get_id()
        else:
            self._objective_bank_id = objective_bank_id
        self._catalog_idstr = str(self._objective_bank_id)
        self._kwargs = kwargs

    def get_objective_hierarchy_id(self):
        """Gets the hierarchy Id associated with this session.

        return: (osid.id.Id) - the hierarchy Id associated with this
                session
        compliance: mandatory - This method must be implemented.

        """
        # OK, No. This isn't returning a Hierarchy Id
        return self._objective_bank_id

    def get_objective_hierarchy(self):
        """Gets the hierarchy associated with this session.

        return: (osid.hierarchy.Hierarchy) - the hierarchy associated
                with this session
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method must be implemented.

        """
        # OK, No. This isn't returning a Hierarchy
        return ObjectiveBankLookupSession().get_objective_bank(self._objective_bank_id)

    def can_access_objective_hierarchy(self):
        """Tests if this user can perform hierarchy queries.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a PermissionDenied. This is intended as a
        hint to an an application that may not offer traversal functions
        to unauthorized users.

        return: (boolean) - false if hierarchy traversal methods are not
                authorized, true otherwise
        compliance: mandatory - This method must be implemented.

        """
        url_path = construct_url('authorization',
                                 bank_id=self._catalog_idstr)
        return self._get_request(url_path)['objectiveHierarchyHints']['canAccessHierarchy']

    def use_comparative_objective_view(self):
        """The returns from the objective methods may omit or translate
        elements based on this session, such as authorization, and not
        result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        compliance: mandatory - This method is must be implemented.

        """
        self._objective_view = COMPARATIVE

    def use_plenary_objective_view(self):
        """A complete view of the Hierarchy returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        compliance: mandatory - This method is must be implemented.

        """
        self._objective_view = PLENARY

    def get_root_objective_ids(self):
        """Gets the root objective Ids in this hierarchy.

        return: (osid.id.IdList) - the root objective Ids
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method must be implemented.

        """
        url_path = construct_url('rootids',
                                 bank_id=self._catalog_idstr)
        id_list = list()
        for identifier in self._get_request(url_path)['ids']:
            id_list.append(Id(idstr=identifier))
        return id_objects.IdList(id_list)

    def get_root_objectives(self):
        """Gets the root objective in this objective hierarchy.

        return: (osid.learning.ObjectiveList) - the root objective
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method is must be implemented.

        """
        url_path = construct_url('roots',
                                 bank_id=self._catalog_idstr)
        return objects.ObjectiveList(self._get_request(url_path))

    def has_parent_objectives(self, objective_id=None):
        """Tests if the Objective has any parents.

        arg:    objective_id (osid.id.Id): the Id of an objective
        return: (boolean) - true if the objective has parents, false
                otherwise
        raise:  NotFound - objective_id is not found
        raise:  NullArgument - objective_id is null
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method must be implemented.

        """
        if objective_id is None:
            raise NullArgument()
        return bool(self.get_parent_objectives(objective_id))

    def is_parent_of_objective(self, id_=None, objective_id=None):
        """Tests if an Id is a direct parent of an objective.

        arg:    id (osid.id.Id): an Id
        arg:    objective_id (osid.id.Id): the Id of an objective
        return: (boolean) - true if this id is a parent of objective_id,
                false otherwise
        raise:  NotFound - objective_id is not found
        raise:  NullArgument - id or objective_id is null
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method must be implemented.
        implementation notes: If id not found return false.

        """
        if id_ is None or objective_id is None:
            raise NullArgument()
        return id_ in list(self.get_parent_objective_ids(objective_id))

    def get_parent_objective_ids(self, objective_id=None):
        """Gets the parent Ids of the given objective.

        arg:    objective_id (osid.id.Id): the Id of an objective
        return: (osid.id.IdList) - the parent Ids of the objective
        raise:  NotFound - objective_id is not found
        raise:  NullArgument - objective_id is null
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method must be implemented.

        """
        if objective_id is None:
            raise NullArgument()
        url_path = construct_url('parentids',
                                 bank_id=self._catalog_idstr,
                                 obj_id=objective_id)
        id_list = list()
        for identifier in self._get_request(url_path)['ids']:
            id_list.append(Id(idstr=identifier))
        return id_objects.IdList(id_list)

    def get_parent_objectives(self, objective_id=None):
        """Gets the parents of the given objective.

        arg:    objective_id (osid.id.Id): the Id of an objective
        return: (osid.learning.ObjectiveList) - the parents of the
                objective
        raise:  NotFound - objective_id is not found
        raise:  NullArgument - objective_id is null
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method must be implemented.

        """
        if objective_id is None:
            raise NullArgument()
        url_path = construct_url('parents',
                                 bank_id=self._catalog_idstr,
                                 obj_id=objective_id)
        return objects.ObjectiveList(self._get_request(url_path))

    def is_ancestor_of_objective(self, id=None, objective_id=None):
        """Tests if an Id is an ancestor of an objective.

        arg:    id (osid.id.Id): an Id
        arg:    objective_id (osid.id.Id): the Id of an objective
        return: (boolean) - true if this id is an ancestor of
                objective_id,  false otherwise
        raise:  NotFound - objective_id is not found
        raise:  NullArgument - id or objective_id is null
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method must be implemented.
        implementation notes: If id not found return false.

        """
        raise Unimplemented()

    def has_child_objectives(self, objective_id=None):
        """Tests if an objective has any children.

        arg:    objective_id (osid.id.Id): the Id of an objective
        return: (boolean) - true if the objective_id has children, false
                otherwise
        raise:  NotFound - objective_id is not found
        raise:  NullArgument - objective_id is null
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method must be implemented.

        """
        if objective_id is None:
            raise NullArgument()
        return bool(self.get_child_objectives(objective_id))

    def is_child_of_objective(self, id_=None, objective_id=None):
        """Tests if an objective is a direct child of another.

        arg:    id (osid.id.Id): an Id
        arg:    objective_id (osid.id.Id): the Id of an objective
        return: (boolean) - true if the id is a child of objective_id,
                false otherwise
        raise:  NotFound - objective_id is not found
        raise:  NullArgument - id or objective_id is null
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method must be implemented.
        implementation notes: If id not found return false.

        """
        if id_ is None or objective_id is None:
            raise NullArgument()
        return id_ in list(self.get_child_objective_ids(objective_id))

    def get_child_objective_ids(self, objective_id=None):
        """Gets the child Ids of the given objective.

        arg:    objective_id (osid.id.Id): the Id to query
        return: (osid.id.IdList) - the children of the objective
        raise:  NotFound - objective_id is not found
        raise:  NullArgument - objective_id is null
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method must be implemented.

        """
        if objective_id is None:
            raise NullArgument()
        url_path = construct_url('childids',
                                 bank_id=self._catalog_idstr,
                                 obj_id=objective_id)
        id_list = list()
        for identifier in self._get_request(url_path)['ids']:
            id_list.append(Id(idstr=identifier))
        return id_objects.IdList(id_list)

    def get_child_objectives(self, objective_id=None):
        """Gets the children of the given objective.

        arg:    objective_id (osid.id.Id): the Id to query
        return: (osid.learning.ObjectiveList) - the children of the
                objective
        raise:  NotFound - objective_id is not found
        raise:  NullArgument - objective_id is null
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method must be implemented.

        """
        if objective_id is None:
            raise NullArgument()
        url_path = construct_url('children',
                                 bank_id=self._catalog_idstr,
                                 obj_id=objective_id)
        return objects.ObjectiveList(self._get_request(url_path))

    def is_descendant_of_objective(self, id=None, objective_id=None):
        """Tests if an Id is a descendant of an objective.

        arg:    id (osid.id.Id): an Id
        arg:    objective_id (osid.id.Id): the Id of an objective
        return: (boolean) - true if the id is a descendant of the
                objective_id,  false otherwise
        raise:  NotFound - objective_id is not found
        raise:  NullArgument - id or objective_id is null
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method must be implemented.
        implementation notes: If id is not found return false.

        """
        raise Unimplemented()

    def get_objective_node_ids(self,
                               objective_id=None,
                               ancestor_levels=None,
                               descendant_levels=None,
                               include_siblings=None):
        """Gets a portion of the hierarchy for the given objective.

        arg:    objective_id (osid.id.Id): the Id to query
        arg:    ancestor_levels (cardinal): the maximum number of
                ancestor levels to include. A value of 0 returns no
                parents in the node.
        arg:    descendant_levels (cardinal): the maximum number of
                descendant levels to include. A value of 0 returns no
                children in the node.
        arg:    include_siblings (boolean): true to include the siblings
                of the given node, false to omit the siblings
        return: (osid.hierarchy.Node) - a catalog node
        raise:  NotFound - objective_id not found
        raise:  NullArgument - objective_id is null
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method must be implemented.

        """
        raise Unimplemented()

    def get_objective_nodes(self,
                            objective_id=None,
                            ancestor_levels=None,
                            descendant_levels=None,
                            include_siblings=None):
        """Gets a portion of the hierarchy for the given objective.

        arg:    objective_id (osid.id.Id): the Id to query
        arg:    ancestor_levels (cardinal): the maximum number of
                ancestor levels to include. A value of 0 returns no
                parents in the node.
        arg:    descendant_levels (cardinal): the maximum number of
                descendant levels to include. A value of 0 returns no
                children in the node.
        arg:    include_siblings (boolean): true to include the siblings
                of the given node, false to omit the siblings
        return: (osid.learning.ObjectiveNode) - an objective node
        raise:  NotFound - objective_id not found
        raise:  NullArgument - objective_id is null
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method must be implemented.

        """
        if objective_id is None:
            url_path = construct_url('roots',
                                     bank_id=self._catalog_idstr,
                                     descendents=descendant_levels)
            return self._get_request(url_path)
        else:
            raise Unimplemented()


class ObjectiveHierarchyDesignSession(abc_learning_sessions.ObjectiveHierarchyDesignSession,
                                      osid_sessions.OsidSession):
    """This session defines methods for managing a hierarchy of Objective
    objects.

    Each node in the hierarchy is a unique Objective.

    """
    def __init__(self, objective_bank_id=None, proxy=None, runtime=None, **kwargs):
        self._service_string = SERVICE_STRING
        self._catalogs_string = CATALOGS_STRING
        osid_sessions.OsidSession.__init__(self)
        osid_sessions.OsidSession._init_catalog(
            self,
            proxy,
            runtime
        )
        self._objective_view = COMPARATIVE
        if objective_bank_id is None:
            # For now we are just going to find the first objective bank
            # This needs to change!
            url_path = construct_url('objective_banks')
            objective_bank = objects.ObjectiveBank(self._get_request(url_path)[0])
            self._objective_bank_id = objective_bank.get_id()
        else:
            self._objective_bank_id = objective_bank_id
        self._catalog_idstr = str(self._objective_bank_id)
        self._kwargs = kwargs

    def get_objective_hierarchy_id(self):
        """Gets the hierarchy Id associated with this session.

        return: (osid.id.Id) - the hierarchy Id associated with this
                session
        compliance: mandatory - This method must be implemented.

        """
        return self._objective_bank_id

    def get_objective_hierarchy(self):
        """Gets the hierarchy associated with this session.

        return: (osid.hierarchy.Hierarchy) - the hierarchy associated
                with this session
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method must be implemented.

        """
        # OK, No. This isn't returning a Hierarchy
        return ObjectiveBankLookupSession().get_objective_bank(self._objective_bank_id)

    def can_modify_objective_hierarchy(self):
        """Tests if this user can change the hierarchy.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known performing any update
        will result in a PermissionDenied. This is intended as a hint to
        an application that may opt not to offer these operations to an
        unauthorized user.

        return: (boolean) - false if changing this hierarchy is not
                authorized, true otherwise
        compliance: mandatory - This method must be implemented.

        """
        url_path = construct_url('authorization',
                                 bank_id=self._catalog_idstr)
        return self._get_request(url_path)['objectiveHierarchyHints']['canModifyHierarchy']

    def add_root_objective(self, objective_id=None):
        """Adds a root objective.

        arg:    objective_id (osid.id.Id): the Id of an objective
        raise:  AlreadyExists - objective_id is already in hierarchy
        raise:  NotFound - objective_id not found
        raise:  NullArgument - objective_id is null
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method must be implemented.

        """
        raise Unimplemented()

    def remove_root_objective(self, objective_id=None):
        """Removes a root objective.

        arg:    objective_id (osid.id.Id): the Id of an objective
        raise:  NotFound - objective_id not found
        raise:  NullArgument - objective_id is null
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method must be implemented.

        """
        raise Unimplemented()

    def add_child_objective(self, objective_id=None, child_id=None):
        """Adds a child to an objective.

        arg:    objective_id (osid.id.Id): the Id of an objective
        arg:    child_id (osid.id.Id): the Id of the new child
        raise:  AlreadyExists - objective_id is already a parent of
                child_id
        raise:  NotFound - objective_id or child_id not found
        raise:  NullArgument - objective_id or child_id is null
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method must be implemented.

        """
        if objective_id is None or child_id is None:
            raise NullArgument()
        ohs = ObjectiveHierarchySession(self._objective_bank_id,
                                        runtime=self._runtime)
        if ohs.is_child_of_objective(child_id, objective_id):
            raise AlreadyExists()
        ids_arg = {'ids': []}
        for ident in ohs.get_child_objective_ids(objective_id):
            ids_arg['ids'].append(str(ident))
        ids_arg['ids'].append(str(child_id))

        url_path = construct_url('childids',
                                 bank_id=self._catalog_idstr,
                                 obj_id=objective_id)
        try:
            result = self._put_request(url_path, ids_arg)
        except Exception:
            raise
        id_list = list()
        for identifier in result['ids']:
            id_list.append(Id(idstr=identifier))
        return id_objects.IdList(id_list)

    def remove_child_objective(self, objective_id=None, child_id=None):
        """Removes a child from an objective.

        arg:    objective_id (osid.id.Id): the Id of an objective
        arg:    child_id (osid.id.Id): the Id of the new child
        raise:  NotFound - objective_id not a parent of child_id
        raise:  NullArgument - objective_id or child_id is null
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method must be implemented.

        """
        if objective_id is None or child_id is None:
            raise NullArgument()
        ohs = ObjectiveHierarchySession(self._objective_bank_id,
                                        runtime=self._runtime)
        if not ohs.is_child_of_objective(child_id, objective_id):
            raise NotFound('objective_id not a parent of child_id')
        ids_arg = {'ids': []}
        for ident in ohs.get_child_objective_ids(objective_id):
            if ident != child_id:
                ids_arg['ids'].append(str(ident))

        url_path = construct_url('childids',
                                 bank_id=self._catalog_idstr,
                                 obj_id=objective_id)
        try:
            result = self._put_request(url_path, ids_arg)
        except Exception:
            raise
        id_list = list()
        for identifier in result['ids']:
            id_list.append(Id(idstr=identifier))
        return id_objects.IdList(id_list)

    def remove_child_objectives(self, objective_id=None):
        """Removes all children from an objective.

        arg:    objective_id (osid.id.Id): the Id of an objective
        raise:  NotFound - objective_id not found
        raise:  NullArgument - objective_id is null
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method must be implemented.

        """
        if objective_id is None:
            raise NullArgument()
        ols = ObjectiveLookupSession(self._objective_bank_id, runtime=self._runtime)
        try:
            ols.get_objective(objective_id)
        except:
            raise  # If no objective, get_objectives will raise NotFound
        ids_arg = {'ids': []}
        url_path = construct_url('childids',
                                 bank_id=self._catalog_idstr,
                                 obj_id=objective_id)
        try:
            result = self._put_request(url_path, ids_arg)
        except Exception:
            raise
        id_list = list()
        for identifier in result['ids']:
            id_list.append(Id(idstr=identifier))
        return id_objects.IdList(id_list)

    def add_child_objectives(self, objective_id=None, child_ids=None):
        """Adds children in bulk to an objective.
        NON-standard method, added by cjshaw

        arg:    objective_id (osid.id.Id): the Id of an objective
        raise:  NotFound - objective_id not found
        raise:  NullArgument - objective_id is null
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method must be implemented.

        """
        if objective_id is None or child_ids is None:
            raise NullArgument()
        ols = ObjectiveLookupSession(self._objective_bank_id, runtime=self._runtime)
        try:
            ols.get_objective(objective_id)
        except:
            raise  # If no objective, get_objectives will raise NotFound
        ids_arg = {'ids': [str(i) for i in child_ids]}
        url_path = construct_url('childids',
                                 bank_id=self._catalog_idstr,
                                 obj_id=objective_id)
        try:
            result = self._put_request(url_path, ids_arg)
        except Exception:
            raise
        id_list = list()
        for identifier in result['ids']:
            id_list.append(Id(idstr=identifier))
        return id_objects.IdList(id_list)


class ObjectiveSequencingSession(abc_learning_sessions.ObjectiveSequencingSession, osid_sessions.OsidSession):
    """This session provides methods to sequence the objectives in the
    objective hierarchy."""
    def __init__(self, objective_bank_id=None, proxy=None, runtime=None, **kwargs):
        self._service_string = SERVICE_STRING
        self._catalogs_string = CATALOGS_STRING
        osid_sessions.OsidSession.__init__(self)
        osid_sessions.OsidSession._init_catalog(
            self,
            proxy,
            runtime
        )
        self._objective_view = COMPARATIVE
        self._objective_bank_view = FEDERATED
        if objective_bank_id is None:
            # For now we are just going to find the first objective bank
            # This needs to change!
            url_path = construct_url('objective_banks')
            objective_bank = objects.ObjectiveBank(self._get_request(url_path)[0])
            self._objective_bank_id = objective_bank.get_id()
        else:
            self._objective_bank_id = objective_bank_id
        self._catalog_idstr = str(self._objective_bank_id)
        self._kwargs = kwargs

    def get_objective_hierarchy_id(self):
        """Gets the hierarchy Id associated with this session.

        return: (osid.id.Id) - the hierarchy Id associated with this
                session
        compliance: mandatory - This method must be implemented.

        """
        return self._objective_bank_id

    def get_objective_hierarchy(self):
        """Gets the hierarchy associated with this session.

        return: (osid.hierarchy.Hierarchy) - the hierarchy associated
                with this session
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method must be implemented.

        """
        # OK, No. This isn't returning a Hierarchy
        return ObjectiveBankLookupSession().get_objective_bank(self._objective_bank_id)

    def can_sequence_objectives(self):
        """Tests if this user can sequence objectives.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known performing any update
        will result in a PermissionDenied. This is intended as a hint to
        an application that may opt not to offer these operations to an
        unauthorized user.

        return: (boolean) - false if sequencing objectives is not
                authorized, true otherwise
        compliance: mandatory - This method must be implemented.

        """
        url_path = construct_url('authorization',
                                 bank_id=self._catalog_idstr)
        return self._get_request(url_path)['objectiveHierarchyHints']['canModifyHierarchy']

    def move_objective_ahead(self, parent_objective_id=None, reference_objective_id=None, objective_id=None):
        """Moves an objective ahead of a refrence objective under the given
        parent.

        arg:    parent_objective_id (osid.id.Id): the Id of the parent
                objective
        arg:    reference_objective_id (osid.id.Id): the Id of the
                objective
        arg:    objective_id (osid.id.Id): the Id of the objective to
                move ahead of reference_objective_id
        raise:  NotFound - parent_objective_id, reference_objective_id,
                or objective_id not found, or reference_objective_id or
                objective_id is not a child of parent_objective_id
        raise:  NullArgument - parent_objective_id,
                reference_objective_id, or id is null
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method must be implemented.

        """
        # NOT YET TESTED:
        if (parent_objective_id is None or
                reference_objective_id is None or
                objective_id is None):
            raise NullArgument()
        ohs = ObjectiveHierarchySession(self._objective_bank_id, runtime=self._runtime)
        if (not ohs.is_child_of_objective(objective_id, parent_objective_id) or
                not ohs.is_child_of_objective(reference_objective_id, parent_objective_id)):
            raise NotFound('The parent objective identified is not the parent of one or both of the other objectives')
        ids_arg = {'ids': []}
        for ident in ohs.get_child_objective_ids(parent_objective_id):
            ids_arg['ids'].append(str(ident))
        if objective_id != reference_objective_id:
            ids_arg['ids'].remove(str(objective_id))
            index = ids_arg['ids'].index(str(reference_objective_id))
            ids_arg['ids'].insert(index, str(objective_id))

        url_path = construct_url('childids',
                                 bank_id=self._catalog_idstr,
                                 obj_id=parent_objective_id)
        try:
            result = self._put_request(url_path, ids_arg)
        except Exception:
            raise

        # The following is not required by the osid specification:
        id_list = list()
        for identifier in result['ids']:
            id_list.append(Id(idstr=identifier))
        return id_objects.IdList(id_list)

    def move_objective_behind(self, parent_objective_id=None, reference_objective_id=None, objective_id=None):
        """Moves an objective behind a refrence objective under the given
        parent.

        arg:    parent_objective_id (osid.id.Id): the Id of the parent
                objective
        arg:    reference_objective_id (osid.id.Id): the Id of the
                objective
        arg:    objective_id (osid.id.Id): the Id of the objective to
                move behind reference_objective_id
        raise:  NotFound - parent_objective_id, reference_objective_id,
                or objective_id not found, or reference_objective_id or
                objective_id is not a child of parent_objective_id
        raise:  NullArgument - parent_objective_id,
                reference_objective_id, or id is null
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method must be implemented.

        """
        # NOT YET TESTED:
        if (parent_objective_id is None or
                reference_objective_id is None or
                objective_id is None):
            raise NullArgument()
        ohs = ObjectiveHierarchySession(self._objective_bank_id, runtime=self._runtime)
        if (not ohs.is_child_of_objective(objective_id, parent_objective_id) or
                not ohs.is_child_of_objective(reference_objective_id, parent_objective_id)):
            raise NotFound('The parent objective identified is not the parent of one or both of the other objectives')
        ids_arg = {'ids': []}
        for ident in ohs.get_child_objective_ids(parent_objective_id):
            ids_arg['ids'].append(str(ident))
        if objective_id != reference_objective_id:
            ids_arg['ids'].remove(str(objective_id))
            index = ids_arg['ids'].index(str(reference_objective_id))
            ids_arg['ids'].insert(index + 1, str(objective_id))

        url_path = construct_url('childids',
                                 bank_id=self._catalog_idstr,
                                 obj_id=parent_objective_id)
        try:
            result = self._put_request(url_path, ids_arg)
        except Exception:
            raise

        # The following is not required by the osid specification:
        id_list = list()
        for identifier in result['ids']:
            id_list.append(Id(idstr=identifier))
        return id_objects.IdList(id_list)

    def sequence_objectives(self, parent_objective_id=None, objective_ids=None):
        """Sequences a set of objectives under a parent.

        arg:    parent_objective_id (osid.id.Id): the Id of the parent
                objective
        arg:    objective_ids (osid.id.Id[]): the Id of the objectives
        raise:  NotFound - parent_id or an objective_id not found, or an
                objective_id is not a child of parent_objective_id
        raise:  NullArgument - parent_objective_id or objective_ids is
                null
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method must be implemented.

        """
        raise Unimplemented()


class ObjectiveRequisiteSession(abc_learning_sessions.ObjectiveRequisiteSession, osid_sessions.OsidSession):
    """This session provides methods for retrieving objective requisites.

    A requisite is a set of Objectives that should be achieved before
    another Objective is attempted.

    This session defines views that offer differing behaviors when
    retrieving multiple objects.

      > comparative view: elements may be silently omitted or re-ordered
      > plenary view: provides a complete set or is an error condition
      > isolated objective bank view: All objective methods in this
        session operate, retrieve and pertain to objectives defined
        explicitly in the current objective bank. Using an isolated view
        is useful for managing objectives with the
        ObjectiveAdminSession.
      > federated objective bank view: All objective methods in this
        session operate, retrieve and pertain to all objectives defined
        in this objective bank and any other objective banks implicitly
        available in this objective bank through objective bank
        inheritence.


    Objectives may have an additional records indicated by their
    respective record types. The record may not be accessed through a
    cast of the Objective.

    """
    def __init__(self, objective_bank_id=None, proxy=None, runtime=None, **kwargs):
        self._service_string = SERVICE_STRING
        self._catalogs_string = CATALOGS_STRING
        osid_sessions.OsidSession.__init__(self)
        osid_sessions.OsidSession._init_catalog(
            self,
            proxy,
            runtime
        )
        self._objective_view = COMPARATIVE
        self._objective_bank_view = FEDERATED
        if objective_bank_id is None:
            # For now we are just going to find the first objective bank
            # This needs to change!
            url_path = construct_url('objective_banks')
            objective_bank = objects.ObjectiveBank(self._get_request(url_path)[0])
            self._objective_bank_id = objective_bank.get_id()
        else:
            self._objective_bank_id = objective_bank_id
        self._catalog_idstr = str(self._objective_bank_id)
        self._kwargs = kwargs

    def get_objective_bank_id(self):
        """Gets the ObjectiveBank  Id associated with this session.

        return: (osid.id.Id) - the ObjectiveBank Id associated with this
                session
        compliance: mandatory - This method must be implemented.

        """
        return self._objective_bank_id

    def get_objective_bank(self):
        """Gets the ObjectiveBank associated with this session.

        return: (osid.learning.ObjectiveBank) - the ObjectiveBank
                associated with this session
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method must be implemented.

        """
        return ObjectiveBankLookupSession().get_objective_bank(self._objective_bank_id)

    def can_lookup_objective_prerequisites(self):
        """Tests if this user can perform Objective lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a PermissionDenied. This is intended as a
        hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        return: (boolean) - false if lookup methods are not authorized,
                true otherwise
        compliance: mandatory - This method must be implemented.

        """
        url_path = construct_url('authorization',
                                 bank_id=self._catalog_idstr)
        return self._get_request(url_path)['objectiveRequisiteHints']['canLookup']

    def use_comparative_objective_view(self):
        """The returns from the lookup methods may omit or translate
        elements based on this session, such as authorization, and not
        result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        compliance: mandatory - This method is must be implemented.

        """
        self._objective_view = COMPARATIVE

    def use_plenary_objective_view(self):
        """A complete view of the Objective returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        compliance: mandatory - This method is must be implemented.

        """
        self._objective_view = PLENARY

    def use_federated_objective_bank_view(self):
        """Federates the view for methods in this session.

        A federated view will include objectives in objective banks
        which are children of this objective bank in the objective bank
        hierarchy.

        compliance: mandatory - This method is must be implemented.

        """
        self._catalog_view = FEDERATED

    def use_isolated_objective_bank_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts lookups to this objective bank only.

        compliance: mandatory - This method is must be implemented.

        """
        self._catalog_view = ISOLATED

    def get_requisite_objectives(self, objective_id=None):
        """Gets a list of Objectives that are the immediate requisites for
        the given Objective.

        In plenary mode, the returned list contains all of the immediate
        requisites, or an error results if an Objective is not found or
        inaccessible. Otherwise, inaccessible Objectives may be omitted
        from the list and may present the elements in any order
        including returning a unique set.

        arg:    objective_id (osid.id.Id): Id of the Objective
        return: (osid.learning.ObjectiveList) - the returned requisite
                Objectives
        raise:  NotFound - objective_id not found
        raise:  NullArgument - objective_id is null
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method is must be implemented.

        """
        if objective_id is None:
            raise NullArgument()
        url_path = construct_url('requisites',
                                 bank_id=self._catalog_idstr,
                                 obj_id=objective_id)
        return objects.ObjectiveList(self._get_request(url_path))

    def _get_requisites_recursively(self, objective_id, requisites, requisite_ids):
        for requisite in self.get_requisite_objectives(objective_id):
            if requisite.get_id() not in requisite_ids:
                requisites.append(requisite)
                requisite_ids.append(requisite.get_id())
                self._get_requisites_recursively(requisite.get_id(), requisites, requisite_ids)
        return requisites

    def get_all_requisite_objectives(self, objective_id=None):
        """Gets a list of Objectives that are the requisites for the given
        Objective including the requistes of the requisites, and so on.

        In plenary mode, the returned list contains all of the immediate
        requisites, or an error results if an Objective is not found or
        inaccessible. Otherwise, inaccessible Objectives may be omitted
        from the list and may present the elements in any order
        including returning a unique set.

        arg:    objective_id (osid.id.Id): Id of the Objective
        return: (osid.learning.ObjectiveList) - the returned Objective
                list
        raise:  NotFound - objective_id not found
        raise:  NullArgument - objective_id is null
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method must be implemented.

        """
        # This should be re-implemented if and when handcar supports
        # getting all requisites directly
        requisites = list()
        requisite_ids = list()
        all_requisites = self._get_requisites_recursively(objective_id, requisites, requisite_ids)
        return objects.ObjectiveList(all_requisites)

    def get_dependent_objectives(self, objective_id=None):
        """Gets a list of Objectives that require the given Objective.

        In plenary mode, the returned list contains all of the immediate
        requisites, or an error results if an Objective is not found or
        inaccessible. Otherwise, inaccessible Objectives may be omitted
        from the list and may present the elements in any order
        including returning a unique set.

        arg:    objective_id (osid.id.Id): Id of the Objective
        return: (osid.learning.ObjectiveList) - the returned Objective
                list
        raise:  NotFound - objective_id not found
        raise:  NullArgument - objective_id is null
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method must be implemented.

        """
        if objective_id is None:
            raise NullArgument()
        url_path = construct_url('dependents',
                                 bank_id=self._catalog_idstr,
                                 obj_id=objective_id)
        return objects.ObjectiveList(self._get_request(url_path))

    def is_objective_required(self, objective_id=None, required_objective_id=None):
        """Tests if an objective is required before proceeding with an
        objective.

        arg:    objective_id (osid.id.Id): Id of the dependent Objective
        arg:    required_objective_id (osid.id.Id): Id of the required
                Objective
        return: (boolean) - true if objective_id depends on
                required_objective_id, false otherwise
        raise:  NotFound - objective_id not found
        raise:  NullArgument - objective_id is null
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method must be implemented.

        """
        if objective_id is None or required_objective_id is None:
            raise NullArgument()
        requisite_objective_ids = list()
        for requisite in self.get_all_requisite_objectives(objective_id):
            requisite_objective_ids.append(requisite.get_id())
        return required_objective_id in requisite_objective_ids

    def get_equivalent_objectives(self, objective_id=None):
        """Gets a list of Objectives that are equivalent to the given
        Objective for the purpose of requisites.

        An equivalent objective can satisfy the given objective. In
        plenary mode, the returned list contains all of the equivalent
        requisites, or an error results if an Objective is not found or
        inaccessible. Otherwise, inaccessible Objectives may be omitted
        from the list and may present the elements in any order
        including returning a unique set.

        arg:    objective_id (osid.id.Id): Id of the Objective
        return: (osid.learning.ObjectiveList) - the returned Objective
                list
        raise:  NotFound - objective_id not found
        raise:  NullArgument - objective_id is null
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method must be implemented.

        """
        if objective_id is None:
            raise NullArgument()
        url_path = construct_url('equivalents',
                                 bank_id=self._catalog_idstr,
                                 obj_id=objective_id)
        return objects.ObjectiveList(self._get_request(url_path))


class ObjectiveRequisiteAssignmentSession(abc_learning_sessions.ObjectiveRequisiteAssignmentSession, osid_sessions.OsidSession):
    """This session provides methods to manage requisites.

    Each ObjectiveBank may have its own authorizations governing who is
    allowed to operate on it.

    Moving or adding a reference of an Objective to another
    ObjectiveBank is not a copy operation (eg: does not change its Id ).

    """
    def __init__(self, objective_bank_id=None, proxy=None, runtime=None, **kwargs):
        self._service_string = SERVICE_STRING
        self._catalogs_string = CATALOGS_STRING
        osid_sessions.OsidSession.__init__(self)
        osid_sessions.OsidSession._init_catalog(
            self,
            proxy,
            runtime
        )
        self._objective_view = COMPARATIVE
        self._objective_bank_view = FEDERATED
        if objective_bank_id is None:
            # For now we are just going to find the first objective bank
            # This needs to change!
            url_path = construct_url('objective_banks')
            objective_bank = objects.ObjectiveBank(self._get_request(url_path)[0])
            self._objective_bank_id = objective_bank.get_id()
        else:
            self._objective_bank_id = objective_bank_id
        self._catalog_idstr = str(self._objective_bank_id)
        self._kwargs = kwargs

    def get_objective_bank_id(self):
        """Gets the ObjectiveBank  Id associated with this session.

        return: (osid.id.Id) - the ObjectiveBank Id associated with this
                session
        compliance: mandatory - This method must be implemented.

        """
        return self._objective_bank_id

    def get_objective_bank(self):
        """Gets the ObjectiveBank associated with this session.

        return: (osid.learning.ObjectiveBank) - the ObjectiveBank
                associated with this session
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method must be implemented.

        """
        return ObjectiveBankLookupSession().get_objective_bank(self._objective_bank_id)

    def can_assign_requisites(self):
        """Tests if this user can manage objective requisites.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a PermissionDenied. This is intended
        as a hint to an application that may opt not to offer assignment
        operations to unauthorized users.

        return: (boolean) - false if mapping is not authorized, true
                otherwise
        compliance: mandatory - This method must be implemented.

        """
        url_path = construct_url('authorization',
                                 bank_id=self._catalog_idstr)
        return self._get_request(url_path)['objectiveRequisiteHints']['canAssign']

    def assign_objective_requisite(self, objective_id=None, requisite_objective_id=None):
        """Creates a requirement dependency between two Objectives.

        arg:    objective_id (osid.id.Id): the Id of the dependent
                Objective
        arg:    requisite_objective_id (osid.id.Id): the Id of the
                required Objective
        raise:  AlreadyExists - objective_id already mapped to
                requisite_objective_id
        raise:  NotFound - objective_id or requisite_objective_id not
                found
        raise:  NullArgument - objective_id or requisite_objective_id is
                null
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method must be implemented.

        """
        if objective_id is None or requisite_objective_id is None:
            raise NullArgument()
        ors = ObjectiveRequisiteSession(self._objective_bank_id, runtime=self._runtime)
        ids_arg = {'ids': []}
        for objective in ors.get_requisite_objectives(objective_id):
            if objective.get_id() == requisite_objective_id:
                raise AlreadyExists()
            ids_arg['ids'].append(str(objective.get_id()))
        ids_arg['ids'].append(str(requisite_objective_id))

        url_path = construct_url('requisiteids',
                                 bank_id=self._catalog_idstr,
                                 obj_id=objective_id)
        try:
            result = self._put_request(url_path, ids_arg)
        except Exception:
            raise
        id_list = list()
        for identifier in result['ids']:
            id_list.append(Id(idstr=identifier))
        return id_objects.IdList(id_list)

    def assign_objective_requisites(self, objective_id=None, requisite_objective_ids=None):
        """Creates a requirement dependency between Objective + a list of objectives.
        NON-standard method impl by cjshaw

        arg:    objective_id (osid.id.Id): the Id of the dependent
                Objective
        arg:    requisite_objective_id (osid.id.Id): the Id of the
                required Objective
        raise:  AlreadyExists - objective_id already mapped to
                requisite_objective_id
        raise:  NotFound - objective_id or requisite_objective_id not
                found
        raise:  NullArgument - objective_id or requisite_objective_id is
                null
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method must be implemented.

        """
        if objective_id is None or requisite_objective_ids is None:
            raise NullArgument()
        ors = ObjectiveRequisiteSession(self._objective_bank_id, runtime=self._runtime)
        ids_arg = {'ids': [str(i) for i in requisite_objective_ids]}

        url_path = construct_url('requisiteids',
                                 bank_id=self._catalog_idstr,
                                 obj_id=objective_id)
        try:
            result = self._put_request(url_path, ids_arg)
        except Exception:
            raise
        id_list = list()
        for identifier in result['ids']:
            id_list.append(Id(idstr=identifier))
        return id_objects.IdList(id_list)

    def unassign_objective_requisite(self, objective_id=None, requisite_objective_id=None):
        """Removes an Objective requisite from an Objective.

        arg:    objective_id (osid.id.Id): the Id of the Objective
        arg:    requisite_objective_id (osid.id.Id): the Id of the
                required Objective
        raise:  NotFound - objective_id or requisite_objective_id not
                found or objective_id not mapped to
                requisite_objective_id
        raise:  NullArgument - objective_id or requisite_objective_id is
                null
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method must be implemented.

        """
        if objective_id is None or requisite_objective_id is None:
            raise NullArgument()
        ors = ObjectiveRequisiteSession(self._objective_bank_id, runtime=self._runtime)
        ids_arg = {'ids': []}
        for objective in ors.get_requisite_objectives(objective_id):
            ids_arg['ids'].append(str(objective.get_id()))
        if str(requisite_objective_id) not in ids_arg['ids']:
            raise NotFound()
        ids_arg['ids'].remove(str(requisite_objective_id))

        url_path = construct_url('requisiteids',
                                 bank_id=self._catalog_idstr,
                                 obj_id=objective_id)
        try:
            result = self._put_request(url_path, ids_arg)
        except Exception:
            raise
        id_list = list()
        for identifier in result['ids']:
            id_list.append(Id(idstr=identifier))
        return id_objects.IdList(id_list)

    def unassign_objective_requisites(self, objective_id=None):
        """Removes all Objective requisites from an Objective.
        NON-standard method impl by cjshaw

        arg:    objective_id (osid.id.Id): the Id of the Objective
        arg:    requisite_objective_id (osid.id.Id): the Id of the
                required Objective
        raise:  NotFound - objective_id or requisite_objective_id not
                found or objective_id not mapped to
                requisite_objective_id
        raise:  NullArgument - objective_id or requisite_objective_id is
                null
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method must be implemented.

        """
        if objective_id is None:
            raise NullArgument()
        ors = ObjectiveRequisiteSession(self._objective_bank_id, runtime=self._runtime)
        ids_arg = {'ids': []}
        url_path = construct_url('requisiteids',
                                 bank_id=self._catalog_idstr,
                                 obj_id=objective_id)
        try:
            result = self._put_request(url_path, ids_arg)
        except Exception:
            raise
        id_list = list()
        for identifier in result['ids']:
            id_list.append(Id(idstr=identifier))
        return id_objects.IdList(id_list)

    def assign_equivalent_objective(self, objective_id=None, equivalent_objective_id=None):
        """Makes an objective equivalent to another objective for the
        purposes of satisfying a requisite.

        arg:    objective_id (osid.id.Id): the Id of the principal
                Objective
        arg:    equivalent_objective_id (osid.id.Id): the Id of the
                equivalent Objective
        raise:  AlreadyExists - objective_id already mapped to
                equiavelnt_objective_id
        raise:  NotFound - objective_id or equivalent_objective_id not
                found
        raise:  NullArgument - objective_id or equivalent_objective_id
                is null
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method must be implemented.

        """
        raise Unimplemented()

    def unassign_equivalent_objective(self, objective_id=None, equivalent_objective_id=None):
        """Removes an Objective requisite from an Objective.

        arg:    objective_id (osid.id.Id): the Id of the principal
                Objective
        arg:    equivalent_objective_id (osid.id.Id): the Id of the
                equivalent Objective
        raise:  NotFound - objective_id or equivalent_objective_id not
                found or objective_id is already equivalent to
                equivalent_objective_id
        raise:  NullArgument - objective_id or equivalent_objective_id
                is null
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method must be implemented.

        """
        raise Unimplemented()


class ActivityLookupSession(abc_learning_sessions.ActivityLookupSession, osid_sessions.OsidSession):
    """This session provides methods for retrieving Activity objects.

    The Activity represents something to perform in order to achieve a
    learning objective.

    This session defines views that offer differing behaviors when
    retrieving multiple objects.
      > comparative view: elements may be silently omitted or re-ordered
      > plenary view: provides a complete set or is an error condition
      > isolated objective bank view: All activity methods in this
        session operate, retrieve and pertain to activities defined
        explicitly in the current objective bank. Using an isolated view
        is useful for managing activities with the ActivityAdminSession.
      > federated objective bank view: All activity methods in this
        session operate, retrieve and pertain to all activities defined
        in this objective bank and any other objective banks implicitly
        available in this objective bank through objective bank
        inheritence.


    Activities may have an additional records indicated by their
    respective record types. The record may not be accessed through a
    cast of the Activity.

    """
    def __init__(self, objective_bank_id=None, proxy=None, runtime=None, **kwargs):
        self._service_string = SERVICE_STRING
        self._catalogs_string = CATALOGS_STRING
        osid_sessions.OsidSession.__init__(self)
        osid_sessions.OsidSession._init_catalog(
            self,
            proxy,
            runtime
        )
        self._activity_view = COMPARATIVE
        self._objective_bank_view = FEDERATED
        if objective_bank_id is None:
            # For now we are just going to find the first objective bank
            # This needs to change!
            url_path = construct_url('objective_banks')
            objective_bank = objects.ObjectiveBank(self._get_request(url_path)[0])
            self._objective_bank_id = objective_bank.get_id()
        else:
            self._objective_bank_id = objective_bank_id
        self._catalog_idstr = str(self._objective_bank_id)
        self._kwargs = kwargs

    def get_objective_bank_id(self):
        """Gets the ObjectiveBank  Id associated with this session.

        return: (osid.id.Id) - the ObjectiveBank Id associated with this
                session
        compliance: mandatory - This method must be implemented.

        """
        return self._objective_bank_id

    def get_objective_bank(self):
        """Gets the ObjectiveBank associated with this session.

        return: (osid.learning.ObjectiveBank) - the ObjectiveBank
                associated with this session
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method must be implemented.

        """
        url_path = construct_url('objective_banks',
                                 bank_id=self._objective_bank_id)
        return objects.ObjectiveBank(self._get_request(url_path))

    def can_lookup_activities(self):
        """Tests if this user can perform Activity lookups.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a PermissionDenied. This is intended as
        a hint to an application that may opt not to offer lookup
        operations to unauthorized users.
        return: (boolean) - false if lookup methods are not authorized,
                true otherwise
        compliance: mandatory - This method must be implemented.

        """
        url_path = construct_url('authorization',
                                 bank_id=self._catalog_idstr)
        return self._get_request(url_path)['activityHints']['canLookup']

    def use_comparative_activity_view(self):
        """The returns from the lookup methods may omit or translate
        elements based on this session, such as authorization, and not
        result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.
        compliance: mandatory - This method is must be implemented.

        """
        self._activity_view = COMPARATIVE

    def use_plenary_activity_view(self):
        """A complete view of the Activity returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.
        compliance: mandatory - This method is must be implemented.

        """
        self._activity_view = PLENARY

    def use_federated_objective_bank_view(self):
        """Federates the view for methods in this session.
        A federated view will include activities in objective banks
        which are children of this objective bank in the objective bank
        hierarchy.
        compliance: mandatory - This method is must be implemented.

        """
        self._objective_bank_view = FEDERATED

    def use_isolated_objective_bank_view(self):
        """Isolates the view for methods in this session.
        An isolated view restricts lookups to this objective bank only.
        compliance: mandatory - This method is must be implemented.

        """
        self._objective_bank_view = ISOLATED

    def get_activity(self, activity_id=None):
        """Gets the Activity specified by its Id.
        In plenary mode, the exact Id is found or a NotFound results.
        Otherwise, the returned Activity may have a different Id than
        requested, such as the case where a duplicate Id was assigned to
        a Activity and retained for compatibility.
        arg:    activityId (osid.id.Id): Id of the Activity
        return: (osid.learning.Activity) - the activity
        raise:  NotFound - activityId not found
        raise:  NullArgument - activityId is null
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method is must be implemented.

        """
        if activity_id is None:
            raise NullArgument()
        url_path = construct_url('activities',
                                 bank_id=self._catalog_idstr,
                                 act_id=activity_id)
        return objects.Activity(self._get_request(url_path))

    def get_activities_by_ids(self, activity_ids=None):
        """Gets an ActivityList corresponding to the given IdList.
        In plenary mode, the returned list contains all of the
        activities specified in the Id list, in the order of the list,
        including duplicates, or an error results if an Id in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible Activities may be omitted from the list and may
        present the elements in any order including returning a unique
        set.
        arg:    activityIds (osid.id.IdList): the list of Ids to
                retrieve
        return: (osid.learning.ActivityList) - the returned Activity
                list
        raise:  NotFound - an Id was not found
        raise:  NullArgument - activityIds is null
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method must be implemented.

        """
        if activity_ids is None:
            raise NullArgument()
        activities = []
        for i in activity_ids:
            activity = None
            url_path = construct_url('activities',
                                     bank_id=self._catalog_idstr,
                                     act_id=i)
            try:
                activity = self._get_request(url_path)
            except (NotFound, OperationFailed):
                if self._activity_view == PLENARY:
                    raise
                else:
                    pass
            if activity:
                if not (self._activity_view == COMPARATIVE and
                        activity in activities):
                    activities.append(activity)
        return objects.ActivityList(activities)

    def get_activities_by_genus_type(self, activity_genus_type=None):
        """Gets an ActivityList corresponding to the given activity genus
        Type which does not include activities of genus types derived
        from the specified Type.
        In plenary mode, the returned list contains all known activities
        or an error results. Otherwise, the returned list may contain
        only those activities that are accessible through this session.
        arg:    activityGenusType (osid.type.Type): an activity genus
                type
        return: (osid.learning.ActivityList) - the returned Activity
                list
        raise:  NullArgument - activityGenusType is null
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method must be implemented.

        """
        if activity_genus_type is None:
            raise NullArgument()
        url_path = construct_url('activities_by_genus',
                                 bank_id=self._catalog_idstr,
                                 genus_type=activity_genus_type.get_identifier())
        return objects.ActivityList(self._get_request(url_path))

    def get_activities_by_parent_genus_type(self, activity_genus_type=None):
        """Gets an ActivityList corresponding to the given activity genus
        Type and include any additional activity with genus types
        derived from the specified Type.
        In plenary mode, the returned list contains all known activities
        or an error results. Otherwise, the returned list may contain
        only those activities that are accessible through this session.
        arg:    activityGenusType (osid.type.Type): an activity genus
                type
        return: (osid.learning.ActivityList) - the returned Activity
                list
        raise:  NullArgument - activityGenusType is null
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method must be implemented.

        """
        raise Unimplemented()

    def get_activities_by_record_type(self, activity_record_type=None):
        """Gets a ActivityList containing the given activity record Type.
        In plenary mode, the returned list contains all known activities
        or an error results. Otherwise, the returned list may contain
        only those activities that are accessible through this session.
        arg:    activityRecordType (osid.type.Type): an activity record
                type
        return: (osid.learning.ActivityList) - the returned Activity
                list
        raise:  NullArgument - activityRecordType is null
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method must be implemented.

        """
        raise Unimplemented()

    def get_activities_for_objective(self, objective_id=None):
        """Gets the activities for the given objective.
        In plenary mode, the returned list contains all of the
        activities mapped to the objective Id or an error results if an
        Id in the supplied list is not found or inaccessible. Otherwise,
        inaccessible Activities may be omitted from the list and may
        present the elements in any order including returning a unique
        set.
        arg:    objectiveId (osid.id.Id): Id of the Objective
        return: (osid.learning.ActivityList) - list of enrollments
        raise:  NotFound - objectiveId not found
        raise:  NullArgument - objectiveId is null
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method is must be implemented.

        """
        if objective_id is None:
            raise NullArgument()
        # Should also check if objective_id exists?
        url_path = construct_url('activities',
                                 bank_id=self._catalog_idstr,
                                 obj_id=objective_id)
        return objects.ActivityList(self._get_request(url_path))

    def get_activities_for_objectives(self, objective_ids=None):
        """Gets the activities for the given objectives.
        In plenary mode, the returned list contains all of the
        activities specified in the objective Id list, in the order of
        the list, including duplicates, or an error results if a course
        offering Id in the supplied list is not found or inaccessible.
        Otherwise, inaccessible Activities may be omitted from the list
        and may present the elements in any order including returning a
        unique set.
        arg:    objectiveIds (osid.id.IdList): list of objective Ids
        return: (osid.learning.ActivityList) - list of activities
        raise:  NotFound - an objectiveId not found
        raise:  NullArgument - objectiveIdList is null
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method is must be implemented.

        """
        if objective_ids is None:
            raise NullArgument()
        # Should also check if objective_id exists?
        activities = []
        for i in objective_ids:
            acts = None
            url_path = construct_url('activities',
                                     bank_id=self._catalog_idstr,
                                     obj_id=i)
            try:
                acts = json.loads(self._get_request(url_path))
            except (NotFound, OperationFailed):
                if self._activity_view == PLENARY:
                    raise
                else:
                    pass
            if acts:
                activities += acts
        return objects.ActivityList(activities)

    def get_activities_by_asset(self, asset_id=None):
        """Gets the activities for the given asset.
        In plenary mode, the returned list contains all of the
        activities mapped to the asset Id or an error results if an Id
        in the supplied list is not found or inaccessible. Otherwise,
        inaccessible Activities may be omitted from the list and may
        present the elements in any order including returning a unique
        set.
        arg:    assetId (osid.id.Id): Id of an Asset
        return: (osid.learning.ActivityList) - list of activities
        raise:  NotFound - assetId not found
        raise:  NullArgument - assetId is null
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method is must be implemented.

        """
        raise Unimplemented()

    def get_activities_by_assets(self, asset_ids=None):
        """Gets the activities for the given asset.
        In plenary mode, the returned list contains all of the
        activities mapped to the asset Id or an error results if an Id
        in the supplied list is not found or inaccessible. Otherwise,
        inaccessible Activities may be omitted from the list and may
        present the elements in any order including returning a unique
        set.
        arg:    assetIds (osid.id.IdList): Ids of Assets
        return: (osid.learning.ActivityList) - list of activities
        raise:  NotFound - an assetId not found
        raise:  NullArgument - assetIdList is null
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method is must be implemented.

        """
        raise Unimplemented()

    def get_activities(self):
        """Gets all Activities.
        In plenary mode, the returned list contains all known activites
        or an error results. Otherwise, the returned list may contain
        only those activities that are accessible through this session.
        return: (osid.learning.ActivityList) - a ActivityList
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method must be implemented.

        """
        url_path = construct_url('activities',
                                 bank_id=self._catalog_idstr)
        return objects.ActivityList(self._get_request(url_path))

    objective_bank_id = property(get_objective_bank_id)
    objective_bank = property(get_objective_bank)
    activities = property(get_activities)


class ActivityQuerySession(abc_learning_sessions.ActivityQuerySession, osid_sessions.OsidSession):
    """This session provides methods for searching Activity objects.

    The search query is constructed using the ActivityQuery. The
    activity record Type also specifies the record for the activity
    query.

    This session defines views that offer differing behaviors for
    searching.
      > federated objective bank view: searches include activities in
        objective banks of which this objective bank is a ancestor in
        the objective bank hierarchy
      > isolated objective bank view: searches are restricted to
        activities in this objective bank


    Activities may have a query record indicated by their respective
    record types. The query record is accessed via the ActivityQuery.

    """
    def __init__(self, objective_bank_id, proxy=None, runtime=None, **kwargs):
        self._service_string = SERVICE_STRING
        self._catalogs_string = CATALOGS_STRING
        osid_sessions.OsidSession.__init__(self)
        osid_sessions.OsidSession._init_catalog(
            self,
            proxy,
            runtime
        )
        self._activity_view = COMPARATIVE
        self._objective_bank_view = ISOLATED
        self._objective_bank_id = objective_bank_id
        self._catalog_idstr = str(objective_bank_id)
        self._kwargs = kwargs

    def get_objective_bank_id(self):
        """Gets the ObjectiveBank  Id associated with this session.

        return: (osid.id.Id) - the ObjectiveBank Id associated with this
                session
        compliance: mandatory - This method must be implemented.

        """
        pass

    def get_objective_bank(self):
        """Gets the ObjectiveBank associated with this session.

        return: (osid.learning.ObjectiveBank) - the ObjectiveBank
                associated with this session
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method must be implemented.

        """
        pass

    def can_search_activities(self):
        """Tests if this user can perform Activity searches.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a PermissionDenied. This is intended as
        a hint to an application that may opt not to offer search
        operations to unauthorized users.
        return: (boolean) - false if search methods are not authorized,
                true otherwise
        compliance: mandatory - This method must be implemented.

        """
        pass

    def use_federated_objective_bank_view(self):
        """Federates the view for methods in this session.
        A federated view will include activities in objective banks
        which are children of this objective bank in the objective bank
        hierarchy.
        compliance: mandatory - This method is must be implemented.

        """
        self._objective_bank_view = FEDERATED

    def use_isolated_objective_bank_view(self):
        """Isolates the view for methods in this session.
        An isolated view restricts searches to this objective bank only.
        compliance: mandatory - This method is must be implemented.

        """
        self._objective_bank_view = ISOLATED

    def get_activity_query(self):
        """Gets an activity query.

        return: (osid.learning.ActivityQuery) - the activity query
        compliance: mandatory - This method must be implemented.

        """
        return queries.ActivityQuery()

    def get_activities_by_query(self, activity_query=None):
        """Gets a list of Activities matching the given activity query.

        arg:    activityQuery (osid.learning.ActivityQuery): the
                activity query
        return: (osid.learning.ActivityList) - the returned ActivityList
        raise:  NullArgument - activityQuery is null
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - activityQuery is not of this service
        compliance: mandatory - This method must be implemented.

        """
        url_path = construct_url('activities',
                                 bank_id=self._catalog_idstr)
        query_terms = [v for k, v in activity_query._query_terms.items()]
        url_path += '?' + '&'.join(query_terms)
        objects.ActivityList(self._get_request(url_path))

    objective_bank_id = property(get_objective_bank_id)
    objective_bank = property(get_objective_bank)
    activity_query = property(get_activity_query)


class ActivitySearchSession(abc_learning_sessions.ActivitySearchSession, ActivityQuerySession):
    """This session provides methods for searching Activity objects.

    The search query is constructed using the ActivityQuery. The
    activity record Type also specifies the record for the activity
    query.

    get_activities_by_query() is the basic search method and returns a
    list of Activities. A more advanced search may be performed with
    get_activities_by_search(). It accepts a ActivitySearch in addition
    to the query for the purpose of specifying additional options
    affecting the entire search, such as ordering.
    get_activities_by_search() returns an ActivitySearchResults that can
    be used to access the resulting ActivityList or be used to perform a
    search within the result set through ActivitySearch.

    This session defines views that offer differing behaviors for
    searching.
      > federated objective bank view: searches include activities in
        objective banks of which this objective bank is a ancestor in
        the objective bank hierarchy
      > isolated objective bank view: searches are restricted to
        activities in this objective bank


    Activities may have a query record indicated by their respective
    record types. The query record is accessed via the ActivityQuery.

    """

    def get_activity_search(self):
        """Gets an activity search.

        return: (osid.learning.ActivitySearch) - the activity search
        compliance: mandatory - This method must be implemented.

        """
        pass

    def get_activity_search_order(self):
        """Gets an activity search order.
        The ActivitySearchOrder is supplied to a ActivitySearch to
        specify the ordering of results.
        return: (osid.learning.ActivitySearchOrder) - the activity
                search order
        compliance: mandatory - This method must be implemented.

        """
        pass

    def get_activities_by_search(self, activity_query=None, activitiesearch=None):
        """Gets the search results matching the given search query using
        the given search.

        arg:    activitiesearch (osid.learning.ActivitySearch): the
                activity search
        return: (osid.learning.ActivitySearchResults) - the returned
                search results
        raise:  NullArgument - activityQuery or activitiesearch is null
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - activitiesearch or activityQuery is not of
                this service
        compliance: mandatory - This method must be implemented.

        """
        pass

    def get_activity_query_from_inspector(self, activity_query_inspector=None):
        """Gets an activity query from an inspector.
        The inspector is available from an ActivitySearchResults.
        arg:    activityQueryInspector
                (osid.learning.ActivityQueryInspector): an activity bank
                query inspector
        return: (osid.learning.ActivityQuery) - the activity query
        raise:  NullArgument - activityQueryInspector is null
        raise:  Unsupported - activityQueryInspector is not of this
                service
        compliance: mandatory - This method must be implemented.

        """
        pass

    activity_search = property(get_activity_search)
    activity_search_order = property(get_activity_search_order)


class ActivityAdminSession(abc_learning_sessions.ActivityAdminSession, osid_sessions.OsidSession):
    """This session creates, updates, and deletes Activities.

    The data for create and update is provided by the consumer via the
    form object. OsidForms are requested for each create or update and
    may not be reused.

    Create and update operations differ in their usage. To create an
    Activity, an ActivityForm is requested using
    get_activity_form_for_create() specifying the desired objective and
    record Types or none if no record Types are needed. The returned
    ActivityForm will indicate that it is to be used with a create
    operation and can be used to examine metdata or validate data prior
    to creation. Once the ActivityForm is submiited to a create
    operation, it cannot be reused with another create operation unless
    the first operation was unsuccessful. Each ActivityForm corresponds
    to an attempted transaction.

    For updates, ActivityForms are requested to the Activity  Id that is
    to be updated using get_activity_form_for_update(). Similarly, the
    ActivityForm has metadata about the data that can be updated and it
    can perform validation before submitting the update. The
    ActivityForm can only be used once for a successful update and
    cannot be reused.

    The delete operations delete Activities. To unmap an Activity from
    the current ObjectiveBank, the
    ActivityObjectiveBankAssignmentSession should be used. These delete
    operations attempt to remove the Activity itself thus removing it
    from all known ObjectiveBank catalogs.

    This session includes an Id aliasing mechanism to assign an external
    Id to an internally assigned Id.

    """
    def __init__(self, objective_bank_id=None, proxy=None, runtime=None, **kwargs):
        self._service_string = SERVICE_STRING
        self._catalogs_string = CATALOGS_STRING
        osid_sessions.OsidSession.__init__(self)
        osid_sessions.OsidSession._init_catalog(
            self,
            proxy,
            runtime
        )
        if objective_bank_id is None:
            # For now we are just going to find the first objective bank
            # This needs to change!
            url_path = construct_url('objective_banks')
            objective_bank = objects.ObjectiveBank(self._get_request(url_path)[0])
            self._objective_bank_id = objective_bank.get_id()
        else:
            self._objective_bank_id = objective_bank_id
        self._catalog_idstr = str(self._objective_bank_id)
        self._forms = dict()
        self._kwargs = kwargs

    def get_objective_bank_id(self):
        """Gets the ObjectiveBank  Id associated with this session.

        return: (osid.id.Id) - the ObjectiveBank Id associated with this
                session
        compliance: mandatory - This method must be implemented.

        """
        return self._objective_bank_id

    def get_objective_bank(self):
        """Gets the ObjectiveBank associated with this session.

        return: (osid.learning.ObjectiveBank) - the ObjectiveBank
                associated with this session
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method must be implemented.

        """
        return ObjectiveBankLookupSession().get_objective_bank(self._objective_bank_id)

    def can_create_activities(self):
        """Tests if this user can create Activities.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating an Activity
        will result in a PermissionDenied. This is intended as a hint
        to an application that may opt not to offer create operations to
        an unauthorized user.
        return: (boolean) - false if Activity creation is not
                authorized, true otherwise
        compliance: mandatory - This method must be implemented.

        """
        url_path = construct_url('authorization',
                                 bank_id=self._catalog_idstr)
        return self._get_request(url_path)['activityHints']['canCreate']

    def can_create_activity_with_record_types(self, activity_record_types=None):
        """Tests if this user can create a single Activity using the
        desired record types.
        While learning_manager.get_activity_record_types() can be used
        to examine which records are supported, this method tests which
        record(s) are required for creating a specific Activity.
        Providing an empty array tests if an Activity can be created
        with no records.
        arg:    activityRecordTypes (osid.type.Type): array of activity
                record types
        return: (boolean) - true if Activity creation using the
                specified record Types is supported, false otherwise
        raise:  NullArgument - activityRecordTypes is null
        compliance: mandatory - This method must be implemented.

        """
        return True

    def get_activity_form_for_create(self, objective_id=None, activity_record_types=None):
        """Gets the activity form for creating new activities.
        A new form should be requested for each create transaction.
        arg:    activityRecordTypes (osid.type.Type): array of activity
                record types
        return: (osid.learning.ActivityForm) - the activity form
        raise:  NotFound - objectiveId is not found
        raise:  NullArgument - objectiveId or activityRecordTypes is
                null
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - unable to get form for requested record
                types
        compliance: mandatory - This method must be implemented.

        """
        if objective_id is None:
            raise NullArgument()
        if activity_record_types is None:
            pass  # Still need to deal with the record_types argument
        activity_form = objects.ActivityForm(osid_object_map=None, objective_id=objective_id)
        self._forms[activity_form.get_id().get_identifier()] = not CREATED
        return activity_form

    def create_activity(self, activity_form=None):
        """Creates a new Activity.

        arg:    activityForm (osid.learning.ActivityForm): the form for
                this Activity
        return: (osid.learning.Activity) - the new Activity
        raise:  IllegalState - activityForm already used in a create
                transaction
        raise:  InvalidArgument - one or more of the form elements is
                invalid
        raise:  NullArgument - activityForm is null
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - activityForm did not originate from
                get_activity_form_for_create()
        compliance: mandatory - This method must be implemented.

        """
        if activity_form is None:
            raise NullArgument()
        if not isinstance(activity_form, abc_learning_objects.ActivityForm):
            raise InvalidArgument('argument type is not an ActivityForm')
        if activity_form.is_for_update():
            raise InvalidArgument('form is for update only, not create')
        try:
            if self._forms[activity_form.get_id().get_identifier()] == CREATED:
                raise IllegalState('form already used in a create transaction')
        except KeyError:
            raise Unsupported('form did not originate from this session')
        if not activity_form.is_valid():
            raise InvalidArgument('one or more of the form elements is invalid')
        url_path = construct_url('activities',
                                 bank_id=self._catalog_idstr)
        try:
            result = self._post_request(url_path, activity_form._my_map)
        except Exception:
            raise  # OperationFailed
        self._forms[activity_form.get_id().get_identifier()] = CREATED
        return objects.Activity(result)

    def can_update_activities(self):
        """Tests if this user can update Activities.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating an Activity
        will result in a PermissionDenied. This is intended as a hint
        to an application that may opt not to offer update operations to
        an unauthorized user.
        return: (boolean) - false if activity modification is not
                authorized, true otherwise
        compliance: mandatory - This method must be implemented.

        """
        url_path = construct_url('authorization',
                                 bank_id=self._catalog_idstr)
        return self._get_request(url_path)['activityHints']['canUpdate']

    def get_activity_form_for_update(self, activity_id=None):
        """Gets the activity form for updating an existing activity.
        A new activity form should be requested for each update
        transaction.
        arg:    activityId (osid.id.Id): the Id of the Activity
        return: (osid.learning.ActivityForm) - the activity form
        raise:  NotFound - activityId is not found
        raise:  NullArgument - activityId is null
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method must be implemented.

        """
        if activity_id is None:
            raise NullArgument()
        try:
            url_path = construct_url('activities',
                                     bank_id=self._catalog_idstr,
                                     act_id=activity_id)
            activity = objects.Activity(self._get_request(url_path))
        except Exception:
            raise
        activity_form = objects.ActivityForm(activity._my_map)
        self._forms[activity_form.get_id().get_identifier()] = not UPDATED
        return activity_form

    def update_activity(self, activity_form=None):
        """Updates an existing activity,.

        arg:    activityForm (osid.learning.ActivityForm): the form
                containing the elements to be updated
        raise:  IllegalState - activityForm already used in an update
                transaction
        raise:  InvalidArgument - the form contains an invalid value
        raise:  NullArgument - activityForm is null
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - activityForm did not originate from
                get_activity_form_for_update()
        compliance: mandatory - This method must be implemented.

        """
        if activity_form is None:
            raise NullArgument()
        if not isinstance(activity_form, abc_learning_objects.ActivityForm):
            raise InvalidArgument('argument type is not an ActivityForm')
        if not activity_form.is_for_update():
            raise InvalidArgument('form is for create only, not update')
        try:
            if self._forms[activity_form.get_id().get_identifier()] == UPDATED:
                raise IllegalState('form already used in an update transaction')
        except KeyError:
            raise Unsupported('form did not originate from this session')
        if not activity_form.is_valid():
            raise InvalidArgument('one or more of the form elements is invalid')

        url_path = construct_url('activities',
                                 bank_id=self._catalog_idstr)
        try:
            result = self._put_request(url_path, activity_form._my_map)
        except Exception:
            raise  # OperationFailed
        self._forms[activity_form.get_id().get_identifier()] = UPDATED
        return objects.Activity(result)  # Not expected to return anything

    def can_delete_activities(self):
        """Tests if this user can delete Activities.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting an Activity
        will result in a PermissionDenied. This is intended as a hint
        to an application that may opt not to offer delete operations to
        an unauthorized user.
        return: (boolean) - false if Activity deletion is not
                authorized, true otherwise
        compliance: mandatory - This method must be implemented.

        """
        url_path = construct_url('authorization',
                                 bank_id=self._catalog_idstr)
        return self._get_request(url_path)['activityHints']['canDelete']

    def delete_activity(self, activity_id=None):
        """Deletes the Activity identified by the given Id.

        arg:    activityId (osid.id.Id): the Id of the Activity to
                delete
        raise:  NotFound - an Activity was not found identified by the
                given Id
        raise:  NullArgument - activityId is null
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method must be implemented.

        """
        if activity_id is None:
            raise NullArgument()
        if not isinstance(activity_id, Id):
            raise InvalidArgument('argument type is not an osid Id')

        url_path = construct_url('activities',
                                 bank_id=self._catalog_idstr,
                                 act_id=activity_id)
        result = self._delete_request(url_path)
        return objects.Activity(result)  # Not expected to return anything

    def can_manage_activity_aliases(self):
        """Tests if this user can manage Id aliases for activities.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a PermissionDenied. This is intended as a hint
        to an application that may opt not to offer alias operations to
        an unauthorized user.
        return: (boolean) - false if Activity aliasing is not
                authorized, true otherwise
        compliance: mandatory - This method must be implemented.

        """
        return False  # Not yet implemented

    def alias_activity(self, activity_id=None, alias_id=None):
        """Adds an Id to an Activity for the purpose of creating
        compatibility.
        The primary Id of the Activity is determined by the provider.
        The new Id performs as an alias to the primary Id. If the alias
        is a pointer to another activity, it is reassigned to the given
        activity Id.
        arg:    aliasId (osid.id.Id): the alias Id
        raise:  ALREADY_EXISTS - aliasId is already assigned
        raise:  NotFound - activityId not found
        raise:  NullArgument - activityId or aliasId is null
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method must be implemented.

        """
        raise Unimplemented()

    objective_bank_id = property(get_objective_bank_id)
    objective_bank = property(get_objective_bank)


class ObjectiveBankLookupSession(abc_learning_sessions.ObjectiveBankLookupSession, osid_sessions.OsidSession):
    """This session provides methods for retrieving ObjectiveBank objects.

    The ObjectiveBank represents a collection of Objectives Activities ,
    and Proficiencies.

    This session defines views that offer differing behaviors when
    retrieving multiple objects.
      > comparative view: elements may be silently omitted or re-ordered
      > plenary view: provides a complete set or is an error condition


    Generally, the comparative view should be used for most applications
    as it permits operation even if there is data that cannot be
    accessed. For example, a browsing application may only need to
    examine the ObjectiveBanks it can access, without breaking
    execution. However, an administrative application may require all
    ObjectiveBank elements to be available.

    ObjectiveBanks may have an additional records indicated by their
    respective record types. The record may not be accessed through a
    cast of the ObjectiveBank.

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
        self._objective_bank_view = COMPARATIVE
        self._kwargs = kwargs
        self._default_bank_id = 'mc3-objectivebank%3A1%40MIT-OEIT'

    def can_lookup_objective_banks(self):
        """Tests if this user can perform ObjectiveBank lookups.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a PermissionDenied. This is intended as
        a hint to an application that may opt not to offer lookup
        operations to unauthorized users.
        return: (boolean) - false if lookup methods are not authorized,
                true otherwise
        compliance: mandatory - This method must be implemented.

        """
        # need to use a default bank_id here...not ideal.
        url_path = construct_url('authorization',
                                 bank_id=self._default_bank_id)
        return self._get_request(url_path)['objectiveBankHints']['canLookup']

    def use_comparative_objective_bank_view(self):
        """The returns from the lookup methods may omit or translate
        elements based on this session, such as authorization, and not
        result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.
        compliance: mandatory - This method is must be implemented.

        """
        self.objective_bank_view = COMPARATIVE

    def use_plenary_objective_bank_view(self):
        """A complete view of the ObjectiveBank returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.
        compliance: mandatory - This method is must be implemented.

        """
        self.objective_bank_view = PLENARY

    def get_objective_bank(self, objective_bank_id=None):
        """Gets the ObjectiveBank specified by its Id.
        In plenary mode, the exact Id is found or a NotFound results.
        Otherwise, the returned ObjectiveBank may have a different Id
        than requested, such as the case where a duplicate Id was
        assigned to a ObjectiveBank and retained for compatility.
        arg:    objectiveBankId (osid.id.Id): Id of the ObjectiveBank
        return: (osid.learning.ObjectiveBank) - the objective bank
        raise:  NotFound - objectiveBankId not found
        raise:  NullArgument - objectiveBankId is null
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method is must be implemented.

        """
        if objective_bank_id is None:
            raise NullArgument()
        url_path = construct_url('objective_banks',
                                 bank_id=objective_bank_id)
        return objects.ObjectiveBank(self._get_request(url_path))

    def get_objective_banks_by_ids(self, objective_bank_ids=None):
        """Gets a ObjectiveBankList corresponding to the given IdList.
        In plenary mode, the returned list contains all of the objective
        banks specified in the Id list, in the order of the list,
        including duplicates, or an error results if an Id in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible ObjectiveBank objects may be omitted from the list
        and may present the elements in any order including returning a
        unique set.
        arg:    objectiveBankIds (osid.id.IdList): the list of Ids to
                retrieve
        return: (osid.learning.ObjectiveBankList) - the returned
                ObjectiveBank list
        raise:  NotFound - an Id was not found
        raise:  NullArgument - objectiveBankIds is null
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method must be implemented.

        """
        if objective_bank_ids is None:
            raise NullArgument()
        banks = []
        # The following runs really slow. Perhaps get all banks and then inspect result for ids
        for i in objective_bank_ids:
            bank = None
            url_path = construct_url('objective_banks',
                                     bank_id=i)
            try:
                bank = self._get_request(url_path)
            except (NotFound, OperationFailed):
                if self._objective_bank_view == PLENARY:
                    raise
                else:
                    pass
            if bank:
                if not (self._objective_bank_view == COMPARATIVE and
                        bank in banks):
                    banks.append(bank)
        return objects.ObjectiveBankList(banks)

    def get_objective_banks_by_genus_type(self, objective_bank_genus_type=None):
        """Gets a ObjectiveBankList corresponding to the given objective
        bank genus Type which does not include objective banks of types
        derived from the specified Type.
        In plenary mode, the returned list contains all known objective
        banks or an error results. Otherwise, the returned list may
        contain only those objective banks that are accessible through
        this session.
        arg:    objectiveBankGenusType (osid.type.Type): an objective
                bank genus type
        return: (osid.learning.ObjectiveBankList) - the returned
                ObjectiveBank list
        raise:  NullArgument - objectiveBankGenusType is null
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method must be implemented.

        """
        if objective_bank_genus_type is None:
            raise NullArgument()
        url_path = construct_url('objective_banks_by_genus',
                                 genus_type=objective_bank_genus_type)
        return objects.ObjectiveBankList(self._get_request(url_path))

    def get_objective_banks_by_parent_genus_type(self, objective_bank_genus_type=None):
        """Gets a ObjectiveBankList corresponding to the given objective
        bank genus Type and include any additional objective banks with
        genus types derived from the specified Type.
        In plenary mode, the returned list contains all known objective
        banks or an error results. Otherwise, the returned list may
        contain only those objective banks that are accessible through
        this session.
        arg:    objectiveBankGenusType (osid.type.Type): an objective
                bank genus type
        return: (osid.learning.ObjectiveBankList) - the returned
                ObjectiveBank list
        raise:  NullArgument - objectiveBankGenusType is null
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method must be implemented.

        """
        raise Unimplemented()

    def get_objective_banks_by_record_type(self, objective_bank_record_type=None):
        """Gets a ObjectiveBankList containing the given objective bank
        record Type.
        In plenary mode, the returned list contains all known objective
        banks or an error results. Otherwise, the returned list may
        contain only those objective banks that are accessible through
        this session.
        arg:    objectiveBankRecordType (osid.type.Type): an objective
                bank record type
        return: (osid.learning.ObjectiveBankList) - the returned
                ObjectiveBank list
        raise:  NullArgument - objectiveBankRecordType is null
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method must be implemented.

        """
        raise Unimplemented()

    def get_objective_banks_by_provider(self, resource_id=None):
        """Gets a ObjectiveBankList for the given provider.
        In plenary mode, the returned list contains all known objective
        banks or an error results. Otherwise, the returned list may
        contain only those objective banks that are accessible through
        this session.
        arg:    resourceId (osid.id.Id): a resource Id
        return: (osid.learning.ObjectiveBankList) - the returned
                ObjectiveBank list
        raise:  NullArgument - resourceId is null
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method must be implemented.

        """
        raise Unimplemented()

    def get_objective_banks(self):
        """Gets all ObjectiveBanks.
        In plenary mode, the returned list contains all known objective
        banks or an error results. Otherwise, the returned list may
        contain only those objective banks that are accessible through
        this session.
        return: (osid.learning.ObjectiveBankList) - a ObjectiveBankList
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method must be implemented.

        """
        url_path = construct_url('objective_banks')
        return objects.ObjectiveBankList(self._get_request(url_path))

    objective_banks = property(get_objective_banks)


class ObjectiveBankQuerySession(abc_learning_sessions.ObjectiveBankQuerySession, osid_sessions.OsidSession):
    """This session provides methods for searching among ObjectiveBank
    objects.

    The search query is constructed using the ObjectiveBankQuery.

    ObjectiveBanks may have a query record indicated by their respective
    record types. The query record is accessed via the
    ObjectiveBankQuery.

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

    def can_search_objective_banks(self):
        """Tests if this user can perform ObjectiveBank searches.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a PermissionDenied. This is intended as
        a hint to an application that may opt not to offer search
        operations to unauthorized users.
        return: (boolean) - false if search methods are not authorized,
                true otherwise
        compliance: mandatory - This method must be implemented.

        """
        pass

    def get_objective_bank_query(self):
        """Gets an objective bank query.

        return: (osid.learning.ObjectiveBankQuery) - an objective bank
                query
        compliance: mandatory - This method must be implemented.

        """
        pass

    def get_objective_banks_by_query(self, objective_bank_query=None):
        """Gets a list of ObjectiveBank objects matching the given
        objectiove bank query.

        arg:    objectiveBankQuery (osid.learning.ObjectiveBankQuery):
                the objective bank query
        return: (osid.learning.ObjectiveBankList) - the returned
                ObjectiveBankList
        raise:  NullArgument - objectiveBankQuery is null
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - objectiveBankQuery is not of this service
        compliance: mandatory - This method must be implemented.

        """
        pass

    objective_bank_query = property(get_objective_bank_query)


class ObjectiveBankSearchSession(abc_learning_sessions.ObjectiveBankSearchSession, ObjectiveBankQuerySession):
    """This session provides methods for searching among ObjectiveBank
    objects.

    The search query is constructed using the ObjectiveBankQuery.

    get_objective_banks_by_query() is the basic search method and
    returns a list of ObjectiveBank objects.A more advanced search may
    be performed with get_objective_banks_by_search(). It accepts a
    ObjectiveBankSearch in addition to the query for the purpose of
    specifying additional options affecting the entire search, such as
    ordering. get_objective_banks_by_search() returns a
    ObjectiveBankSearchResults that can be used to access the resulting
    ObjectiveBankList or be used to perform a search within the result
    set through ObjectiveBankSearch.

    ObjectiveBanks may have a query record indicated by their respective
    record types. The query record is accessed via the
    ObjectiveBankQuery.

    """
    def get_objective_bank_search(self):
        """Gets an objective bank search.

        return: (osid.learning.ObjectiveBankSearch) - an objective bank
                search
        compliance: mandatory - This method must be implemented.

        """
        pass

    def get_objective_bank_search_order(self):
        """Gets an objective bank search order.
        The ObjectiveBankSearchOrder is supplied to a
        ObjectiveBankSearch to specify the ordering of results.
        return: (osid.learning.ObjectiveBankSearchOrder) - the objective
                bank search order
        compliance: mandatory - This method must be implemented.

        """
        pass

    def get_objective_banks_by_search(self, objective_bank_query=None, objective_bank_search=None):
        """Gets the search results matching the given search query using
        the given search.

        arg:    objectiveBankSearch (osid.learning.ObjectiveBankSearch):
                the objective bank search
        return: (osid.learning.ObjectiveBankSearchResults) - the search
                results
        raise:  NullArgument - objectiveBankQuery or
                objectiveBankSearch is null
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - objectiveBankQuery or objectiveBankSearch
                is not of this service
        compliance: mandatory - This method must be implemented.

        """
        pass

    def get_objective_bank_query_from_inspector(self, objective_bank_query_inspector=None):
        """Gets an objective bank query from an inspector.
        The inspector is available from an ObjectiveBankSearchResults.
        arg:    objectiveBankQueryInspector
                (osid.learning.ObjectiveBankQueryInspector): an
                objective bank query inspector
        return: (osid.learning.ObjectiveBankQuery) - the objective bank
                query
        raise:  NullArgument - objectiveBankQueryInspector is null
        raise:  Unsupported - objectiveBankQueryInspector is not of this
                service
        compliance: mandatory - This method must be implemented.

        """
        pass

    objective_bank_search = property(get_objective_bank_search)
    objective_bank_search_order = property(get_objective_bank_search_order)


class ObjectiveBankAdminSession(abc_learning_sessions.ObjectiveBankAdminSession, osid_sessions.OsidSession):
    """This session creates, updates, and deletes ObjectiveBanks.

    The data for create and update is provided by the consumer via the
    form object. OsidForms are requested for each create or update and
    may not be reused.

    Create and update operations differ in their usage. To create an
    ObjectiveBank, an ObjectiveBankForm is requested using
    get_objective_bank_form_for_create() specifying the desired record
    Types or none if no record Types are needed. The returned
    ObjectiveBankForm will indicate that it is to be used with a create
    operation and can be used to examine metdata or validate data prior
    to creation. Once the ObjectiveBankForm is submiited to a create
    operation, it cannot be reused with another create operation unless
    the first operation was unsuccessful. Each ObjectiveBankForm
    corresponds to an attempted transaction.

    For updates, ObjectiveBankForms are requested to the ObjectiveBank
    Id that is to be updated using get_objective_bank_form_for_update().
    Similarly, the ObjectiveBankForm has metadata about the data that
    can be updated and it can perform validation before submitting the
    update. The ObjectiveBankForm can only be used once for a successful
    update and cannot be reused.

    The delete operations delete ObjectiveBanks. It is safer to remove
    all mappings to the ObjectiveBank catalogs before deletion.

    This session includes an Id aliasing mechanism to assign an external
    Id to an internally assigned Id.

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
        self._forms = dict()
        self._kwargs = kwargs

    # To support extension records on banks
    def _record_extension(self, bank_id, key, value):
        """
        To structure a record extension property bean
        """
        record_bean = {
            'value': value,
            'displayName': self._text_bean(key),
            'description': self._text_bean(key),
            'displayLabel': self._text_bean(key),
            'associatedId': str(bank_id)
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

    def extension_url(self, bank_id):
        from ..utilities import construct_url
        extension_url = construct_url('extension_record',
                                      bank_id=bank_id)
        return extension_url

    def extensions(self, bank_id):
        extension_url = self.extension_url(bank_id)
        return self._get_request(extension_url)['recordProperties']

    def search_record_extensions(self, item):
        extensions = self.extensions()
        results = []
        for ext in extensions:
            if ext['displayName']['text'] == item:
                results.append(ext['value'])
        return results

    def set_record_extension(self, bank_id, key, value):
        extension_url = self.extension_url(bank_id)
        current_extensions = self.extensions(bank_id)
        current_extensions.append(self._record_extension(bank_id, key, value))
        updated_extensions = {
            'associatedId': str(bank_id),
            'recordProperties': current_extensions
        }
        return self._put_request(extension_url, updated_extensions)
# ==================================

    def can_create_objective_banks(self):
        """Tests if this user can create ObjectiveBanks.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating an
        ObjectiveBank will result in a PermissionDenied. This is
        intended as a hint to an application that may not wish to offer
        create operations to unauthorized users.
        return: (boolean) - false if ObjectiveBank creation is not
                authorized, true otherwise
        compliance: mandatory - This method must be implemented.

        """
        url_path = construct_url('authorization')
        return self._get_request(url_path)['objectiveBankHints']['canCreate']

    def can_create_objective_bank_with_record_types(self, objective_bank_record_types=None):
        """Tests if this user can create a single ObjectiveBank using the
        desired record types.
        While learning_manager.get_objective_bank_record_types() can be
        used to examine which records are supported, this method tests
        which record(s) are required for creating a specific
        ObjectiveBank. Providing an empty array tests if an
        ObjectiveBank can be created with no records.
        arg:    objectiveBankRecordTypes (osid.type.Type): array of
                objective bank record types
        return: (boolean) - true if ObjectiveBank creation using the
                specified Types is supported, false otherwise
        raise:  NullArgument - objectiveBankRecordTypes is null
        compliance: mandatory - This method must be implemented.

        """
        return True

    def get_objective_bank_form_for_create(self, objective_bank_record_types=None):
        """Gets the objective bank form for creating new objective banks.
        A new form should be requested for each create transaction.
        arg:    objectiveBankRecordTypes (osid.type.Type): array of
                objective bank record types
        return: (osid.learning.ObjectiveBankForm) - the objective bank
                form
        raise:  NullArgument - objectiveBankRecordTypes is null
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - unable to get form for requested record
                types.
        compliance: mandatory - This method must be implemented.

        """
        if objective_bank_record_types is None:
            pass  # Still need to deal with the record_types argument
        objective_bank_form = objects.ObjectiveBankForm()
        self._forms[objective_bank_form.get_id().get_identifier()] = not CREATED
        return objective_bank_form

    def create_objective_bank(self, objective_bank_form=None):
        """Creates a new ObjectiveBank.

        arg:    objectiveBankForm (osid.learning.ObjectiveBankForm): the
                form for this ObjectiveBank
        return: (osid.learning.ObjectiveBankForm) - the new
                ObjectiveBank
        raise:  IllegalState - objectiveBankForm already used in a
                create transaction
        raise:  InvalidArgument - one or more of the form elements is
                invalid
        raise:  NullArgument - objectiveBankForm is null
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - objectiveBankForm did not originate from
                get_objective_bank_form_for_create()
        compliance: mandatory - This method must be implemented.

        """
        if objective_bank_form is None:
            raise NullArgument()
        if not isinstance(objective_bank_form, abc_learning_objects.ObjectiveBankForm):
            raise InvalidArgument('argument type is not an ObjectiveBankForm')
        if objective_bank_form.is_for_update():
            raise InvalidArgument('form is for update only, not create')

        # Check for "sandbox" genus type.  Hardcoded for now:
        #        if objective_bank_form._my_map['genusTypeId'] != 'mc3-objectivebank%3Amc3.learning.objectivebank.sandbox%40MIT-OEIT':
        #            raise PermissionDenied('Handcar only supports creating \'sandbox\' type ObjectiveBanks')

        try:
            if self._forms[objective_bank_form.get_id().get_identifier()] == CREATED:
                raise IllegalState('form already used in a create transaction')
        except KeyError:
            raise Unsupported('form did not originate from this session')
        if not objective_bank_form.is_valid():
            raise InvalidArgument('one or more of the form elements is invalid')

        url_path = construct_url('objective_banks')
        try:
            result = self._post_request(url_path, objective_bank_form._my_map)
        except Exception:
            raise  # OperationFailed
        self._forms[objective_bank_form.get_id().get_identifier()] = CREATED
        return objects.ObjectiveBank(result)

    def can_update_objective_banks(self, objective_bank_id=None):  # This should not have objective_bank_id argument!
        """Tests if this user can update ObjectiveBanks.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating an
        ObjectiveBank will result in a PermissionDenied. This is
        intended as a hint to an application that may not wish to offer
        update operations to unauthorized users.
        return: (boolean) - false if ObjectiveBank modification is not
                authorized, true otherwise
        compliance: mandatory - This method must be implemented.

        """
        if not objective_bank_id:
            url_path = construct_url('authorization')
        else:
            url_path = construct_url('authorization',
                                     bank_id=str(objective_bank_id))
        return self._get_request(url_path)['objectiveBankHints']['canUpdate']

    def get_objective_bank_form_for_update(self, objective_bank_id=None):
        """Gets the objective bank form for updating an existing objective
        bank.
        A new objective bank form should be requested for each update
        transaction.
        arg:    objectiveBankId (osid.id.Id): the Id of the
                ObjectiveBank
        return: (osid.learning.ObjectiveBankForm) - the objective bank
                form
        raise:  NotFound - objectiveBankId is not found
        raise:  NullArgument - objectiveBankId is null
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method must be implemented.

        """
        if objective_bank_id is None:
            raise NullArgument()
        try:
            url_path = construct_url('objective_banks',
                                     bank_id=objective_bank_id)
            objective_bank = objects.ObjectiveBank(self._get_request(url_path))
        except Exception:
            raise
        objective_bank_form = objects.ObjectiveBankForm(objective_bank._my_map)
        self._forms[objective_bank_form.get_id().get_identifier()] = not UPDATED
        return objective_bank_form

    def get_objective_bank_record_types(self):
        """Gets the objective bank types available in Handcar.
        arg:    None
        return: (osid.type.TypeList) - list of objective bank types
        raise:  NotFound - objectiveBankTypes is not found
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method must be implemented.

        """
        try:
            url_path = construct_url('objective_bank_types')
            objective_bank_types = typeObjects.TypeList(self._get_request(url_path))
        except Exception:
            raise
        return objective_bank_types

    def update_objective_bank(self, objective_bank_form=None):
        """Updates an existing objective bank.

        arg:    objectiveBankForm (osid.learning.ObjectiveBankForm): the
                form containing the elements to be updated
        raise:  IllegalState - objectiveBankForm already used in an
                update transaction
        raise:  InvalidArgument - the form contains an invalid value
        raise:  NullArgument - objectiveBankForm is null
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - objective_bank_form did not originate from
                get_objective_bank_form_for_update()
        compliance: mandatory - This method must be implemented.

        """
        if objective_bank_form is None:
            raise NullArgument()
        if not isinstance(objective_bank_form, abc_learning_objects.ObjectiveBankForm):
            raise InvalidArgument('argument type is not an ObjectiveBankForm')
        if not objective_bank_form.is_for_update():
            raise InvalidArgument('form is for create only, not update')

        # Check for "sandbox" genus type.  Hardcoded for now:
        # if objective_bank_form._my_map['genusTypeId'] != 'mc3-objectivebank%3Amc3.learning.objectivebank.sandbox%40MIT-OEIT':
        #    raise PermissionDenied('Handcar only supports updating \'sandbox\' type ObjectiveBanks')

        try:
            if self._forms[objective_bank_form.get_id().get_identifier()] == UPDATED:
                raise IllegalState('form already used in an update transaction')
        except KeyError:
            raise Unsupported('form did not originate from this session')
        if not objective_bank_form.is_valid():
            raise InvalidArgument('one or more of the form elements is invalid')

        url_path = construct_url('objective_banks')
        try:
            result = self._put_request(url_path, objective_bank_form._my_map)
        except Exception:
            raise  # OperationFailed
        self._forms[objective_bank_form.get_id().get_identifier()] = UPDATED
        return objects.ObjectiveBank(result)  # Not expected to return anything

    def can_delete_objective_banks(self, objective_bank_id=None):  # This should not have objective_bank_id argument!
        """Tests if this user can delete objective banks.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting an
        ObjectiveBank will result in a PermissionDenied. This is
        intended as a hint to an application that may not wish to offer
        delete operations to unauthorized users.
        return: (boolean) - false if ObjectiveBank deletion is not
                authorized, true otherwise
        compliance: mandatory - This method must be implemented.

        """
        if not objective_bank_id:
            url_path = construct_url('authorization')
        else:
            url_path = construct_url('authorization',
                                     bank_id=str(objective_bank_id))
        return self._get_request(url_path)['objectiveBankHints']['canDelete']

    def delete_objective_bank(self, objective_bank_id=None):
        """Deletes an ObjectiveBank.

        arg:    objectiveBankId (osid.id.Id): the Id of the
                ObjectiveBank to remove
        raise:  NotFound - objectiveBankId not found
        raise:  NullArgument - objectiveBankId is null
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method must be implemented.

        """
        from dlkit.abstract_osid.id.primitives import Id as ABCId
        if objective_bank_id is None:
            raise NullArgument()
        if not isinstance(objective_bank_id, ABCId):
            raise InvalidArgument('argument type is not an osid Id')

        # Check for "sandbox" genus type.  Hardcoded for now:
        try:
            objective_bank = ObjectiveBankLookupSession(proxy=self._proxy,
                                                        runtime=self._runtime).get_objective_bank(objective_bank_id)
        except Exception:
            raise
        # if objective_bank._my_map['genusTypeId'] != 'mc3-objectivebank%3Amc3.learning.objectivebank.sandbox%40MIT-OEIT':
        #     raise PermissionDenied('Handcar only supports deleting \'sandbox\' type ObjectiveBanks')

        url_path = construct_url('objective_banks',
                                 bank_id=objective_bank_id)
        result = self._delete_request(url_path)
        return objects.ObjectiveBank(result)  # Not expected to return anything

    def can_manage_objective_bank_aliases(self):
        """Tests if this user can manage Id aliases for ObjectiveBanks.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a PermissionDenied. This is intended as a hint
        to an application that may opt not to offer alias operations to
        an unauthorized user.
        return: (boolean) - false if ObjectiveBank aliasing is not
                authorized, true otherwise
        compliance: mandatory - This method must be implemented.

        """
        return False  # Not yet implemented

    def alias_objective_bank(self, objective_bank_id=None, alias_id=None):
        """Adds an Id to an ObjectiveBank for the purpose of creating
        compatibility.
        The primary Id of the ObjectiveBank is determined by the
        provider. The new Id performs as an alias to the primary Id. If
        the alias is a pointer to another objective bank, it is
        reassigned to the given objective bank Id.
        arg:    aliasId (osid.id.Id): the alias Id
        raise:  ALREADY_EXISTS - aliasId is already assigned
        raise:  NotFound - objectiveBankId not found
        raise:  NullArgument - objectiveBankId or aliasId is null
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method must be implemented.

        """
        raise Unimplemented()


class ObjectiveBankNotificationSession(abc_learning_sessions.ObjectiveBankNotificationSession, osid_sessions.OsidSession):
    """This session defines methods to receive notifications on
    adds/changes to ObjectiveBank objects.

    This session is intended for consumers needing to synchronize their
    state with this service without the use of polling. Notifications
    are cancelled when this session i

    """

    def can_register_for_objective_bank_notifications(self):
        """Tests if this user can register for ObjectiveBank notifications.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a PermissionDenied. This is intended as
        a hint to an application that may opt not to offer notification
        operations.
        return: (boolean) - false if notification methods are not
                authorized, true otherwise
        compliance: mandatory - This method must be implemented.

        """
        pass

    def register_for_new_objective_banks(self):
        """Register for notifications of new objective banks.
        objective_bank_receiver.new_objective_bank() is invoked when a
        new ObjectiveBank is created.
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method must be implemented.

        """
        pass

    def register_for_new_objective_bank_ancestors(self, objective_bank_id=None):
        """Registers for notification if an ancestor is added to the
        specified objective bank in the objective bank hierarchy.
        objective_bank_receiver.new_objective_bank_ancestor() is invoked
        when the specified objective bank experiences an addition in
        ancestry.
        arg:    objectiveBankId (osid.id.Id): the Id of the objective
                bank to monitor
        raise:  NullArgument - objectiveBankId is null
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method must be implemented.

        """
        pass

    def register_for_new_objective_bank_descendants(self, objective_bank_id=None):
        """Registers for notification if a descendant is added to the
        specified objective bank in the objective bank hierarchy.
        objective_bank_receiver.new_objective_bank_descendant() is
        invoked when the specified objective bank experiences an
        addition in descendants.
        arg:    objectiveBankId (osid.id.Id): the Id of the objective
                bank to monitor
        raise:  NullArgument - objectiveBankId is null
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method must be implemented.

        """
        pass

    def register_for_changed_objective_banks(self):
        """Registers for notification of updated objective banks.
        objective_bank_receiver.changed_objective_bank() is invoked when
        an objective bank is changed.
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method must be implemented.

        """
        pass

    def register_for_changed_objective_bank(self, objective_bank_id=None):
        """Registers for notification of an updated objective bank.
        objective_bank_receiver.changed_objective_bank() is invoked when
        the specified objective bank is changed.
        arg:    objectiveBankId (osid.id.Id): the Id of the objective
                bank to monitor
        raise:  NullArgument - objectiveBankId is null
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method must be implemented.

        """
        pass

    def register_for_deleted_objective_banks(self):
        """Registers for notification of deleted objective banks.
        objective_bank_receiver.deleted_objective_bank() is invoked when
        a calenedar is deleted.
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method must be implemented.

        """
        pass

    def register_for_deleted_objective_bank(self, objective_bank_id=None):
        """Registers for notification of a deleted objective bank.
        objective_bank_receiver.deleted_objective_bank() is invoked when
        the specified objective bank is deleted.
        arg:    objectiveBankId (osid.id.Id): the Id of the objective
                bank to monitor
        raise:  NullArgument - objectiveBankId is null
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method must be implemented.

        """
        pass

    def register_for_deleted_objective_bank_ancestors(self, objective_bank_id=None):
        """Registers for notification if an ancestor is removed from the
        specified objective bank in the objective bank hierarchy.
        objective_bank_receiver.deleted_objective_bank_ancestor() is
        invoked when the specified objective bank experiences a removal
        of an ancestor.
        arg:    objectiveBankId (osid.id.Id): the Id of the objective
                bank to monitor
        raise:  NullArgument - objectiveBankId is null
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method must be implemented.

        """
        pass

    def register_for_deleted_objective_bank_descendants(self, objective_bank_id=None):
        """Registers for notification if a descendant is removed from fthe
        specified objective bank in the objective bank hierarchy.
        objective_bank_receiver.deleted_objective_bank_descednant() is
        invoked when the specified objective bank experiences a removal
        of one of its descendants.
        arg:    objectiveBankId (osid.id.Id): the Id of the objective
                bank to monitor
        raise:  NullArgument - objectiveBankId is null
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method must be implemented.

        """
        pass


class ObjectiveBankHierarchySession(abc_learning_sessions.ObjectiveBankHierarchySession, osid_sessions.OsidSession):
    """This session defines methods for traversing a hierarchy of
    ObjectiveBank objects.

    Each node in the hierarchy is a unique ObjectiveBank. The hierarchy
    may be traversed recursively to establish the tree structure through
    get_parent_objective_banks() and get_child_objective_banks(). To
    relate these Ids to another OSID, get_objective_bank_nodes() can be
    used for retrievals that can be used for bulk lookups in other
    OSIDs. Any ObjectiveBank available in the ObjectiveBanking OSID is
    known to this hierarchy but does not appear in the hierarchy
    traversal until added as a root node or a child of another node.

    A user may not be authorized to traverse the entire hierarchy. Parts
    of the hierarchy may be made invisible through omission from the
    returns of get_parent_objective_banks() or
    get_child_objective_banks() in lieu of a PermissionDenied error
    that may disrupt the traversal through authorized pathways.

    This session defines views that offer differing behaviors when
    retrieving multiple objects.
      > comparative view: objective bank elements may be silently
        omitted or re-ordered
      > plenary view: provides a complete set or is an error condition


    """
    def __init__(self, alias=None, proxy=None, runtime=None, **kwargs):
        self._service_string = SERVICE_STRING
        self._catalogs_string = CATALOGS_STRING
        osid_sessions.OsidSession.__init__(self)
        osid_sessions.OsidSession._init_catalog(
            self,
            proxy,
            runtime
        )
        self._forms = dict()
        self._alias = alias
        self._urls = BankHierarchyUrls()
        super(ObjectiveBankHierarchySession, self).__init__()

    def get_objective_bank_hierarchy_id(self):
        """Gets the hierarchy Id associated with this session.

        return: (osid.id.Id) - the hierarchy Id associated with this
                session
        compliance: mandatory - This method must be implemented.

        """
        pass

    def get_objective_bank_hierarchy(self, alias=None):
        """Gets the hierarchy associated with this session.

        return: (osid.hierarchy.Hierarchy) - the hierarchy associated
                with this session
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method must be implemented.

        """
        if alias is not None:
            url_path = self._urls.hierarchy(re.sub(r'[ ]', '', alias.lower()))
        else:
            url_path = self._urls.hierarchy()
        return self._get_request(url_path)

    def can_access_objective_bank_hierarchy(self):
        """Tests if this user can perform hierarchy queries.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a PermissionDenied. This is intended as
        a hint to an an application that may not offer traversal
        functions to unauthorized users.
        return: (boolean) - false if hierarchy traversal methods are not
                authorized, true otherwise
        compliance: mandatory - This method must be implemented.

        """
        pass

    def use_comparative_objective_bank_view(self):
        """The returns from the objective bank methods may omit or
        translate elements based on this session, such as authorization,
        and not result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.
        compliance: mandatory - This method is must be implemented.

        """
        pass

    def use_plenary_objective_bank_view(self):
        """A complete view of the Hierarchy returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.
        compliance: mandatory - This method is must be implemented.

        """
        pass

    def get_root_objective_bank_ids(self, alias):
        """Gets the root objective bank Ids in this hierarchy.

        return: (osid.id.IdList) - the root objective bank Ids
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method must be implemented.

        """
        url_path = self._urls.roots(alias)
        return self._get_request(url_path)

    def get_root_objective_banks(self, alias):
        """Gets the root objective banks in this objective bank hierarchy.

        return: (osid.learning.ObjectiveBankList) - the root objective
                banks
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method is must be implemented.

        """
        pass

    def has_parent_objective_banks(self, objective_bank_id=None):
        """Tests if the ObjectiveBank has any parents.

        arg:    objectiveBankId (osid.id.Id): the Id of an objective
                bank
        return: (boolean) - true if the objective bank has parents,
                false otherwise
        raise:  NotFound - objectiveBankId is not found
        raise:  NullArgument - objectiveBankId is null
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method must be implemented.

        """
        pass

    def is_parent_of_objective_bank(self, id=None, objective_bank_id=None):
        """Tests if an Id is a direct parent of an objective bank.

        arg:    objectiveBankId (osid.id.Id): the Id of an objective
                bank
        return: (boolean) - true if this id is a parent of
                objectiveBankId,  false otherwise
        raise:  NotFound - objectiveBankId is not found
        raise:  NullArgument - id or objectiveBankId is null
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method must be implemented.
        implementation notes: If id not found return false.

        """
        pass

    def get_parent_objective_bank_ids(self, objective_bank_id=None):
        """Gets the parent Ids of the given objective bank.

        arg:    objectiveBankId (osid.id.Id): the Id of an objective
                bank
        return: (osid.id.IdList) - the parent Ids of the objective bank
        raise:  NotFound - objectiveBankId is not found
        raise:  NullArgument - objectiveBankId is null
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method must be implemented.

        """
        pass

    def get_parent_objective_banks(self, objective_bank_id=None):
        """Gets the parents of the given objective bank.

        arg:    objectiveBankId (osid.id.Id): the Id of an objective
                bank
        return: (osid.learning.ObjectiveBankList) - the parents of the
                objective bank
        raise:  NotFound - objectiveBankId is not found
        raise:  NullArgument - objectiveBankId is null
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method must be implemented.

        """
        pass

    def is_ancestor_of_objective_bank(self, id=None, objective_bank_id=None):
        """Tests if an Id is an ancestor of an objective bank.

        arg:    objectiveBankId (osid.id.Id): the Id of an objective
                bank
        return: (boolean) - true if this id is an ancestor of
                objectiveBankId,  false otherwise
        raise:  NotFound - objectiveBankId is not found
        raise:  NullArgument - id or objectiveBankId is null
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method must be implemented.
        implementation notes: If id not found return false.

        """
        pass

    def has_child_objective_banks(self, objective_bank_id=None):
        """Tests if an objective bank has any children.

        arg:    objectiveBankId (osid.id.Id): the Id of an objective
                bank
        return: (boolean) - true if the objectiveBankId has children,
                false otherwise
        raise:  NotFound - objectiveBankId is not found
        raise:  NullArgument - objectiveBankId is null
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method must be implemented.

        """
        pass

    def is_child_of_objective_bank(self, id=None, objective_bank_id=None):
        """Tests if an objective bank is a direct child of another.

        arg:    objectiveBankId (osid.id.Id): the Id of an objective
                bank
        return: (boolean) - true if the id is a child of
                objectiveBankId,  false otherwise
        raise:  NotFound - objectiveBankId is not found
        raise:  NullArgument - id or objectiveBankId is null
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method must be implemented.
        implementation notes: If id not found return false.

        """
        pass

    def get_child_objective_bank_ids(self, objective_bank_id=None):
        """Gets the child Ids of the given objective bank.

        arg:    objectiveBankId (osid.id.Id): the Id to query
        return: (osid.id.IdList) - the children of the objective bank
        raise:  NotFound - objectiveBankId is not found
        raise:  NullArgument - objectiveBankId is null
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method must be implemented.

        """
        pass

    def get_child_objective_banks(self, objective_bank_id=None):
        """Gets the children of the given objective bank.

        arg:    objectiveBankId (osid.id.Id): the Id to query
        return: (osid.learning.ObjectiveBankList) - the children of the
                objective bank
        raise:  NotFound - objectiveBankId is not found
        raise:  NullArgument - objectiveBankId is null
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method must be implemented.

        """
        pass

    def is_descendant_of_objective_bank(self, id=None, objective_bank_id=None):
        """Tests if an Id is a descendant of an objective bank.

        arg:    objectiveBankId (osid.id.Id): the Id of an objective
                bank
        return: (boolean) - true if the id is a descendant of the
                objectiveBankId,  false otherwise
        raise:  NotFound - objectiveBankId is not found
        raise:  NullArgument - id or objectiveBankId is null
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method must be implemented.
        implementation notes: If id is not found return false.

        """
        pass

    def get_objective_bank_node_ids(self,
                                    objective_bank_id=None,
                                    ancestor_levels=None,
                                    descendant_levels=None,
                                    include_siblings=None):
        """Gets a portion of the hierarchy for the given objective bank.

        arg:    includeSiblings (boolean): true to include the siblings
                of the given node, false to omit the siblings
        return: (osid.hierarchy.Node) - a catalog node
        raise:  NotFound - objectiveBankId not found
        raise:  NullArgument - objectiveBankId is null
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method must be implemented.

        """
        pass

    def get_objective_bank_nodes(self,
                                 objective_bank_id=None,
                                 ancestor_levels=None,
                                 descendant_levels=None,
                                 include_siblings=None):
        """Gets a portion of the hierarchy for the given objective bank.

        arg:    includeSiblings (boolean): true to include the siblings
                of the given node, false to omit the siblings
        return: (osid.learning.ObjectiveBankNode) - an objective bank
                node
        raise:  NotFound - objectiveBankId not found
        raise:  NullArgument - objectiveBankId is null
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        compliance: mandatory - This method must be implemented.

        """
        if descendant_levels:
            url_path = self._urls.nodes(alias=objective_bank_id, depth=descendant_levels)
        else:
            url_path = self._urls.nodes(alias=objective_bank_id)
        return self._get_request(url_path)


class ObjectiveBankHierarchyDesignSession(abc_learning_sessions.ObjectiveBankHierarchyDesignSession,
                                          osid_sessions.OsidSession):
    """This session defines methods for managing a hierarchy of ``ObjectiveBank`` objects.

    Each node in the hierarchy is a unique ``ObjectiveBank``.

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
        self._forms = dict()
        self._urls = BankHierarchyUrls()
        super(ObjectiveBankHierarchyDesignSession, self).__init__()

    def create_objective_bank_hierarchy(self, alias, desc, genus):
        """
        Create a bank hierarchy with the given alias
        :param alias:
        :return:
        """
        url_path = self._urls.hierarchy()
        data = {
            'id': re.sub(r'[ ]', '', alias.lower()),
            'displayName': {
                'text': alias
            },
            'description': {
                'text': desc
            },
            'genusTypeId': str(genus)
        }
        return self._post_request(url_path, data)

    def delete_objective_bank_hierarchy(self, alias):
        """
        Delete this bank hierarchy
        :param alias:
        :return:
        """
        url_path = self._urls.hierarchy(alias)
        return self._delete_request(url_path)

    def get_objective_bank_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        return: (osid.id.Id) - the hierarchy ``Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    objective_bank_hierarchy_id = property(fget=get_objective_bank_hierarchy_id)

    def get_objective_bank_hierarchy(self, alias):
        """Gets the hierarchy associated with this session.

        return: (osid.hierarchy.Hierarchy) - the hierarchy associated
                with this session
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        url_path = self._urls.hierarchy(re.sub(r'[ ]', '', alias.lower()))
        return self._get_request(url_path)

    objective_bank_hierarchy = property(fget=get_objective_bank_hierarchy)

    def can_modify_objective_bank_hierarchy(self):
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

    def add_root_objective_bank(self, alias=None, objective_bank_id=None):
        """Adds a root objective bank.

        arg:    objective_bank_id (osid.id.Id): the ``Id`` of an
                objective bank
        raise:  AlreadyExists - ``objective_bank_id`` is already in
                hierarchy
        raise:  NotFound - ``objective_bank_id`` not found
        raise:  NullArgument - ``objective_bank_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        url_path = self._urls.roots(alias=alias)
        current_root_ids = self._get_request(url_path)['ids']
        current_root_ids.append(str(objective_bank_id))
        new_root_ids = {
            'ids': current_root_ids
        }
        return self._put_request(url_path, new_root_ids)

    def remove_root_objective_bank(self, alias=None, objective_bank_id=None):
        """Removes a root objective bank.

        arg:    objective_bank_id (osid.id.Id): the ``Id`` of an
                objective bank
        raise:  NotFound - ``objective_bank_id`` is not a root
        raise:  NullArgument - ``objective_bank_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        url_path = self._urls.roots(alias=alias)
        current_root_ids = self._get_request(url_path)['ids']
        modified_list = []
        for root_id in current_root_ids:
            if root_id != str(objective_bank_id):
                modified_list.append(root_id)
        new_root_ids = {
            'ids': modified_list
        }
        return self._put_request(url_path, new_root_ids)

    def add_child_objective_bank(self, objective_bank_id=None, parent_id=None, child_id=None):
        """Adds a child to an objective bank.

        arg:    objective_bank_id (osid.id.Id): the ``Id`` of an
                objective bank
        arg:    child_id (osid.id.Id): the ``Id`` of the new child
        raise:  AlreadyExists - ``objective_bank_id`` is already a
                parent of ``child_id``
        raise:  NotFound - ``objective_bank_id`` or ``child_id`` not
                found
        raise:  NullArgument - ``objective_bank_id`` or ``child_id`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        url_path = self._urls.children(alias=objective_bank_id, bank_id=parent_id)
        current_children_ids = self._get_request(url_path)['ids']
        current_children_ids.append(str(child_id))
        new_children_ids = {
            'ids': current_children_ids
        }
        return self._put_request(url_path, new_children_ids)

    def remove_child_objective_bank(self, objective_bank_id=None, child_id=None):
        """Removes a child from an objective bank.

        arg:    objective_bank_id (osid.id.Id): the ``Id`` of an
                objective bank
        arg:    child_id (osid.id.Id): the ``Id`` of the child
        raise:  NotFound - ``objective_bank_id`` not a parent of
                ``child_id``
        raise:  NullArgument - ``objective_bank_id`` or ``child_id`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def remove_child_objective_banks(self, objective_bank_id=None):
        """Removes all children from an objective bank.

        arg:    objective_bank_id (osid.id.Id): the ``Id`` of an
                objective bank
        raise:  NotFound - ``objective_bank_id`` not in hierarchy
        raise:  NullArgument - ``objective_bank_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def use_comparative_objective_bank_view(self):
        """The returns from the lookup methods may omit or translate
        elements based on this session, such as authorization, and not
        result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.
        compliance: mandatory - This method is must be implemented.

        """
        self._objective_bank_view = COMPARATIVE

    def use_plenary_objective_bank_view(self):
        """A complete view of the Objective returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.
        compliance: mandatory - This method is must be implemented.

        """
        self._objective_bank_view = PLENARY

    def use_federated_objective_bank_view(self):
        """Federates the view for methods in this session.
        A federated view will include objectives in objective banks
        which are children of this objective bank in the objective bank
        hierarchy.
        compliance: mandatory - This method is must be implemented.

        """
        self._objective_bank_view = FEDERATED

    def use_isolated_objective_bank_view(self):
        """Isolates the view for methods in this session.
        An isolated view restricts lookups to this objective bank only.
        compliance: mandatory - This method is must be implemented.

        """
        self._objective_bank_view = ISOLATED
