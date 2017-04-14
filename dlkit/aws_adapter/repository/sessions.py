"""repository.sessions"""
# pylint: disable=too-many-lines,no-member,protected-access,too-many-public-methods
from ...abstract_osid.repository import sessions as abc_repository_sessions
from ..osid import sessions as osid_sessions
from .objects import Asset, AssetList, AssetContent, AssetContentList, AssetContentForm
from ..types import AWS_ASSET_CONTENT_RECORD_TYPE
from ..osid.osid_errors import NotFound, PermissionDenied, Unimplemented
from ..primitives import Id
from .aws_utils import remove_file
from ...json_ import utilities


class AssetLookupSession(abc_repository_sessions.AssetLookupSession,
                         osid_sessions.OsidSession):
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

    def get_repository_id(self):
        """Gets the ``Repository``  ``Id`` associated with this session.

        return: (osid.id.Id) - the ``Repository Id`` associated with
                this session
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from awsosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_repository_id()

    repository_id = property(fget=get_repository_id)

    def get_repository(self):
        """Gets the ``Repository`` associated with this session.

        return: (osid.repository.Repository) - the ``Repository``
                associated with this session
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from awsosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        return self._provider_session.get_repository()

    repository = property(fget=get_repository)

    def can_lookup_assets(self):
        """Tests if this user can perform ``Asset`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations.

        return: (boolean) - ``false`` if lookup methods are not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from awsosid template for -
        # osid.resource.ResourceLookupSession.can_lookup_resources_template
        return self._provider_session.can_lookup_assets()

    def use_comparative_asset_view(self):
        """The returns from the lookup methods may omit or translate elements
        based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from awsosid template for -
        # osid.resource.ResourceLookupSession.use_comparative_resource_view_template
        self._provider_session.use_comparative_asset_view()

    def use_plenary_asset_view(self):
        """A complete view of the ``Asset`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from awsosid template for -
        # osid.resource.ResourceLookupSession.use_plenary_resource_view_template
        self._provider_session.use_plenary_asset_view()

    def use_federated_repository_view(self):
        """Federates the view for methods in this session.

        A federated view will include assets in repositories which are
        children of this repository in the repository hierarchy.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from awsosid template for -
        # osid.resource.ResourceLookupSession.use_federated_bin_view_template
        self._provider_session.use_federated_repository_view()

    def use_isolated_repository_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts lookups to this repository only.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from awsosid template for -
        # osid.resource.ResourceLookupSession.use_isolated_bin_view_template
        self._provider_session.use_isolated_repository_view()

    def get_asset(self, asset_id=None):
        """Gets the ``Asset`` specified by its ``Id``.

        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Asset`` may have a different
        ``Id`` than requested, such as the case where a duplicate ``Id``
        was assigned to an ``Asset`` and retained for compatibility.

        arg:    asset_id (osid.id.Id): the ``Id`` of the ``Asset`` to
                retrieve
        return: (osid.repository.Asset) - the returned ``Asset``
        raise:  NotFound - no ``Asset`` found with the given ``Id``
        raise:  NullArgument - ``asset_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        return Asset(self._provider_session.get_asset(asset_id), self._config_map)

    # def get_asset_content(self, asset_content_id=None):
    #     """Gets the ``AssetContent`` specified by its ``Id``.
    #
    #     In plenary mode, the exact ``Id`` is found or a ``NotFound``
    #     results. Otherwise, the returned ``Asset`` may have a different
    #     ``Id`` than requested, such as the case where a duplicate ``Id``
    #     was assigned to an ``Asset`` and retained for compatibility.
    #
    #     arg:    asset_id (osid.id.Id): the ``Id`` of the ``Asset`` to
    #             retrieve
    #     return: (osid.repository.Asset) - the returned ``Asset``
    #     raise:  NotFound - no ``Asset`` found with the given ``Id``
    #     raise:  NullArgument - ``asset_id`` is ``null``
    #     raise:  OperationFailed - unable to complete request
    #     raise:  PermissionDenied - authorization failure
    #     *compliance: mandatory -- This method must be implemented.*
    #
    #     """
    #     return AssetContent(self._provider_session.get_asset_content(asset_content_id), self._config_map)

    def get_assets_by_ids(self, asset_ids=None):
        """Gets an ``AssetList`` corresponding to the given ``IdList``.

        In plenary mode, the returned list contains all of the assets
        specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if an ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Assets`` may be omitted from the list and may
        present the elements in any order including returning a unique
        set.

        arg:    asset_ids (osid.id.IdList): the list of ``Ids`` to
                retrieve
        return: (osid.repository.AssetList) - the returned ``Asset
                list``
        raise:  NotFound - an ``Id`` was not found
        raise:  NullArgument - ``asset_ids`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        return AssetList(self._provider_session.get_assets_by_ids(asset_ids),
                         self._config_map)

    def get_assets_by_genus_type(self, asset_genus_type=None):
        """Gets an ``AssetList`` corresponding to the given asset genus ``Type``
        which does not include assets of types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known assets or
        an error results. Otherwise, the returned list may contain only
        those assets that are accessible through this session.

        arg:    asset_genus_type (osid.type.Type): an asset genus type
        return: (osid.repository.AssetList) - the returned ``Asset
                list``
        raise:  NullArgument - ``asset_genus_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        return AssetList(self._provider_session.get_assets_by_genus_type(asset_genus_type),
                         self._config_map)

    def get_assets_by_parent_genus_type(self, asset_genus_type=None):
        """Gets an ``AssetList`` corresponding to the given asset genus ``Type``
        and include any additional assets with genus types derived from the specified
        ``Type``.

        In plenary mode, the returned list contains all known assets or
        an error results. Otherwise, the returned list may contain only
        those assets that are accessible through this session.

        arg:    asset_genus_type (osid.type.Type): an asset genus type
        return: (osid.repository.AssetList) - the returned ``Asset
                list``
        raise:  NullArgument - ``asset_genus_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        return AssetList(self._provider_session.get_assets_by_parent_genus_type(asset_genus_type),
                         self._config_map)

    def get_assets_by_record_type(self, asset_record_type=None):
        """Gets an ``AssetList`` containing the given asset record ``Type``.

        In plenary mode, the returned list contains all known assets or
        an error results. Otherwise, the returned list may contain only
        those assets that are accessible through this session.

        arg:    asset_record_type (osid.type.Type): an asset record type
        return: (osid.repository.AssetList) - the returned ``Asset
                list``
        raise:  NullArgument - ``asset_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        return AssetList(self._provider_session.get_assets_by_record_type(asset_record_type),
                         self._config_map)

    def get_assets_by_provider(self, resource_id=None):
        """Gets an ``AssetList`` from the given provider.

        In plenary mode, the returned list contains all known assets or
        an error results. Otherwise, the returned list may contain only
        those assets that are accessible through this session.

        arg:    resource_id (osid.id.Id): a resource ``Id``
        return: (osid.repository.AssetList) - the returned ``Asset
                list``
        raise:  NullArgument - ``resource_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        return AssetList(self._provider_session.get_assets_by_provider(resource_id),
                         self._config_map)

    def get_assets(self):
        """Gets all ``Assets``.

        In plenary mode, the returned list contains all known assets or
        an error results. Otherwise, the returned list may contain only
        those assets that are accessible through this session.

        return: (osid.repository.AssetList) - a list of ``Assets``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        return AssetList(self._provider_session.get_assets(), self._config_map)

    assets = property(fget=get_assets)


