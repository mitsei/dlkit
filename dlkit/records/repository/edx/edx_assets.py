"""
records.repository.edx.edx_assets.py
"""
import re
import time
import tarfile
import requests


from bs4 import BeautifulSoup
from bson import ObjectId
from six import BytesIO

from dlkit.abstract_osid.osid.errors import NotFound
from dlkit.json_.id.objects import IdList
from dlkit.primordium.id.primitives import Id

from ..basic.simple_records import AssetContentTextFormRecord,\
    AssetContentTextRecord
from ...osid.base_records import FilesRecord,\
    FilesFormRecord,\
    TextsFormRecord,\
    TextsRecord,\
    QueryInitRecord,\
    ProvenanceFormRecord,\
    AssetUtils
from ...registry import ASSET_RECORD_TYPES, ASSET_CONTENT_RECORD_TYPES, OSID_OBJECT_RECORD_TYPES
from ...osid.edx_base import edXQueryMethods
from ..basic.base_records import ProvenanceAssetRecord
from .utilities import EdXUtilitiesMixin, clean_str


class edXAssetContentRecord(AssetContentTextRecord,
                            FilesRecord,
                            ProvenanceAssetRecord,
                            AssetUtils,
                            EdXUtilitiesMixin):
    """basic edX asset content"""
    _implemented_record_type_identifiers = [
        'asset-content-text',
        'asset-content-files',
        'edx-asset-content-text-files',
        'provenance-asset-content'
    ]

    def export_olx(self, tarball, root_path, parent_asset):
        my_tag = self.my_osid_object.genus_type.identifier
        my_soup = BeautifulSoup('<' + my_tag + '/>', 'xml')

        # need to get the edX content and replace all
        # assetIds with a file to static/<filename>
        # Also save the files to the tarball under static/<filename>
        edxml = self.get_text().text
        expected_name = self.get_unique_name(tarball, parent_asset.url, my_tag, root_path)
        my_xml_path = '{0}{1}/{2}.xml'.format(root_path,
                                              my_tag,
                                              expected_name)

        getattr(my_soup, my_tag)['display_name'] = parent_asset.display_name.text

        try:
            edxml_soup = BeautifulSoup(edxml, 'xml')
            edxml_soup.html['display_name'] = parent_asset.display_name.text
        except TypeError:
            edxml_soup = BeautifulSoup('', 'xml')
            edxml_soup.append(BeautifulSoup(edxml, 'html5lib'))
            edxml_soup.html['display_name'] = parent_asset.display_name.text

        attrs = {
            'draggable': ['icon'],
            'drag_and_drop_input': ['img'],
            'files': ['included_files'],
            'img': ['src'],
            'a': ['href'],
            'script': ['src'],
            'video': ['sub', 'youtube', 'youtube_id_1_0'],
            'encoded_video': ['url']
        }
        # replace all file listings with an appropriate path...
        for key, attributes in attrs.items():
            for attr in attributes:
                local_regex = re.compile('^repository.Asset')
                search = {attr: local_regex}
                tags = edxml_soup.find_all(**search)
                for item in tags:
                    asset_id = item[attr]
                    asset_content = self._get_asset_content(Id(asset_id))
                    asset_url = asset_content.get_url()
                    asset_file = asset_content.get_data()
                    asset_file_name = asset_url.split('?')[0].split('/')[-1]
                    static_file_path = '{0}static/{1}'.format(root_path,
                                                              asset_file_name)

                    self.write_to_tarfile(tarball, static_file_path, asset_file)

                    relative_static_file_path = '/static/{0}'.format(asset_file_name)
                    item[attr] = relative_static_file_path

        if my_tag == 'html':
            # save the HTML file separately and point to it via the XML file
            my_html_path = '{0}{1}/{2}.html'.format(root_path,
                                                    my_tag,
                                                    expected_name)

            getattr(my_soup, my_tag)['url_name'] = expected_name
            getattr(my_soup, my_tag)['filename'] = '{0}'.format(expected_name)
            # if want separate XML / HTML files, do this
            del edxml_soup.html['url_name']
            self.write_to_tarfile(tarball, my_html_path, edxml_soup.find('html'))
            self.write_to_tarfile(tarball, my_xml_path, my_soup)

            # if only want to write a single XML file, do the following:
            # my_soup = edxml_soup
            # self.write_to_tarfile(tarball, my_xml_path, my_soup)
        else:
            my_soup = getattr(edxml_soup, my_tag)
            self.write_to_tarfile(tarball, my_xml_path, my_soup)

        return my_xml_path

    def get_edxml_with_aws_urls(self):
        """stub"""
        edxml = self.get_text().text

        soup = BeautifulSoup(edxml, 'xml').find('html')
        if soup is None:
            soup = BeautifulSoup('', 'xml')
            soup.append(BeautifulSoup(edxml, 'html5lib'))

        attrs = {
            'draggable': ['icon'],
            'drag_and_drop_input': ['img'],
            'files': ['included_files'],
            'img': ['src'],
            'a': ['href'],
            'script': ['src'],
            'video': ['sub', 'youtube', 'youtube_id_1_0'],
            'encoded_video': ['url']
        }
        # replace all file listings with an appropriate path...
        for key, attributes in attrs.items():
            for attr in attributes:
                local_regex = re.compile('^repository.Asset')
                search = {attr: local_regex}
                tags = soup.find_all(**search)
                for item in tags:
                    asset_id = item[attr]
                    asset_content = self._get_asset_content(Id(asset_id))
                    item[attr] = asset_content.get_url()
        if '<video>' in edxml:
            return soup.find('video').prettify()
        elif '<videoalpha' in edxml:
            return soup.find('videoalpha').prettify()
        elif '<discussion>' in edxml:
            return soup.find('discussion').prettify()
        else:
            return soup.prettify()


