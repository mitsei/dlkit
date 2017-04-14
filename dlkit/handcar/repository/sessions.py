# -*- coding: utf-8 -*-

# This module contains all the Session classes used by the MIT Core Concept
# Catalog (MC3) Handcar based implementation of the OSID Repository Service.
# This includes the learning package sessions for Assets, AssetContents
# and Repositorier.

import json
import pdb
from ...abstract_osid.repository import sessions as abc_repository_sessions
from ...abstract_osid.repository import objects as abc_repository_objects
from ..osid.osid_errors import AlreadyExists, NullArgument, InvalidArgument, NotFound, IllegalState, OperationFailed, PermissionDenied, Unsupported, Unimplemented
from ..osid import sessions as osid_sessions
from ..learning import sessions as learning_sessions  # for delegating to learning sevice
from ..learning import objects as learning_objects   # for delegating to learning sevice
from .. import settings
from . import objects
from ..id import objects as id_objects
from ..primitives import Id, Type, DisplayText
from ..learning.managers import LearningManager

from ..utilities import construct_url

COMPARATIVE = 0
PLENARY = 1
ISOLATED = 0
FEDERATED = 1
CREATED = True
UPDATED = True
SERVICE_STRING = 'repository'
CATALOGS_STRING = 'repositories'


class AssetLookupSession(abc_repository_sessions.AssetLookupSession, osid_sessions.OsidSession):
    """This session defines methods for retrieving assets.

    An ``Asset`` represents an element of content stored in a
    Repository.

    This lookup session defines several views:

      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete result set or is an error
        condition
      * isolated repository view: All asset methods in this session
        operate, retrieve and pertain to assets defined explicitly in
        the current repository. Using an isolated view is useful for
        managing ``Assets`` with the ``AssetAdminSession.``
      * federated repository view: All asset methods in this session
        operate, retrieve and pertain to all assets defined in this
        repository and any other assets implicitly available in this
        repository through repository inheritence.


    The methods ``use_federated_repository_view()`` and
    ``use_isolated_repository_view()`` behave as a radio group and one
    should be selected before invoking any lookup methods.

    Assets may have an additional records indicated by their respective
    record types. The record may not be accessed through a cast of the
    ``Asset``.

    """

    def __init__(self, repository_id=None, proxy=None, runtime=None, **kwargs):
        self._service_string = SERVICE_STRING
        self._catalogs_string = CATALOGS_STRING
        osid_sessions.OsidSession.__init__(self)
        osid_sessions.OsidSession._init_catalog(
            self,
            proxy,
            runtime
        )
        self._asset_view = COMPARATIVE
        self._repository_view = FEDERATED
        if repository_id is None:
            # For now we are just going to find the first objective bank
            # This needs to change!
            url_path = construct_url('objective_banks')
            repository = learning_objects.ObjectiveBank(self._get_request(url_path)[0])
            self._repository_id = repository.get_id()
        else:
            self._repository_id = repository_id
        self._catalog_idstr = str(self._repository_id)

    def get_repository_id(self):
        """Gets the ``Repository``  ``Id`` associated with this session.

        :return: the ``Repository Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return self._repository_id

    repository_id = property(fget=get_repository_id)

    def get_repository(self):
        """Gets the ``Repository`` associated with this session.

        :return: the ``Repository`` associated with this session
        :rtype: ``osid.repository.Repository``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return RepositoryLookupSession().get_repository(self._repository_id)

    repository = property(fget=get_repository)

    def can_lookup_assets(self):
        """Tests if this user can perform ``Asset`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        url_path = construct_url('authorization',
                                 bank_id=self._catalog_idstr)
        return self._get_request(url_path)['assetHints']['canLookup']

    def use_comparative_asset_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session,
        such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        self._asset_view = COMPARATIVE

    def use_plenary_asset_view(self):
        """A complete view of the ``Asset`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        self._asset_view = PLENARY

    def use_federated_repository_view(self):
        """Federates the view for methods in this session.

        A federated view will include assets in repositories which are
        children of this repository in the repository hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        self._repository_view = FEDERATED

    def use_isolated_repository_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts lookups to this repository only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        self._repository_view = ISOLATED

    def get_asset(self, asset_id=None):
        """Gets the ``Asset`` specified by its ``Id``.

        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Asset`` may have a different
        ``Id`` than requested, such as the case where a duplicate ``Id``
        was assigned to an ``Asset`` and retained for compatibility.

        :param asset_id: the ``Id`` of the ``Asset`` to retrieve
        :type asset_id: ``osid.id.Id``
        :return: the returned ``Asset``
        :rtype: ``osid.repository.Asset``
        :raise: ``NotFound`` -- no ``Asset`` found with the given ``Id``
        :raise: ``NullArgument`` -- ``asset_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        if asset_id is None:
            raise NullArgument()
        url_path = construct_url('assets',
                                 bank_id=self._catalog_idstr,
                                 asset_id=asset_id)
        return objects.Asset(self._get_request(url_path))

    def get_assets_by_ids(self, asset_ids=None):
        """Gets an ``AssetList`` corresponding to the given ``IdList``.

        In plenary mode, the returned list contains all of the assets
        specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if an ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Assets`` may be omitted from the list and may
        present the elements in any order including returning a unique
        set.

        :param asset_ids: the list of ``Ids`` to retrieve
        :type asset_ids: ``osid.id.IdList``
        :return: the returned ``Asset list``
        :rtype: ``osid.repository.AssetList``
        :raise: ``NotFound`` -- an ``Id`` was not found
        :raise: ``NullArgument`` -- ``asset_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        if asset_ids is None:
            raise NullArgument()
        assets = []
        for i in asset_ids:
            asset = None
            url_path = construct_url('assets',
                                     bank_id=self._catalog_idstr,
                                     asset_id=i)
            try:
                asset = self._get_request(url_path)
            except (NotFound, OperationFailed):
                if self._objective_view == PLENARY:
                    raise
                else:
                    pass
            if asset:
                if not (self._asset_view == COMPARATIVE and
                        asset in assets):
                    assets.append(asset)
        return objects.AssetList(assets)

    def get_assets_by_genus_type(self, asset_genus_type=None):
        """Gets an ``AssetList`` corresponding to the given asset genus ``Type`` which does not
        include assets of types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known assets or
        an error results. Otherwise, the returned list may contain only
        those assets that are accessible through this session.

        :param asset_genus_type: an asset genus type
        :type asset_genus_type: ``osid.type.Type``
        :return: the returned ``Asset list``
        :rtype: ``osid.repository.AssetList``
        :raise: ``NullArgument`` -- ``asset_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        if asset_genus_type is None:
            raise NullArgument()
        url_path = construct_url('assets_by_genus',
                                 bank_id=self._catalog_idstr,
                                 genus_type=asset_genus_type.get_identifier())
        return objects.AssetList(self._get_request(url_path))

    def get_assets_by_parent_genus_type(self, asset_genus_type=None):
        """Gets an ``AssetList`` corresponding to the given asset genus ``Type`` and include
        any additional assets with genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known assets or
        an error results. Otherwise, the returned list may contain only
        those assets that are accessible through this session.

        :param asset_genus_type: an asset genus type
        :type asset_genus_type: ``osid.type.Type``
        :return: the returned ``Asset list``
        :rtype: ``osid.repository.AssetList``
        :raise: ``NullArgument`` -- ``asset_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

    def get_assets_by_record_type(self, asset_record_type=None):
        """Gets an ``AssetList`` containing the given asset record ``Type``.

        In plenary mode, the returned list contains all known assets or
        an error results. Otherwise, the returned list may contain only
        those assets that are accessible through this session.

        :param asset_record_type: an asset record type
        :type asset_record_type: ``osid.type.Type``
        :return: the returned ``Asset list``
        :rtype: ``osid.repository.AssetList``
        :raise: ``NullArgument`` -- ``asset_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

    def get_assets_by_provider(self, resource_id=None):
        """Gets an ``AssetList`` from the given provider.

        In plenary mode, the returned list contains all known assets or
        an error results. Otherwise, the returned list may contain only
        those assets that are accessible through this session.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :return: the returned ``Asset list``
        :rtype: ``osid.repository.AssetList``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

    def get_assets(self):
        """Gets all ``Assets``.

        In plenary mode, the returned list contains all known assets or
        an error results. Otherwise, the returned list may contain only
        those assets that are accessible through this session.

        :return: a list of ``Assets``
        :rtype: ``osid.repository.AssetList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        url_path = construct_url('assets',
                                 bank_id=self._catalog_idstr)
        return objects.AssetList(self._get_request(url_path))

    assets = property(fget=get_assets)


class AssetQuerySession(abc_repository_sessions.AssetQuerySession, osid_sessions.OsidSession):
    """This session provides methods for searching among ``Asset`` objects.

    The search query is constructed using the ``AssetQuery``.

    This session defines views that offer differing behaviors for
    searching.

      * federated repository view: searches include assets in
        repositories of which this repository is a ancestor in the
        repository hierarchy
      * isolated repository view: searches are restricted to assets in
        this repository


    Assets may have a query record indicated by their respective record
    types. The query record is accessed via the ``AssetQuery``.

    """

    def get_repository_id(self):
        """Gets the ``Repository``  ``Id`` associated with this session.

        :return: the ``Repository Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    repository_id = property(fget=get_repository_id)

    def get_repository(self):
        """Gets the ``Repository`` associated with this session.

        :return: the ``Repository`` associated with this session
        :rtype: ``osid.repository.Repository``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.repository.Repository

    repository = property(fget=get_repository)

    def can_search_assets(self):
        """Tests if this user can perform ``Asset`` searches.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.

        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    def use_federated_repository_view(self):
        """Federates the view for methods in this session.

        A federated view will include assets in repositories which are
        children of this repository in the repository hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_isolated_repository_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts lookups to this repository only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def get_asset_query(self):
        """Gets an asset query.

        :return: the asset query
        :rtype: ``osid.repository.AssetQuery``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.repository.AssetQuery

    asset_query = property(fget=get_asset_query)

    def get_assets_by_query(self, asset_query=None):
        """Gets a list of ``Assets`` matching the given asset query.

        :param asset_query: the asset query
        :type asset_query: ``osid.repository.AssetQuery``
        :return: the returned ``AssetList``
        :rtype: ``osid.repository.AssetList``
        :raise: ``NullArgument`` -- ``asset_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- the ``asset_query`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.repository.AssetList