class AssetContentLookupSession(abc_repository_sessions.AssetContentLookupSession, osid_sessions.OsidSession):
    """This session defines methods for retrieving asset contents.

    An ``AssetContent`` represents an element of content stored associated
    with an ``Asset``.

    This lookup session defines several views:

      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete result set or is an error
        condition
      * isolated repository view: All asset content methods in this session
        operate, retrieve and pertain to asset contents defined explicitly in
        the current repository. Using an isolated view is useful for
        managing ``AssetContents`` with the ``AssetAdminSession.``
      * federated repository view: All asset content methods in this session
        operate, retrieve and pertain to all asset contents defined in this
        repository and any other asset contents implicitly available in this
        repository through repository inheritence.


    The methods ``use_federated_repository_view()`` and
    ``use_isolated_repository_view()`` behave as a radio group and one
    should be selected before invoking any lookup methods.

    AssetContents may have an additional records indicated by their respective
    record types. The record may not be accessed through a cast of the
    ``AssetContent``.

    """

    def get_repository_id(self):
        """Gets the ``Repository``  ``Id`` associated with this session.

        :return: the ``Repository Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return self._provider_session.get_repository_id()

    repository_id = property(fget=get_repository_id)

    def get_repository(self):
        """Gets the ``Repository`` associated with this session.

        :return: the ``Repository`` associated with this session
        :rtype: ``osid.repository.Repository``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return self._provider_session.get_repository()

    repository = property(fget=get_repository)

    def can_lookup_asset_contents(self):
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
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    def use_comparative_asset_content_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        self._provider_session.use_comparative_asset_content_view()

    def use_plenary_asset_content_view(self):
        """A complete view of the ``Asset`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        self._provider_session._use_plenary_object_view()

    def use_federated_repository_view(self):
        """Federates the view for methods in this session.

        A federated view will include assets in repositories which are
        children of this repository in the repository hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        self._provider_session._use_federated_catalog_view()

    def use_isolated_repository_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts lookups to this repository only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        self._provider_session._use_isolated_catalog_view()

    @utilities.arguments_not_none
    def get_asset_content(self, asset_content_id):
        """Gets the ``AssetContent`` specified by its ``Id``.

        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``AssetContent`` may have a different
        ``Id`` than requested, such as the case where a duplicate ``Id``
        was assigned to an ``AssetContent`` and retained for compatibility.

        :param asset_content_id: the ``Id`` of the ``AssetContent`` to retrieve
        :type asset_content_id: ``osid.id.Id``
        :return: the returned ``AssetContent``
        :rtype: ``osid.repository.Asset``
        :raise: ``NotFound`` -- no ``AssetContent`` found with the given ``Id``
        :raise: ``NullArgument`` -- ``asset_content_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return AssetContent(self._provider_session.get_asset_content(asset_content_id), self._config_map)

    @utilities.arguments_not_none
    def get_asset_contents_by_ids(self, asset_content_ids):
        """Gets an ``AssetList`` corresponding to the given ``IdList``.

        In plenary mode, the returned list contains all of the asset contents
        specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if an ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible ``AssetContnts`` may be omitted from the list and may
        present the elements in any order including returning a unique
        set.

        :param asset_content_ids: the list of ``Ids`` to retrieve
        :type asset_content_ids: ``osid.id.IdList``
        :return: the returned ``AssetContent list``
        :rtype: ``osid.repository.AssetContentList``
        :raise: ``NotFound`` -- an ``Id`` was not found
        :raise: ``NullArgument`` -- ``asset_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return AssetContentList(self._provider_session.get_asset_contents_by_ids(asset_content_ids), self._config_map)

    @utilities.arguments_not_none
    def get_asset_contents_by_genus_type(self, asset_content_genus_type):
        """Gets an ``AssetContentList`` corresponding to the given asset content genus ``Type`` which does not include asset contents of types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known asset contents or
        an error results. Otherwise, the returned list may contain only
        those asset contents that are accessible through this session.

        :param asset_content_genus_type: an asset content genus type
        :type asset_content_genus_type: ``osid.type.Type``
        :return: the returned ``AssetContent list``
        :rtype: ``osid.repository.AssetContentList``
        :raise: ``NullArgument`` -- ``asset_content_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return AssetContentList(self._provider_session.get_asset_contents_by_genus_type(asset_content_genus_type), self._config_map)

    @utilities.arguments_not_none
    def get_asset_contents_by_parent_genus_type(self, asset_content_genus_type):
        """Gets an ``AssetContentList`` corresponding to the given asset content genus ``Type`` and include any additional asset contents with genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known asset contents or
        an error results. Otherwise, the returned list may contain only
        those asset contents that are accessible through this session.

        :param asset_content_genus_type: an asset content genus type
        :type asset_content_genus_type: ``osid.type.Type``
        :return: the returned ``AssetContent list``
        :rtype: ``osid.repository.AssetContentList``
        :raise: ``NullArgument`` -- ``asset_content_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return AssetContentList(self._provider_session.get_asset_contents_by_parent_genus_type(asset_content_genus_type), self._config_map)

    @utilities.arguments_not_none
    def get_asset_contents_by_record_type(self, asset_content_record_type):
        """Gets an ``AssetContentList`` containing the given asset record ``Type``.

        In plenary mode, the returned list contains all known asset contents or
        an error results. Otherwise, the returned list may contain only
        those asset contents that are accessible through this session.

        :param asset_content_record_type: an asset content record type
        :type asset_content_record_type: ``osid.type.Type``
        :return: the returned ``AssetContent list``
        :rtype: ``osid.repository.AssetContentList``
        :raise: ``NullArgument`` -- ``asset_content_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return AssetContentList(self._provider_session.get_asset_contents_by_record_type(asset_content_record_type), self._config_map)

    @utilities.arguments_not_none
    def get_asset_contents_for_asset(self, asset_id):
        """Gets an ``AssetList`` from the given Asset.

        In plenary mode, the returned list contains all known asset contents or
        an error results. Otherwise, the returned list may contain only
        those asset contents that are accessible through this session.

        :param asset_id: an asset ``Id``
        :type asset_id: ``osid.id.Id``
        :return: the returned ``AssetContent list``
        :rtype: ``osid.repository.AssetContentList``
        :raise: ``NullArgument`` -- ``asset_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return AssetContentList(self._provider_session.get_asset_contents_for_asset(asset_id), self._config_map)

    @utilities.arguments_not_none
    def get_asset_contents_by_genus_type_for_asset(self, asset_content_genus_type, asset_id):
        """Gets an ``AssetContentList`` from the given GenusType and Asset Id.

        In plenary mode, the returned list contains all known asset contents or
        an error results. Otherwise, the returned list may contain only
        those asset contents that are accessible through this session.

        :param asset_content_genus_type: an an asset content genus type
        :type asset_id: ``osid.type.Type``
        :param asset_id: an asset ``Id``
        :type asset_id: ``osid.id.Id``
        :return: the returned ``AssetContent list``
        :rtype: ``osid.repository.AssetContentList``
        :raise: ``NullArgument`` -- ``asset_content_genus_type`` or ``asset_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return AssetContentList(self._provider_session.get_asset_contents_by_genus_type_for_asset(asset_content_genus_type, asset_id), self._config_map)


class AssetQuerySession(abc_repository_sessions.AssetQuerySession,
                        osid_sessions.OsidSession):
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

        return: (osid.id.Id) - the ``Repository Id`` associated with
                this session
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from awsosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_repository_id()

    repository_id = property(fget=get_repository_id)

    def get_repository(self):
        """Gets the ``Repository`` associated with this session.

        return: (osid.repository.Repository) - the ``Repository``
                associated with this session
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from awsosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        return self._provider_session.get_repository()

    repository = property(fget=get_repository)

    def can_search_assets(self):
        """Tests if this user can perform ``Asset`` searches.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.

        return: (boolean) - ``false`` if search methods are not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from awsosid template for -
        # osid.resource.ResourceQuerySession.can_search_resources_template
        return self._provider_session.can_search_assets()

    def use_federated_repository_view(self):
        """Federates the view for methods in this session.

        A federated view will include assets in repositories which are
        children of this repository in the repository hierarchy.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from awsosid template for -
        # osid.resource.ResourceLookupSession.use_federated_bin_view_template
        self._provider_session.use_federated_repository_view()

    def use_isolated_repository_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts lookups to this repository only.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from awsosid template for -
        # osid.resource.ResourceLookupSession.use_isolated_bin_view_template
        self._provider_session.use_isolated_repository_view()

    def get_asset_query(self):
        """Gets an asset query.

        return: (osid.repository.AssetQuery) - the asset query
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from awsosid template for -
        # osid.resource.ResourceQuerySession.get_resource_query_template
        return self._provider_session.get_asset_query()

    asset_query = property(fget=get_asset_query)

    def get_assets_by_query(self, asset_query=None):
        """Gets a list of ``Assets`` matching the given asset query.

        arg:    asset_query (osid.repository.AssetQuery): the asset
                query
        return: (osid.repository.AssetList) - the returned ``AssetList``
        raise:  NullArgument - ``asset_query`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - the ``asset_query`` is not of this service
        *compliance: mandatory -- This method must be implemented.*

        """
        return AssetList(self._provider_session.get_assets_by_query(asset_query),
                         self._config_map)

    def get_asset_content_query(self):
        """Gets an asset content query.

        return: (osid.repository.AssetContentQuery) - the asset content query
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._provider_session.get_asset_content_query()

    asset_content_query = property(fget=get_asset_content_query)

    def get_asset_contents_by_query(self, asset_content_query=None):
        """Gets a list of ``AssetContents`` matching the given asset content query.

        arg:    asset_content_query (osid.repository.AssetContentQuery): the asset
                content query
        return: (osid.repository.AssetContentList) - the returned ``AssetContentList``
        raise:  NullArgument - ``asset_content_query`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - the ``asset_content_query`` is not of this service
        *compliance: mandatory -- This method must be implemented.*

        """
        return AssetContentList(self._provider_session.get_asset_contents_by_query(asset_content_query),
                                self._config_map)


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

      PhotographRecordForm photoForm = (PhotographRecordForm)
      form.getRecordForm(assetPhotogaphType);
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

    def __init__(self, provider_session, config_map, lookup_session, proxy=None):
        osid_sessions.OsidSession.__init__(self, provider_session, config_map, proxy)
        self._asset_lookup_session = lookup_session

    def get_repository_id(self):
        """Gets the ``Repository``  ``Id`` associated with this session.

        return: (osid.id.Id) - the ``Repository Id`` associated with
                this session
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from awsosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_repository_id()

    repository_id = property(fget=get_repository_id)

    def get_repository(self):
        """Gets the ``Repository`` associated with this session.

        return: (osid.repository.Repository) - the ``Repository``
                associated with this session
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from awsosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        return self._provider_session.get_repository()

    repository = property(fget=get_repository)

    def can_create_assets(self):
        """Tests if this user can create ``Assets``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating an ``Asset``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer create
        operations to an unauthorized user.

        return: (boolean) - ``false`` if ``Asset`` creation is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from awsosid template for -
        # osid.resource.ResourceLookupSession.can_create_resources_template
        return self._provider_session.can_create_assets()

    def can_create_asset_with_record_types(self, asset_record_types=None):
        """Tests if this user can create a single ``Asset`` using the desired record types.

        While ``RepositoryManager.getAssetRecordTypes()`` can be used to
        examine which records are supported, this method tests which
        record(s) are required for creating a specific ``Asset``.
        Providing an empty array tests if an ``Asset`` can be created
        with no records.

        arg:    asset_record_types (osid.type.Type[]): array of asset
                record types
        return: (boolean) - ``true`` if ``Asset`` creation using the
                specified record ``Types`` is supported, ``false``
                otherwise
        raise:  NullArgument - ``asset_record_types`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from awsosid template for -
        # osid.resource.ResourceAdminSession.can_create_resource_with_record_types_template
        return self._provider_session.can_create_asset_with_record_types(asset_record_types)

    def get_asset_form_for_create(self, asset_record_types=None):
        """Gets the asset form for creating new assets.

        A new form should be requested for each create transaction.

        arg:    asset_record_types (osid.type.Type[]): array of asset
                record types
        return: (osid.repository.AssetForm) - the asset form
        raise:  NullArgument - ``asset_record_types`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - unable to get form for requested record
                types
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from awsosid template for -
        # osid.resource.ResourceAdminSession.get_resource_form_for_create_template
        return self._provider_session.get_asset_form_for_create(asset_record_types)

    def create_asset(self, asset_form=None):
        """Creates a new ``Asset``.

        arg:    asset_form (osid.repository.AssetForm): the form for
                this ``Asset``
        return: (osid.repository.Asset) - the new ``Asset``
        raise:  IllegalState - ``asset_form`` already used in a create
                transaction
        raise:  InvalidArgument - one or more of the form elements is
                invalid
        raise:  NullArgument - ``asset_form`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - ``asset_form`` did not originate from
                ``get_asset_form_for_create()``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from awsosid template for -
        # osid.resource.ResourceAdminSession.create_resource_template
        return self._provider_session.create_asset(asset_form)

    def can_update_assets(self):
        """Tests if this user can update ``Assets``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating an ``Asset``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer update
        operations to an unauthorized user.

        return: (boolean) - ``false`` if ``Asset`` modification is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from awsosid template for -
        # osid.resource.ResourceLookupSession.can_create_resources_template
        return self._provider_session.can_update_assets()

    def get_asset_form_for_update(self, asset_id=None):
        """Gets the asset form for updating an existing asset.

        A new asset form should be requested for each update
        transaction.

        arg:    asset_id (osid.id.Id): the ``Id`` of the ``Asset``
        return: (osid.repository.AssetForm) - the asset form
        raise:  NotFound - ``asset_id`` is not found
        raise:  NullArgument - ``asset_id`` is null
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from awsosid template for -
        # osid.resource.ResourceAdminSession.get_resource_form_for_update_template
        return self._provider_session.get_asset_form_for_update(asset_id)

    def duplicate_asset(self, asset_id):
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.get_resource_form_for_update
        return self._provider_session.duplicate_asset(asset_id)

    def update_asset(self, asset_form=None):
        """Updates an existing asset.

        arg:    asset_form (osid.repository.AssetForm): the form
                containing the elements to be updated
        raise:  IllegalState - ``asset_form`` already used in anupdate
                transaction
        raise:  InvalidArgument - the form contains an invalid value
        raise:  NullArgument - ``asset_form`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - ``asset_form`` did not originate from
                ``get_asset_form_for_update()``
        *compliance: mandatory -- This method must be implemented.*

        """
        return Asset(self._provider_session.update_asset(asset_form), self._config_map)

    def can_delete_assets(self):
        """Tests if this user can delete ``Assets``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting an ``Asset``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer delete
        operations to an unauthorized user.

        return: (boolean) - ``false`` if ``Asset`` deletion is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from awsosid template for -
        # osid.resource.ResourceLookupSession.can_create_resources_template
        return self._provider_session.can_delete_assets()

    def delete_asset(self, asset_id=None):
        """Deletes an ``Asset``.

        arg:    asset_id (osid.id.Id): the ``Id`` of the ``Asset`` to
                remove
        raise:  NotFound - ``asset_id`` not found
        raise:  NullArgument - ``asset_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from awsosid template for -
        # osid.resource.ResourceAdminSession.delete_resource_template
        # clean up AWS
        asset = self._asset_lookup_session.get_asset(asset_id)
        for ac in asset.asset_contents:
            self.delete_asset_content(ac.ident)
        self._provider_session.delete_asset(asset_id)

    def can_manage_asset_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Assets``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        return: (boolean) - ``false`` if ``Asset`` aliasing is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def alias_asset(self, asset_id=None, alias_id=None):
        """Adds an ``Id`` to an ``Asset`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``Asset`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another asset, it is
        reassigned to the given asset ``Id``.

        arg:    asset_id (osid.id.Id): the ``Id`` of an ``Asset``
        arg:    alias_id (osid.id.Id): the alias ``Id``
        raise:  AlreadyExists - ``alias_id`` is already assigned
        raise:  NotFound - ``asset_id`` not found
        raise:  NullArgument - ``asset_id`` or ``alias_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def can_create_asset_content(self):
        """Tests if this user can create content for ``Assets``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating an
        ``AssetContent`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        create operations to an unauthorized user.

        return: (boolean) - ``false`` if ``Asset`` content creation is
                not authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from awsosid template for -
        # osid.resource.ResourceLookupSession.can_create_resources_template
        return self._provider_session.can_create_asset_content()

    def can_create_asset_content_with_record_types(self, asset_content_record_types=None):
        """Tests if this user can create an ``AssetContent`` using the desired record types.

        While ``RepositoryManager.getAssetContentRecordTypes()`` can be
        used to test which records are supported, this method tests
        which records are required for creating a specific
        ``AssetContent``. Providing an empty array tests if an
        ``AssetContent`` can be created with no records.

        arg:    asset_content_record_types (osid.type.Type[]): array of
                asset content record types
        return: (boolean) - ``true`` if ``AssetContent`` creation using
                the specified ``Types`` is supported, ``false``
                otherwise
        raise:  NullArgument - ``asset_content_record_types`` is
                ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from awsosid template for -
        # osid.resource.ResourceAdminSession.can_create_resource_with_record_types_template
        return self._provider_session.can_create_asset_content_with_record_types(
            asset_content_record_types)

    def get_asset_content_form_for_create(self,
                                          asset_id=None,
                                          asset_content_record_types=None):
        """Gets an asset content form for creating new assets.

        arg:    asset_id (osid.id.Id): the ``Id`` of an ``Asset``
        arg:    asset_content_record_types (osid.type.Type[]): array of
                asset content record types
        return: (osid.repository.AssetContentForm) - the asset content
                form
        raise:  NotFound - ``asset_id`` is not found
        raise:  NullArgument - ``asset_id`` or
                ``asset_content_record_types`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - unable to get form for requested record
                types
        *compliance: mandatory -- This method must be implemented.*

        """
        if AWS_ASSET_CONTENT_RECORD_TYPE in asset_content_record_types:
            asset_content_record_types.remove(AWS_ASSET_CONTENT_RECORD_TYPE)
            return AssetContentForm(
                self._provider_session.get_asset_content_form_for_create(
                    asset_id,
                    asset_content_record_types),
                self._config_map,
                self.get_repository_id())
        else:
            return self._provider_session.get_asset_content_form_for_create(
                asset_id,
                asset_content_record_types)

    def create_asset_content(self, asset_content_form=None):
        """Creates new ``AssetContent`` for a given asset.

        arg:    asset_content_form (osid.repository.AssetContentForm):
                the form for this ``AssetContent``
        return: (osid.repository.AssetContent) - the new
                ``AssetContent``
        raise:  IllegalState - ``asset_content_form`` already used in a
                create transaction
        raise:  InvalidArgument - one or more of the form elements is
                invalid
        raise:  NullArgument - ``asset_content_form`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - ``asset_content_form`` did not originate
                from ``get_asset_content_form_for_create()``
        *compliance: mandatory -- This method must be implemented.*

        """
        if isinstance(asset_content_form, AssetContentForm):
            asset_content = self._provider_session.create_asset_content(
                asset_content_form._payload)
        else:
            asset_content = self._provider_session.create_asset_content(
                asset_content_form)
        try:
            if asset_content.has_url() and 'amazonaws.com' in asset_content.get_url():
                return AssetContent(asset_content, self._config_map)
        except TypeError:
            pass
        return asset_content

    def can_update_asset_contents(self):
        """Tests if this user can update ``AssetContent``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating an
        ``AssetContent`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        update operations to an unauthorized user.

        return: (boolean) - ``false`` if ``AssetContent`` modification
                is not authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from awsosid template for -
        # osid.resource.ResourceLookupSession.can_create_resources_template
        return self._provider_session.can_update_asset_contents()

    def get_asset_content_form_for_update(self, asset_content_id=None):
        """Gets the asset content form for updating an existing asset content.

        A new asset content form should be requested for each update
        transaction.

        arg:    asset_content_id (osid.id.Id): the ``Id`` of the
                ``AssetContent``
        return: (osid.repository.AssetContentForm) - the asset content
                form
        raise:  NotFound - ``asset_content_id`` is not found
        raise:  NullArgument - ``asset_content_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        asset_content_form = self._provider_session.get_asset_content_form_for_update(
            asset_content_id)
        if 'amazonaws.com' in asset_content_form.get_url_metadata().get_existing_string_values()[0]:
            return AssetContentForm(asset_content_form,
                                    self._config_map,
                                    self.get_repository_id())
        return asset_content_form

    def update_asset_content(self, asset_content_form=None):
        """Updates an existing asset content.

        arg:    asset_content_form (osid.repository.AssetContentForm):
                the form containing the elements to be updated
        raise:  IllegalState - ``asset_content_form`` already used in an
                update transaction
        raise:  InvalidArgument - the form contains an invalid value
        raise:  NullArgument - ``asset_form`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - ``asset_content_form`` did not originate
                from ``get_asset_content_form_for_update()``
        *compliance: mandatory -- This method must be implemented.*

        """
        if isinstance(asset_content_form, AssetContentForm):
            asset_content = self._provider_session.update_asset_content(
                asset_content_form._payload)
        else:
            asset_content = self._provider_session.update_asset_content(
                asset_content_form)
        if asset_content is not None and asset_content.has_url() and \
                'amazonaws.com' in asset_content.get_url():
            return AssetContent(asset_content, self._config_map)
        return asset_content

    def can_delete_asset_contents(self):
        """Tests if this user can delete ``AssetsContents``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting an
        ``AssetContent`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        delete operations to an unauthorized user.

        return: (boolean) - ``false`` if ``AssetContent`` deletion is
                not authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from awsosid template for -
        # osid.resource.ResourceLookupSession.can_create_resources_template
        return self._provider_session.can_delete_asset_contents()

    def delete_asset_content(self, asset_content_id=None):
        """Deletes content from an ``Asset``.

        arg:    asset_content_id (osid.id.Id): the ``Id`` of the
                ``AssetContent``
        raise:  NotFound - ``asset_content_id`` is not found
        raise:  NullArgument - ``asset_content_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        asset_content = self._get_asset_content(asset_content_id)
        if asset_content.has_url() and 'amazonaws.com' in asset_content.get_url():
            # print "Still have to implement removing files from aws"
            key = asset_content.get_url().split('amazonaws.com')[1]
            remove_file(self._config_map, key)
            self._provider_session.delete_asset_content(asset_content_id)
        else:
            self._provider_session.delete_asset_content(asset_content_id)

    def _get_asset_id_with_enclosure(self, enclosure_id):
        return self._provider_session._get_asset_id_with_enclosure(enclosure_id)

    def _get_asset_content(self, asset_content_id):
        """stub"""
        asset_content = None
        for asset in self._asset_lookup_session.get_assets():
            for content in asset.get_asset_contents():
                if content.get_id() == asset_content_id:
                    asset_content = content
                    break
            if asset_content is not None:
                break
        if asset_content is None:
            raise NotFound('THe AWS Adapter could not find AssetContent ' +
                           str(asset_content_id))
        return asset_content


class RepositoryLookupSession(abc_repository_sessions.RepositoryLookupSession,
                              osid_sessions.OsidSession):
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

    def __init__(self, provider_session, authz_session, proxy=None):
        osid_sessions.OsidSession.__init__(self, provider_session, authz_session, proxy)
        self._qualifier_id = Id('authorization.Qualifier%3AROOT%40dlkit.mit.edu')
        # This needs to be done right
        self._id_namespace = 'repository.Repository'

    def can_lookup_repositories(self):
        """Tests if this user can perform ``Repository`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        return: (boolean) - ``false`` if lookup methods are not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from awsosid template for -
        # osid.resource.ResourceLookupSession.can_lookup_resources_template
        return self._provider_session.can_lookup_repositories()

    def use_comparative_repository_view(self):
        """The returns from the lookup methods may omit or translate elements
        based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from awsosid template for -
        # osid.resource.BinLookupSession.use_comparative_bin_view_template
        self._provider_session.use_comparative_repository_view()

    def use_plenary_repository_view(self):
        """A complete view of the ``Repository`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from awsosid template for -
        # osid.resource.BinLookupSession.use_plenary_bin_view_template
        self._provider_session.use_plenary_repository_view()

    def get_repository(self, repository_id=None):
        """Gets the ``Repository`` specified by its ``Id``.

        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Repository`` may have a
        different ``Id`` than requested, such as the case where a
        duplicate ``Id`` was assigned to a ``Repository`` and retained
        for compatibility.

        arg:    repository_id (osid.id.Id): ``Id`` of the ``Repository``
        return: (osid.repository.Repository) - the repository
        raise:  NotFound - ``repository_id`` not found
        raise:  NullArgument - ``repository_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from awsosid template for -
        # osid.resource.BinLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_repository(repository_id)

    def get_repositories_by_ids(self, repository_ids=None):
        """Gets a ``RepositoryList`` corresponding to the given ``IdList``.

        In plenary mode, the returned list contains all of the
        repositories specified in the ``Id`` list, in the order of the
        list, including duplicates, or an error results if an ``Id`` in
        the supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Repositories`` may be omitted from the list and
        may present the elements in any order including returning a
        unique set.

        arg:    repository_ids (osid.id.IdList): the list of ``Ids`` to
                retrieve
        return: (osid.repository.RepositoryList) - the returned
                ``Repository list``
        raise:  NotFound - an ``Id`` was not found
        raise:  NullArgument - ``repository_ids`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from awsosid template for -
        # osid.resource.BinLookupSession.get_bins_by_ids_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_repositories_by_ids(repository_ids)

    def get_repositories_by_genus_type(self, repository_genus_type=None):
        """Gets a ``RepositoryList`` corresponding to the given repository genus
        ``Type`` which does not include repositories of types derived from the
        specified ``Type``.

        In plenary mode, the returned list contains all known
        repositories or an error results. Otherwise, the returned list
        may contain only those repositories that are accessible through
        this session.

        arg:    repository_genus_type (osid.type.Type): a repository
                genus type
        return: (osid.repository.RepositoryList) - the returned
                ``Repository list``
        raise:  NullArgument - ``repository_genus_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def get_repositories_by_parent_genus_type(self, repository_genus_type=None):
        """Gets a ``RepositoryList`` corresponding to the given repository genus
        ``Type`` and include any additional repositories with genus types
        derived from the specified ``Type``.

        In plenary mode, the returned list contains all known
        repositories or an error results. Otherwise, the returned list
        may contain only those repositories that are accessible through
        this session.

        arg:    repository_genus_type (osid.type.Type): a repository
                genus type
        return: (osid.repository.RepositoryList) - the returned
                ``Repository list``
        raise:  NullArgument - ``repository_genus_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def get_repositories_by_record_type(self, repository_record_type=None):
        """Gets a ``RepositoryList`` containing the given repository record ``Type``.

        In plenary mode, the returned list contains all known
        repositories or an error results. Otherwise, the returned list
        may contain only those repositories that are accessible through
        this session.

        arg:    repository_record_type (osid.type.Type): a repository
                record type
        return: (osid.repository.RepositoryList) - the returned
                ``Repository list``
        raise:  NullArgument - ``repository_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def get_repositories_by_provider(self, resource_id=None):
        """Gets a ``RepositoryList`` from the given provider ````.

        In plenary mode, the returned list contains all known
        repositories or an error results. Otherwise, the returned list
        may contain only those repositories that are accessible through
        this session.

        arg:    resource_id (osid.id.Id): a resource ``Id``
        return: (osid.repository.RepositoryList) - the returned
                ``Repository list``
        raise:  NullArgument - ``resource_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def get_repositories(self):
        """Gets all ``Repositories``.

        In plenary mode, the returned list contains all known
        repositories or an error results. Otherwise, the returned list
        may contain only those repositories that are accessible through
        this session.

        return: (osid.repository.RepositoryList) - a list of
                ``Repositories``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from awsosid template for -
        # osid.resource.BinLookupSession.get_bins_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_repositories()

    repositories = property(fget=get_repositories)


class RepositoryAdminSession(abc_repository_sessions.RepositoryAdminSession,
                             osid_sessions.OsidSession):
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

    def __init__(self, provider_session, authz_session, proxy=None):
        osid_sessions.OsidSession.__init__(self, provider_session, authz_session, proxy)
        self._qualifier_id = Id('authorization.Qualifier%3AROOT%40dlkit.mit.edu')
        # This needs to be done right
        self._id_namespace = 'repository.Repository'

    def can_create_repositories(self):
        """Tests if this user can create ``Repositories``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a
        ``Repository`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        create operations to unauthorized users.

        return: (boolean) - ``false`` if ``Repository`` creation is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from awsosid template for -
        # osid.resource.ResourceLookupSession.can_create_resources_template
        return self._provider_session.can_create_repositories()

    def can_create_repository_with_record_types(self, repository_record_types=None):
        """Tests if this user can create a single ``Repository`` using the desired
        record types.

        While ``RepositoryManager.getRepositoryRecordTypes()`` can be
        used to examine which records are supported, this method tests
        which record(s) are required for creating a specific
        ``Repository``. Providing an empty array tests if a
        ``Repository`` can be created with no records.

        arg:    repository_record_types (osid.type.Type[]): array of
                repository record types
        return: (boolean) - ``true`` if ``Repository`` creation using
                the specified ``Types`` is supported, ``false``
                otherwise
        raise:  NullArgument - ``repository_record_types`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from awsosid template for -
        # osid.resource.ResourceAdminSession.can_create_resource_with_record_types_template
        return self._provider_session.can_create_repository_with_record_types(
            repository_record_types)

    def get_repository_form_for_create(self, repository_record_types=None):
        """Gets the repository form for creating new repositories.

        A new form should be requested for each create transaction.

        arg:    repository_record_types (osid.type.Type[]): array of
                repository record types
        return: (osid.repository.RepositoryForm) - the repository form
        raise:  NullArgument - ``repository_record_types`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - unable to get form for requested record
                types
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from awsosid template for -
        # osid.resource.BinAdminSession.get_bin_form_for_create_template
        if not self._can('create'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_repository_form_for_create(repository_record_types)

    def create_repository(self, repository_form=None):
        """Creates a new ``Repository``.

        arg:    repository_form (osid.repository.RepositoryForm): the
                form for this ``Repository``
        return: (osid.repository.Repository) - the new ``Repository``
        raise:  IllegalState - ``repository_form`` already used in a
                create transaction
        raise:  InvalidArgument - one or more of the form elements is
                invalid
        raise:  NullArgument - ``repository_form`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - ``repository_form`` did not originate from
                ``get_repository_form_for_create()``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from awsosid template for -
        # osid.resource.BinAdminSession.create_bin_template
        if not self._can('create'):
            raise PermissionDenied()
        else:
            return self._provider_session.create_repository(repository_form)

    def can_update_repositories(self):
        """Tests if this user can update ``Repositories``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a
        ``Repository`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        update operations to unauthorized users.

        return: (boolean) - ``false`` if ``Repository`` modification is
                not authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from awsosid template for -
        # osid.resource.ResourceLookupSession.can_create_resources_template
        return self._provider_session.can_update_repositories()

    def get_repository_form_for_update(self, repository_id=None):
        """Gets the repository form for updating an existing repository.

        A new repository form should be requested for each update
        transaction.

        arg:    repository_id (osid.id.Id): the ``Id`` of the
                ``Repository``
        return: (osid.repository.RepositoryForm) - the repository form
        raise:  NotFound - ``repository_id`` is not found
        raise:  NullArgument - ``repository_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from awsosid template for -
        # osid.resource.BinAdminSession.get_bin_form_for_update_template
        if not self._can('update'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_repository_form_for_update(repository_id)

    def update_repository(self, repository_form=None):
        """Updates an existing repository.

        arg:    repository_form (osid.repository.RepositoryForm): the
                form containing the elements to be updated
        raise:  IllegalState - ``repository_form`` already used in an
                update transaction
        raise:  InvalidArgument - the form contains an invalid value
        raise:  NullArgument - ``repository_form`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - ``repository_form`` did not originate from
                ``get_repository_form_for_update()``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from awsosid template for -
        # osid.resource.BinAdminSession.update_bin_template
        if not self._can('update'):
            raise PermissionDenied()
        else:
            return self._provider_session.update_repository(repository_form)

    def can_delete_repositories(self):
        """Tests if this user can delete ``Repositories``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a
        ``Repository`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        delete operations to unauthorized users.

        return: (boolean) - ``false`` if ``Repository`` deletion is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from awsosid template for -
        # osid.resource.ResourceLookupSession.can_create_resources_template
        return self._provider_session.can_delete_repositories()

    def delete_repository(self, repository_id=None):
        """Deletes a ``Repository``.

        arg:    repository_id (osid.id.Id): the ``Id`` of the
                ``Repository`` to remove
        raise:  NotFound - ``repository_id`` not found
        raise:  NullArgument - ``repository_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from awsosid template for -
        # osid.resource.BinAdminSession.delete_bin_template
        if not self._can('delete'):
            raise PermissionDenied()
        else:
            return self._provider_session.delete_repository(repository_id)

    def can_manage_repository_aliases(self):
        """Tests if this user can manage ``Id`` aliases for repositories.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        return: (boolean) - ``false`` if ``Repository`` aliasing is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def alias_repository(self, repository_id=None, alias_id=None):
        """Adds an ``Id`` to a ``Repository`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``Repository`` is determined by the
        provider. The new ``Id`` is an alias to the primary ``Id``. If
        the alias is a pointer to another repository, it is reassigned
        to the given repository ``Id``.

        arg:    repository_id (osid.id.Id): the ``Id`` of a
                ``Repository``
        arg:    alias_id (osid.id.Id): the alias ``Id``
        raise:  AlreadyExists - ``alias_id`` is in use as a primary
                ``Id``
        raise:  NotFound - ``repository_id`` not found
        raise:  NullArgument - ``repository_id`` or ``alias_id`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from awsosid template for -
        # osid.resource.BinAdminSession.alias_bin_template
        if not self._can('alias'):
            raise PermissionDenied()
        else:
            return self._provider_session.alias_repository(repository_id)


class AssetCompositionSession(abc_repository_sessions.AssetCompositionSession, osid_sessions.OsidSession):
    """This session defines methods for looking up ``Asset`` to ``Composition`` mappings.

    A ``Composition`` represents a collection of ``Assets``.

    This lookup session defines several views:

      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete result set or is an error
        condition
      * isolated repository view: All lookup methods in this session
        operate, retrieve and pertain to asseta and compositions defined
        explicitly in the current repository. Using an isolated view is
        useful for managing compositions with the
        CompositionAdminSession.
      * federated repository view: All lookup methods in this session
        operate, retrieve and pertain to all compositions and assets
        defined in this repository and any other compositions implicitly
        available in this repository through repository inheritence.


    The methods ``use_federated_asset_composition_view()`` and
    ``use_isolated_asset_compositiont_view()`` behave as a radio group
    and one should be selected before invoking any lookup methods.

    """

    def get_repository_id(self):
        """Gets the ``Repository``  ``Id`` associated with this session.

        return: (osid.id.Id) - the ``Repository Id`` associated with
                this session
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin_id
        return self._provider_session.get_repository_id()

    repository_id = property(fget=get_repository_id)

    def get_repository(self):
        """Gets the ``Repository`` associated with this session.

        return: (osid.repository.Repository) - the ``Repository``
                associated with this session
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin
        return self._provider_session.get_repository()

    repository = property(fget=get_repository)

    def can_access_asset_compositions(self):
        """Tests if this user can perform composition lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        return: (boolean) - ``false`` if lookup methods are not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

    def use_comparative_asset_composition_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_comparative_resource_view
        self._provider_session.use_comparative_asset_composition_view()

    def use_plenary_asset_composition_view(self):
        """A complete view of the returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_plenary_resource_view
        self._provider_session.use_plenary_asset_composition_view()

    def use_federated_repository_view(self):
        """Federates the view for methods in this session.

        A federated view will include compositions in repositories which
        are children of this repository in the repository hierarchy.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_federated_bin_view
        self._provider_session.use_federated_repository_view()

    def use_isolated_repository_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts lookups to this repository only.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_isolated_bin_view
        self._provider_session.use_isolated_repository_view()

    @utilities.arguments_not_none
    def get_composition_assets(self, composition_id):
        """Gets the list of assets mapped to the given ``Composition``.

        arg:    composition_id (osid.id.Id): ``Id`` of the
                ``Composition``
        return: (osid.repository.AssetList) - list of assets
        raise:  NotFound - ``composition_id`` not found
        raise:  NullArgument - ``composition_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method is must be implemented.*

        """
        self._provider_session.get_composition_assets(composition_id)

    @utilities.arguments_not_none
    def get_compositions_by_asset(self, asset_id):
        """Gets a list of compositions including the given asset.

        arg:    asset_id (osid.id.Id): ``Id`` of the ``Asset``
        return: (osid.repository.CompositionList) - the returned
                ``Composition list``
        raise:  NotFound - ``asset_id`` is not found
        raise:  NullArgument - ``asset_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        self._provider_session.get_compositions_by_asset(asset_id)


class AssetCompositionDesignSession(abc_repository_sessions.AssetCompositionDesignSession, osid_sessions.OsidSession):
    """This session provides the means for adding assets to an asset composiiton.

    The asset is identified inside a composition using its own Id. To
    add the same asset to the composition, multiple compositions should
    be used and placed at the same level in the ``Composition``
    hierarchy.

    """

    def get_repository_id(self):
        """Gets the ``Repository``  ``Id`` associated with this session.

        return: (osid.id.Id) - the ``Repository Id`` associated with
                this session
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin_id
        return self._provider_session.get_repository_id()

    repository_id = property(fget=get_repository_id)

    def get_repository(self):
        """Gets the ``Repository`` associated with this session.

        return: (osid.repository.Repository) - the ``Repository``
                associated with this session
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin
        return self._provider_session.get_repository()

    repository = property(fget=get_repository)

    def can_compose_assets(self):
        """Tests if this user can manage mapping of ``Assets`` to ``Compositions``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as an application hint that may opt not to offer composition
        operations.

        return: (boolean) - ``false`` if asset composiion is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return True

    @utilities.arguments_not_none
    def add_asset(self, asset_id, composition_id):
        """Appends an asset to a composition.

        arg:    asset_id (osid.id.Id): ``Id`` of the ``Asset``
        arg:    composition_id (osid.id.Id): ``Id`` of the
                ``Composition``
        raise:  AlreadyExists - ``asset_id`` already part
                ``composition_id``
        raise:  NotFound - ``asset_id`` or ``composition_id`` not found
        raise:  NullArgument - ``asset_id`` or ``composition_id`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization fauilure
        *compliance: mandatory -- This method must be implemented.*

        """
        self._provider_session.add_asset(self, asset_id, composition_id)

    @utilities.arguments_not_none
    def move_asset_ahead(self, asset_id, composition_id, reference_id):
        """Reorders assets in a composition by moving the specified asset in front of a reference asset.

        arg:    asset_id (osid.id.Id): ``Id`` of the ``Asset``
        arg:    composition_id (osid.id.Id): ``Id`` of the
                ``Composition``
        arg:    reference_id (osid.id.Id): ``Id`` of the reference
                ``Asset``
        raise:  NotFound - ``asset_id`` or ``reference_id``  ``not found
                in composition_id``
        raise:  NullArgument - ``asset_id, reference_id`` or
                ``composition_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization fauilure
        *compliance: mandatory -- This method must be implemented.*

        """
        self._provider_session.move_asset_ahead(self, asset_id, composition_id, reference_id)

    @utilities.arguments_not_none
    def move_asset_behind(self, asset_id, composition_id, reference_id):
        """Reorders assets in a composition by moving the specified asset behind of a reference asset.

        arg:    asset_id (osid.id.Id): ``Id`` of the ``Asset``
        arg:    composition_id (osid.id.Id): ``Id`` of the
                ``Composition``
        arg:    reference_id (osid.id.Id): ``Id`` of the reference
                ``Asset``
        raise:  NotFound - ``asset_id`` or ``reference_id``  ``not found
                in composition_id``
        raise:  NullArgument - ``asset_id, reference_id`` or
                ``composition_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization fauilure
        *compliance: mandatory -- This method must be implemented.*

        """
        self._provider_session.move_asset_behind(self, asset_id, composition_id, reference_id)

    @utilities.arguments_not_none
    def order_assets(self, asset_ids, composition_id):
        """Reorders a set of assets in a composition.

        arg:    asset_ids (osid.id.Id[]): ``Ids`` for a set of
                ``Assets``
        arg:    composition_id (osid.id.Id): ``Id`` of the
                ``Composition``
        raise:  NotFound - ``composition_id`` not found or, an
                ``asset_id`` not related to ``composition_id``
        raise:  NullArgument - ``instruction_ids`` or ``agenda_id`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        self._provider_session.order_assets(self, asset_ids, composition_id)

    @utilities.arguments_not_none
    def remove_asset(self, asset_id, composition_id):
        """Removes an ``Asset`` from a ``Composition``.

        arg:    asset_id (osid.id.Id): ``Id`` of the ``Asset``
        arg:    composition_id (osid.id.Id): ``Id`` of the
                ``Composition``
        raise:  NotFound - ``asset_id``  ``not found in composition_id``
        raise:  NullArgument - ``asset_id`` or ``composition_id`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization fauilure
        *compliance: mandatory -- This method must be implemented.*

        """
        self._provider_session.remove_asset(self, asset_id, composition_id)


class CompositionLookupSession(abc_repository_sessions.CompositionLookupSession, osid_sessions.OsidSession):
    """This session provides methods for retrieving ``Composition`` objects.

    The ``Composition`` represents a collection of ``Assets``.

    This session defines views that offer differing behaviors when
    retrieving multiple objects.

      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete and ordered result set or is
        an error condition
      * isolated repository view: All lookup methods in this session
        operate, retrieve and pertain to compositions defined explicitly
        in the current repository. Using an isolated view is useful for
        managing compositions with the ``CompositionAdminSession.``
      * federated repository view: All composition methods in this
        session operate, retrieve and pertain to all compositions
        defined in this repository and any other compositions implicitly
        available in this repository through repository inheritence.
      * active composition view: All composition lookup methods return
        active compositions.
      * any status composition view: Compositions of any active or
        inactive status are returned from methods.
      * sequestered composition viiew: All composition methods suppress
        sequestered compositions.
      * unsequestered composition view: All composition methods return
        all compositions.


    Generally, the comparative view should be used for most applications
    as it permits operation even if there is data that cannot be
    accessed. For example, a browsing application may only need to
    examine the ``Composition`` it can access, without breaking
    execution. However, an administrative application may require a
    complete set of ``Composition`` objects to be returned.

    Compositions may have an additional records indicated by their
    respective record types. The record may not be accessed through a
    cast of the ``Composition``.

    """
    def get_repository_id(self):
        """Gets the ``Repository``  ``Id`` associated with this session.

        return: (osid.id.Id) - the ``Repository Id`` associated with
                this session
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin_id
        return self._provider_session.get_repository_id()

    repository_id = property(fget=get_repository_id)

    def get_repository(self):
        """Gets the ``Repository`` associated with this session.

        return: (osid.repository.Repository) - the ``Repository``
                associated with this session
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin
        return self._provider_session.get_repository()

    repository = property(fget=get_repository)

    def can_lookup_compositions(self):
        """Tests if this user can perform ``Composition`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        return: (boolean) - ``false`` if lookup methods are not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.can_lookup_resources
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    def use_comparative_composition_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_comparative_resource_view
        self._provider_session.use_comparative_composition_view()

    def use_plenary_composition_view(self):
        """A complete view of the ``Composition`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_plenary_resource_view
        self._provider_session.use_plenary_composition_view()

    def use_federated_repository_view(self):
        """Federates the view for methods in this session.

        A federated view will include compositions in repositories which
        are children of this repository in the repository hierarchy.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_federated_bin_view
        self._provider_session.use_federated_repository_view()

    def use_isolated_repository_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts lookups to this repository only.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_isolated_bin_view
        self._provider_session.use_isolated_repository_view()

    def use_active_composition_view(self):
        """Only active compositions are returned by methods in this session.

        *compliance: mandatory -- This method is must be implemented.*

        """
        self._provider_session.use_active_composition_view()

    def use_any_status_composition_view(self):
        """All active and inactive compositions are returned by methods in this session.

        *compliance: mandatory -- This method is must be implemented.*

        """
        self._provider_session.use_any_status_composition_view()

    def use_sequestered_composition_view(self):
        """The methods in this session omit sequestered compositions.

        *compliance: mandatory -- This method is must be implemented.*

        """
        self._provider_session.use_sequestered_composition_view()

    def use_unsequestered_composition_view(self):
        """The methods in this session return all compositions, including sequestered compositions.

        *compliance: mandatory -- This method is must be implemented.*

        """
        self._provider_session.use_unsequestered_composition_view()

    @utilities.arguments_not_none
    def get_composition(self, composition_id):
        """Gets the ``Composition`` specified by its ``Id``.

        arg:    composition_id (osid.id.Id): ``Id`` of the
                ``Composiiton``
        return: (osid.repository.Composition) - the composition
        raise:  NotFound - ``composition_id`` not found
        raise:  NullArgument - ``composition_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resource
        # NOTE: This implementation currently ignores plenary view
        return self._provider_session.get_composition(composition_id)

    @utilities.arguments_not_none
    def get_compositions_by_ids(self, composition_ids):
        """Gets a ``CompositionList`` corresponding to the given ``IdList``.

        arg:    composition_ids (osid.id.IdList): the list of ``Ids`` to
                retrieve
        return: (osid.repository.CompositionList) - the returned
                ``Composition list``
        raise:  NotFound - an ``Id`` was not found
        raise:  NullArgument - ``composition_ids`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resources_by_ids
        # NOTE: This implementation currently ignores plenary view
        return self._provider_session.get_compositions_by_ids(composition_ids)

    @utilities.arguments_not_none
    def get_compositions_by_genus_type(self, composition_genus_type):
        """Gets a ``CompositionList`` corresponding to the given composition genus ``Type`` which does not include compositions of types derived from the specified ``Type``.

        arg:    composition_genus_type (osid.type.Type): a composition
                genus type
        return: (osid.repository.CompositionList) - the returned
                ``Composition list``
        raise:  NullArgument - ``composition_genus_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resources_by_genus_type
        # NOTE: This implementation currently ignores plenary view
        return self._provider_session.get_compositions_by_genus_type(composition_genus_type)

    @utilities.arguments_not_none
    def get_compositions_by_parent_genus_type(self, composition_genus_type):
        """Gets a ``CompositionList`` corresponding to the given composition genus ``Type`` and include any additional compositions with genus types derived from the specified ``Type``.

        arg:    composition_genus_type (osid.type.Type): a composition
                genus type
        return: (osid.repository.CompositionList) - the returned
                ``Composition list``
        raise:  NullArgument - ``composition_genus_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resources_by_parent_genus_type
        return self._provider_session.get_compositions_by_parent_genus_type(composition_genus_type)

    @utilities.arguments_not_none
    def get_compositions_by_record_type(self, composition_record_type):
        """Gets a ``CompositionList`` containing the given composition record ``Type``.

        arg:    composition_record_type (osid.type.Type): a composition
                record type
        return: (osid.repository.CompositionList) - the returned
                ``Composition list``
        raise:  NullArgument - ``composition_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resources_by_record_type
        # STILL NEED TO IMPLEMENT!!!
        return self._provider_session.get_compositions_by_record_type(composition_record_type)

    @utilities.arguments_not_none
    def get_compositions_by_provider(self, resource_id):
        """Gets a ``CompositionList`` from the given provider ````.

        In plenary mode, the returned list contains all known
        compositions or an error results. Otherwise, the returned list
        may contain only those compositions that are accessible through
        this session.

        In sequestered mode, no sequestered compositions are returned.
        In unsequestered mode, all compositions are returned.

        arg:    resource_id (osid.id.Id): a resource ``Id``
        return: (osid.repository.CompositionList) - the returned
                ``Composition list``
        raise:  NullArgument - ``resource_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._provider_session.get_compositions_by_provider(resource_id)

    def get_compositions(self):
        """Gets all ``Compositions``.

        return: (osid.repository.CompositionList) - a list of
                ``Compositions``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resources
        # NOTE: This implementation currently ignores plenary view
        return self._provider_session.get_compositions()

    compositions = property(fget=get_compositions)


class CompositionAdminSession(abc_repository_sessions.CompositionAdminSession, osid_sessions.OsidSession):
    """This session creates, updates, and deletes ``Compositions``.

    The data for create and update is provided by the consumer via the
    form object. ``OsidForms`` are requested for each create or update
    and may not be reused.

    Create and update operations differ in their usage. To create a
    ``Composition,`` a ``CompositionForm`` is requested using
    ``get_composition_form_for_create()`` specifying the desired record
    ``Types`` or none if no record ``Types`` are needed. The returned
    ``CompositionForm`` will indicate that it is to be used with a
    create operation and can be used to examine metdata or validate data
    prior to creation. Once the ``CompositionForm`` is submiited to a
    create operation, it cannot be reused with another create operation
    unless the first operation was unsuccessful. Each
    ``CompositionForm`` corresponds to an attempted transaction.

    For updates, ``CompositionForms`` are requested to the
    ``Composition``  ``Id`` that is to be updated using
    ``getCompositionFormForUpdate()``. Similarly, the
    ``CompositionForm`` has metadata about the data that can be updated
    and it can perform validation before submitting the update. The
    ``CompositionForm`` can only be used once for a successful update
    and cannot be reused.

    The delete operations delete ``Compositions``. To unmap a
    ``Composition`` from the current ``Repository,`` the
    ``CompositionRepositoryAssignmentSession`` should be used. These
    delete operations attempt to remove the ``Bid`` itself thus removing
    it from all known ``Repository`` catalogs.

    This session includes an ``Id`` aliasing mechanism to assign an
    external ``Id`` to an internally assigned Id.

    """

    def get_repository_id(self):
        """Gets the ``Repository``  ``Id`` associated with this session.

        return: (osid.id.Id) - the ``Repository Id`` associated with
                this session
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin_id
        return self._provider_session.get_repository_id()

    repository_id = property(fget=get_repository_id)

    def get_repository(self):
        """Gets the ``Repository`` associated with this session.

        return: (osid.repository.Repository) - the ``Repository``
                associated with this session
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin
        return self._provider_session.get_repository()

    repository = property(fget=get_repository)

    def can_create_compositions(self):
        """Tests if this user can create ``Compositions``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a
        ``Composition`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        create operations to unauthorized users.

        return: (boolean) - ``false`` if ``Composition`` creation is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.can_create_resources
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def can_create_composition_with_record_types(self, composition_record_types):
        """Tests if this user can create a single ``Composition`` using the desired record types.

        While ``RepositoryManager.getCompositionRecordTypes()`` can be
        used to examine which records are supported, this method tests
        which record(s) are required for creating a specific
        ``Composition``. Providing an empty array tests if a
        ``Composition`` can be created with no records.

        arg:    composition_record_types (osid.type.Type[]): array of
                composition record types
        return: (boolean) - ``true`` if ``Composition`` creation using
                the specified ``Types`` is supported, ``false``
                otherwise
        raise:  NullArgument - ``composition_record_types`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.can_create_resource_with_record_types
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def get_composition_form_for_create(self, composition_record_types):
        """Gets the composition form for creating new compositions.

        A new form should be requested for each create transaction.

        arg:    composition_record_types (osid.type.Type[]): array of
                composition record types
        return: (osid.repository.CompositionForm) - the composition form
        raise:  NullArgument - ``composition_record_types`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - unable to get form for requested record
                types
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.get_resource_form_for_create_template
        return self._provider_session.get_composition_form_for_create(composition_record_types)

    @utilities.arguments_not_none
    def create_composition(self, composiiton_form):
        """Creates a new ``Composition``.

        arg:    composiiton_form (osid.repository.CompositionForm): the
                form for this ``Composition``
        return: (osid.repository.Composition) - the new ``Composition``
        raise:  IllegalState - ``composition_form`` already used in a
                create transaction
        raise:  InvalidArgument - one or more of the form elements is
                invalid
        raise:  NullArgument - ``composition_form`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - ``composition_form`` did not originate
                from ``get_composition_form_for_create()``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.create_resource_template
        return self._provider_session.create_composition(composiiton_form)

    def can_update_compositions(self):
        """Tests if this user can update ``Compositions``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a
        ``Composition`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        update operations to unauthorized users.

        return: (boolean) - ``false`` if ``Composition`` modification is
                not authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.can_create_resources
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def get_composition_form_for_update(self, composition_id):
        """Gets the composition form for updating an existing composition.

        A new composition form should be requested for each update
        transaction.

        arg:    composition_id (osid.id.Id): the ``Id`` of the
                ``Composition``
        return: (osid.repository.CompositionForm) - the composition form
        raise:  NotFound - ``composition_id`` is not found
        raise:  NullArgument - ``composition_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.get_resource_form_for_update_template
        return self._provider_session.get_composition_form_for_update(composition_id)

    def _get_composition_id_with_enclosure(self, enclosure_id):
        """Create an Composition with an enclosed foreign object.

        return: (osid.id.Id) - the id of the new Composition

        """
        return self._provider_session._get_composition_id_with_enclosure(enclosure_id)

    @utilities.arguments_not_none
    def update_composition(self, composition_form):
        """Updates an existing composition.

        arg:    composiiton_form (osid.repository.CompositionForm): the
                form containing the elements to be updated
        raise:  IllegalState - ``composition_form`` already used in an
                update transaction
        raise:  InvalidArgument - the form contains an invalid value
        raise:  NullArgument - ``composition_form`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - ``composition_form`` did not originate
                from ``get_composition_form_for_update()``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.update_resource_template
        return self._provider_session.update_composition(composition_form)

    def can_delete_compositions(self):
        """Tests if this user can delete ``Compositions``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a
        ``Composition`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        delete operations to unauthorized users.

        return: (boolean) - ``false`` if ``Composition`` deletion is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.can_create_resources
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def delete_composition(self, composition_id):
        """Deletes a ``Composition``.

        arg:    composition_id (osid.id.Id): the ``Id`` of the
                ``Composition`` to remove
        raise:  NotFound - ``composition_id`` not found
        raise:  NullArgument - ``composition_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.delete_resource_template
        self._provider_session.delete_composition(composition_id)

    @utilities.arguments_not_none
    def delete_composition_node(self, composition_id):
        """Deletes a ``Composition`` and all contained children.

        arg:    composition_id (osid.id.Id): the ``Id`` of the
                ``Composition`` to remove
        raise:  NotFound - ``composition_id`` not found
        raise:  NullArgument - ``composition_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

    @utilities.arguments_not_none
    def add_composition_child(self, composition_id, child_composition_id):
        """Adds a composition to a parent composition.

        arg:    composition_id (osid.id.Id): the ``Id`` of a parent
                ``Composition``
        arg:    child_composition_id (osid.id.Id): the ``Id`` of a child
                ``Composition``
        raise:  AlreadyExists - ``child_composition_id`` is already a
                child of ``composition_id``
        raise:  NotFound - ``composition_id`` or
                ``child_composition_id`` is not found
        raise:  NullArgument - ``composition_id`` or
                ``child_composition_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

    @utilities.arguments_not_none
    def remove_composition_child(self, composition_id, child_composition_id):
        """Removes a composition from a parent composition.

        arg:    composition_id (osid.id.Id): the ``Id`` of a parent
                ``Composition``
        arg:    child_composition_id (osid.id.Id): the ``Id`` of a child
                ``Composition``
        raise:  NotFound - ``composition_id`` or
                ``child_composition_id`` is not found or not related
        raise:  NullArgument - ``composition_id`` or
                ``child_composition_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

    def can_manage_composition_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Compositions``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        return: (boolean) - ``false`` if ``Composition`` aliasing is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

    @utilities.arguments_not_none
    def alias_composition(self, composition_id, alias_id):
        """Adds an ``Id`` to a ``Composition`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``Composition`` is determined by the
        provider. The new ``Id`` is an alias to the primary ``Id``. If
        the alias is a pointer to another composition, it is reassigned
        to the given composition ``Id``.

        arg:    composition_id (osid.id.Id): the ``Id`` of a
                ``Composition``
        arg:    alias_id (osid.id.Id): the alias ``Id``
        raise:  AlreadyExists - ``alias_id`` is in use as a primary
                ``Id``
        raise:  NotFound - ``composition_id`` not found
        raise:  NullArgument - ``composition_id`` or ``alias_id`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()
