# -*- coding: utf-8 -*-

# This module contains all the Object classes used by the MIT Core Concept
# Catalog (MC3) Handcar based implementation of the OSID Repository Service.

import json
import pdb
from ...abstract_osid.repository import objects as abc_repository_objects
from ..osid import objects as osid_objects
from ..osid import markers
from ..osid.metadata import Metadata
from .. import settings
from ..primitives import Id, Type, DisplayText
from ..id.objects import IdList
from ..osid.osid_errors import NullArgument, InvalidArgument, \
    NotFound, NoAccess, IllegalState, OperationFailed, Unimplemented, Unsupported

INVALID = 0
VALID = 1


class Asset(abc_repository_objects.Asset, osid_objects.OsidObject, markers.Aggregateable, markers.Sourceable):
    """An Asset represents some digital content.

    Example assets might be a text document, an image, or a movie. The
    content data, and metadata related directly to the content format
    and quality, is accessed through AssetContent. Assets , like all
    OsidObjects, include a type a record to qualify the Asset and
    include additional data. The division between the Asset Type and
    AssetContent is to separate data describing the asset from data
    describing the format of the contents, allowing a consumer to select
    among multiple formats, sizes or levels of fidelity.

    An example is a photograph of the Bay Bridge. The content may
    deliver a JPEG in multiple resolutions where the AssetContent may
    also desribe size or compression factor for each one. The content
    may also include an uncompressed TIFF version. The Asset  Type may
    be "photograph" indicating that the photo itself is the asset
    managed in this repository.

    Since an Asset may have multiple AssetContent structures, the
    decision of how many things to stuff inside a single asset comes
    down to if the content is actually a different format, or size, or
    quality, falling under the same creator, copyright, publisher and
    distribution rights as the original. This may, in some cases,
    provide a means to implement some accessibility, it doesn't handle
    the case where, to meet an accessibility requirement, one asset
    needs to be substituted for another. The Repository OSID manages
    this aspect outside the scope of the core Asset definition.

    Assets map to AssetSubjects.  AssetSubjects are OsidObjects that
    capture a subject matter. In the above example, an AssetSubject may
    be defined for the Bay Bridge and include data describing the
    bridge. The single subject can map to multiple assets depicting the
    bridge providing a single entry for a search and a single place to
    describe a bridge. Bridges, as physical items, may also be described
    using the Resource OSID in which case the use of the AssetSubject
    acts as a cover for the underlying Resource to assist repository-
    only consumers.

    The Asset definition includes some basic copyright and related
    licensing information to assist in finding free-to-use content, or
    to convey the distribution restrictions that may be placed on the
    asset. Generally, if no data is available it is to be assumed that
    all rights are reserved.

    A publisher is applicable if the content of this Asset has been
    published. Not all Assets in this Repository may have a published
    status and such a status may effect the applicability of copyright
    law. To trace the source of an Asset, both a provider and source are
    defined. The provider indicates where this repository acquired the
    asset and the source indicates the original provider or copyright
    owner. In the case of a published asset, the source is the
    publisher.

    Assets also define methods to facilitate searches over time and
    space as it relates to the subject matter. This may at times be
    redundant with the AssetSubject. In the case of the Bay Bridge
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
    Asset or AssetContent record Type.

    """
    _namespace = 'repository.Asset'

    def get_title(self):
        """Gets the proper title of this asset.

        This may be the same as the display name or the display name may
        be used for a less formal label.

        return: (osid.locale.DisplayText) - the title of this asset
        compliance: mandatory - This method must be implemented.

        """
        return DisplayText(self._my_map['title'])

    def is_copyright_status_known(self):
        """Tests if the copyright status is known.

        return: (boolean) - true if the copyright status of this asset
                is known, false otherwise. If false, is_public_domain(),
                can_distribute_verbatim(), can_distribute_alterations()
                and can_distribute_compositions() may also be false.
        compliance: mandatory - This method must be implemented.

        """
        return self._my_map['copyrightStatusKnown']

    def is_public_domain(self):
        """Tests if this asset is in the public domain.

        An asset is in the public domain if copyright is not applicable,
        the copyright has expired, or the copyright owner has expressly
        relinquished the copyright.

        return: (boolean) - true if this asset is in the public domain,
                false otherwise. If true, can_distribute_verbatim(),
                can_distribute_alterations() and
                can_distribute_compositions() must also be true.
        raise:  IllegalState - is_copyright_status_known() is false
        compliance: mandatory - This method must be implemented.

        """
        return self._my_map['publicDomain']

    def get_copyright(self):
        """Gets the copyright statement and of this asset which identifies
        the current copyright holder.

        For an asset in the public domain, this method may return the
        original copyright statement although it may be no longer valid.

        return: (osid.locale.DisplayText) - the copyright statement or
                an empty string if none available. An empty string does
                not imply the asset is not protected by copyright.
        raise:  IllegalState - is_copyright_status_known() is false
        compliance: mandatory - This method must be implemented.

        """
        try:
            # for some reason, some contents don't have this key
            # mc3-asset%3A222%40MIT-OEIT on oki-dev
            return DisplayText(self._my_map['copyright'])
        except:
            return DisplayText({
                "formatTypeId": "format.text%3APlain%40okapia.net",
                "languageTypeId": "639-2%3AENG%40iso.org",
                "scriptTypeId": "15924%3ALATN%40iso.org",
                "text": ""
            })

    def get_copyright_registration(self):
        """Gets the copyright registration information for this asset.

        return: (string) - the copyright registration. An empty string
                means the registration status isn't known.
        raise:  IllegalState - is_copyright_status_known() is false
        compliance: mandatory - This method must be implemented.

        """
        return self._my_map['copyrightRegistration']

    def can_distribute_verbatim(self):
        """Tests if there are any license restrictions on this asset that
        restrict the distribution, re-publication or public display of
        this asset, commercial or otherwise, without modification,
        alteration, or inclusion in other works.

        This method is intended to offer consumers a means of filtering
        out search results that restrict distribution for any purpose.
        The scope of this method does not include licensing that
        describes warranty disclaimers or attribution requirements. This
        method is intended for informational purposes only and does not
        replace or override the terms specified in a license agreement
        which may specify exceptions or additional restrictions.

        return: (boolean) - true if the asset can be distributed
                verbatim, false otherwise.
        raise:  IllegalState - is_copyright_status_known() is false
        compliance: mandatory - This method must be implemented.

        """
        return self._my_map['canDistributeVerbatim']

    def can_distribute_alterations(self):
        """Tests if there are any license restrictions on this asset that
        restrict the distribution, re-publication or public display of
        any alterations or modifications to this asset, commercial or
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

        return: (boolean) - true if the asset can be modified, false
                otherwise. If true, can_distribute_verbatim() must also
                be true.
        raise:  IllegalState - is_copyright_status_known() is false
        compliance: mandatory - This method must be implemented.

        """
        return self._my_map['canDistributeAlterations']

    def can_distribute_compositions(self):
        """Tests if there are any license restrictions on this asset that
        restrict the distribution, re-publication or public display of
        this asset as an inclusion within other content or composition,
        commercial or otherwise, for any purpose, including restrictions
        upon the distribution or license of the resulting composition.

        This method is intended to offer consumers a means of filtering
        out search results that restrict the use of this asset within
        compositions. The scope of this method does not include
        licensing that describes warranty disclaimers or attribution
        requirements. This method is intended for informational purposes
        only and does not replace or override the terms specified in a
        license agreement which may specify exceptions or additional
        restrictions.

        return: (boolean) - true if the asset can be part of a larger
                composition false otherwise. If true,
                can_distribute_verbatim() must also be true.
        raise:  IllegalState - is_copyright_status_known() is false
        compliance: mandatory - This method must be implemented.

        """
        return self._my_map['canDistributeCompositions']

    def get_source_id(self):
        """Gets the Resource Id of the source of this asset.

        The source is the original owner of the copyright of this asset
        and may differ from the creator of this asset. The source for a
        published book written by Margaret Mitchell would be Macmillan.
        The source for an unpublished painting by Arthur Goodwin would
        be Arthur Goodwin.

        An Asset is Sourceable and also contains a provider identity.
        The provider is the entity that makes this digital asset
        available in this repository but may or may not be the publisher
        of the contents depicted in the asset. For example, a map
        published by Ticknor and Fields in 1848 may have a provider of
        Library of Congress and a source of Ticknor and Fields. If
        copied from a repository at Middlebury College, the provider
        would be Middlebury College and a source of Ticknor and Fields.

        return: (osid.id.Id) - the source Id
        compliance: mandatory - This method must be implemented.

        """
        return Id(self._my_map['sourceId'])

    def get_source(self):
        """Gets the Resource of the source of this asset.

        The source is the original owner of the copyright of this asset
        and may differ from the creator of this asset. The source for a
        published book written by Margaret Mitchell would be Macmillan.
        The source for an unpublished painting by Arthur Goodwin would
        be Arthur Goodwin.

        return: (osid.resource.Resource) - the source
        compliance: mandatory - This method must be implemented.

        """
        raise Unimplemented()

    def get_provider_link_ids(self):
        """Gets the resource Ids representing the source of this asset in
        order from the most recent provider to the originating source.

        return: (osid.id.IdList) - the provider Ids
        compliance: mandatory - This method must be implemented.

        """
        id_list = []
        for id_ in self._my_map['providerLinkIds']:
            id_list.append(Id(id_))
        return IdList(id_list)

    def get_provider_links(self):
        """Gets the Resources representing the source of this asset in
        order from the most recent provider to the originating source.

        return: (osid.resource.ResourceList) - the provider chain
        raise:  OperationFailed - unable to complete request
        compliance: mandatory - This method must be implemented.

        """
        raise Unimplemented()

    def get_created_date(self):
        """Gets the created date of this asset, which is generally not
        related to when the object representing the asset was created.

        The date returned may indicate that not much is known.

        return: (osid.calendaring.DateTime) - the created date
        compliance: mandatory - This method must be implemented.

        """
        raise Unimplemented()

    def is_published(self):
        """Tests if this asset has been published.

        Not all assets viewable in this repository may have been
        published. The source of a published asset indicates the
        publisher.

        return: (boolean) - true if this asset has been published, false
                if unpublished or its published status is not known
        compliance: mandatory - This method must be implemented.

        """
        return self._my_map['published']

    def get_published_date(self):
        """Gets the published date of this asset.

        Unpublished assets have no published date. A published asset has
        a date available, however the date returned may indicate that
        not much is known.

        return: (osid.calendaring.DateTime) - the published date
        raise:  IllegalState - is_published() is false
        compliance: mandatory - This method must be implemented.

        """
        raise Unimplemented()

    def get_principal_credit_string(self):
        """Gets the credits of the principal people involved in the
        production of this asset as a display string.

        return: (osid.locale.DisplayText) - the principal credits
        compliance: mandatory - This method must be implemented.

        """
        return DisplayText(self._my_map['principalCreditString'])

    def get_asset_content_ids(self):
        """Gets the content Ids of this asset.

        return: (osid.id.IdList) - the asset content Ids
        compliance: mandatory - This method must be implemented.

        """
        contents = self._my_map['assetContents']
        return IdList([c['id'] for c in contents])

    def get_asset_contents(self):
        """Gets the content of this asset.

        return: (osid.repository.AssetContentList) - the asset contents
        raise:  OperationFailed - unable to complete request
        compliance: mandatory - This method must be implemented.

        """
        return AssetContentList(self._my_map['assetContents'])

    def is_composition(self):
        """Tetss if this asset is a representation of a composition of
        assets.

        return: (boolean) - true if this asset is a composition, false
                otherwise
        compliance: mandatory - This method must be implemented.

        """
        return self._my_map['composition']

    def get_composition_id(self):
        """Gets the Composition  Id corresponding to this asset.

        return: (osid.id.Id) - the composiiton Id
        raise:  IllegalState - is_composition() is false
        compliance: mandatory - This method must be implemented.

        """
        return Id(self._my_map['compositionId'])

    def get_composition(self):
        """Gets the Composition corresponding to this asset.

        return: (osid.repository.Composition) - the composiiton
        raise:  IllegalState - is_composition() is false
        raise:  OperationFailed - unable to complete request
        compliance: mandatory - This method must be implemented.

        """
        raise Unimplemented()

    def get_asset_record(self, asset_record_type=None):
        """Gets the asset record corresponding to the given Asset record
        Type.

        This method is used to retrieve an object implementing the
        requested record. The assetRecordType may be the Type returned
        in get_record_types() or any of its parents in a Type hierarchy
        where hasRecordType(assetRecordType) is true .

        arg:    assetRecordType (osid.type.Type): an asset record type
        return: (osid.repository.records.AssetRecord) - the asset record
        raise:  NullArgument - assetRecordType is null
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported - hasRecordType(assetRecordType) is false
        compliance: mandatory - This method must be implemented.

        """
        if not self.has_record_type():
            raise IllegalState()
        else:  # This should never get called.
            raise Unimplemented()

    title = property(get_title)
    copyright = property(get_copyright)
    copyright_registration = property(get_copyright_registration)
    source_id = property(get_source_id)
    source = property(get_source)
    provider_link_ids = property(get_provider_link_ids)
    provider_links = property(get_provider_links)
    created_date = property(get_created_date)
    published_date = property(get_published_date)
    principal_credit_string = property(get_principal_credit_string)
    asset_content_ids = property(get_asset_content_ids)
    asset_contents = property(get_asset_contents)
    composition_id = property(get_composition_id)
    composition = property(get_composition)