class AssetSearchSession(AssetQuerySession):
    """This session provides methods for searching among ``Asset`` objects.

    The search query is constructed using the ``AssetQuery``.

    ``get_assets_by_query()`` is the basic search method and returns a
    list of ``Assets``. A more advanced search may be performed with
    ``getAssetsBySearch()``. It accepts an ``AssetSearch`` in addition
    to the query for the purpose of specifying additional options
    affecting the entire search, such as ordering.
    ``get_assets_by_search()`` returns an ``AssetSearchResults`` that
    can be used to access the resulting ``AssetList`` or be used to
    perform a search within the result set through ``AssetList``.

    This session defines views that offer differing behaviors for
    searching.

      * federated repository view: searches include assets in
        repositories of which this repository is a ancestor in the
        repository hierarchy
      * isolated repository view: searches are restricted to assets in
        this repository


    Assets may have a query record indicated by their respective record
    types. The query record is accessed via the ``AssetQuery``.

    """

    def get_asset_search(self):
        """Gets an asset search.

        :return: the asset search
        :rtype: ``osid.repository.AssetSearch``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.repository.AssetSearch

    asset_search = property(fget=get_asset_search)

    def get_asset_search_order(self):
        """Gets an asset search order.

        The ``AssetSearchOrder`` is supplied to an ``AssetSearch`` to
        specify the ordering of results.

        :return: the asset search order
        :rtype: ``osid.repository.AssetSearchOrder``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.repository.AssetSearchOrder

    asset_search_order = property(fget=get_asset_search_order)

    def get_assets_by_search(self, asset_query=None, asset_search=None):
        """Gets the search results matching the given search query using the given search.

        :param asset_query: the asset query
        :type asset_query: ``osid.repository.AssetQuery``
        :param asset_search: the asset search
        :type asset_search: ``osid.repository.AssetSearch``
        :return: the asset search results
        :rtype: ``osid.repository.AssetSearchResults``
        :raise: ``NullArgument`` -- ``asset_query`` or ``asset_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``asset_query`` or ``asset_search`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.repository.AssetSearchResults

    def get_asset_query_from_inspector(self, asset_query_inspector=None):
        """Gets an asset query from an inspector.

        The inspector is available from a ``AssetSearchResults``.

        :param asset_query_inspector: an asset query inspector
        :type asset_query_inspector: ``osid.repository.AssetQueryInspector``
        :return: the asset query
        :rtype: ``osid.repository.AssetQuery``
        :raise: ``NullArgument`` -- ``asset_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``asset_query_inspector`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.repository.AssetQuery


class AssetAdminSession(abc_repository_sessions.AssetAdminSession, osid_sessions.OsidSession):
    """This session creates, updates, and deletes ``Assets``.

    The data for create and update is provided by the consumer via the
    form object. ``OsidForms`` are requested for each create or update
    and may not be reused.

    Create and update operations differ in their usage. To create an
    ``Asset,`` an ``AssetForm`` is requested using
    ``get_asset_form_for_create()`` specifying the desired record
    ``Types`` or none if no record ``Types`` are needed. The returned
    ``AssetyForm`` will indicate that it is to be used with a create
    operation and can be used to examine metdata or validate data prior
    to creation. Once the ``AssetForm`` is submiited to a create
    operation, it cannot be reused with another create operation unless
    the first operation was unsuccessful. Each ``AssetForm`` corresponds
    to an attempted transaction.

    For updates, ``AssetForms`` are requested to the ``Asset``  ``Id``
    that is to be updated using ``getAssetFormForUpdate()``. Similarly,
    the ``AssetForm`` has metadata about the data that can be updated
    and it can perform validation before submitting the update. The
    ``AssetForm`` can only be used once for a successful update and
    cannot be reused.

    The delete operations delete ``Assets``. To unmap an ``Asset`` from
    the current ``Repository,`` the ``AssetRepositoryAssignmentSession``
    should be used. These delete operations attempt to remove the
    ``Bid`` itself thus removing it from all known ``Repository``
    catalogs.

    This session includes an ``Id`` aliasing mechanism to assign an
    external ``Id`` to an internally assigned Id.

    The view of the administrative methods defined in this session is
    determined by the provider. For an instance of this session where no
    repository has been specified, it may not be parallel to the
    ``AssetLookupSession``. For example, a default
    ``AssetLookupSession`` may view the entire repository hierarchy
    while the default ``AssetAdminSession`` uses an isolated
    ``Repository`` to create new ``Assets`` ora specific repository to
    operate on a predetermined set of ``Assets``. Another scenario is a
    federated provider who does not wish to permit administrative
    operations for the federation unaware.

    Example create:
      if (!session.canCreateAssets()) {
          return "asset creation not permitted";
      }

      Type types[1];
      types[0] = assetPhotographType;
      if (!session.canCreateAssetWithRecordTypes(types)) {
          return "creating an asset with a photograph type is not supported";
      }

      AssetForm form = session.getAssetFormForCreate();
      Metadata metadata = form.getDisplayNameMetadata();
      if (metadata.isReadOnly()) {
          return "cannot set display name";
      }

      form.setDisplayName("my photo");

      PhotographRecordForm photoForm = (PhotographRecordForn) form.getRecordForm(assetPhotogaphType);
      Metadata metadata = form.getApertureMetadata();
      if (metadata.isReadOnly()) {
          return ("cannot set aperture");
      }

      photoForm.setAperture("5.6");
      if (!form.isValid()) {
          return form.getValidationMessage();
      }

      Asset newAsset = session.createAsset(form);

    """
    def __init__(self, repository_id=None, proxy=None, runtime=None, **kwargs):
        self._service_string = SERVICE_STRING
        self._catalogs_string = CATALOGS_STRING
        osid_sessions.OsidSession.__init__(self)
        osid_sessions.OsidSession._init_catalog(
            self,
            proxy,
            runtime
        )
        if repository_id is None:
            # For now we are just going to find the first objective bank
            # This needs to change!
            url_path = construct_url('objective_banks')
            repository = learning_objects.ObjectiveBank(self._get_request(url_path)[0])
            self._repository_id = repository.get_id()
        else:
            self._repository_id = repository_id
        self._catalog_idstr = str(self._repository_id)
        self._forms = dict()

    def get_repository_id(self):
        """Gets the ``Repository``  ``Id`` associated with this session.

        :return: the ``Repository Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return self._repository_id

    repository_id = property(fget=get_repository_id)

    def get_repository(self):
        """Gets the ``Repository`` associated with this session.

        :return: the ``Repository`` associated with this session
        :rtype: ``osid.repository.Repository``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return RepositoryLookupSession().get_repository(self._repository_id)

    repository = property(fget=get_repository)

    def can_create_assets(self):
        """Tests if this user can create ``Assets``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating an ``Asset``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer create
        operations to an unauthorized user.

        :return: ``false`` if ``Asset`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        url_path = construct_url('authorization',
                                 bank_id=self._catalog_idstr)
        return self._get_request(url_path)['assetHints']['canCreate']

    def can_create_asset_with_record_types(self, asset_record_types=None):
        """Tests if this user can create a single ``Asset`` using the desired record types.

        While ``RepositoryManager.getAssetRecordTypes()`` can be used to
        examine which records are supported, this method tests which
        record(s) are required for creating a specific ``Asset``.
        Providing an empty array tests if an ``Asset`` can be created
        with no records.

        :param asset_record_types: array of asset record types
        :type asset_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Asset`` creation using the specified record ``Types`` is supported,
            ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``asset_record_types`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return True

    def get_asset_form_for_create(self, asset_record_types=None):
        """Gets the asset form for creating new assets.

        A new form should be requested for each create transaction.

        :param asset_record_types: array of asset record types
        :type asset_record_types: ``osid.type.Type[]``
        :return: the asset form
        :rtype: ``osid.repository.AssetForm``
        :raise: ``NullArgument`` -- ``asset_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form for requested record types

        *compliance: mandatory -- This method must be implemented.*

        """
        if asset_record_types is None:
            pass  # Still need to deal with the record_types argument
        asset_form = objects.AssetForm()
        self._forms[asset_form.get_id().get_identifier()] = not CREATED
        return asset_form

    def create_asset(self, asset_form=None):
        """Creates a new ``Asset``.

        :param asset_form: the form for this ``Asset``
        :type asset_form: ``osid.repository.AssetForm``
        :return: the new ``Asset``
        :rtype: ``osid.repository.Asset``
        :raise: ``IllegalState`` -- ``asset_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``asset_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``asset_form`` did not originate from ``get_asset_form_for_create()``

        *compliance: mandatory -- This method must be implemented.*

        """
        if asset_form is None:
            raise NullArgument()
        if not isinstance(asset_form, abc_repository_objects.AssetForm):
            raise InvalidArgument('argument type is not an AssetForm')
        if asset_form.is_for_update():
            raise InvalidArgument('form is for update only, not create')
        try:
            if self._forms[asset_form.get_id().get_identifier()] == CREATED:
                raise IllegalState('form already used in a create transaction')
        except KeyError:
            raise Unsupported('form did not originate from this session')
        if not asset_form.is_valid():
            raise InvalidArgument('one or more of the form elements is invalid')

        url_path = construct_url('assets',
                                 bank_id=self._catalog_idstr)
        try:
            result = self._post_request(url_path, asset_form._my_map)
        except Exception:
            raise  # OperationFailed
        self._forms[asset_form.get_id().get_identifier()] = CREATED
        return objects.Asset(result)

    def can_update_assets(self):
        """Tests if this user can update ``Assets``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating an ``Asset``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer update
        operations to an unauthorized user.

        :return: ``false`` if ``Asset`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        url_path = construct_url('authorization',
                                 bank_id=self._catalog_idstr)
        return self._get_request(url_path)['assetHints']['canUpdate']

    def get_asset_form_for_update(self, asset_id=None):
        """Gets the asset form for updating an existing asset.

        A new asset form should be requested for each update
        transaction.

        :param asset_id: the ``Id`` of the ``Asset``
        :type asset_id: ``osid.id.Id``
        :return: the asset form
        :rtype: ``osid.repository.AssetForm``
        :raise: ``NotFound`` -- ``asset_id`` is not found
        :raise: ``NullArgument`` -- ``asset_id`` is null
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        if asset_id is None:
            raise NullArgument()
        try:
            url_path = construct_url('assets',
                                     bank_id=self._catalog_idstr,
                                     asset_id=asset_id)
            asset = objects.Asset(self._get_request(url_path))
        except Exception:
            raise
        asset_form = objects.AssetForm(asset._my_map)
        self._forms[asset_form.get_id().get_identifier()] = not UPDATED
        return asset_form

    def update_asset(self, asset_form=None):
        """Updates an existing asset.

        :param asset_form: the form containing the elements to be updated
        :type asset_form: ``osid.repository.AssetForm``
        :raise: ``IllegalState`` -- ``asset_form`` already used in anupdate transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``asset_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``asset_form`` did not originate from ``get_asset_form_for_update()``

        *compliance: mandatory -- This method must be implemented.*

        """
        if asset_form is None:
            raise NullArgument()
        if not isinstance(asset_form, abc_repository_objects.AssetForm):
            raise InvalidArgument('argument type is not an AssetForm')
        if not asset_form.is_for_update():
            raise InvalidArgument('form is for create only, not update')
        try:
            if self._forms[asset_form.get_id().get_identifier()] == UPDATED:
                raise IllegalState('form already used in an update transaction')
        except KeyError:
            raise Unsupported('form did not originate from this session')
        if not asset_form.is_valid():
            raise InvalidArgument('one or more of the form elements is invalid')

        url_path = construct_url('assets',
                                 bank_id=self._catalog_idstr)
        try:
            result = self._put_request(url_path, asset_form._my_map)
        except Exception:
            raise  # OperationFailed()
        self._forms[asset_form.get_id().get_identifier()] = UPDATED
        return objects.Asset(result)  # Not expected to return anything

    def can_delete_assets(self):
        """Tests if this user can delete ``Assets``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting an ``Asset``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer delete
        operations to an unauthorized user.

        :return: ``false`` if ``Asset`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        url_path = construct_url('authorization',
                                 bank_id=self._catalog_idstr)
        return self._get_request(url_path)['assetHints']['canDelete']

    def delete_asset(self, asset_id=None):
        """Deletes an ``Asset``.

        :param asset_id: the ``Id`` of the ``Asset`` to remove
        :type asset_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``asset_id`` not found
        :raise: ``NullArgument`` -- ``asset_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        if asset_id is None:
            raise NullArgument()
        if not isinstance(asset_id, Id):
            raise InvalidArgument('argument type is not an osid Id')

        url_path = construct_url('assets',
                                 bank_id=self._catalog_idstr,
                                 asset_id=asset_id)
        result = self._delete_request(url_path)
        return objects.Asset(result)  # Not expected to return anything

    def can_manage_asset_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Assets``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``Asset`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return False  # Not yet implemented

    def alias_asset(self, asset_id=None, alias_id=None):
        """Adds an ``Id`` to an ``Asset`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``Asset`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another asset, it is
        reassigned to the given asset ``Id``.

        :param asset_id: the ``Id`` of an ``Asset``
        :type asset_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``asset_id`` not found
        :raise: ``NullArgument`` -- ``asset_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

    def can_create_asset_content(self, asset_id=None):
        """Tests if this user can create content for ``Assets``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating an ``Asset``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer create
        operations to an unauthorized user.

        :param asset_id: the ``Id`` of an ``Asset``
        :type asset_id: ``osid.id.Id``
        :return: ``false`` if ``Asset`` content ceration is not authorized, ``true`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``asset_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        url_path = construct_url('authorization',
                                 bank_id=self._catalog_idstr)
        return self._get_request(url_path)['assetHints']['canCreate']

    def can_create_asset_content_with_record_types(self, asset_id=None, asset_content_record_types=None):
        """Tests if this user can create an ``AssetContent`` using the desired record types.

        While ``RepositoryManager.getAssetContentRecordTypes()`` can be
        used to test which records are supported, this method tests
        which records are required for creating a specific
        ``AssetContent``. Providing an empty array tests if an
        ``AssetContent`` can be created with no records.

        :param asset_id: the ``Id`` of an ``Asset``
        :type asset_id: ``osid.id.Id``
        :param asset_content_record_types: array of asset content record types
        :type asset_content_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``AssetContent`` creation using the specified ``Types`` is supported,
            ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``asset_id`` or ``asset_content_record_types`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        url_path = construct_url('authorization',
                                 bank_id=self._catalog_idstr)
        return self._get_request(url_path)['assetHints']['canCreate']

    def get_asset_content_form_for_create(self, asset_id=None, asset_content_record_types=None):
        """Gets an asset content form for creating new assets.

        :param asset_id: the ``Id`` of an ``Asset``
        :type asset_id: ``osid.id.Id``
        :param asset_content_record_types: array of asset content record types
        :type asset_content_record_types: ``osid.type.Type[]``
        :return: the asset content form
        :rtype: ``osid.repository.AssetContentForm``
        :raise: ``NotFound`` -- ``asset_id`` is not found
        :raise: ``NullArgument`` -- ``asset_id`` or ``asset_content_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form for requested record types

        *compliance: mandatory -- This method must be implemented.*

        """
        if asset_id is None:
            raise NullArgument()
        if asset_content_record_types is None:
            pass  # Still need to deal with the record_types argument
        asset_content_form = objects.AssetContentForm(asset_id=asset_id)
        self._forms[asset_content_form.get_id().get_identifier()] = not CREATED
        return asset_content_form

    def create_asset_content(self, asset_content_form=None):
        """Creates new ``AssetContent`` for a given asset.

        :param asset_content_form: the form for this ``AssetContent``
        :type asset_content_form: ``osid.repository.AssetContentForm``
        :return: the new ``AssetContent``
        :rtype: ``osid.repository.AssetContent``
        :raise: ``IllegalState`` -- ``asset_content_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``asset_content_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``asset_content_form`` did not originate from ``get_asset_content_form_for_create()``

        *compliance: mandatory -- This method must be implemented.*

        """
        if asset_content_form is None:
            raise NullArgument()
        if not isinstance(asset_content_form, abc_repository_objects.AssetContentForm):
            raise InvalidArgument('argument type is not an AssetContentForm')
        if asset_content_form.is_for_update():
            raise InvalidArgument('form is for update only, not create')
        try:
            if self._forms[asset_content_form.get_id().get_identifier()] == CREATED:
                raise IllegalState('form already used in a create transaction')
        except KeyError:
            raise Unsupported('form did not originate from this session')
        if not asset_content_form.is_valid():
            raise InvalidArgument('one or more of the form elements is invalid')

        url_path = construct_url('assets',
                                 bank_id=self._catalog_idstr,
                                 asset_id=asset_content_form._asset_id)
        asset = objects.Asset(self._get_request(url_path))
        previous_contents = asset._my_map['assetContents']
        previous_content_ids = [c['id'] for c in previous_contents]
        asset._my_map['assetContents'].append(asset_content_form._my_map)
        url_path = construct_url('assets',
                                 bank_id=self._catalog_idstr)
        try:
            result = self._put_request(url_path, asset._my_map)
        except Exception:
            raise  # OperationFailed
        self._forms[asset_content_form.get_id().get_identifier()] = CREATED
        content = result['assetContents']
        if len(content) == 1:
            return objects.AssetContent(content[0])
        else:
            # Assumes that in the split second this requires,
            # no one else creates a new asset content for this
            # asset...
            for c in content:
                if c['id'] not in previous_content_ids:
                    return objects.AssetContent(c)

    def can_update_asset_contents(self, asset_id=None):
        """Tests if this user can update ``AssetContent``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating an
        ``AssetContent`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        update operations to an unauthorized user.

        :param asset_id: the ``Id`` of an ``Asset``
        :type asset_id: ``osid.id.Id``
        :return: ``false`` if ``AssetContent`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``asset_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        url_path = construct_url('authorization',
                                 bank_id=self._catalog_idstr)
        return self._get_request(url_path)['assetHints']['canUpdate']

    def get_asset_content_form_for_update(self, asset_content_id=None):
        """Gets the asset form for updating content for an existing asset.

        A new asset content form should be requested for each update
        transaction.

        :param asset_content_id: the ``Id`` of the ``AssetContent``
        :type asset_content_id: ``osid.id.Id``
        :return: the asset content form
        :rtype: ``osid.repository.AssetContentForm``
        :raise: ``NotFound`` -- ``asset_content_id`` is not found
        :raise: ``NullArgument`` -- ``asset_content_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        if asset_content_id is None:
            raise NullArgument()
        asset = None
        for a in AssetLookupSession(self._repository_id,
                                    proxy=self._proxy,
                                    runtime=self._runtime).get_assets():
            # might want to set plenary view
            # to assure ordering?
            for ac in a.get_asset_contents():
                if ac.get_id() == asset_content_id:
                    asset = a
                    asset_content = ac
        if asset is None:
            raise NotFound()
        asset_content_form = objects.AssetContentForm(asset_content._my_map, asset_id=asset.get_id())
        self._forms[asset_content_form.get_id().get_identifier()] = not UPDATED
        return asset_content_form

    def update_asset_content(self, asset_content_form=None):
        """Updates an existing asset.

        :param asset_content_form: the form containing the elements to be updated
        :type asset_content_form: ``osid.repository.AssetContentForm``
        :raise: ``IllegalState`` -- ``asset_content_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``asset_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``asset_content_form`` did not originate from ``get_asset_content_form_for_update()``

        *compliance: mandatory -- This method must be implemented.*

        """
        if asset_content_form is None:
            raise NullArgument()
        if not isinstance(asset_content_form, abc_repository_objects.AssetContentForm):
            raise InvalidArgument('argument type is not an AssetContentForm')
        if not asset_content_form.is_for_update():
            raise InvalidArgument('form is for create only, not update')
        try:
            if self._forms[asset_content_form.get_id().get_identifier()] == CREATED:
                raise IllegalState('form already used in a create transaction')
        except KeyError:
            raise Unsupported('form did not originate from this session')
        if not asset_content_form.is_valid():
            raise InvalidArgument('one or more of the form elements is invalid')

        url_path = construct_url('assets',
                                 bank_id=self._catalog_idstr,
                                 asset_id=asset_content_form._asset_id)
        asset = objects.Asset(self._get_request(url_path))
        index = 0
        for ac in asset.get_asset_contents():
            if str(ac.get_id()) == asset_content_form._my_map['id']:
                break
            index += 1
        asset._my_map['assetContents'].pop(index)
        asset._my_map['assetContents'].insert(index, asset_content_form._my_map)
        url_path = construct_url('assets',
                                 bank_id=self._catalog_idstr)
        try:
            result = self._put_request(url_path, asset._my_map)
        except Exception:
            raise  # OperationFailed
        self._forms[asset_content_form.get_id().get_identifier()] = CREATED
        return objects.AssetContent(asset_content_form._my_map)

    def can_delete_asset_contents(self, asset_id=None):
        """Tests if this user can delete ``AssetsContent`` from ``Assets``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting an
        ``AssetContent`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        delete operations to an unauthorized user.

        :param asset_id: the ``Id`` of an ``Asset``
        :type asset_id: ``osid.id.Id``
        :return: ``false`` if ``AssetContent`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``asset_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        url_path = construct_url('authorization',
                                 bank_id=self._catalog_idstr)
        return self._get_request(url_path)['assetHints']['canDelete']

    def delete_asset_content(self, asset_content_id=None):
        """Deletes content from an ``Asset``.

        :param asset_content_id: the ``Id`` of the ``AssetContent``
        :type asset_content_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``asset_content_id`` is not found
        :raise: ``NullArgument`` -- ``asset_content_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        if asset_content_id is None:
            raise NullArgument()
        asset = None
        for a in AssetLookupSession(self._repository_id,
                                    proxy=self._proxy,
                                    runtime=self._runtime).get_assets():
            i = 0
            # might want to set plenary view
            # to assure ordering?
            for ac in a.get_asset_contents():
                if ac.get_id() == asset_content_id:
                    asset = a
                    asset_content = ac
                    index = i
                i += 1
        if asset is None:
            raise NotFound()

        asset._my_map['assetContents'].pop(index)
        url_path = construct_url('assets',
                                 bank_id=self._catalog_idstr)
        try:
            result = self._put_request(url_path, asset._my_map)
        except Exception:
            raise  # OperationFailed


class RepositoryLookupSession(abc_repository_sessions.RepositoryLookupSession, osid_sessions.OsidSession):
    """This session provides methods for retrieving ``Repository`` objects.

    The ``Repository`` represents a collection of ``Assets`` and
    ``Compositions``.

    This session defines views that offer differing behaviors when
    retrieving multiple objects.

      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete set or is an error condition


    Generally, the comparative view should be used for most applications
    as it permits operation even if there is data that cannot be
    accessed. For example, a browsing application may only need to
    examine the ``Repositories`` it can access, without breaking
    execution. However, an administrative application may require all
    ``Repository`` elements to be available.

    Repositories may have an additional records indicated by their
    respective record types. The record may not be accessed through a
    cast of the ``Repository``.

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
        self._repository_view = COMPARATIVE

    def can_lookup_repositories(self):
        """Tests if this user can perform ``Repository`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        url_path = construct_url('authorization',
                                 bank_id=self._repository_id_str)
        return self._get_request(url_path)['objectiveBankHints']['canLookup']

    def use_comparative_repository_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        self._repository_view = COMPARATIVE

    def use_plenary_repository_view(self):
        """A complete view of the ``Repository`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        self._repository_view = COMPARATIVE

    def get_repository(self, repository_id=None):
        """Gets the ``Repository`` specified by its ``Id``.

        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Repository`` may have a
        different ``Id`` than requested, such as the case where a
        duplicate ``Id`` was assigned to a ``Repository`` and retained
        for compatibility.

        :param repository_id: ``Id`` of the ``Repository``
        :type repository_id: ``osid.id.Id``
        :return: the repository
        :rtype: ``osid.repository.Repository``
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method is must be implemented.*

        """
        if repository_id is None:
            raise NullArgument()
        url_path = construct_url('objective_banks',
                                 bank_id=repository_id)
        return objects.Repository(self._get_request(url_path))

    def get_repositories_by_ids(self, repository_ids=None):
        """Gets a ``RepositoryList`` corresponding to the given ``IdList``.

        In plenary mode, the returned list contains all of the
        repositories specified in the ``Id`` list, in the order of the
        list, including duplicates, or an error results if an ``Id`` in
        the supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Repositories`` may be omitted from the list and
        may present the elements in any order including returning a
        unique set.

        :param repository_ids: the list of ``Ids`` to retrieve
        :type repository_ids: ``osid.id.IdList``
        :return: the returned ``Repository list``
        :rtype: ``osid.repository.RepositoryList``
        :raise: ``NotFound`` -- an ``Id`` was not found
        :raise: ``NullArgument`` -- ``repository_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        if repository_ids is None:
            raise NullArgument()
        repositories = []
        for i in repository_ids:
            repository = None
            url_path = construct_url('objective_banks',
                                     bank_id=i)
            try:
                repository = self._get_request(url_path)
            except (NotFound, OperationFailed):
                if self._repository_view == PLENARY:
                    raise
                else:
                    pass
            if repository:
                if not (self._repository_view == COMPARATIVE and
                        repository in repositories):
                    repositories.append(repository)
        return objects.RepositoryList(repositories)

    def get_repositories_by_genus_type(self, repository_genus_type=None):
        """Gets a ``RepositoryList`` corresponding to the given repository genus ``Type`` which
            does not include repositories of types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known
        repositories or an error results. Otherwise, the returned list
        may contain only those repositories that are accessible through
        this session.

        :param repository_genus_type: a repository genus type
        :type repository_genus_type: ``osid.type.Type``
        :return: the returned ``Repository list``
        :rtype: ``osid.repository.RepositoryList``
        :raise: ``NullArgument`` -- ``repository_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        if repository_genus_type is None:
            raise NullArgument()
        url_path = construct_url('objective_banks')
        repositories_of_type = []
        all_repositories = self._get_request(url_path)
        for repository in all_repositories:
            # DO WE NEED TO CHECK ALL THREE ATRIBUTES OF THE Id HERE?
            if repository['genusTypeId'] == repository_genus_type.get_identifier():
                repositories_of_type.append[repository]
        return objects.RepositoryList(repositories_of_type)

    def get_repositories_by_parent_genus_type(self, repository_genus_type=None):
        """Gets a ``RepositoryList`` corresponding to the given repository genus ``Type`` and
            include any additional repositories with genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known
        repositories or an error results. Otherwise, the returned list
        may contain only those repositories that are accessible through
        this session.

        :param repository_genus_type: a repository genus type
        :type repository_genus_type: ``osid.type.Type``
        :return: the returned ``Repository list``
        :rtype: ``osid.repository.RepositoryList``
        :raise: ``NullArgument`` -- ``repository_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

    def get_repositories_by_record_type(self, repository_record_type=None):
        """Gets a ``RepositoryList`` containing the given repository record ``Type``.

        In plenary mode, the returned list contains all known
        repositories or an error results. Otherwise, the returned list
        may contain only those repositories that are accessible through
        this session.

        :param repository_record_type: a repository record type
        :type repository_record_type: ``osid.type.Type``
        :return: the returned ``Repository list``
        :rtype: ``osid.repository.RepositoryList``
        :raise: ``NullArgument`` -- ``repository_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

    def get_repositories_by_provider(self, resource_id=None):
        """Gets a ``RepositoryList`` from the given provider ````.

        In plenary mode, the returned list contains all known
        repositories or an error results. Otherwise, the returned list
        may contain only those repositories that are accessible through
        this session.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :return: the returned ``Repository list``
        :rtype: ``osid.repository.RepositoryList``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

    def get_repositories(self):
        """Gets all ``Repositories``.

        In plenary mode, the returned list contains all known
        repositories or an error results. Otherwise, the returned list
        may contain only those repositories that are accessible through
        this session.

        :return: a list of ``Repositories``
        :rtype: ``osid.repository.RepositoryList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        url_path = construct_url('objective_banks')
        return objects.RepositoryList(self._get_request(url_path))

    repositories = property(fget=get_repositories)


class RepositoryQuerySession(abc_repository_sessions.RepositoryQuerySession, osid_sessions.OsidSession):
    """This session provides methods for searching among ``Repository`` objects.

    The search query is constructed using the ``RepositoryQuery``.

    Repositories may have a query record indicated by their respective
    record types. The query record is accessed via the
    ``RepositoryQuery``.

    """

    def can_search_repositories(self):
        """Tests if this user can perform ``Repository`` searches.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.

        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    def get_repository_query(self):
        """Gets a repository query.

        :return: the repository query
        :rtype: ``osid.repository.RepositoryQuery``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.repository.RepositoryQuery

    repository_query = property(fget=get_repository_query)

    def get_repositories_by_query(self, repository_query=None):
        """Gets a list of ``Repositories`` matching the given repository query.

        :param repository_query: the repository query
        :type repository_query: ``osid.repository.RepositoryQuery``
        :return: the returned ``RepositoryList``
        :rtype: ``osid.repository.RepositoryList``
        :raise: ``NullArgument`` -- ``repository_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``repository_query`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.repository.RepositoryList


class RepositorySearchSession(RepositoryQuerySession):
    """This session provides methods for searching among ``Repository`` objects.

    The search query is constructed using the ``RepositoryQuery``.

    ``get_repositories_by_query()`` is the basic search method and
    returns a list of ``Repository`` objects.A more advanced search may
    be performed with ``getRepositoriesBySearch()``. It accepts a
    ``RepositorySearch`` in addition to the query for the purpose of
    specifying additional options affecting the entire search, such as
    ordering. ``get_repositories_by_search()`` returns a
    ``RepositorySearchResults`` that can be used to access the resulting
    ``RepositoryList`` or be used to perform a search within the result
    set through ``RepositorySearch``.

    Repositories may have a query record indicated by their respective
    record types. The query record is accessed via the
    ``RepositoryQuery``.

    """

    def get_repository_search(self):
        """Gets a repository search.

        :return: the repository search
        :rtype: ``osid.repository.RepositorySearch``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.repository.RepositorySearch

    repository_search = property(fget=get_repository_search)

    def get_repository_search_order(self):
        """Gets a repository search order.

        The ``RepositorySearchOrder`` is supplied to a
        ``RepositorySearch`` to specify the ordering of results.

        :return: the repository search order
        :rtype: ``osid.repository.RepositorySearchOrder``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.repository.RepositorySearchOrder

    repository_search_order = property(fget=get_repository_search_order)

    def get_repositories_by_search(self, repository_query=None, repository_search=None):
        """Gets the search results matching the given search query using the given search.

        :param repository_query: the repository query
        :type repository_query: ``osid.repository.RepositoryQuery``
        :param repository_search: the repository search
        :type repository_search: ``osid.repository.RepositorySearch``
        :return: the repository search results
        :rtype: ``osid.repository.RepositorySearchResults``
        :raise: ``NullArgument`` -- ``repository_query`` or ``repository_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``repository_query`` or ``repository_search`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.repository.RepositorySearchResults

    def get_repository_query_from_inspector(self, repository_query_inspector=None):
        """Gets a repository query from an inspector.

        The inspector is available from a ``RepositorySearchResults``.

        :param repository_query_inspector: a repository query inspector
        :type repository_query_inspector: ``osid.repository.RepositoryQueryInspector``
        :return: the repository query
        :rtype: ``osid.repository.RepositoryQuery``
        :raise: ``NullArgument`` -- ``repository_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``repository_query_inspector`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.repository.RepositoryQuery


class RepositoryAdminSession(abc_repository_sessions.RepositoryAdminSession, osid_sessions.OsidSession):
    """This session creates, updates, and deletes ``Repositories``.

    The data for create and update is provided by the consumer via the
    form object. ``OsidForms`` are requested for each create or update
    and may not be reused.

    Create and update operations differ in their usage. To create a
    ``Repository,`` a ``RepositoryForm`` is requested using
    ``get_repository_form_for_create()`` specifying the desired record
    ``Types`` or none if no record ``Types`` are needed. The returned
    ``RepositoryForm`` will indicate that it is to be used with a create
    operation and can be used to examine metdata or validate data prior
    to creation. Once the ``RepositoryForm`` is submiited to a create
    operation, it cannot be reused with another create operation unless
    the first operation was unsuccessful. Each ``RepositoryForm``
    corresponds to an attempted transaction.

    For updates, ``RepositoryForms`` are requested to the ``Repository``
    ``Id`` that is to be updated using ``getRepositoryFormForUpdate()``.
    Similarly, the ``RepositoryForm`` has metadata about the data that
    can be updated and it can perform validation before submitting the
    update. The ``RepositoryForm`` can only be used once for a
    successful update and cannot be reused.

    The delete operations delete ``Repositories``. This session includes
    an ``Id`` aliasing mechanism to assign an external ``Id`` to an
    internally assigned Id.

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

    def can_create_repositories(self):
        """Tests if this user can create ``Repositories``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a
        ``Repository`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        create operations to unauthorized users.

        :return: ``false`` if ``Repository`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        url_path = construct_url('authorization',
                                 bank_id=self._catalog_idstr)
        return self._get_request(url_path)['objectiveBankHints']['canCreate']

    def can_create_repository_with_record_types(self, repository_record_types=None):
        """Tests if this user can create a single ``Repository`` using the desired record types.

        While ``RepositoryManager.getRepositoryRecordTypes()`` can be
        used to examine which records are supported, this method tests
        which record(s) are required for creating a specific
        ``Repository``. Providing an empty array tests if a
        ``Repository`` can be created with no records.

        :param repository_record_types: array of repository record types
        :type repository_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Repository`` creation using the specified ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``repository_record_types`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        url_path = construct_url('authorization',
                                 bank_id=self._catalog_idstr)
        return self._get_request(url_path)['objectiveBankHints']['canCreate']

    def get_repository_form_for_create(self, repository_record_types=None):
        """Gets the repository form for creating new repositories.

        A new form should be requested for each create transaction.

        :param repository_record_types: array of repository record types
        :type repository_record_types: ``osid.type.Type[]``
        :return: the repository form
        :rtype: ``osid.repository.RepositoryForm``
        :raise: ``NullArgument`` -- ``repository_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form for requested record types

        *compliance: mandatory -- This method must be implemented.*

        """
        if repository_record_types is None:
            pass  # Still need to deal with the record_types argument
        repository_form = objects.RepositoryForm()
        self._forms[repository_form.get_id().get_identifier()] = not CREATED
        return repository_form

    def create_repository(self, repository_form=None):
        """Creates a new ``Repository``.

        :param repository_form: the form for this ``Repository``
        :type repository_form: ``osid.repository.RepositoryForm``
        :return: the new ``Repository``
        :rtype: ``osid.repository.Repository``
        :raise: ``IllegalState`` -- ``repository_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``repository_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``repository_form`` did not originate from ``get_repository_form_for_create()``

        *compliance: mandatory -- This method must be implemented.*

        """
        if repository_form is None:
            raise NullArgument()
        if not isinstance(repository_form, abc_repository_objects.RepositoryForm):
            raise InvalidArgument('argument type is not a RepositoryForm')
        if repository_form.is_for_update():
            raise InvalidArgument('form is for update only, not create')
        try:
            if self._forms[repository_form.get_id().get_identifier()] == CREATED:
                raise IllegalState('form already used in a create transaction')
        except KeyError:
            raise Unsupported('form did not originate from this session')
        if not repository_form.is_valid():
            raise InvalidArgument('one or more of the form elements is invalid')

        url_path = construct_url('objective_banks')
        try:
            result = self._post_request(url_path, repository_form._my_map)
        except Exception:
            raise  # OperationFailed
        self._forms[repository_form.get_id().get_identifier()] = CREATED
        return objects.Repository(result)

    def can_update_repositories(self):
        """Tests if this user can update ``Repositories``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a
        ``Repository`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        update operations to unauthorized users.

        :return: ``false`` if ``Repository`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        url_path = construct_url('authorization',
                                 bank_id=self._catalog_idstr)
        return self._get_request(url_path)['objectiveBankHints']['canUpdate']

    def get_repository_form_for_update(self, repository_id=None):
        """Gets the repository form for updating an existing repository.

        A new repository form should be requested for each update
        transaction.

        :param repository_id: the ``Id`` of the ``Repository``
        :type repository_id: ``osid.id.Id``
        :return: the repository form
        :rtype: ``osid.repository.RepositoryForm``
        :raise: ``NotFound`` -- ``repository_id`` is not found
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        if repository_id is None:
            raise NullArgument()
        try:
            repository = RepositoryLookupSession(proxy=self._proxy,
                                                 runtime=self._runtime).get_repository(repository_id)
        except Exception:
            raise
        repository_form = objects.RepositoryForm(repository._my_map)
        self._forms[repository_form.get_id().get_identifier()] = not UPDATED
        return repository_form

    def update_repository(self, repository_form=None):
        """Updates an existing repository.

        :param repository_form: the form containing the elements to be updated
        :type repository_form: ``osid.repository.RepositoryForm``
        :raise: ``IllegalState`` -- ``repository_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``repository_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``repository_form`` did not originate from ``get_repository_form_for_update()``

        *compliance: mandatory -- This method must be implemented.*

        """
        if repository_form is None:
            raise NullArgument()
        if not isinstance(repository_form, abc_repository_objects.RepositoryForm):
            raise InvalidArgument('argument type is not a RepositoryForm')
        if not repository_form.is_for_update():
            raise InvalidArgument('form is for create only, not update')

        # Check for "sandbox" genus type.  Hardcoded for now:
        if repository_form._my_map['genusTypeId'] != 'mc3-objectivebank%3Amc3.learning.objectivebank.sandbox%40MIT-OEIT':
            raise PermissionDenied('Handcar only supports updating \'sandbox\' type Repositories')

        try:
            if self._forms[repository_form.get_id().get_identifier()] == UPDATED:
                raise IllegalState('form already used in an update transaction')
        except KeyError:
            raise Unsupported('form did not originate from this session')
        if not repository_form.is_valid():
            raise InvalidArgument('one or more of the form elements is invalid')

        url_path = construct_url('objective_banks')
        try:
            result = self._put_request(url_path, repository_form._my_map)
        except Exception:
            raise  # OperationFailed
        self._forms[repository_form.get_id().get_identifier()] = UPDATED
        return objects.Repository(result)  # Not expected to return anything

    def can_delete_repositories(self):
        """Tests if this user can delete ``Repositories``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a
        ``Repository`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        delete operations to unauthorized users.

        :return: ``false`` if ``Repository`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        url_path = construct_url('authorization',
                                 bank_id=self._catalog_idstr)
        return self._get_request(url_path)['objectiveBankHints']['canDelete']

    def delete_repository(self, repository_id=None):
        """Deletes a ``Repository``.

        :param repository_id: the ``Id`` of the ``Repository`` to remove
        :type repository_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        if repository_id is None:
            raise NullArgument()
        if not isinstance(repository_id, Id):
            raise InvalidArgument('argument type is not an osid Id')

        # Check for "sandbox" genus type.  Hardcoded for now:
        try:
            repository = RepositoryLookupSession(proxy=self._proxy,
                                                 runtime=self._runtime).get_repository(repository_id)
        except Exception:
            raise
        if repository._my_map['genusTypeId'] != 'mc3-objectivebank%3Amc3.learning.objectivebank.sandbox%40MIT-OEIT':
            raise PermissionDenied('Handcar only supports deleting \'sandbox\' type Repositories')

        url_path = construct_url('objective_banks',
                                 bank_id=repository_id)
        result = self._delete_request(url_path)
        return objects.Repository(result)  # Not expected to return anything

    def can_manage_repository_aliases(self):
        """Tests if this user can manage ``Id`` aliases for repositories.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``Repository`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return False  # Not yet implemented

    def alias_repository(self, repository_id=None, alias_id=None):
        """Adds an ``Id`` to a ``Repository`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``Repository`` is determined by the
        provider. The new ``Id`` is an alias to the primary ``Id``. If
        the alias is a pointer to another repository, it is reassigned
        to the given repository ``Id``.

        :param repository_id: the ``Id`` of a ``Repository``
        :type repository_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is in use as a primary ``Id``
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``repository_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()


class RepositoryHierarchySession(abc_repository_sessions.RepositoryHierarchySession, osid_sessions.OsidSession):
    """This session defines methods for traversing a hierarchy of ``Repository`` objects.

    Each node in the hierarchy is a unique ``Repository``. The hierarchy
    may be traversed recursively to establish the tree structure through
    ``get_parents()`` and ``getChildren()``. To relate these ``Ids`` to
    another OSID, ``get_ancestors()`` and ``get_descendants()`` can be
    used for retrievals that can be used for bulk lookups in other
    OSIDs. Any ``Repository`` available in the Repository OSID is known
    to this hierarchy but does not appear in the hierarchy traversal
    until added as a root node or a child of another node.

    A user may not be authorized to traverse the entire hierarchy. Parts
    of the hierarchy may be made invisible through omission from the
    returns of ``get_parents()`` or ``get_children()`` in lieu of a
    ``PermissionDenied`` error that may disrupt the traversal through
    authorized pathways.

    This session defines views that offer differing behaviors when
    retrieving multiple objects.

      * comparative view: repository elements may be silently omitted or
        re-ordered
      * plenary view: provides a complete set or is an error condition


    """

    def get_repository_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    repository_hierarchy_id = property(fget=get_repository_hierarchy_id)

    def get_repository_hierarchy(self):
        """Gets the hierarchy associated with this session.

        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.hierarchy.Hierarchy

    repository_hierarchy = property(fget=get_repository_hierarchy)

    def can_access_repository_hierarchy(self):
        """Tests if this user can perform hierarchy queries.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations.

        :return: ``false`` if hierarchy traversal methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    def use_comparative_repository_view(self):
        """The returns from the repository methods may omit or translate elements based on
            this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_plenary_repository_view(self):
        """A complete view of the ``Repository`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def get_root_repository_ids(self):
        """Gets the root repository ``Ids`` in this hierarchy.

        :return: the root repository ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    root_repository_ids = property(fget=get_root_repository_ids)

    def get_root_repositories(self):
        """Gets the root repositories in the repository hierarchy.

        A node with no parents is an orphan. While all repository
        ``Ids`` are known to the hierarchy, an orphan does not appear in
        the hierarchy unless explicitly added as a root node or child of
        another node.

        :return: the root repositories
        :rtype: ``osid.repository.RepositoryList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method is must be implemented.*

        """
        return  # osid.repository.RepositoryList

    root_repositories = property(fget=get_root_repositories)

    def has_parent_repositories(self, repository_id=None):
        """Tests if the ``Repository`` has any parents.

        :param repository_id: a repository ``Id``
        :type repository_id: ``osid.id.Id``
        :return: ``true`` if the repository has parents, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``repository_id`` is not found
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    def is_parent_of_repository(self, id_, repository_id=None):
        """Tests if an ``Id`` is a direct parent of a repository.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param repository_id: the ``Id`` of a repository
        :type repository_id: ``osid.id.Id``
        :return: ``true`` if this ``id`` is a parent of ``repository_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``repository_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.

        """
        return  # boolean

    def get_parent_repository_ids(self, repository_id=None):
        """Gets the parent ``Ids`` of the given repository.

        :param repository_id: a repository ``Id``
        :type repository_id: ``osid.id.Id``
        :return: the parent ``Ids`` of the repository
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``repository_id`` is not found
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    def get_parent_repositories(self, repository_id=None):
        """Gets the parents of the given repository.

        :param repository_id: the ``Id`` to query
        :type repository_id: ``osid.id.Id``
        :return: the parents of the repository
        :rtype: ``osid.repository.RepositoryList``
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.repository.RepositoryList

    def is_ancestor_of_repository(self, id_=None, repository_id=None):
        """Tests if an ``Id`` is an ancestor of a repository.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param repository_id: the Id of a repository
        :type repository_id: ``osid.id.Id``
        :return: ``true`` if this ``id`` is an ancestor of ``repository_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.

        """
        return  # boolean

    def has_child_repositories(self, repository_id=None):
        """Tests if a repository has any children.

        :param repository_id: a repository ``Id``
        :type repository_id: ``osid.id.Id``
        :return: ``true`` if the ``repository_id`` has children, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    def is_child_of_repository(self, id_=None, repository_id=None):
        """Tests if a node is a direct child of another.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param repository_id: the ``Id`` of a repository
        :type repository_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is a child of ``repository_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.

        """
        return  # boolean

    def get_child_repository_ids(self, repository_id=None):
        """Gets the ``Ids`` of the children of the given repository.

        :param repository_id: the ``Id`` to query
        :type repository_id: ``osid.id.Id``
        :return: the children of the repository
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    def get_child_repositories(self, repository_id=None):
        """Gets the children of the given repository.

        :param repository_id: the ``Id`` to query
        :type repository_id: ``osid.id.Id``
        :return: the children of the repository
        :rtype: ``osid.repository.RepositoryList``
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.repository.RepositoryList

    def is_descendant_of_repository(self, id_=None, repository_id=None):
        """Tests if an ``Id`` is a descendant of a repository.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param repository_id: the ``Id`` of a repository
        :type repository_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is a descendant of the ``repository_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``repository_id`` or ``id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` is not found return ``false``.

        """
        return  # boolean

    def get_repository_node_ids(self,
                                repository_id=None,
                                ancestor_levels=None,
                                descendant_levels=None,
                                include_siblings=None):
        """Gets a portion of the hierarchy for the given repository.

        :param repository_id: the ``Id`` to query
        :type repository_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0
            returns no parents in the node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value
            of 0 returns no children in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false``
            to omit the siblings
        :type include_siblings: ``boolean``
        :return: the specified repository node
        :rtype: ``osid.hierarchy.Node``
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.hierarchy.Node

    def get_repository_nodes(self,
                             repository_id=None,
                             ancestor_levels=None,
                             descendant_levels=None,
                             include_siblings=None):
        """Gets a portion of the hierarchy for the given repository.

        :param repository_id: the ``Id`` to query
        :type repository_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0
            returns no parents in the node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value
            of 0 returns no children in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false``
            to omit the siblings
        :type include_siblings: ``boolean``
        :return: the specified repository node
        :rtype: ``osid.repository.RepositoryNode``
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.repository.RepositoryNode


