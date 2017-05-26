"""
records.assessment.edx.item_records.py
"""

import re
import time
import tarfile

try:
    # python 2
    from cStringIO import StringIO
except ImportError:
    # python 3
    from io import StringIO

from bson import ObjectId

from dlkit.abstract_osid.osid.errors import IllegalState, NotFound
from dlkit.primordium.id.primitives import Id

from ..basic.base_records import ProvenanceItemRecord
from ..basic.simple_records import ItemTextsRecord,\
    ItemTextsFormRecord,\
    ItemFilesRecord,\
    ItemFilesFormRecord
from ..analytic.irt import IRTItemFormRecord, IRTItemRecord

from ...osid.base_records import QueryInitRecord,\
    edXBaseFormRecord,\
    edXBaseRecord,\
    TimeValueFormRecord,\
    TimeValueRecord,\
    ProvenanceFormRecord
from ...osid.edx_base import edXQueryMethods
from ...repository.edx.utilities import EdXUtilitiesMixin, clean_str

from bs4 import BeautifulSoup, NavigableString


class edXItemRecord(ItemTextsRecord,
                    ItemFilesRecord,
                    IRTItemRecord,
                    edXBaseRecord,
                    TimeValueRecord,
                    ProvenanceItemRecord,
                    EdXUtilitiesMixin):
    """basic edX item with raw XML"""
    _implemented_record_type_identifiers = [
        'edx_item',
        'item-texts',
        'item-files',
        'irt-item',
        'item-time',
        'provenance-item'
    ]

    def _clean(self, label):
        """stub"""
        return re.sub(r'[^\w\d]', '_', label)

    def has_raw_edxml(self):
        """stub"""
        try:
            if self.get_text('edxml') is not None:
                return True
            return False
        except IllegalState:
            return False

    def get_raw_edxml(self):
        """stub"""
        if self.has_raw_edxml():
            return self.get_text('edxml')
        raise IllegalState()

    def get_edxml(self):
        """stub"""
        if self.has_raw_edxml():
            has_python = False
            my_files = self.my_osid_object.object_map['fileIds']
            raw_text = self.get_text('edxml')
            soup = BeautifulSoup(raw_text, 'xml')
            # replace all file listings with an appropriate path...
            attrs = {
                'draggable': 'icon',
                'drag_and_drop_input': 'img',
                'files': 'included_files',
                'img': 'src'
            }
            local_regex = re.compile('[^http]')
            for key, attr in attrs.items():
                search = {attr: local_regex}
                tags = soup.find_all(**search)
                for item in tags:
                    if key == 'files' or item.name == key:
                        file_label = self._clean(item[attr])
                        if file_label in my_files:
                            content_type = Id(my_files[file_label]['assetContentTypeId'])
                            item[attr] = '/static/' + file_label + '.' + \
                                         content_type.get_identifier()

            # replace any python script with the item's get_text('python_script')
            # text...will fix weird whitespace issues
            if len(soup.find_all('script')) >= 1:
                scripts = soup.find_all('script')
                for script in scripts:
                    if 'python' in script['type']:
                        has_python = True
                        # contents = script.contents[0]
                        # contents.replaceWith(str(NavigableString(self.python)))
                        break

            try:
                if has_python:
                    return str(soup.find('problem'))
                else:
                    return soup.find('problem').prettify()
            except Exception:
                # if the edxml is not valid XML, it will not parse properly in soup
                # return just the raw edxml
                return self.get_text('edxml')
        else:
            # have to construct the edxml from various components
            obj_map = self.my_osid_object.object_map
            question = obj_map['question']
            answers = obj_map['answers']
            if 'edx-multi-choice-problem-type' in obj_map['genusTypeId']:
                # get answer Ids to compare them to the choices
                answer_ids = []
                for answer in answers:
                    answer_ids += answer['choiceIds']
                # add the body text element (item.question.text)
                soup = BeautifulSoup('<problem></problem>', 'xml')
                p = soup.new_tag('p')
                p.string = self.get_text('questionString').text
                problem = soup.find('problem')
                problem.append(p)
                # add the metadata
                problem['display_name'] = question['displayName']['text']
                problem['showanswer'] = self.showanswer
                if 'rerandomize' in obj_map:
                    problem['rerandomize'] = obj_map['rerandomize']
                elif 'rerandomize' in question:
                    problem['rerandomize'] = question['rerandomize']
                problem['max_attempts'] = self.attempts

                # add the choices
                multichoice = soup.new_tag('multiplechoiceresponse')
                problem.append(multichoice)

                choicegroup = soup.new_tag('choicegroup')
                choicegroup['direction'] = 'vertical'
                multichoice.append(choicegroup)

                choices = question['choices']
                for choice in choices:
                    new_choice = soup.new_tag('choice')

                    # mark the correct choice(s)
                    if choice['id'] in answer_ids:
                        new_choice['correct'] = 'true'
                    else:
                        new_choice['correct'] = 'false'

                    new_choice['name'] = choice['name']
                    choice_text = soup.new_tag('text')
                    choice_text.string = choice['text']
                    new_choice.append(choice_text)
                    choicegroup.append(new_choice)
                return problem.prettify()
        raise IllegalState('records.assessment.edx.item_records.get_edxml()')

    def get_edxml_with_aws_urls(self):
        """stub"""
        edxml = self.get_edxml()
        soup = BeautifulSoup(edxml, 'xml')

        attrs = {
            'draggable': 'icon',
            'drag_and_drop_input': 'img',
            'files': 'included_files',
            'img': 'src'
        }
        # replace all file listings with an appropriate path...
        if len(self.my_osid_object.object_map['fileIds']) > 0:
            file_map = self.my_osid_object.get_files()
            for file_label, url in file_map.items():
                local_regex = re.compile(file_label + r'\.')
                for key, attr in attrs.items():
                    search = {attr: local_regex}
                    tags = soup.find_all(**search)
                    for item in tags:
                        item[attr] = url
        return soup.find('problem').prettify()

    def export_olx(self, tarball, root_path):
        # only useful to do the my_soup stuff if we start
        # parsing out the problem attributes for editing

        # my_soup = BeautifulSoup('<problem/>', 'xml')

        # need to get the edX content and replace all
        # assetIds with a file to static/<filename>
        # Also save the files to the tarball under static/<filename>
        edxml = self.get_edxml()
        edxml_soup = BeautifulSoup(edxml, 'xml')

        expected_name = self.get_unique_name(tarball,
                                             self.my_osid_object.url,
                                             'problem',
                                             root_path)
        my_xml_path = '{0}problem/{1}.xml'.format(root_path,
                                                  expected_name)

        # my_soup.problem['display_name'] = self.my_osid_object.display_name.text
        # my_soup.problem['url_name'] = self.my_osid_object.url
        #
        # for attr in ['rerandomize', 'showanswer', 'weight', 'attempts']:
        #     if attr == 'rerandomize':
        #         my_soup.problem['rerandomize'] = self.my_osid_object.get_question().rerandomize
        #     elif attr == 'attempts':
        #         my_soup.problem['max_attempts'] = self.my_osid_object.attempts
        #     else:
        #         my_soup.problem[attr] = getattr(self.my_osid_object, attr)

        attrs = {
            'draggable': 'icon',
            'drag_and_drop_input': 'img',
            'files': 'included_files',
            'img': 'src',
            'a': 'href',
            'script': 'src'
        }
        # replace all file listings with an appropriate path...
        if len(self.my_osid_object.object_map['fileIds']) > 0:
            file_map = self.my_osid_object.get_files()
            for file_label, url in file_map.items():
                local_regex = re.compile(file_label + r'\.')
                for key, attr in attrs.items():
                    search = {attr: local_regex}
                    tags = edxml_soup.find_all(**search)
                    for item in tags:
                        asset_url = url
                        asset_file_name = asset_url.split('?')[0].split('/')[-1]
                        relative_static_file_path = '/static/{0}'.format(asset_file_name)
                        item[attr] = relative_static_file_path

        self.write_to_tarfile(tarball, my_xml_path, edxml_soup, prettify=False)
        return my_xml_path

    def export_standalone_olx(self):
        filename = '{0}_{1}'.format(self.my_osid_object.display_name.text,
                                    str(int(time.time())))
        filename = clean_str(filename) + '.tar.gz'
        root_path = ''

        olx = StringIO()
        tarball = tarfile.open(filename, mode='w', fileobj=olx)
        self.my_osid_object.export_olx(tarball, root_path)

        return filename, olx

    def has_urlname(self):
        """stub"""
        if self.get_text('urlname') is not None:
            return True
        return False

    def get_urlname(self):
        """stub"""
        if self.has_urlname():
            return self.get_text('urlname')
        raise IllegalState()

    def has_python_script(self):
        """stub"""
        if self.get_text('python_script') is not None:
            return True
        return False

    def get_python_script(self):
        """stub"""
        if self.has_python_script():
            return self.get_text('python_script')
        raise IllegalState()

    def has_raw_latex(self):
        """stub"""
        if self.get_text('latex') is not None:
            return True
        return False

    def get_raw_latex(self):
        """stub"""
        if self.has_raw_latex():
            return self.get_text('latex')
        raise IllegalState()

    def get_xproblem(self, parameters=None):
        """stub"""
        if not self.get_text('python_script'):
            return self.get_text('edxml')
        if not parameters:
            parameters = self.get_parameters()
        return self._get_parameterized_text(parameters)

    def has_solution(self):
        """stub"""
        if self.get_text('solution') is not None:
            return True
        return False

    def get_solution(self, parameters=None):
        """stub"""
        if not self.has_solution():
            raise IllegalState()
        try:
            if not self.get_text('python_script'):
                return self.get_text('solution')
            if not parameters:
                parameters = self.get_parameters()
            return self._get_parameterized_text(parameters)
        except Exception:
            return self.get_text('solution')

    def is_parameterized(self):
        """stub"""
        if not self.get_text('python_script'):
            return False
        return True

    def get_parameters(self):
        """stub"""
        if not self.is_parameterized():
            raise IllegalState()
        if not self.get_text('python_script'):
            return dict()
        import imp
        from types import ModuleType, FunctionType
        script_module = imp.new_module('script_module')
        exec(self.get_text('python_script').text, script_module.__dict__)
        params = dict()
        for attr in dir(script_module):
            if (not isinstance(getattr(script_module, attr), ModuleType) and
                    not isinstance(getattr(script_module, attr), FunctionType) and
                    not attr.startswith('__')):
                params[attr] = getattr(script_module, attr)
        return params

    def _get_parameterized_text(self, parameters):
        """stub"""
        text = self.get_text('edxml')
        done = False
        while not done:
            result = re.search(r'\$\w+', text)
            if result:
                replacement = str(parameters[result.group()[1:]])
                text = text.replace(result.group(), replacement)
            else:
                done = True
        return text

    def get_configuration(self):
        """stub"""
        try:
            return {'parameters': self.get_parameters()}
        except IllegalState:
            return {}

    def _update_object_map(self, map):
        super(edXItemRecord, self)._update_object_map(map)

    edxml = property(fget=get_raw_edxml)
    latex = property(fget=get_raw_latex)
    urlname = property(fget=get_urlname)
    python = property(fget=get_python_script)
    solution = property(fget=get_solution)