class AssetForm(abc_repository_objects.AssetForm, osid_objects.OsidObjectForm, osid_objects.OsidAggregateableForm, osid_objects.OsidSourceableForm):
    """This is the form for creating and updating ``Assets``.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``AssetAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.

    """
    _namespace = 'repository.Asset'

    def _init_map(self):
        osid_objects.OsidObjectForm._init_map(self)
        #        self._my_map['@type'] = 'assetBean'
        self._my_map['Id'] = ''
        #        self._my_map['current'] = True
        self._my_map['title'] = {
            'languageTypeId': settings.LANGUAGE_TYPE_ID,
            'scriptTypeId': settings.SCRIPT_TYPE_ID,
            'formatTypeId': settings.FORMAT_TYPE_ID,
            'text': ''
        }
        self._my_map['publicDomain'] = False
        self._my_map['copyright'] = {
            'languageTypeId': settings.LANGUAGE_TYPE_ID,
            'scriptTypeId': settings.SCRIPT_TYPE_ID,
            'formatTypeId': settings.FORMAT_TYPE_ID,
            'text': ''
        }
        self._my_map['copyrightStatusKnown'] = False
        self._my_map['canDistributeVerbatim'] = False
        self._my_map['canDistributeAlterations'] = False
        self._my_map['canDistributeCompositions'] = False
        self._my_map['sourceId'] = None
        self._my_map['providerLinkIds'] = []
        #        self._my_map['createdDate'] = ''
        self._my_map['published'] = False
        #        self._my_map['publishedDate'] = ''
        self._my_map['principalCreditString'] = {
            'languageTypeId': settings.LANGUAGE_TYPE_ID,
            'scriptTypeId': settings.SCRIPT_TYPE_ID,
            'formatTypeId': settings.FORMAT_TYPE_ID,
            'text': ''
        }
        #        self._my_map['composition'] = False
        self._my_map['compositionId'] = None
        self._my_map['assetContents'] = []

    def _init_validity_map(self):
        osid_objects.OsidObjectForm._init_validity_map(self)
        self._validity_map['title'] = VALID
        self._validity_map['public_domain'] = VALID
        self._validity_map['copyright'] = VALID
        self._validity_map['distribute_verbatim'] = VALID
        self._validity_map['distribute_alterations'] = VALID
        self._validity_map['distribute_compositions'] = VALID
        self._validity_map['source'] = VALID
        self._validity_map['provider_links'] = VALID
        self._validity_map['created_date'] = VALID
        self._validity_map['published'] = VALID
        self._validity_map['published_date'] = VALID
        self._validity_map['principal_credit_string'] = VALID
        self._validity_map['composition_id'] = VALID

    def get_title_metadata(self):
        """Gets the metadata for an asset title.

        :return: metadata for the title
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return Metadata(**settings.METADATA['title'])

    title_metadata = property(fget=get_title_metadata)

    def set_title(self, title=None):
        """Sets the title.

        :param title: the new title
        :type title: ``string``
        :raise: ``InvalidArgument`` -- ``title`` is invalid
        :raise: ``NoAccess`` -- ``Metadata.isReadOnly()`` is ``true``
        :raise: ``NullArgument`` -- ``title`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        if title is None:
            raise NullArgument()
        metadata = Metadata(**settings.METADATA['title'])
        if metadata.is_read_only():
            raise NoAccess()
        if self._is_valid_input(title, metadata, array=False):
            self._my_map['title']['text'] = title
        else:
            raise InvalidArgument()

    def clear_title(self):
        """Removes the title.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` is ``true`` or
            ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        metadata = Metadata(**settings.METADATA['title'])
        if metadata.is_read_only() or metadata.is_required():
            raise NoAccess()
        self._my_map['title']['text'] = ''

    title = property(fset=set_title, fdel=clear_title)

    def get_public_domain_metadata(self):
        """Gets the metadata for the public domain flag.

        :return: metadata for the public domain
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return Metadata(**settings.METADATA['public_domain'])

    public_domain_metadata = property(fget=get_public_domain_metadata)

    def set_public_domain(self, public_domain=None):
        """Sets the public domain flag.

        :param public_domain: the public domain status
        :type public_domain: ``boolean``
        :raise: ``NoAccess`` -- ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        if public_domain is None:
            raise NullArgument()
        metadata = Metadata(**settings.METADATA['public_domain'])
        if metadata.is_read_only():
            raise NoAccess()
        if self._is_valid_input(public_domain, metadata, array=False):
            self._my_map['publicDomain'] = public_domain
        else:
            raise InvalidArgument()

    def clear_public_domain(self):
        """Removes the public domain status.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` is ``true`` or
            ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        metadata = Metadata(**settings.METADATA['public_domain'])
        if metadata.is_read_only() or metadata.is_required():
            raise NoAccess()
        self._my_map['publicDomain'] = False

    public_domain = property(fset=set_public_domain, fdel=clear_public_domain)

    def get_copyright_metadata(self):
        """Gets the metadata for the copyright.

        :return: metadata for the copyright
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return Metadata(**settings.METADATA['copyright'])

    copyright_metadata = property(fget=get_copyright_metadata)

    def set_copyright(self, copyright=None):
        """Sets the copyright.

        :param copyright: the new copyright
        :type copyright: ``string``
        :raise: ``InvalidArgument`` -- ``copyright`` is invalid
        :raise: ``NoAccess`` -- ``Metadata.isReadOnly()`` is ``true``
        :raise: ``NullArgument`` -- ``copyright`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        if copyright is None:
            raise NullArgument()
        metadata = Metadata(**settings.METADATA['copyright'])
        if metadata.is_read_only():
            raise NoAccess()
        if self._is_valid_input(copyright, metadata, array=False):
            self._my_map['copyright']['text'] = copyright
        else:
            raise InvalidArgument()

    def clear_copyright(self):
        """Removes the copyright.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` is ``true`` or
            ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        metadata = Metadata(**settings.METADATA['copyright'])
        if metadata.is_read_only() or metadata.is_required():
            raise NoAccess()
        self._my_map['copyright']['text'] = ''

    copyright = property(fset=set_copyright, fdel=clear_copyright)

    def get_copyright_registration_metadata(self):
        """Gets the metadata for the copyright registration.

        return: (osid.Metadata) - metadata for the copyright
                registration
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceForm.get_group_metadata_template
        metadata = dict(self._mdata['copyright_registration'])
        metadata.update({'existing_string_values': self._my_map['copyrightRegistration']})
        return Metadata(**metadata)

    copyright_registration_metadata = property(fget=get_copyright_registration_metadata)

    def set_copyright_registration(self, registration):
        """Sets the copyright registration.

        arg:    registration (string): the new copyright registration
        raise:  InvalidArgument - ``copyright`` is invalid
        raise:  NoAccess - ``Metadata.isReadOnly()`` is ``true``
        raise:  NullArgument - ``copyright`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.repository.AssetContentForm.set_url_template
        if self.get_copyright_registration_metadata().is_read_only():
            raise NoAccess()
        if not self._is_valid_string(
                registration,
                self.get_copyright_registration_metadata()):
            raise InvalidArgument()
        self._my_map['copyrightRegistration'] = registration

    def clear_copyright_registration(self):
        """Removes the copyright registration.

        raise:  NoAccess - ``Metadata.isRequired()`` is ``true`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        if (self.get_copyright_registration_metadata().is_read_only() or
                self.get_copyright_registration_metadata().is_required()):
            raise NoAccess()
        self._my_map['copyrightRegistration'] = dict(self._copyright_registration_default)

    copyright_registration = property(fset=set_copyright_registration, fdel=clear_copyright_registration)

    def get_distribute_verbatim_metadata(self):
        """Gets the metadata for the distribute verbatim rights flag.

        :return: metadata for the distribution rights fields
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return Metadata(**settings.METADATA['distribute_verbatim'])

    distribute_verbatim_metadata = property(fget=get_distribute_verbatim_metadata)

    def set_distribute_verbatim(self, distribute_verbatim=None):
        """Sets the distribution rights.

        :param distribute_verbatim: right to distribute verbatim copies
        :type distribute_verbatim: ``boolean``
        :raise: ``InvalidArgument`` -- ``distribute_verbatim`` is invalid
        :raise: ``NoAccess`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        if distribute_verbatim is None:
            raise NullArgument()
        metadata = Metadata(**settings.METADATA['distribute_verbatim'])
        if metadata.is_read_only():
            raise NoAccess()
        if self._is_valid_input(distribute_verbatim, metadata, array=False):
            self._my_map['canDistributeVerbatim'] = distribute_verbatim
        else:
            raise InvalidArgument()

    def clear_distribute_verbatim(self):
        """Removes the distribution rights.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` is ``true`` or
            ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        metadata = Metadata(**settings.METADATA['distribute_verbatim'])
        if metadata.is_read_only() or metadata.is_required():
            raise NoAccess()
        self._my_map['canDistributeVerbatim'] = False

    distribute_verbatim = property(fset=set_distribute_verbatim,
                                   fdel=clear_distribute_verbatim)

    def get_distribute_alterations_metadata(self):
        """Gets the metadata for the distribute alterations rights flag.

        :return: metadata for the distribution rights fields
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return Metadata(**settings.METADATA['distribute_alterations'])

    distribute_alterations_metadata = property(fget=get_distribute_alterations_metadata)

    def set_distribute_alterations(self, distribute_mods=None):
        """Sets the distribute alterations flag.

        This also sets distribute verbatim to ``true``.

        :param distribute_mods: right to distribute modifications
        :type distribute_mods: ``boolean``
        :raise: ``InvalidArgument`` -- ``distribute_mods`` is invalid
        :raise: ``NoAccess`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        if distribute_mods is None:
            raise NullArgument()
        metadata = Metadata(**settings.METADATA['distribute_alterations'])
        if metadata.is_read_only():
            raise NoAccess()
        if self._is_valid_input(distribute_mods, metadata, array=False):
            self._my_map['canDistributeAlterations'] = distribute_mods
        else:
            raise InvalidArgument()

    def clear_distribute_alterations(self):
        """Removes the distribution rights.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` is ``true`` or
            ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        metadata = Metadata(**settings.METADATA['distribute_alterations'])
        if metadata.is_read_only() or metadata.is_required():
            raise NoAccess()
        self._my_map['canDistributeAlterations'] = False

    distribute_alterations = property(fset=set_distribute_alterations,
                                      fdel=clear_distribute_alterations)

    def get_distribute_compositions_metadata(self):
        """Gets the metadata for the distribute compositions rights flag.

        :return: metadata for the distribution rights fields
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return Metadata(**settings.METADATA['distribute_compositions'])

    distribute_compositions_metadata = property(fget=get_distribute_compositions_metadata)

    def set_distribute_compositions(self, distribute_comps=None):
        """Sets the distribution rights.

        This sets distribute verbatim to ``true``.

        :param distribute_comps: right to distribute modifications
        :type distribute_comps: ``boolean``
        :raise: ``InvalidArgument`` -- ``distribute_comps`` is invalid
        :raise: ``NoAccess`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        if distribute_comps is None:
            raise NullArgument()
        metadata = Metadata(**settings.METADATA['distribute_compositions'])
        if metadata.is_read_only():
            raise NoAccess()
        if self._is_valid_input(distribute_comps, metadata, array=False):
            self._my_map['canDistributeCompositions'] = distribute_comps
        else:
            raise InvalidArgument()

    def clear_distribute_compositions(self):
        """Removes the distribution rights.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` is ``true`` or
            ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        metadata = Metadata(**settings.METADATA['distribute_compositions'])
        if metadata.is_read_only() or metadata.is_required():
            raise NoAccess()
        self._my_map['canDistributeCompositions'] = False

    distribute_compositions = property(fset=set_distribute_compositions,
                                       fdel=clear_distribute_compositions)

    def get_source_metadata(self):
        """Gets the metadata for the source.

        :return: metadata for the source
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return Metadata(**settings.METADATA['source_id'])

    source_metadata = property(fget=get_source_metadata)

    def set_source(self, source_id=None):
        """Sets the source.

        :param source_id: the new publisher
        :type source_id: ``osid.id.Id``
        :raise: ``InvalidArgument`` -- ``source_id`` is invalid
        :raise: ``NoAccess`` -- ``Metadata.isReadOnly()`` is ``true``
        :raise: ``NullArgument`` -- ``source_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        if source_id is None:
            raise NullArgument()
        metadata = Metadata(**settings.METADATA['source_id'])
        if metadata.is_read_only():
            raise NoAccess()
        if self._is_valid_input(source_id, metadata, array=False):
            self._my_map['sourceId'] = str(source_id)
        else:
            raise InvalidArgument()

    def clear_source(self):
        """Removes the source.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` is ``true`` or
            ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        metadata = Metadata(**settings.METADATA['source_id'])
        if metadata.is_read_only() or metadata.is_required():
            raise NoAccess()
        self._my_map['source_id'] = ''

    source = property(fset=set_source, fdel=clear_source)

    def get_provider_links_metadata(self):
        """Gets the metadata for the provider chain.

        :return: metadata for the provider chain
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return Metadata(**settings.METADATA['provider_links'])

    provider_links_metadata = property(fget=get_provider_links_metadata)

    def set_provider_links(self, resource_ids=None):
        """Sets a provider chain in order from the most recent source to
        the originating source.

        :param resource_ids: the new source
        :type resource_ids: ``osid.id.Id[]``
        :raise: ``InvalidArgument`` -- ``resource_ids`` is invalid
        :raise: ``NoAccess`` -- ``Metadata.isReadOnly()`` is ``true``
        :raise: ``NullArgument`` -- ``resource_ids`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        if resource_ids is None:
            raise NullArgument()
        metadata = Metadata(**settings.METADATA['provider_link_ids'])
        if metadata.is_read_only():
            raise NoAccess()
        if self._is_valid_input(resource_ids, metadata, array=True):
            self._my_map['providerLinkIds'] = []
            for i in resource_ids:
                self._my_map['providerLinkIds'].append(str(i))
        else:
            raise InvalidArgument()

    def clear_provider_links(self):
        """Removes the provider chain.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` is ``true`` or
            ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        metadata = Metadata(**settings.METADATA['provider_link_ids'])
        if metadata.is_read_only() or metadata.is_required():
            raise NoAccess()
        self._my_map['providerLinkIds'] = []

    provider_links = property(fset=set_provider_links, fdel=clear_provider_links)

    def get_created_date_metadata(self):
        """Gets the metadata for the asset creation date.

        :return: metadata for the created date
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return Metadata(**settings.METADATA['created_date'])

    created_date_metadata = property(fget=get_created_date_metadata)

    def set_created_date(self, created_date=None):
        """Sets the created date.

        :param created_date: the new created date
        :type created_date: ``osid.calendaring.DateTime``
        :raise: ``InvalidArgument`` -- ``created_date`` is invalid
        :raise: ``NoAccess`` -- ``Metadata.isReadOnly()`` is ``true``
        :raise: ``NullArgument`` -- ``created_date`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        if created_date is None:
            raise NullArgument()
        metadata = Metadata(**settings.METADATA['created_date'])
        if metadata.is_read_only():
            raise NoAccess()
        if self._is_valid_input(created_date, metadata, array=False):
            self._my_map['createdDate'] = created_date  # This is probably wrong
        else:
            raise InvalidArgument()

    def clear_created_date(self):
        """Removes the created date.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` is ``true`` or ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        metadata = Metadata(**settings.METADATA['created_date'])
        if metadata.is_read_only() or metadata.is_required():
            raise NoAccess()
        self._my_map['createdDate'] = ''  # This might be wrong

    created_date = property(fset=set_created_date, fdel=clear_created_date)

    def get_published_metadata(self):
        """Gets the metadata for the published status.

        :return: metadata for the published field
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return Metadata(**settings.METADATA['published'])

    published_metadata = property(fget=get_published_metadata)

    def set_published(self, published=None):
        """Sets the published status.

        :param published: the published status
        :type published: ``boolean``
        :raise: ``NoAccess`` -- ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        if published is None:
            raise NullArgument()
        metadata = Metadata(**settings.METADATA['published'])
        if metadata.is_read_only():
            raise NoAccess()
        if self._is_valid_input(published, metadata, array=False):
            self._my_map['published'] = published
        else:
            raise InvalidArgument()

    def clear_published(self):
        """Removes the published status.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` is ``true`` or ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        metadata = Metadata(**settings.METADATA['published'])
        if metadata.is_read_only() or metadata.is_required():
            raise NoAccess()
        self._my_map['published'] = False

    published = property(fset=set_published, fdel=clear_published)

    def get_published_date_metadata(self):
        """Gets the metadata for the published date.

        :return: metadata for the published date
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return Metadata(**settings.METADATA['published_date'])

    published_date_metadata = property(fget=get_published_date_metadata)

    def set_published_date(self, published_date=None):
        """Sets the published date.

        :param published_date: the new published date
        :type published_date: ``osid.calendaring.DateTime``
        :raise: ``InvalidArgument`` -- ``published_date`` is invalid
        :raise: ``NoAccess`` -- ``Metadata.isReadOnly()`` is ``true``
        :raise: ``NullArgument`` -- ``published_date`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        if published_date is None:
            raise NullArgument()
        metadata = Metadata(**settings.METADATA['published_date'])
        if metadata.is_read_only():
            raise NoAccess()
        if self._is_valid_input(published_date, metadata, array=False):
            self._my_map['publishedDate'] = published_date  # This is probably wrong
        else:
            raise InvalidArgument()

    def clear_published_date(self):
        """Removes the puiblished date.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` is ``true`` or ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        metadata = Metadata(**settings.METADATA['published_date'])
        if metadata.is_read_only() or metadata.is_required():
            raise NoAccess()
        self._my_map['publishedDate'] = ''  # This might be wrong

    published_date = property(fset=set_published_date, fdel=clear_published_date)

    def get_principal_credit_string_metadata(self):
        """Gets the metadata for the principal credit string.

        :return: metadata for the credit string
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return Metadata(**settings.METADATA['principal_credit_string'])

    principal_credit_string_metadata = property(fget=get_principal_credit_string_metadata)

    def set_principal_credit_string(self, credit_string=None):
        """Sets the principal credit string.

        :param credit_string: the new credit string
        :type credit_string: ``string``
        :raise: ``InvalidArgument`` -- ``credit_string`` is invalid
        :raise: ``NoAccess`` -- ``Metadata.isReadOnly()`` is ``true``
        :raise: ``NullArgument`` -- ``credit_string`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        if credit_string is None:
            raise NullArgument()
        metadata = Metadata(**settings.METADATA['principal_credit_string'])
        if metadata.is_read_only():
            raise NoAccess()
        if self._is_valid_input(credit_string, metadata, array=False):
            self._my_map['principalCreditString']['text'] = credit_string
        else:
            raise InvalidArgument()

    def clear_principal_credit_string(self):
        """Removes the principal credit string.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` is ``true`` or ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        metadata = Metadata(**settings.METADATA['principal_credit_string'])
        if metadata.is_read_only() or metadata.is_required():
            raise NoAccess()
        self._my_map['principalCreditString']['text'] = ''

    principal_credit_string = property(fset=set_principal_credit_string, fdel=clear_principal_credit_string)

    def get_composition_metadata(self):
        """Gets the metadata for linking this asset to a composition.

        :return: metadata for the composition
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return Metadata(**settings.METADATA['composition'])

    composition_metadata = property(fget=get_composition_metadata)

    def set_composition(self, composition_id=None):
        """Sets the composition.

        :param composition_id: a composition
        :type composition_id: ``osid.id.Id``
        :raise: ``InvalidArgument`` -- ``composition_id`` is invalid
        :raise: ``NoAccess`` -- ``Metadata.isReadOnly()`` is ``true``
        :raise: ``NullArgument`` -- ``composition_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        if composition_id is None:
            raise NullArgument()
        metadata = Metadata(**settings.METADATA['composition_id'])
        if metadata.is_read_only():
            raise NoAccess()
        if self._is_valid_input(composition_id, metadata, array=False):
            self._my_map['compositionId'] = str(composition_id)
        else:
            raise InvalidArgument()

    def clear_composition(self):
        """Removes the composition link.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` is ``true`` or ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        metadata = Metadata(**settings.METADATA['composition_id'])
        if metadata.is_read_only() or metadata.is_required():
            raise NoAccess()
        self._my_map['compositionId'] = ''

    composition = property(fset=set_composition, fdel=clear_composition)

    def get_asset_form_record(self, asset_record_type=None):
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
        raise Unimplemented()


class AssetList(abc_repository_objects.AssetList, osid_objects.OsidList):
    """Like all OsidLists,  AssetList provides a means for accessing Asset
    elements sequentially either one at a time or many at a time.

    Examples: while (al.hasNext()) { Asset asset = al.getNextAsset(); }

    or
      while (al.hasNext()) {
           Asset[] assets = al.getNextAssets(al.available());
      }



    """

    def get_next_asset(self):
        """Gets the next Asset in this list.

        return: (osid.repository.Asset) - the next Asset in this list.
                The has_next() method should be used to test that a next
                Asset is available before calling this method.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        compliance: mandatory - This method must be implemented.

        """
        try:
            next_object = next(self)
        except StopIteration:
            raise IllegalState('no more elements available in this list')
        except Exception:  # Need to specify exceptions here!
            raise OperationFailed()
        else:
            return next_object

    def next(self):
        try:
            next_object = osid_objects.OsidList.next(self)
        except StopIteration:
            raise
        except Exception:  # Need to specify exceptions here!
            raise OperationFailed()
        if isinstance(next_object, dict):
            next_object = Asset(next_object)
        return next_object

    __next__ = next

    def get_next_assets(self, n=None):
        """Gets the next set of Assets in this list which must be less than
        or equal to the return from available().

        arg:    n (cardinal): the number of Asset elements requested
                which must be less than or equal to available()
        return: (osid.repository.Asset) - an array of Asset elements.
                The length of the array is less than or equal to the
                number specified.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        compliance: mandatory - This method must be implemented.

        """
        if n > self.available():
            # !!! This is not quite as specified (see method docs) !!!
            raise IllegalState('not enough elements available in this list')
        else:
            next_list = []
            x = 0
            while x < n:
                try:
                    next_list.append(next(self))
                except Exception:  # Need to specify exceptions here!
                    raise OperationFailed()
                x = x + 1
            return next_list

    next_asset = property(get_next_asset)


class AssetContent(abc_repository_objects.AssetContent, osid_objects.OsidObject):
    """AssetContent represents a version of content represented by an
    Asset.

    Although AssetContent is a separate OsidObject with its own Id to
    distuinguish it from other content inside an Asset, AssetContent can
    only be accessed through an Asset.

    Once an Asset is selected, multiple contents should be negotiated
    using the size, fidelity, accessibility requirements or application
    evnironment.

    """
    _namespace = 'repository.AssetContent'

    def get_asset_id(self):
        """Gets the Asset Id corresponding to this content.

        return: (osid.id.Id) - the asset Id
        compliance: mandatory - This method must be implemented.

        """
        return Id(self._my_map['assetId'])

    def get_asset(self):
        """Gets the Asset corresponding to this content.

        return: (osid.repository.Asset) - the asset
        compliance: mandatory - This method must be implemented.

        """
        # get osid_object_map for asset
        # or initialize AssetContent with the asset map too?
        return Asset()  # THIS WILL FAIL!

    def get_accessibility_types(self):
        """Gets the accessibility types associated with this content.

        return: (osid.type.TypeList) - list of content accessibility
                types
        compliance: mandatory - This method must be implemented.

        """
        raise Unimplemented()

    def has_data_length(self):
        """Tests if a data length is available.

        return: (boolean) - true if a length is available for this
                content, false otherwise.
        compliance: mandatory - This method must be implemented.

        """
        return False

    def get_data_length(self):
        """Gets the length of the data represented by this content in
        bytes.

        return: (cardinal) - the length of the data stream
        raise:  IllegalState - has_data_length() is false
        compliance: mandatory - This method must be implemented.

        """
        if not self.has_data_length():
            raise IllegalState()
        else:  # this should never be called
            raise Unimplemented()

    def get_data(self):
        """Gets the asset content data.

        return: (osid.transport.DataInputStream) - the length of the
                content data
        raise:  OperationFailed - unable to complete request
        compliance: mandatory - This method must be implemented.

        """
        raise Unimplemented()

    def has_url(self):
        """Tests if a URL is associated with this content.

        return: (boolean) - true if a URL is available, false otherwise
        compliance: mandatory - This method must be implemented.

        """
        # changing this, because it returns FALSE for an empty url
        return 'url' in self._my_map
        # return bool(self._my_map['url'])

    def get_url(self):
        """Gets the URL associated with this content for web-based
        retrieval.

        return: (string) - the url for this data
        raise:  IllegalState - has_url() is false
        compliance: mandatory - This method must be implemented.

        """
        if not self.has_url():
            raise IllegalState()
        else:
            return self._my_map['url']

    def get_asset_content_record(self, asset_content_content_record_type=None):
        """Gets the asset content record corresponding to the given
        AssetContent record Type.

        This method is used to retrieve an object implementing the
        requested record. The assetRecordType may be the Type returned
        in get_record_types() or any of its parents in a Type hierarchy
        where hasRecordType(assetRecordType) is true .

        arg:    assetContentContentRecordType (osid.type.Type): the type
                of the record to retrieve
        return: (osid.repository.records.AssetContentRecord) - the asset
                content record
        raise:  NullArgument - assetContentRecordType is null
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported - hasRecordType(assetContentRecordType) is
                false
        compliance: mandatory - This method must be implemented.

        """
        if not self.has_record_type():
            raise IllegalState()
        else:  # This should never get called.
            raise Unimplemented()

    asset_id = property(get_asset_id)
    asset = property(get_asset)
    accessibility_types = property(get_accessibility_types)
    data_length = property(get_data_length)
    data = property(get_data)
    url = property(get_url)


class AssetContentForm(abc_repository_objects.AssetContentForm, osid_objects.OsidObjectForm):
    """This is the form for creating and updating content for ``AssetContent``.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``AssetAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.

    """
    _namespace = 'repository.AssetContent'

    def _init_map(self):
        osid_objects.OsidObjectForm._init_map(self)
        self._my_map['accessibilityTypeIds'] = []
        self._my_map['data'] = ''
        self._my_map['url'] = ''

    def _init_validity_map(self):
        osid_objects.OsidObjectForm._init_validity_map(self)
        self._asset_id = self.kwargs['asset_id']
        self._my_map['assetId'] = str(self.kwargs['asset_id'])
        self._validity_map['accessibility_types'] = VALID
        self._validity_map['data'] = VALID
        self._validity_map['url'] = VALID

    def get_asset_id(self):
        """Gets the ``Id`` of the ``Asset`` as given to ``getAssetContentFormForCreate()``.

        :return: the asset ``Id``
        :rtype: ``osid.id.Id``
        :raise: ``IllegalState`` -- ``is_for_update()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        if self.is_for_update():
            raise IllegalState()
        else:
            return self._asset_id

    asset_id = property(fget=get_asset_id)

    def get_accessibility_type_metadata(self):
        """Gets the metadata for an accessibility type.

        :return: metadata for the accessibility types
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return Metadata(**settings.METADATA['accessibility_type'])

    accessibility_type_metadata = property(fget=get_accessibility_type_metadata)

    def add_accessibility_type(self, accessibility_type=None):
        """Adds an accessibility type.

        Multiple types can be added.

        :param accessibility_type: a new accessibility type
        :type accessibility_type: ``osid.type.Type``
        :raise: ``InvalidArgument`` -- ``accessibility_type`` is invalid
        :raise: ``NoAccess`` -- ``Metadata.isReadOnly()`` is ``true``
        :raise: ``NullArgument`` -- ``accessibility_t_ype`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        if accessibility_type is None:
            raise NullArgument()
        metadata = Metadata(**settings.METADATA['accessibility_type'])
        if metadata.is_read_only():
            raise NoAccess()
        if self._is_valid_input(accessibility_type, metadata, array=False):
            self._my_map['accessibilityTypeIds'].append(accessibility_type._my_map['id'])
            # REALLY?  This assumes that all accessibility_type arguments
            # will be Types that have come from Handcar.  Perhaps?
        else:
            raise InvalidArgument

    def remove_accessibility_type(self, accessibility_type=None):
        """Removes an accessibility type.

        :param accessibility_type: accessibility type to remove
        :type accessibility_type: ``osid.type.Type``
        :raise: ``NoAccess`` -- ``Metadata.isReadOnly()`` is ``true``
        :raise: ``NotFound`` -- acessibility type not found
        :raise: ``NullArgument`` -- ``accessibility_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        if accessibility_type is None:
            raise NullArgument
        metadata = Metadata(**settings.METADATA['accessibility_type'])
        if metadata.is_read_only() or metadata.is_required():
            raise NoAccess()
        if (accessibility_type._my_map['id']) not in self._my_map['accessibility_type']:
            raise NotFound()
        self._my_map['accessibility_types'].remove(accessibility_type._my_map['id'])

    def clear_accessibility_types(self):
        """Removes all accessibility types.

        :raise: ``NoAccess`` -- ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        metadata = Metadata(**settings.METADATA['accessibility_types'])
        if metadata.is_read_only() or metadata.is_required():
            raise NoAccess()
        self._my_map['accessibility_types'] = []

    accessibility_types = property(fdel=clear_accessibility_types)

    def get_data_metadata(self):
        """Gets the metadata for the content data.

        :return: metadata for the content data
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

    data_metadata = property(fget=get_data_metadata)

    def set_data(self, data=None):
        """Sets the content data.

        :param data: the content data
        :type data: ``osid.transport.DataInputStream``
        :raise: ``InvalidArgument`` -- ``data`` is invalid
        :raise: ``NoAccess`` -- ``Metadata.isReadOnly()`` is ``true``
        :raise: ``NullArgument`` -- ``data`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

    def clear_data(self):
        """Removes the content data.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` is ``true`` or ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

    data = property(fset=set_data, fdel=clear_data)

    def get_url_metadata(self):
        """Gets the metadata for the url.

        :return: metadata for the url
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.Metadata

    url_metadata = property(fget=get_url_metadata)

    def set_url(self, url=None):
        """Sets the url.

        :param url: the new copyright
        :type url: ``string``
        :raise: ``InvalidArgument`` -- ``url`` is invalid
        :raise: ``NoAccess`` -- ``Metadata.isReadOnly()`` is ``true``
        :raise: ``NullArgument`` -- ``url`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        if url is None:
            raise NullArgument()
        metadata = Metadata(**settings.METADATA['url'])
        if metadata.is_read_only():
            raise NoAccess()
        if self._is_valid_input(url, metadata, array=False):
            self._my_map['url'] = url
        else:
            raise InvalidArgument()

    def clear_url(self):
        """Removes the url.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` is ``true`` or ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        metadata = Metadata(**settings.METADATA['url'])
        if metadata.is_read_only() or metadata.is_required():
            raise NoAccess()
        self._my_map['url'] = ''

    url = property(fset=set_url, fdel=clear_url)

    def get_asset_content_form_record(self, asset_content_record_type=None):
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
        raise Unimplemented()