class edXAssetContentFormRecord(AssetContentTextFormRecord,
                                FilesFormRecord,
                                ProvenanceFormRecord):
    """form to create basic edX content"""
    _implemented_record_type_identifiers = [
        'asset-content-text',
        'asset-content-files',
        'edx-asset-content-text-files',
        'provenance-asset-content'
    ]

    def __init__(self, osid_object_form):
        if osid_object_form is not None:
            self.my_osid_object_form = osid_object_form
        self._init_metadata()
        if not osid_object_form.is_for_update():
            self._init_map()
        super(edXAssetContentFormRecord, self).__init__(
            osid_object_form=osid_object_form)

    def _init_map(self):
        """stub"""
        super(edXAssetContentFormRecord, self)._init_map()
        AssetContentTextFormRecord._init_map(self)
        FilesFormRecord._init_map(self)
        ProvenanceFormRecord._init_map(self)

    def _init_metadata(self):
        """stub"""
        super(edXAssetContentFormRecord, self)._init_metadata()
        AssetContentTextFormRecord._init_metadata(self)
        FilesFormRecord._init_metadata(self)
        ProvenanceFormRecord._init_metadata(self)


class edXAssetRecord(TextsRecord, ProvenanceAssetRecord, EdXUtilitiesMixin):
    _implemented_record_type_identifiers = [
        'edx-asset',
        'provenance-asset'
    ]

    def __init__(self, osid_object):
        super(edXAssetRecord, self).__init__(osid_object)
        if (not hasattr(self.my_osid_object, '_supported_record_type_ids') or
                self.my_osid_object._supported_record_type_ids is None):
            self.my_osid_object._supported_record_type_ids = []

    def clone_to(self, target_repo):
        """stub"""
        new_asset = target_repo.duplicate_asset(self.my_osid_object.ident)
        form = target_repo.get_asset_form_for_update(new_asset.ident)
        form.set_provenance(str(self.my_osid_object.ident))
        return target_repo.update_asset(form)

    def export_olx(self, tarball, root_path):
        # write out each asset content that is in this asset...
        paths = []
        for ac in self.my_osid_object.get_asset_contents():
            paths.append(ac.export_olx(tarball, root_path, self.my_osid_object))
        return paths

    def export_standalone_olx(self):
        filename = '{0}_{1}'.format(self.my_osid_object.display_name.text,
                                    str(int(time.time())))
        filename = clean_str(filename) + '.tar.gz'
        root_path = ''

        olx = BytesIO()
        tarball = tarfile.open(filename, mode='w', fileobj=olx)
        self.my_osid_object.export_olx(tarball, root_path)

        tarball.close()
        olx.seek(0)

        return filename, olx

    def get_learning_objective_ids(self):
        return IdList(self.my_osid_object._my_map['learningObjectiveIds'],
                      runtime=self.my_osid_object._runtime,
                      proxy=self.my_osid_object._proxy)

    learning_objective_ids = property(fget=get_learning_objective_ids)