class edXItemFormRecord(ItemTextsFormRecord,
                        ItemFilesFormRecord,
                        IRTItemFormRecord,
                        edXBaseFormRecord,
                        TimeValueFormRecord,
                        ProvenanceFormRecord):
    """form for basic edX item"""
    _implemented_record_type_identifiers = [
        'edx-item',
        'item-texts',
        'item-files',
        'irt-item',
        'item-time',
        'provenance-item'
    ]

    def __init__(self, osid_object_form=None):
        if osid_object_form is not None:
            self.my_osid_object_form = osid_object_form
        self._init_metadata()
        if not self.my_osid_object_form.is_for_update():
            self._init_map()
        super(edXItemFormRecord, self).__init__(osid_object_form=osid_object_form)

    def _init_map(self):
        """Have to call these all separately because they are "end" classes,
        with no super() in them. Non-cooperative."""
        ItemTextsFormRecord._init_map(self)
        ItemFilesFormRecord._init_map(self)
        edXBaseFormRecord._init_map(self)
        IRTItemFormRecord._init_map(self)
        TimeValueFormRecord._init_map(self)
        ProvenanceFormRecord._init_map(self)
        super(edXItemFormRecord, self)._init_map()

    def _init_metadata(self):
        """Have to call these all separately because they are "end" classes,
        with no super() in them. Non-cooperative."""
        ItemTextsFormRecord._init_metadata(self)
        ItemFilesFormRecord._init_metadata(self)
        edXBaseFormRecord._init_metadata(self)
        IRTItemFormRecord._init_metadata(self)
        TimeValueFormRecord._init_metadata(self)
        ProvenanceFormRecord._init_metadata(self)
        super(edXItemFormRecord, self)._init_metadata()