class AssetContentList(abc_repository_objects.AssetContentList, osid_objects.OsidList):
    """Like all OsidLists,  AssetContentList provides a means for accessing
    AssetContent elements sequentially either one at a time or many at a
    time.

    Examples: while (acl.hasNext()) { AssetContent content =
    acl.getNextAssetContent(); }

    or
      while (acl.hasNext()) {
           AssetContent[] contents = acl.getNextAssetContents(acl.available());
      }

    """

    def get_next_asset_content(self):
        """Gets the next AssetContent in this list.

        return: (osid.repository.AssetContent) - the next AssetContent
                in this list. The has_next() method should be used to
                test that a next AssetContent is available before
                calling this method.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        compliance: mandatory - This method must be implemented.

        """
        try:
            next_object = next(self)
        except StopIteration:
            raise IllegalState('no more elements available in this list')
        except Exception:  # Need to specify exceptions here!
            raise OperationFailed()
        else:
            return next_object

    def next(self):
        try:
            next_object = osid_objects.OsidList.next(self)
        except StopIteration:
            raise
        except Exception:  # Need to specify exceptions here!
            raise OperationFailed()
        if isinstance(next_object, dict):
            next_object = AssetContent(next_object)
        return next_object

    __next__ = next

    def get_next_asset_contents(self, n=None):
        """Gets the next set of AssetContents in this list which must be
        less than or equal to the return from available().

        arg:    n (cardinal): the number of AssetContent elements
                requested which must be less than or equal to
                available()
        return: (osid.repository.AssetContent) - an array of
                AssetContent elements.  The length of the array is less
                than or equal to the number specified.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        compliance: mandatory - This method must be implemented.

        """
        if n > self.available():
            # !!! This is not quite as specified (see method docs) !!!
            raise IllegalState('not enough elements available in this list')
        else:
            next_list = []
            x = 0
            while x < n:
                try:
                    next_list.append(next(self))
                except Exception:  # Need to specify exceptions here!
                    raise OperationFailed()
                x = x + 1
            return next_list

    next_asset_content = property(get_next_asset_content)


class Repository(abc_repository_objects.Repository, osid_objects.OsidCatalog):
    """A repository defines a collection of assets."""

    _namespace = 'repository.Repository'

    def get_repository_record(self, repository_record_type):
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
        raise Unimplemented()


class RepositoryForm(abc_repository_objects.RepositoryForm, osid_objects.OsidCatalogForm):
    """This is the form for creating and updating repositories.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``RepositoryAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.

    """
    _namespace = 'repository.Repository'

    def _init_map(self):
        osid_objects.OsidObjectForm._init_map(self)

    def _init_validity_map(self):
        osid_objects.OsidObjectForm._init_validity_map(self)

    def get_repository_form_record(self, repository_record_type):
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
        if not self.has_record_type():
            raise Unsupported()
        else:  # This should never get called:
            raise Unimplemented()


class RepositoryList(abc_repository_objects.RepositoryList, osid_objects.OsidList):
    """Like all ``OsidLists,``  ``RepositoryList`` provides a means for accessing ``Repository`` elements sequentially either one at a time or many at a time.

    Examples: while (rl.hasNext()) { Repository repository =
    rl.getNextRepository(); }

    or
      while (rl.hasNext()) {
           Repository[] repositories = rl.getNextRepositories(rl.available());
      }



    """

    def get_next_repository(self):
        """Gets the next ``Repository`` in this list.

        :return: the next ``Repository`` in this list. The ``has_next()`` method should be used to test that a next ``Repository`` is available before calling this method.
        :rtype: ``osid.repository.Repository``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        try:
            next_object = next(self)
        except StopIteration:
            raise IllegalState('no more elements available in this list')
        except Exception:  # Need to specify exceptions here!
            raise OperationFailed()
        else:
            return next_object

    def next(self):
        try:
            next_object = osid_objects.OsidList.next(self)
        except StopIteration:
            raise
        except Exception:  # Need to specify exceptions here!
            raise OperationFailed()
        if isinstance(next_object, dict):
            next_object = Repository(next_object)
        return next_object

    __next__ = next
    next_repository = property(fget=get_next_repository)

    def get_next_repositories(self, n):
        """Gets the next set of ``Repository`` elements in this list which must be less than or equal to the return from ``available()``.

        :param n: the number of ``Repository`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``Repository`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.repository.Repository``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        if n > self.available():
            # !!! This is not quite as specified (see method docs) !!!
            raise IllegalState('not enough elements available in this list')
        else:
            next_list = []
            x = 0
            while x < n:
                try:
                    next_list.append(next(self))
                except Exception:  # Need to specify exceptions here!
                    raise OperationFailed()
                x = x + 1
            return next_list
