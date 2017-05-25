"""repository.objects"""
# pylint: disable=too-many-lines,too-many-ancestors,too-many-public-methods,protected-access
import os
import codecs

from ...abstract_osid.repository import objects as abc_repository_objects
from ..osid import objects as osid_objects
from ..osid import markers as osid_markers
from ..osid.osid_errors import IllegalState,\
    InvalidArgument, NoAccess, NullArgument, OperationFailed

from bson.objectid import ObjectId


class Asset(abc_repository_objects.Asset,
            osid_objects.OsidObject,
            osid_markers.Aggregateable,
            osid_markers.Sourceable):
    """An ``Asset`` represents some digital content.

    Example assets might be a text document, an image, or a movie. The
    content data, and metadata related directly to the content format
    and quality, is accessed through ``AssetContent. Assets`` , like all
    ``OsidObjects,`` include a type a record to qualify the ``Asset``
    and include additional data. The division between the ``Asset``
    ``Type`` and ``AssetContent`` is to separate data describing the
    asset from data describing the format of the contents, allowing a
    consumer to select among multiple formats, sizes or levels of
    fidelity.

    An example is a photograph of the Bay Bridge. The content may
    deliver a JPEG in multiple resolutions where the ``AssetContent``
    may also desribe size or compression factor for each one. The
    content may also include an uncompressed TIFF version. The ``Asset``
    ``Type`` may be "photograph" indicating that the photo itself is the
    asset managed in this repository.

    Since an Asset may have multiple ``AssetContent`` structures, the
    decision of how many things to stuff inside a single asset comes
    down to if the content is actually a different format, or size, or
    quality, falling under the same creator, copyright, publisher and
    distribution rights as the original. This may, in some cases,
    provide a means to implement some accessibility, it doesn't handle
    the case where, to meet an accessibility requirement, one asset
    needs to be substituted for another. The Repository OSID manages
    this aspect outside the scope of the core ``Asset`` definition.

    ``Assets`` map to ``AssetSubjects``.  ``AssetSubjects`` are
    ``OsidObjects`` that capture a subject matter. In the above example,
    an ``AssetSubject`` may be defined for the Bay Bridge and include
    data describing the bridge. The single subject can map to multiple
    assets depicting the bridge providing a single entry for a search
    and a single place to describe a bridge. Bridges, as physical items,
    may also be described using the Resource OSID in which case the use
    of the ``AssetSubject`` acts as a cover for the underlying
    ``Resource`` to assist repository-only consumers.

    The ``Asset`` definition includes some basic copyright and related
    licensing information to assist in finding free-to-use content, or
    to convey the distribution restrictions that may be placed on the
    asset. Generally, if no data is available it is to be assumed that
    all rights are reserved.

    A publisher is applicable if the content of this ``Asset`` has been
    published. Not all ``Assets`` in this ``Repository`` may have a
    published status and such a status may effect the applicability of
    copyright law. To trace the source of an ``Asset,`` both a provider
    and source are defined. The provider indicates where this repository
    acquired the asset and the source indicates the original provider or
    copyright owner. In the case of a published asset, the source is the
    publisher.

    ``Assets`` also define methods to facilitate searches over time and
    space as it relates to the subject matter. This may at times be
    redundant with the ``AssetSubject``. In the case of the Bay Bridge
    photograph, the temporal coverage may include 1936, when it opened,
    and/or indicate when the photo was taken to capture a current event
    of the bridge. The decision largeley depends on what desired effect
    is from a search. The spatial coverage may describe the gps
    coordinates of the bridge or describe the spatial area encompassed
    in the view. In either case, a "photograph" type may unambiguously
    defined methods to describe the exact time the photograph was taken
    and the location of the photographer.

    The core Asset defines methods to perform general searches and
    construct bibliographic entries without knowledge of a particular
    ``Asset`` or ``AssetContent`` record ``Type``.

    """

    def __iter__(self):
        for attr in dir(self):
            if not attr.startswith('__'):
                yield attr

    def __getitem__(self, item):
        return getattr(self, item)

    def __getattr__(self, name):
        if '_payload' in self.__dict__ and name not in ['object_map', 'get_object_map']:
            try:
                return self._payload[name]
            except:
                raise
        raise AttributeError(name)

    def get_title(self):
        """Gets the proper title of this asset.

        This may be the same as the display name or the display name may
        be used for a less formal label.

        return: (osid.locale.DisplayText) - the title of this asset
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._payload.get_title()

    title = property(fget=get_title)

    def is_copyright_status_known(self):
        """Tests if the copyright status is known.

        return: (boolean) - ``true`` if the copyright status of this
                asset is known, ``false`` otherwise. If ``false,
                is_public_domain(),`` ``can_distribute_verbatim(),
                can_distribute_alterations() and
                can_distribute_compositions()`` may also be ``false``.
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._payload.is_copyright_status_known()

    def is_public_domain(self):
        """Tests if this asset is in the public domain.

        An asset is in the public domain if copyright is not applicable,
        the copyright has expired, or the copyright owner has expressly
        relinquished the copyright.

        return: (boolean) - ``true`` if this asset is in the public
                domain, ``false`` otherwise. If ``true,``
                ``can_distribute_verbatim(),
                can_distribute_alterations() and
                can_distribute_compositions()`` must also be ``true``.
        raise:  IllegalState - ``is_copyright_status_known()`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._payload.is_public_domain()

    def get_copyright(self):
        """Gets the copyright statement and of this asset which identifies
        the current copyright holder.

        For an asset in the public domain, this method may return the
        original copyright statement although it may be no longer valid.

        return: (osid.locale.DisplayText) - the copyright statement or
                an empty string if none available. An empty string does
                not imply the asset is not protected by copyright.
        raise:  IllegalState - ``is_copyright_status_known()`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._payload.get_copyright()

    copyright_ = property(fget=get_copyright)

    def get_copyright_registration(self):
        """Gets the copyright registration information for this asset.

        return: (string) - the copyright registration. An empty string
                means the registration status isn't known.
        raise:  IllegalState - ``is_copyright_status_known()`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._payload.get_copyright_registration()

    copyright_registration = property(fget=get_copyright_registration)

    def can_distribute_verbatim(self):
        """Tests if there are any license restrictions on this asset that
        restrict the distribution, re-publication or public display of this
        asset, commercial or otherwise, without modification, alteration,
        or inclusion in other works.

        This method is intended to offer consumers a means of filtering
        out search results that restrict distribution for any purpose.
        The scope of this method does not include licensing that
        describes warranty disclaimers or attribution requirements. This
        method is intended for informational purposes only and does not
        replace or override the terms specified in a license agreement
        which may specify exceptions or additional restrictions.

        return: (boolean) - ``true`` if the asset can be distributed
                verbatim, ``false`` otherwise.
        raise:  IllegalState - ``is_copyright_status_known()`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._payload.can_distribute_verbatim()

    def can_distribute_alterations(self):
        """Tests if there are any license restrictions on this asset that
        restrict the distribution, re-publication or public display of any
        alterations or modifications to this asset, commercial or
        otherwise, for any purpose.

        This method is intended to offer consumers a means of filtering
        out search results that restrict the distribution or public
        display of any modification or alteration of the content or its
        metadata of any kind, including editing, translation,
        resampling, resizing and cropping. The scope of this method does
        not include licensing that describes warranty disclaimers or
        attribution requirements. This method is intended for
        informational purposes only and does not replace or override the
        terms specified in a license agreement which may specify
        exceptions or additional restrictions.

        return: (boolean) - ``true`` if the asset can be modified,
                ``false`` otherwise. If ``true,``
                ``can_distribute_verbatim()`` must also be ``true``.
        raise:  IllegalState - ``is_copyright_status_known()`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._payload.can_distribute_alterations()

    def can_distribute_compositions(self):
        """Tests if there are any license restrictions on this asset that
        restrict the distribution, re-publication or public display of this
        asset as an inclusion within other content or composition, commercial
        or otherwise, for any purpose, including restrictions upon the
        distribution or license of the resulting composition.

        This method is intended to offer consumers a means of filtering
        out search results that restrict the use of this asset within
        compositions. The scope of this method does not include
        licensing that describes warranty disclaimers or attribution
        requirements. This method is intended for informational purposes
        only and does not replace or override the terms specified in a
        license agreement which may specify exceptions or additional
        restrictions.

        return: (boolean) - ``true`` if the asset can be part of a
                larger composition ``false`` otherwise. If ``true,``
                ``can_distribute_verbatim()`` must also be ``true``.
        raise:  IllegalState - ``is_copyright_status_known()`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._payload.can_distribute_compositions()

    def get_source_id(self):
        """Gets the ``Resource Id`` of the source of this asset.

        The source is the original owner of the copyright of this asset
        and may differ from the creator of this asset. The source for a
        published book written by Margaret Mitchell would be Macmillan.
        The source for an unpublished painting by Arthur Goodwin would
        be Arthur Goodwin.

        An ``Asset`` is ``Sourceable`` and also contains a provider
        identity. The provider is the entity that makes this digital
        asset available in this repository but may or may not be the
        publisher of the contents depicted in the asset. For example, a
        map published by Ticknor and Fields in 1848 may have a provider
        of Library of Congress and a source of Ticknor and Fields. If
        copied from a repository at Middlebury College, the provider
        would be Middlebury College and a source of Ticknor and Fields.

        return: (osid.id.Id) - the source ``Id``
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._payload.get_source_id()

    source_id = property(fget=get_source_id)

    def get_source(self):
        """Gets the ``Resource`` of the source of this asset.

        The source is the original owner of the copyright of this asset
        and may differ from the creator of this asset. The source for a
        published book written by Margaret Mitchell would be Macmillan.
        The source for an unpublished painting by Arthur Goodwin would
        be Arthur Goodwin.

        return: (osid.resource.Resource) - the source
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._payload.get_source()

    source = property(fget=get_source)

    def get_provider_link_ids(self):
        """Gets the resource ``Ids`` representing the source of this asset in
        order from the most recent provider to the originating source.

        return: (osid.id.IdList) - the provider ``Ids``
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._payload.get_provider_link_ids()

    provider_link_ids = property(fget=get_provider_link_ids)

    def get_provider_links(self):
        """Gets the ``Resources`` representing the source of this asset in
        order from the most recent provider to the originating source.

        return: (osid.resource.ResourceList) - the provider chain
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._payload.get_provider_links()

    provider_links = property(fget=get_provider_links)

    def get_created_date(self):
        """Gets the created date of this asset, which is generally not related
        to when the object representing the asset was created.

        The date returned may indicate that not much is known.

        return: (osid.calendaring.DateTime) - the created date
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._payload.get_created_date()

    created_date = property(fget=get_created_date)

    def is_published(self):
        """Tests if this asset has been published.

        Not all assets viewable in this repository may have been
        published. The source of a published asset indicates the
        publisher.

        return: (boolean) - true if this asset has been published,
                ``false`` if unpublished or its published status is not
                known
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._payload.is_published()

    def get_published_date(self):
        """Gets the published date of this asset.

        Unpublished assets have no published date. A published asset has
        a date available, however the date returned may indicate that
        not much is known.

        return: (osid.calendaring.DateTime) - the published date
        raise:  IllegalState - ``is_published()`` is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._payload.get_published_date()

    published_date = property(fget=get_published_date)

    def get_principal_credit_string(self):
        """Gets the credits of the principal people involved in the production
        of this asset as a display string.

        return: (osid.locale.DisplayText) - the principal credits
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._payload.get_principal_credit_string()

    principal_credit_string = property(fget=get_principal_credit_string)

    def get_asset_content_ids(self):
        """Gets the content ``Ids`` of this asset.

        return: (osid.id.IdList) - the asset content ``Ids``
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._payload.get_asset_content_ids()

    asset_content_ids = property(fget=get_asset_content_ids)

    def get_asset_contents(self):
        """Gets the content of this asset.

        return: (osid.repository.AssetContentList) - the asset contents
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Note that this one is different. It wraps the returned AssetContentList
        # in an Filesystem AssetContentList
        return AssetContentList(self._payload.get_asset_contents(), self._config_map)

    asset_contents = property(fget=get_asset_contents)

    def is_composition(self):
        """Tetss if this asset is a representation of a composition of assets.

        return: (boolean) - true if this asset is a composition,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._payload.is_composition()

    def get_composition_id(self):
        """Gets the ``Composition``  ``Id`` corresponding to this asset.

        return: (osid.id.Id) - the composiiton ``Id``
        raise:  IllegalState - ``is_composition()`` is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._payload.get_composition_id()

    composition_id = property(fget=get_composition_id)

    def get_composition(self):
        """Gets the Composition corresponding to this asset.

        return: (osid.repository.Composition) - the composiiton
        raise:  IllegalState - ``is_composition()`` is ``false``
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._payload.get_composition()

    composition = property(fget=get_composition)

    def get_asset_record(self, asset_record_type=None):
        """Gets the asset record corresponding to the given ``Asset`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``asset_record_type`` may be the ``Type``
        returned in ``get_record_types()`` or any of its parents in a
        ``Type`` hierarchy where ``has_record_type(asset_record_type)``
        is ``true`` .

        arg:    asset_record_type (osid.type.Type): an asset record type
        return: (osid.repository.records.AssetRecord) - the asset record
        raise:  NullArgument - ``asset_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported - ``has_record_type(asset_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._payload.get_asset_record()

    def get_object_map(self):
        """stub"""
        obj_map = self._payload.get_object_map()
        obj_map['assetContents'] = []
        for asset_content in self.get_asset_contents():
            obj_map['assetContents'].append(asset_content.object_map)
        return obj_map

    object_map = property(fget=get_object_map)


class AssetForm(abc_repository_objects.AssetForm,
                osid_objects.OsidObjectForm,
                osid_objects.OsidAggregateableForm,
                osid_objects.OsidSourceableForm):
    """This is the form for creating and updating ``Assets``.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``AssetAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.

    """

    def get_title_metadata(self):
        """Gets the metadata for an asset title.

        return: (osid.Metadata) - metadata for the title
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    title_metadata = property(fget=get_title_metadata)

    def set_title(self, title=None):
        """Sets the title.

        arg:    title (string): the new title
        raise:  InvalidArgument - ``title`` is invalid
        raise:  NoAccess - ``Metadata.isReadOnly()`` is ``true``
        raise:  NullArgument - ``title`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def clear_title(self):
        """Removes the title.

        raise:  NoAccess - ``Metadata.isRequired()`` is ``true`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    title = property(fset=set_title, fdel=clear_title)

    def get_public_domain_metadata(self):
        """Gets the metadata for the public domain flag.

        return: (osid.Metadata) - metadata for the public domain
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    public_domain_metadata = property(fget=get_public_domain_metadata)

    def set_public_domain(self, public_domain=None):
        """Sets the public domain flag.

        arg:    public_domain (boolean): the public domain status
        raise:  NoAccess - ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def clear_public_domain(self):
        """Removes the public domain status.

        raise:  NoAccess - ``Metadata.isRequired()`` is ``true`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    public_domain = property(fset=set_public_domain, fdel=clear_public_domain)

    def get_copyright_metadata(self):
        """Gets the metadata for the copyright.

        return: (osid.Metadata) - metadata for the copyright
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    copyright_metadata = property(fget=get_copyright_metadata)

    def set_copyright(self, copyright_=None):
        """Sets the copyright.

        arg:    copyright (string): the new copyright
        raise:  InvalidArgument - ``copyright`` is invalid
        raise:  NoAccess - ``Metadata.isReadOnly()`` is ``true``
        raise:  NullArgument - ``copyright`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def clear_copyright(self):
        """Removes the copyright.

        raise:  NoAccess - ``Metadata.isRequired()`` is ``true`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    copyright_ = property(fset=set_copyright, fdel=clear_copyright)

    def get_copyright_registration_metadata(self):
        """Gets the metadata for the copyright registration.

        return: (osid.Metadata) - metadata for the copyright
                registration
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    copyright_registration_metadata = property(fget=get_copyright_registration_metadata)

    def set_copyright_registration(self, registration=None):
        """Sets the copyright registration.

        arg:    registration (string): the new copyright registration
        raise:  InvalidArgument - ``copyright`` is invalid
        raise:  NoAccess - ``Metadata.isReadOnly()`` is ``true``
        raise:  NullArgument - ``copyright`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def clear_copyright_registration(self):
        """Removes the copyright registration.

        raise:  NoAccess - ``Metadata.isRequired()`` is ``true`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    copyright_registration = property(fset=set_copyright_registration,
                                      fdel=clear_copyright_registration)

    def get_distribute_verbatim_metadata(self):
        """Gets the metadata for the distribute verbatim rights flag.

        return: (osid.Metadata) - metadata for the distribution rights
                fields
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    distribute_verbatim_metadata = property(fget=get_distribute_verbatim_metadata)

    def set_distribute_verbatim(self, distribute_verbatim=None):
        """Sets the distribution rights.

        arg:    distribute_verbatim (boolean): right to distribute
                verbatim copies
        raise:  InvalidArgument - ``distribute_verbatim`` is invalid
        raise:  NoAccess - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def clear_distribute_verbatim(self):
        """Removes the distribution rights.

        raise:  NoAccess - ``Metadata.isRequired()`` is ``true`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    distribute_verbatim = property(fset=set_distribute_verbatim,
                                   fdel=clear_distribute_verbatim)

    def get_distribute_alterations_metadata(self):
        """Gets the metadata for the distribute alterations rights flag.

        return: (osid.Metadata) - metadata for the distribution rights
                fields
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    distribute_alterations_metadata = property(fget=get_distribute_alterations_metadata)

    def set_distribute_alterations(self, distribute_mods=None):
        """Sets the distribute alterations flag.

        This also sets distribute verbatim to ``true``.

        arg:    distribute_mods (boolean): right to distribute
                modifications
        raise:  InvalidArgument - ``distribute_mods`` is invalid
        raise:  NoAccess - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def clear_distribute_alterations(self):
        """Removes the distribution rights.

        raise:  NoAccess - ``Metadata.isRequired()`` is ``true`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    distribute_alterations = property(fset=set_distribute_alterations,
                                      fdel=clear_distribute_alterations)

    def get_distribute_compositions_metadata(self):
        """Gets the metadata for the distribute compositions rights flag.

        return: (osid.Metadata) - metadata for the distribution rights
                fields
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    distribute_compositions_metadata = property(fget=get_distribute_compositions_metadata)

    def set_distribute_compositions(self, distribute_comps=None):
        """Sets the distribution rights.

        This sets distribute verbatim to ``true``.

        arg:    distribute_comps (boolean): right to distribute
                modifications
        raise:  InvalidArgument - ``distribute_comps`` is invalid
        raise:  NoAccess - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def clear_distribute_compositions(self):
        """Removes the distribution rights.

        raise:  NoAccess - ``Metadata.isRequired()`` is ``true`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    distribute_compositions = property(fset=set_distribute_compositions,
                                       fdel=clear_distribute_compositions)

    def get_source_metadata(self):
        """Gets the metadata for the source.

        return: (osid.Metadata) - metadata for the source
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    source_metadata = property(fget=get_source_metadata)

    def set_source(self, source_id=None):
        """Sets the source.

        arg:    source_id (osid.id.Id): the new publisher
        raise:  InvalidArgument - ``source_id`` is invalid
        raise:  NoAccess - ``Metadata.isReadOnly()`` is ``true``
        raise:  NullArgument - ``source_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def clear_source(self):
        """Removes the source.

        raise:  NoAccess - ``Metadata.isRequired()`` is ``true`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    source = property(fset=set_source, fdel=clear_source)

    def get_provider_links_metadata(self):
        """Gets the metadata for the provider chain.

        return: (osid.Metadata) - metadata for the provider chain
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    provider_links_metadata = property(fget=get_provider_links_metadata)

    def set_provider_links(self, resource_ids=None):
        """Sets a provider chain in order from the most recent source to the
        originating source.

        arg:    resource_ids (osid.id.Id[]): the new source
        raise:  InvalidArgument - ``resource_ids`` is invalid
        raise:  NoAccess - ``Metadata.isReadOnly()`` is ``true``
        raise:  NullArgument - ``resource_ids`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def clear_provider_links(self):
        """Removes the provider chain.

        raise:  NoAccess - ``Metadata.isRequired()`` is ``true`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    provider_links = property(fset=set_provider_links, fdel=clear_provider_links)

    def get_created_date_metadata(self):
        """Gets the metadata for the asset creation date.

        return: (osid.Metadata) - metadata for the created date
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    created_date_metadata = property(fget=get_created_date_metadata)

    def set_created_date(self, created_date=None):
        """Sets the created date.

        arg:    created_date (osid.calendaring.DateTime): the new
                created date
        raise:  InvalidArgument - ``created_date`` is invalid
        raise:  NoAccess - ``Metadata.isReadOnly()`` is ``true``
        raise:  NullArgument - ``created_date`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def clear_created_date(self):
        """Removes the created date.

        raise:  NoAccess - ``Metadata.isRequired()`` is ``true`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    created_date = property(fset=set_created_date, fdel=clear_created_date)

    def get_published_metadata(self):
        """Gets the metadata for the published status.

        return: (osid.Metadata) - metadata for the published field
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    published_metadata = property(fget=get_published_metadata)

    def set_published(self, published=None):
        """Sets the published status.

        arg:    published (boolean): the published status
        raise:  NoAccess - ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def clear_published(self):
        """Removes the published status.

        raise:  NoAccess - ``Metadata.isRequired()`` is ``true`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    published = property(fset=set_published, fdel=clear_published)

    def get_published_date_metadata(self):
        """Gets the metadata for the published date.

        return: (osid.Metadata) - metadata for the published date
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    published_date_metadata = property(fget=get_published_date_metadata)

    def set_published_date(self, published_date=None):
        """Sets the published date.

        arg:    published_date (osid.calendaring.DateTime): the new
                published date
        raise:  InvalidArgument - ``published_date`` is invalid
        raise:  NoAccess - ``Metadata.isReadOnly()`` is ``true``
        raise:  NullArgument - ``published_date`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def clear_published_date(self):
        """Removes the puiblished date.

        raise:  NoAccess - ``Metadata.isRequired()`` is ``true`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    published_date = property(fset=set_published_date, fdel=clear_published_date)

    def get_principal_credit_string_metadata(self):
        """Gets the metadata for the principal credit string.

        return: (osid.Metadata) - metadata for the credit string
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    principal_credit_string_metadata = property(fget=get_principal_credit_string_metadata)

    def set_principal_credit_string(self, credit_string=None):
        """Sets the principal credit string.

        arg:    credit_string (string): the new credit string
        raise:  InvalidArgument - ``credit_string`` is invalid
        raise:  NoAccess - ``Metadata.isReadOnly()`` is ``true``
        raise:  NullArgument - ``credit_string`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def clear_principal_credit_string(self):
        """Removes the principal credit string.

        raise:  NoAccess - ``Metadata.isRequired()`` is ``true`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    principal_credit_string = property(fset=set_principal_credit_string,
                                       fdel=clear_principal_credit_string)

    def get_composition_metadata(self):
        """Gets the metadata for linking this asset to a composition.

        return: (osid.Metadata) - metadata for the composition
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    composition_metadata = property(fget=get_composition_metadata)

    def set_composition(self, composition_id=None):
        """Sets the composition.

        arg:    composition_id (osid.id.Id): a composition
        raise:  InvalidArgument - ``composition_id`` is invalid
        raise:  NoAccess - ``Metadata.isReadOnly()`` is ``true``
        raise:  NullArgument - ``composition_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def clear_composition(self):
        """Removes the composition link.

        raise:  NoAccess - ``Metadata.isRequired()`` is ``true`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    composition = property(fset=set_composition, fdel=clear_composition)

    def get_asset_form_record(self, asset_record_type=None):
        """Gets the ``AssetFormRecord`` corresponding to the given ``Asset`` record ``Type``.

        arg:    asset_record_type (osid.type.Type): an asset record type
        return: (osid.repository.records.AssetFormRecord) - the asset
                form record
        raise:  NullArgument - ``asset_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported - ``has_record_type(asset_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class AssetList(osid_objects.OsidList, abc_repository_objects.AssetList):
    """Like all ``OsidLists,``  ``AssetList`` provides a means for accessing
    ``Asset`` elements sequentially either one at a time or many at a time.

    Examples: while (al.hasNext()) { Asset asset = al.getNextAsset(); }

    or
      while (al.hasNext()) {
           Asset[] assets = al.getNextAssets(al.available());
      }



    """

    def get_next_asset(self):
        """Gets the next ``Asset`` in this list.

        return: (osid.repository.Asset) - the next ``Asset`` in this
                list. The ``has_next()`` method should be used to test
                that a next ``Asset`` is available before calling this
                method.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceList.get_next_resource
        return next(self)

    def next(self):
        try:
            next_object = next(self._payload_list)
        except StopIteration:
            raise
        except Exception as ex:  # Need to specify exceptions here!
            raise OperationFailed()
        next_object = Asset(next_object, self._config_map)
        return next_object

    __next__ = next

    next_asset = property(fget=get_next_asset)

    def get_next_assets(self, n=None):
        """Gets the next set of ``Assets`` in this list which must be less
        than or equal to the return from ``available()``.

        arg:    n (cardinal): the number of ``Asset`` elements requested
                which must be less than or equal to ``available()``
        return: (osid.repository.Asset) - an array of ``Asset``
                elements.The length of the array is less than or equal
                to the number specified.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._get_next_n(n)


class AssetContent(abc_repository_objects.AssetContent,
                   osid_objects.OsidObject,
                   osid_markers.Subjugateable):
    """``AssetContent`` represents a version of content represented by an ``Asset``.

    Although ``AssetContent`` is a separate ``OsidObject`` with its own
    ``Id`` to distuinguish it from other content inside an ``Asset,
    AssetContent`` can only be accessed through an ``Asset``.

    Once an ``Asset`` is selected, multiple contents should be
    negotiated using the size, fidelity, accessibility requirements or
    application evnironment.

    """

    def __iter__(self):
        for attr in dir(self):
            if not attr.startswith('__'):
                yield attr

    def __getitem__(self, item):
        return getattr(self, item)

    def __getattr__(self, name):
        if '_payload' in self.__dict__ and name not in ['object_map', 'get_object_map']:
            try:
                return self._payload[name]
            except:
                raise
        raise AttributeError(name)

    def get_asset_id(self):
        """Gets the ``Asset Id`` corresponding to this content.

        return: (osid.id.Id) - the asset ``Id``
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._payload.get_asset_id()

    asset_id = property(fget=get_asset_id)

    def get_asset(self):
        """Gets the ``Asset`` corresponding to this content.

        return: (osid.repository.Asset) - the asset
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._payload.get_asset()

    asset = property(fget=get_asset)

    def get_accessibility_types(self):
        """Gets the accessibility types associated with this content.

        return: (osid.type.TypeList) - list of content accessibility
                types
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._payload.get_accessibility_types()

    accessibility_types = property(fget=get_accessibility_types)

    def has_data_length(self):
        """Tests if a data length is available.

        return: (boolean) - ``true`` if a length is available for this
                content, ``false`` otherwise.
        *compliance: mandatory -- This method must be implemented.*

        """
        return False  # can we get a data length from AWS?

    def get_data_length(self):
        """Gets the length of the data represented by this content in bytes.

        return: (cardinal) - the length of the data stream
        raise:  IllegalState - ``has_data_length()`` is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise IllegalState()  # can we get a data length from AWS?

    data_length = property(fget=get_data_length)

    def get_data(self):
        """Gets the asset content data.

        return: (osid.transport.DataInputStream) - the length of the
                content data
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        # gets you a file-like object...not sure if it will behave
        exactly as expected...
        """
        # read the file from self.get_url()
        # return the file object to be streamed?
        url = self._payload.get_url()
        file_handle = codecs.open(url, 'r', encoding='utf-8')
        try:
            file_handle.read()
        except UnicodeDecodeError:
            file_handle.close()
            # non-Unicode file, like an image
            file_handle = open(url, 'rb')
        file_handle.seek(0)
        return file_handle

    data = property(fget=get_data)

    def has_url(self):
        """Tests if a URL is associated with this content.

        return: (boolean) - ``true`` if a URL is available, ``false``
                otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._payload.has_url()

    def get_url(self):
        """Gets the URL associated with this content for web-based retrieval.

        return: (string) - the url for this data
        raise:  IllegalState - ``has_url()`` is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        # construct the URL from runtime's FILESYSTEM location param
        # plus what we know about the location of repository / assetContents
        # have to get repositoryId from the asset?
        # return self._payload.get_url()
        url = '/repository/repositories/{0}/assets/{1}/contents/{2}/stream'.format(self._my_map['assignedRepositoryIds'][0],
                                                                                   str(self.get_asset_id()),
                                                                                   str(self.get_id()))

        if 'url_hostname' in self._config_map:
            url_hostname = self._config_map['url_hostname']
            return '{0}{1}'.format(url_hostname, url)

        return url

    url = property(fget=get_url)

    def get_asset_content_record(self, asset_content_content_record_type=None):
        """Gets the asset content record corresponding to the given
        ``AssetContent`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``asset_record_type`` may be the ``Type``
        returned in ``get_record_types()`` or any of its parents in a
        ``Type`` hierarchy where ``has_record_type(asset_record_type)``
        is ``true`` .

        arg:    asset_content_content_record_type (osid.type.Type): the
                type of the record to retrieve
        return: (osid.repository.records.AssetContentRecord) - the asset
                content record
        raise:  NullArgument - ``asset_content_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported -
                ``has_record_type(asset_content_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._payload.get_asset_content_record()

    def get_object_map(self):
        """stub"""
        obj_map = self._payload.get_object_map()
        obj_map.update({'url': self.get_url()})
        # obj_map['recordTypeIds'].append(str(FILESYSTEM_ASSET_CONTENT_RECORD_TYPE))
        return obj_map

    object_map = property(fget=get_object_map)


class AssetContentForm(abc_repository_objects.AssetContentForm,
                       osid_objects.OsidObjectForm,
                       osid_objects.OsidSubjugateableForm):
    """This is the form for creating and updating content for ``AssetContent``.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``AssetAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.

    """

    def __iter__(self):
        for attr in dir(self):
            if not attr.startswith('__'):
                yield attr

    def __getitem__(self, item):
        return getattr(self, item)

    def __getattr__(self, name):
        if '_payload' in self.__dict__:
            try:
                return self._payload[name]
            except:
                raise
        raise AttributeError(name)

    def get_accessibility_type_metadata(self):
        """Gets the metadata for an accessibility type.

        return: (osid.Metadata) - metadata for the accessibility types
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._payload.get_accessibility_type_metadata()

    accessibility_type_metadata = property(fget=get_accessibility_type_metadata)

    def add_accessibility_type(self, accessibility_type=None):
        """Adds an accessibility type.

        Multiple types can be added.

        arg:    accessibility_type (osid.type.Type): a new accessibility
                type
        raise:  InvalidArgument - ``accessibility_type`` is invalid
        raise:  NoAccess - ``Metadata.isReadOnly()`` is ``true``
        raise:  NullArgument - ``accessibility_t_ype`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        self._payload.add_accessibility_type(accessibility_type)

    def remove_accessibility_type(self, accessibility_type=None):
        """Removes an accessibility type.

        arg:    accessibility_type (osid.type.Type): accessibility type
                to remove
        raise:  NoAccess - ``Metadata.isReadOnly()`` is ``true``
        raise:  NotFound - acessibility type not found
        raise:  NullArgument - ``accessibility_type`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        self._payload.remove_accessibility_type(accessibility_type)

    def clear_accessibility_types(self):
        """Removes all accessibility types.

        raise:  NoAccess - ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        self._payload.clear_accessibility_types()

    accessibility_types = property(fdel=clear_accessibility_types)

    def get_data_metadata(self):
        """Gets the metadata for the content data.

        return: (osid.Metadata) - metadata for the content data
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._payload.get_data_metadata()

    data_metadata = property(fget=get_data_metadata)

    def set_data(self, data=None):
        """Sets the content data.

        arg:    data (osid.transport.DataInputStream): the content data
        raise:  InvalidArgument - ``data`` is invalid
        raise:  NoAccess - ``Metadata.isReadOnly()`` is ``true``
        raise:  NullArgument - ``data`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        def has_secondary_storage():
            return 'secondary_data_store_path' in self._config_map

        extension = data.name.split('.')[-1]
        data_store_path = self._config_map['data_store_path']
        if has_secondary_storage():
            secondary_data_store_path = self._config_map['secondary_data_store_path']

        if '_id' in self._my_map:
            filename = self._my_map['_id']
            # remove any old file that is set
            if str(self._my_map['_id']) not in self._my_map['url']:
                os.remove(self._my_map['url'])

                if has_secondary_storage():
                    old_path = '{0}/repository/AssetContent'.format(data_store_path)
                    secondary_file_location = self._my_map['url'].replace(old_path,
                                                                          secondary_data_store_path)
                    os.remove(secondary_file_location)
        else:
            filename = ObjectId()

        filesystem_location = '{0}/repository/AssetContent/'.format(data_store_path)

        if not os.path.isdir(filesystem_location):
            os.makedirs(filesystem_location)

        file_location = '{0}{1}.{2}'.format(filesystem_location,
                                            str(filename),
                                            extension)

        data.seek(0)

        with open(file_location, 'wb') as file_handle:
            file_handle.write(data.read())

        # this URL should be a filesystem path...relative
        # to the setting in runtime
        self._payload.set_url(file_location)

        # if set, also make a backup copy in the secondary_data_store_path
        if has_secondary_storage():
            data.seek(0)

            if not os.path.isdir(secondary_data_store_path):
                os.makedirs(secondary_data_store_path)

            file_location = '{0}/{1}.{2}'.format(secondary_data_store_path,
                                                 str(filename),
                                                 extension)
            with open(file_location, 'wb') as file_handle:
                file_handle.write(data.read())

    def clear_data(self):
        """Removes the content data.

        raise:  NoAccess - ``Metadata.isRequired()`` is ``true`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Removes the item from filesystem and resets URL to ''
        url = self.get_url()
        # try to clear from payload first, in case that fails we won't mess with AWS
        self._payload.clear_url()
        os.remove(url)

    data = property(fset=set_data, fdel=clear_data)

    def get_url_metadata(self):
        """Gets the metadata for the url.

        return: (osid.Metadata) - metadata for the url
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._payload.get_url_metadata()

    url_metadata = property(fget=get_url_metadata)

    def set_url(self, url=None):
        """Sets the url.

        arg:    url (string): the new copyright
        raise:  InvalidArgument - ``url`` is invalid
        raise:  NoAccess - ``Metadata.isReadOnly()`` is ``true``
        raise:  NullArgument - ``url`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        # raise NoAccess('Use set_data() only. URLs for Filesystem AssetContents ' +
        #                'are managed by the system')
        if url is not None:
            self._payload.set_url(url)

    def clear_url(self):
        """Removes the url.

        raise:  NoAccess - ``Metadata.isRequired()`` is ``true`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise NoAccess('Use clear_data() only. URLs for Filesystem AssetContents ' +
                       'are managed by the system')

    url = property(fset=set_url, fdel=clear_url)

    def get_asset_content_form_record(self, asset_content_record_type=None):
        """Gets the ``AssetContentFormRecord`` corresponding to the given
        asset content record ``Type``.

        arg:    asset_content_record_type (osid.type.Type): an asset
                content record type
        return: (osid.repository.records.AssetContentFormRecord) - the
                asset content form record
        raise:  NullArgument - ``asset_content_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported -
                ``has_record_type(asset_content_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._payload.get_asset_content_form_record(asset_content_record_type)

    def _clean_up(self):
        """stub"""
        pass  # This is where we could deal with the un-updated form issue


class AssetContentList(abc_repository_objects.AssetContentList,
                       osid_objects.OsidList):
    """Like all ``OsidLists,``  ``AssetContentList`` provides a means for
    accessing ``AssetContent`` elements sequentially either one at a time or
    many at a time.

    Examples: while (acl.hasNext()) { AssetContent content =
    acl.getNextAssetContent(); }

    or
      while (acl.hasNext()) {
           AssetContent[] contents = acl.getNextAssetContents(acl.available());
      }

    """

    def get_next_asset_content(self):
        """Gets the next ``AssetContent`` in this list.

        return: (osid.repository.AssetContent) - the next
                ``AssetContent`` in this list. The ``has_next()`` method
                should be used to test that a next ``AssetContent`` is
                available before calling this method.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        return next(self)

    def next(self):
        asset_content = next(self._payload_list)
        try:
            if asset_content.has_url() and 'repository/AssetContent' in asset_content.get_url():
                return AssetContent(asset_content, self._config_map)
        except TypeError:
            pass
        return asset_content

    __next__ = next

    next_asset_content = property(fget=get_next_asset_content)

    def get_next_asset_contents(self, n=None):
        """Gets the next set of ``AssetContents`` in this list which must be
        less than or equal to the return from ``available()``.

        arg:    n (cardinal): the number of ``AssetContent`` elements
                requested which must be less than or equal to
                ``available()``
        return: (osid.repository.AssetContent) - an array of
                ``AssetContent`` elements.The length of the array is
                less than or equal to the number specified.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        if n is None:
            raise NullArgument()
        if not isinstance(n, int):
            raise InvalidArgument()
        provider_list = self._payload_list.get_next_asset_contents(n)
        new_list = []
        for asset_content in provider_list:
            if asset_content.has_url() and 'repository/AssetContent' in asset_content.get_url():
                new_list.append(AssetContent(asset_content, self._config_map))
            else:
                new_list.append(asset_content)
        return new_list


class Repository(abc_repository_objects.Repository, osid_objects.OsidCatalog):
    """A repository defines a collection of assets."""

    def get_repository_record(self, repository_record_type=None):
        """Gets the record corresponding to the given ``Repository`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``repository_record_type`` may be the
        ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(repository_record_type)`` is ``true`` .

        arg:    repository_record_type (osid.type.Type): a repository
                record type
        return: (osid.repository.records.RepositoryRecord) - the
                repository record
        raise:  NullArgument - ``repository_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported -
                ``has_record_type(repository_record_type)`` is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class RepositoryForm(abc_repository_objects.RepositoryForm, osid_objects.OsidCatalogForm):
    """This is the form for creating and updating repositories.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``RepositoryAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.

    """

    def get_repository_form_record(self, repository_record_type=None):
        """Gets the ``RepositoryFormRecord`` corresponding to the given
        repository record ``Type``.

        arg:    repository_record_type (osid.type.Type): a repository
                record type
        return: (osid.repository.records.RepositoryFormRecord) - the
                repository form record
        raise:  NullArgument - ``repository_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported -
                ``has_record_type(repository_record_type)`` is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class RepositoryList(abc_repository_objects.RepositoryList, osid_objects.OsidList):
    """Like all ``OsidLists,``  ``RepositoryList`` provides a means for accessing
    ``Repository`` elements sequentially either one at a time or many at a time.

    Examples: while (rl.hasNext()) { Repository repository =
    rl.getNextRepository(); }

    or
      while (rl.hasNext()) {
           Repository[] repositories = rl.getNextRepositories(rl.available());
      }

    """

    def get_next_repository(self):
        """Gets the next ``Repository`` in this list.

        return: (osid.repository.Repository) - the next ``Repository``
                in this list. The ``has_next()`` method should be used
                to test that a next ``Repository`` is available before
                calling this method.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceList.get_next_resource
        return next(self)

    def next(self):
        return self._get_next_object(Repository)

    __next__ = next
    next_repository = property(fget=get_next_repository)

    def get_next_repositories(self, n=None):
        """Gets the next set of ``Repository`` elements in this list which
        must be less than or equal to the return from ``available()``.

        arg:    n (cardinal): the number of ``Repository`` elements
                requested which must be less than or equal to
                ``available()``
        return: (osid.repository.Repository) - an array of
                ``Repository`` elements.The length of the array is less
                than or equal to the number specified.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceList.get_next_resources
        return self._get_next_n(n)