class RepositoryHierarchyDesignSession(abc_repository_sessions.RepositoryHierarchyDesignSession,
                                       osid_sessions.OsidSession):
    """This session defines methods for managing a hierarchy of ``Repository`` objects.

    Each node in the hierarchy is a unique ``Repository``.

    """

    def get_repository_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    repository_hierarchy_id = property(fget=get_repository_hierarchy_id)

    def get_repository_hierarchy(self):
        """Gets the hierarchy associated with this session.

        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.hierarchy.Hierarchy

    repository_hierarchy = property(fget=get_repository_hierarchy)

    def can_modify_repository_hierarchy(self):
        """Tests if this user can change the hierarchy.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known performing any update
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer these
        operations to an unauthorized user.

        :return: ``false`` if changing this hierarchy is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    def add_root_repository(self, repository_id=None):
        """Adds a root repository.

        :param repository_id: the ``Id`` of a repository
        :type repository_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``repository_id`` is already in hierarchy
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def remove_root_repository(self, repository_id=None):
        """Removes a root repository.

        :param repository_id: the ``Id`` of a repository
        :type repository_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``repository_id`` not a root
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def add_child_repository(self, repository_id=None, child_id=None):
        """Adds a child to a repository.

        :param repository_id: the ``Id`` of a repository
        :type repository_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the new child
        :type child_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``repository_id`` is already a parent of ``child_id``
        :raise: ``NotFound`` -- ``repository_id`` or ``child_id`` not found
        :raise: ``NullArgument`` -- ``repository_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def remove_child_repository(self, repository_id=None, child_id=None):
        """Removes a child from a repository.

        :param repository_id: the ``Id`` of a repository
        :type repository_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the new child
        :type child_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``repository_id`` not a parent of ``child_id``
        :raise: ``NullArgument`` -- ``repository_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def remove_child_repositories(self, repository_id=None):
        """Removes all children from a repository.

        :param repository_id: the ``Id`` of a repository
        :type repository_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``repository_id`` not in hierarchy
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass
