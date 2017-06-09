"""Implementations of repository abstract base class objects."""
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


class Asset:
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
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_title(self):  # pragma: no cover
        """Gets the proper title of this asset.

        This may be the same as the display name or the display name may
        be used for a less formal label.

        :return: the title of this asset
        :rtype: ``osid.locale.DisplayText``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.locale.DisplayText

    title = property(fget=get_title)

    @abc.abstractmethod
    def is_copyright_status_known(self):  # pragma: no cover
        """Tests if the copyright status is known.

        :return: ``true`` if the copyright status of this asset is known, ``false`` otherwise. If ``false, is_public_domain(),``  ``can_distribute_verbatim(), can_distribute_alterations() and
can_distribute_compositions()`` may also be ``false``.
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def is_public_domain(self):  # pragma: no cover
        """Tests if this asset is in the public domain.

        An asset is in the public domain if copyright is not applicable,
        the copyright has expired, or the copyright owner has expressly
        relinquished the copyright.

        :return: ``true`` if this asset is in the public domain, ``false`` otherwise. If ``true,``  ``can_distribute_verbatim(), can_distribute_alterations() and can_distribute_compositions()`` must also be ``true``.
        :rtype: ``boolean``
        :raise: ``IllegalState`` -- ``is_copyright_status_known()`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_copyright(self):  # pragma: no cover
        """Gets the copyright statement and of this asset which identifies the current copyright holder.

        For an asset in the public domain, this method may return the
        original copyright statement although it may be no longer valid.

        :return: the copyright statement or an empty string if none available. An empty string does not imply the asset is not protected by copyright.
        :rtype: ``osid.locale.DisplayText``
        :raise: ``IllegalState`` -- ``is_copyright_status_known()`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.locale.DisplayText

    copyright_ = property(fget=get_copyright)

    @abc.abstractmethod
    def get_copyright_registration(self):  # pragma: no cover
        """Gets the copyright registration information for this asset.

        :return: the copyright registration. An empty string means the registration status isn't known.
        :rtype: ``string``
        :raise: ``IllegalState`` -- ``is_copyright_status_known()`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # string

    copyright_registration = property(fget=get_copyright_registration)

    @abc.abstractmethod
    def can_distribute_verbatim(self):  # pragma: no cover
        """Tests if there are any license restrictions on this asset that restrict the distribution, re-publication or public display of this asset, commercial or otherwise, without modification, alteration, or inclusion in other works.

        This method is intended to offer consumers a means of filtering
        out search results that restrict distribution for any purpose.
        The scope of this method does not include licensing that
        describes warranty disclaimers or attribution requirements. This
        method is intended for informational purposes only and does not
        replace or override the terms specified in a license agreement
        which may specify exceptions or additional restrictions.

        :return: ``true`` if the asset can be distributed verbatim, ``false`` otherwise.
        :rtype: ``boolean``
        :raise: ``IllegalState`` -- ``is_copyright_status_known()`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def can_distribute_alterations(self):  # pragma: no cover
        """Tests if there are any license restrictions on this asset that restrict the distribution, re-publication or public display of any alterations or modifications to this asset, commercial or otherwise, for any purpose.

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

        :return: ``true`` if the asset can be modified, ``false`` otherwise. If ``true,``  ``can_distribute_verbatim()`` must also be ``true``.
        :rtype: ``boolean``
        :raise: ``IllegalState`` -- ``is_copyright_status_known()`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def can_distribute_compositions(self):  # pragma: no cover
        """Tests if there are any license restrictions on this asset that restrict the distribution, re-publication or public display of this asset as an inclusion within other content or composition, commercial or otherwise, for any purpose, including restrictions upon the distribution or license of the resulting composition.

        This method is intended to offer consumers a means of filtering
        out search results that restrict the use of this asset within
        compositions. The scope of this method does not include
        licensing that describes warranty disclaimers or attribution
        requirements. This method is intended for informational purposes
        only and does not replace or override the terms specified in a
        license agreement which may specify exceptions or additional
        restrictions.

        :return: ``true`` if the asset can be part of a larger composition ``false`` otherwise. If ``true,``  ``can_distribute_verbatim()`` must also be ``true``.
        :rtype: ``boolean``
        :raise: ``IllegalState`` -- ``is_copyright_status_known()`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_source_id(self):  # pragma: no cover
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

        :return: the source ``Id``
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    source_id = property(fget=get_source_id)

    @abc.abstractmethod
    def get_source(self):  # pragma: no cover
        """Gets the ``Resource`` of the source of this asset.

        The source is the original owner of the copyright of this asset
        and may differ from the creator of this asset. The source for a
        published book written by Margaret Mitchell would be Macmillan.
        The source for an unpublished painting by Arthur Goodwin would
        be Arthur Goodwin.

        :return: the source
        :rtype: ``osid.resource.Resource``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.resource.Resource

    source = property(fget=get_source)

    @abc.abstractmethod
    def get_provider_link_ids(self):  # pragma: no cover
        """Gets the resource ``Ids`` representing the source of this asset in order from the most recent provider to the originating source.

        :return: the provider ``Ids``
        :rtype: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    provider_link_ids = property(fget=get_provider_link_ids)

    @abc.abstractmethod
    def get_provider_links(self):  # pragma: no cover
        """Gets the ``Resources`` representing the source of this asset in order from the most recent provider to the originating source.

        :return: the provider chain
        :rtype: ``osid.resource.ResourceList``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.resource.ResourceList

    provider_links = property(fget=get_provider_links)

    @abc.abstractmethod
    def get_created_date(self):  # pragma: no cover
        """Gets the created date of this asset, which is generally not related to when the object representing the asset was created.

        The date returned may indicate that not much is known.

        :return: the created date
        :rtype: ``osid.calendaring.DateTime``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.DateTime

    created_date = property(fget=get_created_date)

    @abc.abstractmethod
    def is_published(self):  # pragma: no cover
        """Tests if this asset has been published.

        Not all assets viewable in this repository may have been
        published. The source of a published asset indicates the
        publisher.

        :return: true if this asset has been published, ``false`` if unpublished or its published status is not known
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_published_date(self):  # pragma: no cover
        """Gets the published date of this asset.

        Unpublished assets have no published date. A published asset has
        a date available, however the date returned may indicate that
        not much is known.

        :return: the published date
        :rtype: ``osid.calendaring.DateTime``
        :raise: ``IllegalState`` -- ``is_published()`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.DateTime

    published_date = property(fget=get_published_date)

    @abc.abstractmethod
    def get_principal_credit_string(self):  # pragma: no cover
        """Gets the credits of the principal people involved in the production of this asset as a display string.

        :return: the principal credits
        :rtype: ``osid.locale.DisplayText``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.locale.DisplayText

    principal_credit_string = property(fget=get_principal_credit_string)

    @abc.abstractmethod
    def get_asset_content_ids(self):  # pragma: no cover
        """Gets the content ``Ids`` of this asset.

        :return: the asset content ``Ids``
        :rtype: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    asset_content_ids = property(fget=get_asset_content_ids)

    @abc.abstractmethod
    def get_asset_contents(self):  # pragma: no cover
        """Gets the content of this asset.

        :return: the asset contents
        :rtype: ``osid.repository.AssetContentList``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.repository.AssetContentList

    asset_contents = property(fget=get_asset_contents)

    @abc.abstractmethod
    def is_composition(self):  # pragma: no cover
        """Tetss if this asset is a representation of a composition of assets.

        :return: true if this asset is a composition, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_composition_id(self):  # pragma: no cover
        """Gets the ``Composition``  ``Id`` corresponding to this asset.

        :return: the composiiton ``Id``
        :rtype: ``osid.id.Id``
        :raise: ``IllegalState`` -- ``is_composition()`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    composition_id = property(fget=get_composition_id)

    @abc.abstractmethod
    def get_composition(self):  # pragma: no cover
        """Gets the Composition corresponding to this asset.

        :return: the composiiton
        :rtype: ``osid.repository.Composition``
        :raise: ``IllegalState`` -- ``is_composition()`` is ``false``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.repository.Composition

    composition = property(fget=get_composition)

    @abc.abstractmethod
    def get_asset_record(self, asset_record_type):  # pragma: no cover
        """Gets the asset record corresponding to the given ``Asset`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``asset_record_type`` may be the ``Type``
        returned in ``get_record_types()`` or any of its parents in a
        ``Type`` hierarchy where ``has_record_type(asset_record_type)``
        is ``true`` .

        :param asset_record_type: an asset record type
        :type asset_record_type: ``osid.type.Type``
        :return: the asset record
        :rtype: ``osid.repository.records.AssetRecord``
        :raise: ``NullArgument`` -- ``asset_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(asset_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.repository.records.AssetRecord


class AssetForm:
    """This is the form for creating and updating ``Assets``.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``AssetAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_title_metadata(self):  # pragma: no cover
        """Gets the metadata for an asset title.

        :return: metadata for the title
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.Metadata

    title_metadata = property(fget=get_title_metadata)

    @abc.abstractmethod
    def set_title(self, title):  # pragma: no cover
        """Sets the title.

        :param title: the new title
        :type title: ``string``
        :raise: ``InvalidArgument`` -- ``title`` is invalid
        :raise: ``NoAccess`` -- ``Metadata.isReadOnly()`` is ``true``
        :raise: ``NullArgument`` -- ``title`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_title(self):  # pragma: no cover
        """Removes the title.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` is ``true`` or ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    title = property(fset=set_title, fdel=clear_title)

    @abc.abstractmethod
    def get_public_domain_metadata(self):  # pragma: no cover
        """Gets the metadata for the public domain flag.

        :return: metadata for the public domain
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.Metadata

    public_domain_metadata = property(fget=get_public_domain_metadata)

    @abc.abstractmethod
    def set_public_domain(self, public_domain):  # pragma: no cover
        """Sets the public domain flag.

        :param public_domain: the public domain status
        :type public_domain: ``boolean``
        :raise: ``NoAccess`` -- ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_public_domain(self):  # pragma: no cover
        """Removes the public domain status.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` is ``true`` or ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    public_domain = property(fset=set_public_domain, fdel=clear_public_domain)

    @abc.abstractmethod
    def get_copyright_metadata(self):  # pragma: no cover
        """Gets the metadata for the copyright.

        :return: metadata for the copyright
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.Metadata

    copyright_metadata = property(fget=get_copyright_metadata)

    @abc.abstractmethod
    def set_copyright(self, copyright_):  # pragma: no cover
        """Sets the copyright.

        :param copyright: the new copyright
        :type copyright: ``string``
        :raise: ``InvalidArgument`` -- ``copyright`` is invalid
        :raise: ``NoAccess`` -- ``Metadata.isReadOnly()`` is ``true``
        :raise: ``NullArgument`` -- ``copyright`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_copyright(self):  # pragma: no cover
        """Removes the copyright.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` is ``true`` or ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    copyright_ = property(fset=set_copyright, fdel=clear_copyright)

    @abc.abstractmethod
    def get_copyright_registration_metadata(self):  # pragma: no cover
        """Gets the metadata for the copyright registration.

        :return: metadata for the copyright registration
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.Metadata

    copyright_registration_metadata = property(fget=get_copyright_registration_metadata)

    @abc.abstractmethod
    def set_copyright_registration(self, registration):  # pragma: no cover
        """Sets the copyright registration.

        :param registration: the new copyright registration
        :type registration: ``string``
        :raise: ``InvalidArgument`` -- ``copyright`` is invalid
        :raise: ``NoAccess`` -- ``Metadata.isReadOnly()`` is ``true``
        :raise: ``NullArgument`` -- ``copyright`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_copyright_registration(self):  # pragma: no cover
        """Removes the copyright registration.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` is ``true`` or ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    copyright_registration = property(fset=set_copyright_registration, fdel=clear_copyright_registration)

    @abc.abstractmethod
    def get_distribute_verbatim_metadata(self):  # pragma: no cover
        """Gets the metadata for the distribute verbatim rights flag.

        :return: metadata for the distribution rights fields
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.Metadata

    distribute_verbatim_metadata = property(fget=get_distribute_verbatim_metadata)

    @abc.abstractmethod
    def set_distribute_verbatim(self, distribute_verbatim):  # pragma: no cover
        """Sets the distribution rights.

        :param distribute_verbatim: right to distribute verbatim copies
        :type distribute_verbatim: ``boolean``
        :raise: ``InvalidArgument`` -- ``distribute_verbatim`` is invalid
        :raise: ``NoAccess`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_distribute_verbatim(self):  # pragma: no cover
        """Removes the distribution rights.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` is ``true`` or ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    distribute_verbatim = property(fset=set_distribute_verbatim, fdel=clear_distribute_verbatim)

    @abc.abstractmethod
    def get_distribute_alterations_metadata(self):  # pragma: no cover
        """Gets the metadata for the distribute alterations rights flag.

        :return: metadata for the distribution rights fields
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.Metadata

    distribute_alterations_metadata = property(fget=get_distribute_alterations_metadata)

    @abc.abstractmethod
    def set_distribute_alterations(self, distribute_mods):  # pragma: no cover
        """Sets the distribute alterations flag.

        This also sets distribute verbatim to ``true``.

        :param distribute_mods: right to distribute modifications
        :type distribute_mods: ``boolean``
        :raise: ``InvalidArgument`` -- ``distribute_mods`` is invalid
        :raise: ``NoAccess`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_distribute_alterations(self):  # pragma: no cover
        """Removes the distribution rights.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` is ``true`` or ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    distribute_alterations = property(fset=set_distribute_alterations, fdel=clear_distribute_alterations)

    @abc.abstractmethod
    def get_distribute_compositions_metadata(self):  # pragma: no cover
        """Gets the metadata for the distribute compositions rights flag.

        :return: metadata for the distribution rights fields
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.Metadata

    distribute_compositions_metadata = property(fget=get_distribute_compositions_metadata)

    @abc.abstractmethod
    def set_distribute_compositions(self, distribute_comps):  # pragma: no cover
        """Sets the distribution rights.

        This sets distribute verbatim to ``true``.

        :param distribute_comps: right to distribute modifications
        :type distribute_comps: ``boolean``
        :raise: ``InvalidArgument`` -- ``distribute_comps`` is invalid
        :raise: ``NoAccess`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_distribute_compositions(self):  # pragma: no cover
        """Removes the distribution rights.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` is ``true`` or ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    distribute_compositions = property(fset=set_distribute_compositions, fdel=clear_distribute_compositions)

    @abc.abstractmethod
    def get_source_metadata(self):  # pragma: no cover
        """Gets the metadata for the source.

        :return: metadata for the source
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.Metadata

    source_metadata = property(fget=get_source_metadata)

    @abc.abstractmethod
    def set_source(self, source_id):  # pragma: no cover
        """Sets the source.

        :param source_id: the new publisher
        :type source_id: ``osid.id.Id``
        :raise: ``InvalidArgument`` -- ``source_id`` is invalid
        :raise: ``NoAccess`` -- ``Metadata.isReadOnly()`` is ``true``
        :raise: ``NullArgument`` -- ``source_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_source(self):  # pragma: no cover
        """Removes the source.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` is ``true`` or ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    source = property(fset=set_source, fdel=clear_source)

    @abc.abstractmethod
    def get_provider_links_metadata(self):  # pragma: no cover
        """Gets the metadata for the provider chain.

        :return: metadata for the provider chain
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.Metadata

    provider_links_metadata = property(fget=get_provider_links_metadata)

    @abc.abstractmethod
    def set_provider_links(self, resource_ids):  # pragma: no cover
        """Sets a provider chain in order from the most recent source to the originating source.

        :param resource_ids: the new source
        :type resource_ids: ``osid.id.Id[]``
        :raise: ``InvalidArgument`` -- ``resource_ids`` is invalid
        :raise: ``NoAccess`` -- ``Metadata.isReadOnly()`` is ``true``
        :raise: ``NullArgument`` -- ``resource_ids`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_provider_links(self):  # pragma: no cover
        """Removes the provider chain.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` is ``true`` or ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    provider_links = property(fset=set_provider_links, fdel=clear_provider_links)

    @abc.abstractmethod
    def get_created_date_metadata(self):  # pragma: no cover
        """Gets the metadata for the asset creation date.

        :return: metadata for the created date
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.Metadata

    created_date_metadata = property(fget=get_created_date_metadata)

    @abc.abstractmethod
    def set_created_date(self, created_date):  # pragma: no cover
        """Sets the created date.

        :param created_date: the new created date
        :type created_date: ``osid.calendaring.DateTime``
        :raise: ``InvalidArgument`` -- ``created_date`` is invalid
        :raise: ``NoAccess`` -- ``Metadata.isReadOnly()`` is ``true``
        :raise: ``NullArgument`` -- ``created_date`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_created_date(self):  # pragma: no cover
        """Removes the created date.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` is ``true`` or ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    created_date = property(fset=set_created_date, fdel=clear_created_date)

    @abc.abstractmethod
    def get_published_metadata(self):  # pragma: no cover
        """Gets the metadata for the published status.

        :return: metadata for the published field
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.Metadata

    published_metadata = property(fget=get_published_metadata)

    @abc.abstractmethod
    def set_published(self, published):  # pragma: no cover
        """Sets the published status.

        :param published: the published status
        :type published: ``boolean``
        :raise: ``NoAccess`` -- ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_published(self):  # pragma: no cover
        """Removes the published status.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` is ``true`` or ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    published = property(fset=set_published, fdel=clear_published)

    @abc.abstractmethod
    def get_published_date_metadata(self):  # pragma: no cover
        """Gets the metadata for the published date.

        :return: metadata for the published date
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.Metadata

    published_date_metadata = property(fget=get_published_date_metadata)

    @abc.abstractmethod
    def set_published_date(self, published_date):  # pragma: no cover
        """Sets the published date.

        :param published_date: the new published date
        :type published_date: ``osid.calendaring.DateTime``
        :raise: ``InvalidArgument`` -- ``published_date`` is invalid
        :raise: ``NoAccess`` -- ``Metadata.isReadOnly()`` is ``true``
        :raise: ``NullArgument`` -- ``published_date`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_published_date(self):  # pragma: no cover
        """Removes the puiblished date.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` is ``true`` or ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    published_date = property(fset=set_published_date, fdel=clear_published_date)

    @abc.abstractmethod
    def get_principal_credit_string_metadata(self):  # pragma: no cover
        """Gets the metadata for the principal credit string.

        :return: metadata for the credit string
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.Metadata

    principal_credit_string_metadata = property(fget=get_principal_credit_string_metadata)

    @abc.abstractmethod
    def set_principal_credit_string(self, credit_string):  # pragma: no cover
        """Sets the principal credit string.

        :param credit_string: the new credit string
        :type credit_string: ``string``
        :raise: ``InvalidArgument`` -- ``credit_string`` is invalid
        :raise: ``NoAccess`` -- ``Metadata.isReadOnly()`` is ``true``
        :raise: ``NullArgument`` -- ``credit_string`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_principal_credit_string(self):  # pragma: no cover
        """Removes the principal credit string.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` is ``true`` or ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    principal_credit_string = property(fset=set_principal_credit_string, fdel=clear_principal_credit_string)

    @abc.abstractmethod
    def get_composition_metadata(self):  # pragma: no cover
        """Gets the metadata for linking this asset to a composition.

        :return: metadata for the composition
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.Metadata

    composition_metadata = property(fget=get_composition_metadata)

    @abc.abstractmethod
    def set_composition(self, composition_id):  # pragma: no cover
        """Sets the composition.

        :param composition_id: a composition
        :type composition_id: ``osid.id.Id``
        :raise: ``InvalidArgument`` -- ``composition_id`` is invalid
        :raise: ``NoAccess`` -- ``Metadata.isReadOnly()`` is ``true``
        :raise: ``NullArgument`` -- ``composition_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_composition(self):  # pragma: no cover
        """Removes the composition link.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` is ``true`` or ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    composition = property(fset=set_composition, fdel=clear_composition)

    @abc.abstractmethod
    def get_asset_form_record(self, asset_record_type):  # pragma: no cover
        """Gets the ``AssetFormRecord`` corresponding to the given ``Asset`` record ``Type``.

        :param asset_record_type: an asset record type
        :type asset_record_type: ``osid.type.Type``
        :return: the asset form record
        :rtype: ``osid.repository.records.AssetFormRecord``
        :raise: ``NullArgument`` -- ``asset_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(asset_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.repository.records.AssetFormRecord


class AssetList:
    """Like all ``OsidLists,``  ``AssetList`` provides a means for accessing ``Asset`` elements sequentially either one at a time or many at a time.

    Examples: while (al.hasNext()) { Asset asset = al.getNextAsset(); }

    or
      while (al.hasNext()) {
           Asset[] assets = al.getNextAssets(al.available());
      }

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_next_asset(self):  # pragma: no cover
        """Gets the next ``Asset`` in this list.

        :return: the next ``Asset`` in this list. The ``has_next()`` method should be used to test that a next ``Asset`` is available before calling this method.
        :rtype: ``osid.repository.Asset``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.repository.Asset

    next_asset = property(fget=get_next_asset)

    @abc.abstractmethod
    def get_next_assets(self, n):  # pragma: no cover
        """Gets the next set of ``Assets`` in this list which must be less than or equal to the return from ``available()``.

        :param n: the number of ``Asset`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``Asset`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.repository.Asset``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.repository.Asset


class AssetContent:
    """``AssetContent`` represents a version of content represented by an ``Asset``.

    Although ``AssetContent`` is a separate ``OsidObject`` with its own
    ``Id`` to distuinguish it from other content inside an ``Asset,
    AssetContent`` can only be accessed through an ``Asset``.

    Once an ``Asset`` is selected, multiple contents should be
    negotiated using the size, fidelity, accessibility requirements or
    application evnironment.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_asset_id(self):  # pragma: no cover
        """Gets the ``Asset Id`` corresponding to this content.

        :return: the asset ``Id``
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    asset_id = property(fget=get_asset_id)

    @abc.abstractmethod
    def get_asset(self):  # pragma: no cover
        """Gets the ``Asset`` corresponding to this content.

        :return: the asset
        :rtype: ``osid.repository.Asset``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.repository.Asset

    asset = property(fget=get_asset)

    @abc.abstractmethod
    def get_accessibility_types(self):  # pragma: no cover
        """Gets the accessibility types associated with this content.

        :return: list of content accessibility types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    accessibility_types = property(fget=get_accessibility_types)

    @abc.abstractmethod
    def has_data_length(self):  # pragma: no cover
        """Tests if a data length is available.

        :return: ``true`` if a length is available for this content, ``false`` otherwise.
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_data_length(self):  # pragma: no cover
        """Gets the length of the data represented by this content in bytes.

        :return: the length of the data stream
        :rtype: ``cardinal``
        :raise: ``IllegalState`` -- ``has_data_length()`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # cardinal

    data_length = property(fget=get_data_length)

    @abc.abstractmethod
    def get_data(self):  # pragma: no cover
        """Gets the asset content data.

        :return: the length of the content data
        :rtype: ``osid.transport.DataInputStream``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.transport.DataInputStream

    data = property(fget=get_data)

    @abc.abstractmethod
    def has_url(self):  # pragma: no cover
        """Tests if a URL is associated with this content.

        :return: ``true`` if a URL is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_url(self):  # pragma: no cover
        """Gets the URL associated with this content for web-based retrieval.

        :return: the url for this data
        :rtype: ``string``
        :raise: ``IllegalState`` -- ``has_url()`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # string

    url = property(fget=get_url)

    @abc.abstractmethod
    def get_asset_content_record(self, asset_content_content_record_type):  # pragma: no cover
        """Gets the asset content record corresponding to the given ``AssetContent`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``asset_record_type`` may be the ``Type``
        returned in ``get_record_types()`` or any of its parents in a
        ``Type`` hierarchy where ``has_record_type(asset_record_type)``
        is ``true`` .

        :param asset_content_content_record_type: the type of the record to retrieve
        :type asset_content_content_record_type: ``osid.type.Type``
        :return: the asset content record
        :rtype: ``osid.repository.records.AssetContentRecord``
        :raise: ``NullArgument`` -- ``asset_content_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(asset_content_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.repository.records.AssetContentRecord


class AssetContentForm:
    """This is the form for creating and updating content for ``AssetContent``.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``AssetAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_accessibility_type_metadata(self):  # pragma: no cover
        """Gets the metadata for an accessibility type.

        :return: metadata for the accessibility types
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.Metadata

    accessibility_type_metadata = property(fget=get_accessibility_type_metadata)

    @abc.abstractmethod
    def add_accessibility_type(self, accessibility_type):  # pragma: no cover
        """Adds an accessibility type.

        Multiple types can be added.

        :param accessibility_type: a new accessibility type
        :type accessibility_type: ``osid.type.Type``
        :raise: ``InvalidArgument`` -- ``accessibility_type`` is invalid
        :raise: ``NoAccess`` -- ``Metadata.isReadOnly()`` is ``true``
        :raise: ``NullArgument`` -- ``accessibility_t_ype`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def remove_accessibility_type(self, accessibility_type):  # pragma: no cover
        """Removes an accessibility type.

        :param accessibility_type: accessibility type to remove
        :type accessibility_type: ``osid.type.Type``
        :raise: ``NoAccess`` -- ``Metadata.isReadOnly()`` is ``true``
        :raise: ``NotFound`` -- acessibility type not found
        :raise: ``NullArgument`` -- ``accessibility_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_accessibility_types(self):  # pragma: no cover
        """Removes all accessibility types.

        :raise: ``NoAccess`` -- ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    accessibility_types = property(fdel=clear_accessibility_types)

    @abc.abstractmethod
    def get_data_metadata(self):  # pragma: no cover
        """Gets the metadata for the content data.

        :return: metadata for the content data
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.Metadata

    data_metadata = property(fget=get_data_metadata)

    @abc.abstractmethod
    def set_data(self, data):  # pragma: no cover
        """Sets the content data.

        :param data: the content data
        :type data: ``osid.transport.DataInputStream``
        :raise: ``InvalidArgument`` -- ``data`` is invalid
        :raise: ``NoAccess`` -- ``Metadata.isReadOnly()`` is ``true``
        :raise: ``NullArgument`` -- ``data`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_data(self):  # pragma: no cover
        """Removes the content data.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` is ``true`` or ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    data = property(fset=set_data, fdel=clear_data)

    @abc.abstractmethod
    def get_url_metadata(self):  # pragma: no cover
        """Gets the metadata for the url.

        :return: metadata for the url
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.Metadata

    url_metadata = property(fget=get_url_metadata)

    @abc.abstractmethod
    def set_url(self, url):  # pragma: no cover
        """Sets the url.

        :param url: the new copyright
        :type url: ``string``
        :raise: ``InvalidArgument`` -- ``url`` is invalid
        :raise: ``NoAccess`` -- ``Metadata.isReadOnly()`` is ``true``
        :raise: ``NullArgument`` -- ``url`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_url(self):  # pragma: no cover
        """Removes the url.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` is ``true`` or ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    url = property(fset=set_url, fdel=clear_url)

    @abc.abstractmethod
    def get_asset_content_form_record(self, asset_content_record_type):  # pragma: no cover
        """Gets the ``AssetContentFormRecord`` corresponding to the given asset content record ``Type``.

        :param asset_content_record_type: an asset content record type
        :type asset_content_record_type: ``osid.type.Type``
        :return: the asset content form record
        :rtype: ``osid.repository.records.AssetContentFormRecord``
        :raise: ``NullArgument`` -- ``asset_content_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(asset_content_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.repository.records.AssetContentFormRecord


class AssetContentList:
    """Like all ``OsidLists,``  ``AssetContentList`` provides a means for accessing ``AssetContent`` elements sequentially either one at a time or many at a time.

    Examples: while (acl.hasNext()) { AssetContent content =
    acl.getNextAssetContent(); }

    or
      while (acl.hasNext()) {
           AssetContent[] contents = acl.getNextAssetContents(acl.available());
      }

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_next_asset_content(self):  # pragma: no cover
        """Gets the next ``AssetContent`` in this list.

        :return: the next ``AssetContent`` in this list. The ``has_next()`` method should be used to test that a next ``AssetContent`` is available before calling this method.
        :rtype: ``osid.repository.AssetContent``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.repository.AssetContent

    next_asset_content = property(fget=get_next_asset_content)

    @abc.abstractmethod
    def get_next_asset_contents(self, n):  # pragma: no cover
        """Gets the next set of ``AssetContents`` in this list which must be less than or equal to the return from ``available()``.

        :param n: the number of ``AssetContent`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``AssetContent`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.repository.AssetContent``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.repository.AssetContent


class Composition:
    """A ``Composition`` represents an authenticatable identity.

    Like all OSID objects, a ``Composition`` is identified by its Id and
    any persisted references should use the Id.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_children_ids(self):  # pragma: no cover
        """Gets the child ``Ids`` of this composition.

        :return: the composition child ``Ids``
        :rtype: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    children_ids = property(fget=get_children_ids)

    @abc.abstractmethod
    def get_children(self):  # pragma: no cover
        """Gets the children of this composition.

        :return: the composition children
        :rtype: ``osid.repository.CompositionList``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.repository.CompositionList

    children = property(fget=get_children)

    @abc.abstractmethod
    def get_composition_record(self, composition_record_type):  # pragma: no cover
        """Gets the composition record corresponding to the given ``Composition`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``composition_record_type`` may be the
        ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(composition_record_type)`` is ``true`` .

        :param composition_record_type: a composition record type
        :type composition_record_type: ``osid.type.Type``
        :return: the composition record
        :rtype: ``osid.repository.records.CompositionRecord``
        :raise: ``NullArgument`` -- ``composition_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(composition_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.repository.records.CompositionRecord


class CompositionForm:
    """This is the form for creating and updating ``Compositions``.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``CompositionAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_composition_form_record(self, composition_record_type):  # pragma: no cover
        """Gets the ``CompositionFormRecord`` corresponding to the given repository record ``Type``.

        :param composition_record_type: a composition record type
        :type composition_record_type: ``osid.type.Type``
        :return: the composition form record
        :rtype: ``osid.repository.records.CompositionFormRecord``
        :raise: ``NullArgument`` -- ``composition_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(composition_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.repository.records.CompositionFormRecord


class CompositionList:
    """Like all ``OsidLists,``  ``CompositionList`` provides a means for accessing ``Composition`` elements sequentially either one at a time or many at a time.

    Examples: while (cl.hasNext()) { Composition composition =
    cl.getNextComposition(); }

    or
      while (cl.hasNext()) {
           Composition[] compositions = cl.getNextCompositions(cl.available());
      }

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_next_composition(self):  # pragma: no cover
        """Gets the next ``Composition`` in this list.

        :return: the next ``Composition`` in this list. The ``has_next()`` method should be used to test that a next ``Composition`` is available before calling this method.
        :rtype: ``osid.repository.Composition``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.repository.Composition

    next_composition = property(fget=get_next_composition)

    @abc.abstractmethod
    def get_next_compositions(self, n):  # pragma: no cover
        """Gets the next set of ``Composition`` elements in this list which must be less than or equal to the return from ``available()``.

        :param n: the number of ``Composition`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``Composition`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.repository.Composition``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.repository.Composition


class Repository:
    """A repository defines a collection of assets."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_repository_record(self, repository_record_type):  # pragma: no cover
        """Gets the record corresponding to the given ``Repository`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``repository_record_type`` may be the
        ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(repository_record_type)`` is ``true`` .

        :param repository_record_type: a repository record type
        :type repository_record_type: ``osid.type.Type``
        :return: the repository record
        :rtype: ``osid.repository.records.RepositoryRecord``
        :raise: ``NullArgument`` -- ``repository_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(repository_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.repository.records.RepositoryRecord


class RepositoryForm:
    """This is the form for creating and updating repositories.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``RepositoryAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_repository_form_record(self, repository_record_type):  # pragma: no cover
        """Gets the ``RepositoryFormRecord`` corresponding to the given repository record ``Type``.

        :param repository_record_type: a repository record type
        :type repository_record_type: ``osid.type.Type``
        :return: the repository form record
        :rtype: ``osid.repository.records.RepositoryFormRecord``
        :raise: ``NullArgument`` -- ``repository_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(repository_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.repository.records.RepositoryFormRecord


class RepositoryList:
    """Like all ``OsidLists,``  ``RepositoryList`` provides a means for accessing ``Repository`` elements sequentially either one at a time or many at a time.

    Examples: while (rl.hasNext()) { Repository repository =
    rl.getNextRepository(); }

    or
      while (rl.hasNext()) {
           Repository[] repositories = rl.getNextRepositories(rl.available());
      }

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_next_repository(self):  # pragma: no cover
        """Gets the next ``Repository`` in this list.

        :return: the next ``Repository`` in this list. The ``has_next()`` method should be used to test that a next ``Repository`` is available before calling this method.
        :rtype: ``osid.repository.Repository``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.repository.Repository

    next_repository = property(fget=get_next_repository)

    @abc.abstractmethod
    def get_next_repositories(self, n):  # pragma: no cover
        """Gets the next set of ``Repository`` elements in this list which must be less than or equal to the return from ``available()``.

        :param n: the number of ``Repository`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``Repository`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.repository.Repository``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.repository.Repository


class RepositoryNode:
    """This interface is a container for a partial hierarchy retrieval.

    The number of hierarchy levels traversable through this interface
    depend on the number of levels requested in the
    ``RepositoryHierarchySession``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_repository(self):  # pragma: no cover
        """Gets the ``Repository`` at this node.

        :return: the repository represented by this node
        :rtype: ``osid.repository.Repository``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.repository.Repository

    repository = property(fget=get_repository)

    @abc.abstractmethod
    def get_parent_repository_nodes(self):  # pragma: no cover
        """Gets the parents of this repository.

        :return: the parents of the ``id``
        :rtype: ``osid.repository.RepositoryNodeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.repository.RepositoryNodeList

    parent_repository_nodes = property(fget=get_parent_repository_nodes)

    @abc.abstractmethod
    def get_child_repository_nodes(self):  # pragma: no cover
        """Gets the children of this repository.

        :return: the children of this repository
        :rtype: ``osid.repository.RepositoryNodeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.repository.RepositoryNodeList

    child_repository_nodes = property(fget=get_child_repository_nodes)


class RepositoryNodeList:
    """Like all ``OsidLists,``  ``RepositoryNodeList`` provides a means for accessing ``RepositoryNode`` elements sequentially either one at a time or many at a time.

    Examples: while (rnl.hasNext()) { RepositoryNode node =
    rnl.getNextRepositoryNode(); }

    or
      while (rnl.hasNext()) {
           RepositoryNode[] nodes = rnl.getNextRepositoryNodes(rnl.available());
      }

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_next_repository_node(self):  # pragma: no cover
        """Gets the next ``RepositoryNode`` in this list.

        :return: the next ``RepositoryNode`` in this list. The ``has_next()`` method should be used to test that a next ``RepositoryNode`` is available before calling this method.
        :rtype: ``osid.repository.RepositoryNode``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.repository.RepositoryNode

    next_repository_node = property(fget=get_next_repository_node)

    @abc.abstractmethod
    def get_next_repository_nodes(self, n):  # pragma: no cover
        """Gets the next set of ``RepositoryNode`` elements in this list which must be less than or equal to the return from ``available()``.

        :param n: the number of ``RepositoryNode`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``RepositoryNode`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.repository.RepositoryNode``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.repository.RepositoryNode