class edXItemQueryRecord(edXQueryMethods, QueryInitRecord):
    """make edX items queryable"""
    def match_composition_descendants(self, composition_id, repository_id, match):
        if match:
            inin = '$in'
        else:
            inin = '$nin'

        rm = self._my_osid_query._get_provider_manager('REPOSITORY')
        child_ids = self._get_descendant_ids(composition_id, repository_id, rm)

        # Now get all the assetIds that enclose Items,
        # for each of these compositions
        acs = rm.get_asset_composition_session_for_repository(repository_id)
        assets = []
        for child_id in child_ids:
            try:
                assets += list(acs.get_composition_assets(child_id))
            except NotFound:
                pass
        assessments = [asset.get_enclosed_object()
                       for asset in assets
                       if ('enclosedObjectId' in asset._my_map and
                       'assessment.Assessment' in asset._my_map['enclosedObjectId'])]
        assessments = list(set(assessments))

        am = self._my_osid_query._get_provider_manager('ASSESSMENT')
        abas = am.get_assessment_basic_authoring_session()
        items = []
        for assessment in assessments:
            items += list(abas.get_items(assessment.ident))

        items = [ObjectId(item.ident.identifier) for item in items]
        items = list(set(items))
        self._my_osid_query._query_terms['_id'] = {inin: items}

    def clear_match_composition_descendants(self):
        self._my_osid_query._clear_terms('_id')