class edXAssetQueryRecord(edXQueryMethods, QueryInitRecord):
    def match_asset_content_genus_type(self, genus_type, match):
        self._my_osid_query._add_match('assetContents.0.genusTypeId', str(genus_type), match)

    def clear_match_asset_content_genus_type(self):
        self._my_osid_query._clear_terms('assetContents.0.genusTypeId')

    def match_learning_objective(self, learning_objective_id, match):
        self._my_osid_query._add_match('learningObjectiveIds', str(learning_objective_id), match)

    def clear_match_learning_objective(self):
        self._my_osid_query._clear_terms('learningObjectiveIds')

    def match_any_learning_objective(self, match):
        """Matches an item with any objective.

        arg:    match (boolean): ``true`` to match items with any
                learning objective, ``false`` to match items with no
                learning objectives
        *compliance: mandatory -- This method must be implemented.*

        """
        match_key = 'learningObjectiveIds'
        param = '$exists'
        if match:
            flag = 'true'
        else:
            flag = 'false'
        if match_key in self._my_osid_query._query_terms:
            self._my_osid_query._query_terms[match_key][param] = flag
        else:
            self._my_osid_query._query_terms[match_key] = {param: flag}
        self._my_osid_query._query_terms[match_key]['$nin'] = [[], ['']]

    def clear_learning_objective_terms(self):
        """Clears all learning objective terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        self._my_osid_query._clear_terms('learningObjectiveIds')

    def match_composition_descendants(self, composition_id, repository_id, match):
        if match:
            inin = '$in'
        else:
            inin = '$nin'

        rm = self._my_osid_query._get_provider_manager('REPOSITORY')
        child_ids = self._get_descendant_ids(composition_id, repository_id, rm)

        # Now get all the assetIds for each of these compositions
        acs = rm.get_asset_composition_session_for_repository(repository_id)
        assets = []
        for child_id in child_ids:
            try:
                assets += [ObjectId(asset.ident.identifier)
                           for asset in acs.get_composition_assets(child_id)]
            except NotFound:
                pass
        assets = list(set(assets))
        self._my_osid_query._query_terms['_id'] = {inin: assets}

    def clear_match_composition_descendants(self):
        self._my_osid_query._clear_terms('_id')


class edXAssetFormRecord(TextsFormRecord, ProvenanceFormRecord):
    _implemented_record_type_identifiers = [
        'edx-asset',
        'provenance-asset'
    ]

    def __init__(self, osid_object_form):
        if osid_object_form is not None:
            self.my_osid_object_form = osid_object_form
        self._init_metadata()
        if not osid_object_form.is_for_update():
            self._init_map()

    def _init_map(self):
        ProvenanceFormRecord._init_map(self)
        TextsFormRecord._init_map(self)
        super(edXAssetFormRecord, self)._init_map()

        self.my_osid_object_form._my_map['learningObjectiveIds'] = \
            self._learning_objective_ids_metadata['default_string_values'][0]

    def _init_metadata(self):
        ProvenanceFormRecord._init_metadata(self)
        TextsFormRecord._init_metadata(self)
        super(edXAssetFormRecord, self)._init_metadata()

        # ideally this would be type LIST?
        self._learning_objective_ids_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'learning_objectives'),
            'element_label': 'learning_objectives',
            'instructions': 'enter a list of strings',
            'required': False,
            'read_only': False,
            'linked': False,
            'array': False,
            'default_string_values': [[]],
            'syntax': 'STRING',
            'minimum_string_length': self._min_string_length,
            'maximum_string_length': self._max_string_length,
            'string_set': []
        }

    def set_learning_objective_ids(self, learning_objective_ids):
        lo_ids_str = [str(lo) for lo in learning_objective_ids]
        self.my_osid_object_form._my_map['learningObjectiveIds'] = lo_ids_str

    def clear_learning_objective_ids(self):
        self.my_osid_object_form._my_map['learningObjectiveIds'] = \
            self._learning_objective_ids_metadata['default_string_values'][0]
