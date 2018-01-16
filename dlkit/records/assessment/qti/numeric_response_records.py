"""
records.assessment.qti.numeric_response_records.py
"""
import json
from bs4 import BeautifulSoup
from random import randint, uniform

from dlkit.json_ import types
from dlkit.json_.osid.metadata import Metadata
from dlkit.json_.osid import objects as osid_objects
from dlkit.json_.assessment.objects import Question, AnswerList, ItemList
from dlkit.json_.assessment.sessions import ItemLookupSession
from dlkit.json_.id.objects import IdList

from dlkit.primordium.id.primitives import Id
from dlkit.primordium.type.primitives import Type
from dlkit.abstract_osid.osid.errors import IllegalState,\
    InvalidArgument, NotFound

from sympy import sympify
from sympy.core.numbers import Rational, Float

try:
    # python 2
    from urllib import quote, unquote
except ImportError:
    # python 3
    from urllib.parse import quote, unquote

from ..basic.simple_records import QuestionFilesRecord,\
    TextAnswerFormRecord,\
    TextAnswerRecord,\
    QuestionTextFormRecord,\
    QuestionFilesFormRecord,\
    FilesAnswerRecord, FilesAnswerFormRecord
from ..basic.text_answer_records import QuestionTextRecord
from ...osid.base_records import DecimalValuesFormRecord,\
    DecimalValuesRecord, IntegerValuesRecord, IntegerValuesFormRecord
from ..basic.feedback_answer_records import FeedbackAnswerFormRecord, FeedbackAnswerRecord,\
    MultiLanguageFeedbacksAnswerFormRecord, MultiLanguageFeedbacksAnswerRecord
from ..basic.wrong_answers import WrongAnswerItemFormRecord, WrongAnswerItemRecord
from ...osid.base_records import ObjectInitRecord
from ..basic.base_records import MultiLanguageQuestionFormRecord, MultiLanguageQuestionRecord

from ..registry import ITEM_GENUS_TYPES


DEFAULT_LANGUAGE_TYPE = Type(**types.Language().get_type_data('DEFAULT'))
DEFAULT_SCRIPT_TYPE = Type(**types.Script().get_type_data('DEFAULT'))
DEFAULT_FORMAT_TYPE = Type(**types.Format().get_type_data('DEFAULT'))

MAGIC_AUTHORITY = 'qti-numeric-response'
NUMERIC_RESPONSE_GENUS_TYPE = Type(**ITEM_GENUS_TYPES['qti-numeric-response'])


class MagicNumericResponseItemLookupSession(ItemLookupSession):
    def __init__(self, *args, **kwargs):
        super(MagicNumericResponseItemLookupSession, self).__init__(*args, **kwargs)

    def get_item(self, item_id):
        """ see if this is a magic item id (i.e. questionId).
        If so, grab the item and set the params.
        If not, just pass through to the original Mongo ItemLookupSession
        :param item_id:
        :return:
        """
        authority = item_id.authority
        mgr = self._get_provider_manager('ASSESSMENT', local=True)
        if self._proxy is not None:
            ils = mgr.get_item_lookup_session(proxy=self._proxy)
        else:
            ils = mgr.get_item_lookup_session()
        ils.use_federated_bank_view()
        if authority == MAGIC_AUTHORITY:
            magic_identifier = unquote(item_id.identifier)
            params = json.loads(magic_identifier.split('?')[-1])
            orig_identifier = magic_identifier.split('?')[0]
            original_item_id = Id(
                namespace=item_id.namespace,
                authority=self._catalog.ident.authority,
                identifier=orig_identifier
            )
            orig_item = ils.get_item(original_item_id)
            orig_item.set_params(params)
            return orig_item
        else:
            return ils.get_item(item_id)

    def get_items_by_ids(self, item_ids):
        item_list = []
        for item_id in item_ids:
            item_list.append(super(MagicNumericResponseItemLookupSession, self).get_item(item_id))
        return ItemList(item_list, runtime=self._runtime, proxy=self._proxy)


class CalculationInteractionItemRecord(WrongAnswerItemRecord):
    """QTI numeric response question"""
    _implemented_record_type_identifiers = [
        'qti-numeric-response'
    ]

    def __init__(self, *args, **kwargs):
        super(CalculationInteractionItemRecord, self).__init__(*args, **kwargs)
        self._magic_params = None

    def get_question(self):
        question = Question(osid_object_map=self.my_osid_object._my_map['question'],
                            runtime=self.my_osid_object._runtime,
                            proxy=self.my_osid_object._proxy)
        if self._magic_params is not None:
            question.set_values(self._magic_params)
        return question

    question = property(fget=get_question)

    def set_params(self, params):
        self._magic_params = params

    def get_answers(self):
        def get_var_sig_fig(_format):
            return int(_format.split('.')[-1][0:-1])

        updated_answers = []
        # answers = AnswerList(self.my_osid_object._my_map['answers'],
        #                      runtime=self.my_osid_object._runtime,
        #                      proxy=self.my_osid_object._proxy)
        answers = super(CalculationInteractionItemRecord, self).get_answers()
        if str(self.my_osid_object.genus_type) == str(NUMERIC_RESPONSE_GENUS_TYPE):
            try:
                question = self.question
            except TypeError:
                # no question!
                pass
            else:
                soup = BeautifulSoup(question.get_text().text, 'xml')

                numeric_choice_wrapper = None
                interaction = soup.itemBody.textEntryInteraction
                for parent in interaction.parents:
                    if parent.name == 'p':
                        numeric_choice_wrapper = parent
                        break

                numeric_choice_line_str = str(numeric_choice_wrapper)
                expression = numeric_choice_line_str[3:numeric_choice_line_str.index('=')].strip()  # skip the opening <p> tag

                output_format = None
                # check if any of the variables are floats
                # if so, take the one with the largest significant figures
                for var in question._my_map['variables'].items():
                    var_dict = var[1]
                    if 'format' in var_dict and var_dict['format'] != '':
                        var_format = var_dict['format']
                        if output_format is None:
                            output_format = var_format
                            continue

                        current_sig_figs = get_var_sig_fig(output_format)
                        new_sig_figs = get_var_sig_fig(var_format)
                        if new_sig_figs > current_sig_figs:
                            output_format = var_format

                for answer in answers:
                    # send the actual value, because we need to use the
                    # question variable params to limit the precision
                    # of the expected value...
                    expected_value = sympify(expression.split(':')[-1].split('=')[0].strip())

                    if output_format is not None:
                        expected_value = sympify(float(output_format % expected_value))

                    answer.set_answer_value(expected_value)
                    updated_answers.append(answer)
        else:
            updated_answers = answers

        return AnswerList(updated_answers,
                          runtime=self.my_osid_object._runtime,
                          proxy=self.my_osid_object._proxy)

    answers = property(fget=get_answers)

    def _is_match(self, response, answer):
        if answer._value is not None:
            if isinstance(answer._value, Rational):
                for label, value in response._my_map['integerValues'].items():
                    if not isinstance(value, int):
                        continue
                    return value == answer._value
            elif isinstance(answer._value, Float):
                for label, value in response._my_map['decimalValues'].items():
                    if not isinstance(value, float):
                        continue
                    return value == answer._value
        return False

    def is_correctness_available_for_response(self, response):
        """is a measure of correctness available for a particular mc response"""
        return True

    def is_response_correct(self, response):
        """returns True if response evaluates to an Item Answer that is 100 percent correct"""
        for answer in self.my_osid_object.get_answers():
            if self._is_match(response, answer):
                return True
        return False

    def get_correctness_for_response(self, response):
        """get measure of correctness available for a particular response"""
        for answer in self.my_osid_object.get_answers():
            if self._is_match(response, answer):
                try:
                    return answer.get_score()
                except AttributeError:
                    return 100
        for answer in self.my_osid_object.get_wrong_answers():
            if self._is_match(response, answer):
                try:
                    return answer.get_score()
                except AttributeError:
                    return 0

    def get_answer_for_response(self, response):
        for answer in self.my_osid_object.get_answers():
            if self._is_match(response, answer):
                return answer

        wrong_answers = None
        try:
            wrong_answers = list(self.my_osid_object.get_wrong_answers())
        except AttributeError:
            pass
        else:
            for answer in wrong_answers:
                if self._is_match(response, answer):
                    return answer

        # also look for generic incorrect answer
        if wrong_answers is not None:
            for answer in wrong_answers:
                if (not answer.has_decimal_values() and
                        not answer.has_integer_values()):
                    return answer

        raise NotFound('no matching answer found for response')

    def is_feedback_available_for_response(self, response):
        try:
            answer = self.get_answer_for_response(response)
        except NotFound:
            return False
        try:
            return answer.has_feedback()
        except AttributeError:
            return False

    def get_feedback_for_response(self, response):
        try:
            answer = self.get_answer_for_response(response)
        except NotFound:
            raise IllegalState('no answer matching response was found')
        return answer.get_feedback()  # raises IllegalState

    def get_confused_learning_objective_ids_for_response(self, response):
        try:
            answer = self.get_answer_for_response(response)
        except NotFound:
            raise IllegalState('no answer matching response was found')
        try:
            return answer.get_confused_learning_objective_ids()
        except AttributeError:
            return IdList([])


class CalculationInteractionItemFormRecord(WrongAnswerItemFormRecord):
    """form for QTI numeric response question"""
    _implemented_record_type_identifiers = [
        'qti-numeric-response'
    ]

    def __init__(self, osid_object_form=None):
        if osid_object_form is not None:
            self.my_osid_object_form = osid_object_form
        super(CalculationInteractionItemFormRecord, self).__init__(osid_object_form)


class CalculationInteractionQuestionRecord(QuestionTextRecord,
                                           QuestionFilesRecord):
    """QTI numeric response question"""
    _implemented_record_type_identifiers = [
        'question-text',
        'question-files',
        'qti-numeric-response'
    ]

    def __init__(self, osid_object):
        self.my_osid_object = osid_object
        self.my_osid_object._authority = MAGIC_AUTHORITY
        super(CalculationInteractionQuestionRecord, self).__init__(osid_object)
        # evaluate the randomly assigned variables and put values into the _my_map?
        self._vars = {}
        self._orig_question_text = str(self.my_osid_object._my_map['text']['text'])  # get a copy, not a pointer
        for variable, params in self.my_osid_object._my_map['variables'].items():
            if params['type'] == 'integer':
                self._vars[variable] = randint(int(params['min_value']), int(params['max_value']))
            elif params['type'] == 'float':
                self._vars[variable] = uniform(float(params['min_value']), float(params['max_value']))
            else:
                raise IllegalState('that type not supported')
            self._set_variable_value(variable, self._vars[variable])

    def _set_variable_value(self, variable_name, value):
        for variable, params in self.my_osid_object._my_map['variables'].items():
            if variable == variable_name and params['min_value'] <= value <= params['max_value']:
                if params['type'] == 'integer':
                    orig_text = self.my_osid_object._my_map['text']['text']
                    simple_var_label = '{{{0}}}'.format(variable)
                    if simple_var_label in orig_text:
                        self.my_osid_object._my_map['text']['text'] = orig_text.replace(simple_var_label,
                                                                                        str(value))
                    else:
                        item_body_soup = BeautifulSoup(orig_text, 'xml').itemBody
                        placeholder = item_body_soup.find('printedVariable', identifier=variable)
                        if placeholder:
                            placeholder.replace_with(str(value))
                            self.my_osid_object._my_map['text']['text'] = str(item_body_soup)
                elif params['type'] == 'float':
                    orig_text = self.my_osid_object._my_map['text']['text']
                    item_body_soup = BeautifulSoup(orig_text, 'xml').itemBody
                    placeholder = item_body_soup.find('printedVariable', identifier=variable)
                    if placeholder:
                        if params['format'] != '':
                            placeholder.replace_with(params['format'] % (value,))
                        else:
                            placeholder.replace_with(str(value))
                        self.my_osid_object._my_map['text']['text'] = str(item_body_soup)

    def get_id(self):
        # to handle new, unique session question IDs
        if self.my_osid_object._authority != MAGIC_AUTHORITY:
            return self.my_osid_object._item_id

        encoded_data = json.dumps(self._vars)
        magic_identifier = quote('{0}?{1}'.format(str(self.my_osid_object._my_map['_id']),
                                                  encoded_data))
        magic_id = Id(namespace='assessment.Item',
                      authority=MAGIC_AUTHORITY,
                      identifier=magic_identifier)
        return magic_id

    ident = property(fget=get_id)
    id_ = property(fget=get_id)

    def set_values(self, variable_values):
        self.my_osid_object._my_map['text']['text'] = str(self._orig_question_text)
        self._vars = variable_values
        for variable, value in variable_values.items():
            self._set_variable_value(variable, value)


class CalculationInteractionQuestionFormRecord(QuestionTextFormRecord,
                                               QuestionFilesFormRecord):
    """form for QTI numeric response question"""
    _implemented_record_type_identifiers = [
        'question-text',
        'question-files',
        'qti-numeric-response'
    ]

    def __init__(self, osid_object_form=None):
        if osid_object_form is not None:
            self.my_osid_object_form = osid_object_form
        self._init_metadata()
        if not self.my_osid_object_form.is_for_update():
            self._init_map()
        super(CalculationInteractionQuestionFormRecord, self).__init__(
            osid_object_form=osid_object_form)

    def _init_map(self):
        """stub"""
        super(CalculationInteractionQuestionFormRecord, self)._init_map()
        QuestionTextFormRecord._init_map(self)
        QuestionFilesFormRecord._init_map(self)
        self.my_osid_object_form._my_map['text']['text'] = ''
        self.my_osid_object_form._my_map['variables'] = \
            self._variables_metadata['default_object_values'][0]
        self.my_osid_object_form._my_map['expression'] = \
            self._expression_metadata['default_string_values'][0]

    def _init_metadata(self):
        """stub"""
        super(CalculationInteractionQuestionFormRecord, self)._init_metadata()
        QuestionTextFormRecord._init_metadata(self)
        QuestionFilesFormRecord._init_metadata(self)
        self._variables_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'variables'),
            'element_label': 'variables',
            'instructions': 'Enter the variables',
            'required': True,
            'read_only': False,
            'linked': False,
            'array': True,
            'default_object_values': [{}],
            'syntax': 'OBJECT',
            'object_set': []
        }
        self._expression_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'expression'),
            'element_label': 'expression',
            'instructions': 'enter the expression',
            'required': True,
            'read_only': False,
            'linked': False,
            'array': False,
            'default_string_values': [{
                'text': '',
                'languageTypeId': str(DEFAULT_LANGUAGE_TYPE),
                'scriptTypeId': str(DEFAULT_SCRIPT_TYPE),
                'formatTypeId': str(DEFAULT_FORMAT_TYPE),
            }],
            'syntax': 'STRING',
            'minimum_string_length': 0,
            'maximum_string_length': 1024,
            'string_set': []
        }

    def clear_variables(self):
        self.my_osid_object_form._my_map['variables'] = {}

    def add_variable(self, variable_name, variable_type, var_min, var_max, var_step=1, format=''):
        if variable_name in self.my_osid_object_form._my_map['variables']:
            raise IllegalState('variable already exists')
        if variable_type == 'integer':
            self.my_osid_object_form._my_map['variables'][variable_name] = {
                'type': variable_type,
                'min_value': int(var_min),
                'max_value': int(var_max),
                'step': int(var_step)
            }
        elif variable_type == 'float':
            self.my_osid_object_form._my_map['variables'][variable_name] = {
                'type': variable_type,
                'format': format,
                'min_value': float(var_min),
                'max_value': float(var_max)
            }

    def remove_variable(self, variable_name):
        if variable_name not in self.my_osid_object_form._my_map['variables']:
            raise IllegalState('variable not present')
        del self.my_osid_object_form._my_map['variables'][variable_name]

    def clear_expression(self):
        self.my_osid_object_form._my_map['expression'] = ''

    def set_expression(self, expression):
        # list of possible problems from
        # http://code.activestate.com/recipes/496746-restricted-safe-eval/
        if any(t in expression for t in ['import', 'os.', '__class__', 'raise', 'from', 'exec', 'eval',
                                         'try', 'except', 'finally', 'dir', 'compile', 'delattr', 'getattr',
                                         'file', 'locals', 'globals', 'open', 'setattr', 'vars',
                                         'input', 'raw_input', 'execFile', 'reload', 'im_class',
                                         'im_func', 'im_self', 'func_code', 'func_defaults', 'func_globals',
                                         'func_name', 'tb_frame', 'tb_next', 'f_back', 'f_builtins',
                                         'f_code', 'f_exc_traceback', 'f_exc_type', 'f_exc_value',
                                         'f_globals', 'f_locals']):
            raise IllegalState('bad expression')
        self.my_osid_object_form._my_map['expression'] = str(expression)


class CalculationInteractionFeedbackAndFilesAnswerRecord(DecimalValuesRecord,
                                                         IntegerValuesRecord,
                                                         TextAnswerRecord,
                                                         FilesAnswerRecord,
                                                         FeedbackAnswerRecord):
    """answer record for numeric response"""
    _implemented_record_type_identifiers = [
        'item-decimal-values',
        'item-integer-values',
        'text-answer',
        'item-text-values',
        'qti-numeric-response'
    ]

    def __init__(self, osid_object):
        self.my_osid_object = osid_object
        super(CalculationInteractionFeedbackAndFilesAnswerRecord, self).__init__(osid_object)
        self._value = None

    def has_tolerance_value(self):
        """stub"""
        return 'tolerance' in self.my_osid_object._my_map['decimalValues']

    def get_tolerance_value(self):
        """stub"""
        if self.has_tolerance_value():
            return self.get_decimal_value('tolerance')
        raise IllegalState()

    tolerance = property(fget=get_tolerance_value)

    def get_object_map(self):
        obj_map = dict(self.my_osid_object._my_map)
        obj_map = osid_objects.OsidObject.get_object_map(self.my_osid_object, obj_map)
        for label, value in obj_map['decimalValues'].items():
            obj_map['decimalValues'][label] = float(value)
        return obj_map

    object_map = property(fget=get_object_map)

    def set_answer_value(self, value):
        self._value = value

    def is_match(self, response):
        if self._value is not None:
            try:
                return int(str(response)) == int(str(self._value))
            except ValueError:
                try:
                    int(str(self._value))
                    # expect an int; response is not
                    return False
                except ValueError:
                    try:
                        return float(str(response)) == float(str(self._value))
                    except Exception:
                        # response is empty string / not a float
                        return False
        else:
            return False


class CalculationInteractionFeedbackAndFilesAnswerFormRecord(DecimalValuesFormRecord,
                                                             IntegerValuesFormRecord,
                                                             TextAnswerFormRecord,
                                                             FilesAnswerFormRecord,
                                                             FeedbackAnswerFormRecord):
    """answer form for numeric response"""
    _implemented_record_type_identifiers = [
        'item-decimal-values',
        'item-integer-values',
        'text-answer',
        'item-text-values',
        'qti-numeric-response'
    ]

    def __init__(self, osid_object_form=None):
        if osid_object_form is not None:
            self.my_osid_object_form = osid_object_form
        self._init_metadata()
        if not self.my_osid_object_form.is_for_update():
            self._init_map()
        super(CalculationInteractionFeedbackAndFilesAnswerFormRecord, self).__init__(
            osid_object_form=osid_object_form)

    def _init_map(self):
        """call these all manually because non-cooperative"""
        DecimalValuesFormRecord._init_map(self)
        IntegerValuesFormRecord._init_map(self)
        TextAnswerFormRecord._init_map(self)
        FilesAnswerFormRecord._init_map(self)
        FeedbackAnswerFormRecord._init_map(self)
        super(CalculationInteractionFeedbackAndFilesAnswerFormRecord, self)._init_map()
        self.my_osid_object_form._my_map['toleranceMode'] = \
            self._tolerance_mode_metadata['default_string_values'][0]

    def _init_metadata(self):
        """stub"""
        DecimalValuesFormRecord._init_metadata(self)
        IntegerValuesFormRecord._init_metadata(self)
        TextAnswerFormRecord._init_metadata(self)
        FilesAnswerFormRecord._init_metadata(self)
        FeedbackAnswerFormRecord._init_metadata(self)
        super(CalculationInteractionFeedbackAndFilesAnswerFormRecord, self)._init_metadata()
        self._tolerance_mode_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'tolerance_mode'),
            'element_label': 'tolerance_mode',
            'instructions': 'enter the tolerance mode',
            'required': True,
            'read_only': False,
            'linked': False,
            'array': False,
            'default_string_values': [{
                'text': '',
                'languageTypeId': str(DEFAULT_LANGUAGE_TYPE),
                'scriptTypeId': str(DEFAULT_SCRIPT_TYPE),
                'formatTypeId': str(DEFAULT_FORMAT_TYPE),
            }],
            'syntax': 'STRING',
            'minimum_string_length': 0,
            'maximum_string_length': 1024,
            'string_set': []
        }

    def get_tolerance_metadata(self):
        """stub"""
        return Metadata(**self._decimal_value_metadata)

    def set_tolerance_value(self, tolerance):
        """stub"""
        # include index because could be multiple response / tolerance pairs
        if not isinstance(tolerance, float):
            raise InvalidArgument('tolerance value must be a decimal')
        self.add_decimal_value(tolerance, 'tolerance')

    def clear_tolerance_value(self):
        self.clear_decimal_value('tolerance')

    def set_tolerance_mode(self, tolerance_mode):
        """stub"""
        # include index because could be multiple response / tolerance pairs
        self.my_osid_object_form._my_map['toleranceMode'] = str(tolerance_mode)

    def clear_tolerance_mode(self):
        self.my_osid_object_form._my_map['toleranceMode'] = ''


class MultiLanguageCalculationInteractionQuestionRecord(MultiLanguageQuestionRecord,
                                                        QuestionFilesRecord):
    """multi language QTI numeric response question"""
    _implemented_record_type_identifiers = [
        'multi-language-question-text',
        'question-files',
        'qti-numeric-response'
    ]

    def __init__(self, osid_object):
        self.my_osid_object = osid_object
        self.my_osid_object._authority = MAGIC_AUTHORITY
        super(MultiLanguageCalculationInteractionQuestionRecord, self).__init__(osid_object)
        # evaluate the randomly assigned variables and put values into the _my_map?
        self._vars = {}
        self._orig_question_text = list(self.my_osid_object._my_map['texts'])  # get a copy, not a pointer
        for variable, params in self.my_osid_object._my_map['variables'].items():
            if params['type'] == 'integer':
                self._vars[variable] = randint(int(params['min_value']), int(params['max_value']))
            elif params['type'] == 'float':
                self._vars[variable] = uniform(float(params['min_value']), float(params['max_value']))
            else:
                raise IllegalState('that type not supported')
            self._set_variable_value(variable, self._vars[variable])

    def _set_variable_value(self, variable_name, value):
        for variable, params in self.my_osid_object._my_map['variables'].items():
            if variable == variable_name and params['min_value'] <= value <= params['max_value']:
                if params['type'] == 'integer':
                    # cannot do self.my_osid_object.get_text().text because it can't
                    # find the record methods yet...
                    orig_text = self.get_matching_language_value('texts').text
                    simple_var_label = '{{{0}}}'.format(variable)
                    if simple_var_label in orig_text:
                        self.my_osid_object._my_map['texts'] = [self._display_text_dict(orig_text.replace(simple_var_label,
                                                                                                          str(value)))]
                    else:
                        item_body_soup = BeautifulSoup(orig_text, 'lxml-xml').itemBody
                        placeholder = item_body_soup.find('printedVariable', identifier=variable)
                        if placeholder:
                            placeholder.replace_with(str(value))
                            self.my_osid_object._my_map['texts'] = [self._display_text_dict(str(item_body_soup))]
                elif params['type'] == 'float':
                    # cannot do self.my_osid_object.get_text().text because it can't
                    # find the record methods yet...
                    orig_text = self.get_matching_language_value('texts').text
                    if '<itemBody' not in orig_text:
                        orig_text = '<itemBody>{0}</itemBody>'.format(orig_text)
                    item_body_soup = BeautifulSoup(orig_text, 'xml').itemBody
                    placeholder = item_body_soup.find('printedVariable', identifier=variable)
                    if placeholder:
                        if params['format'] != '':
                            placeholder.replace_with(params['format'] % (value,))
                        else:
                            placeholder.replace_with(str(value))
                        self.my_osid_object._my_map['texts'] = [self._display_text_dict(str(item_body_soup))]

    def get_id(self):
        # to handle new, unique session question IDs
        if self.my_osid_object._authority != MAGIC_AUTHORITY:
            return self.my_osid_object._item_id

        encoded_data = json.dumps(self._vars)
        magic_identifier = quote('{0}?{1}'.format(str(self.my_osid_object._my_map['_id']),
                                                  encoded_data))
        magic_id = Id(namespace='assessment.Item',
                      authority=MAGIC_AUTHORITY,
                      identifier=magic_identifier)
        return magic_id

    ident = property(fget=get_id)
    id_ = property(fget=get_id)

    def set_values(self, variable_values):
        self.my_osid_object._my_map['texts'] = list(self._orig_question_text)
        self._vars = variable_values
        for variable, value in variable_values.items():
            self._set_variable_value(variable, value)


class MultiLanguageCalculationInteractionQuestionFormRecord(MultiLanguageQuestionFormRecord,
                                                            QuestionFilesFormRecord):
    """form for QTI numeric response question"""
    _implemented_record_type_identifiers = [
        'multi-language-question-text',
        'question-files',
        'qti-numeric-response'
    ]

    def __init__(self, osid_object_form=None):
        if osid_object_form is not None:
            self.my_osid_object_form = osid_object_form
        self._init_metadata()
        if not self.my_osid_object_form.is_for_update():
            self._init_map()
        super(MultiLanguageCalculationInteractionQuestionFormRecord, self).__init__(
            osid_object_form=osid_object_form)

    def _init_map(self):
        """stub"""
        super(MultiLanguageCalculationInteractionQuestionFormRecord, self)._init_map()
        MultiLanguageQuestionFormRecord._init_map(self)
        QuestionFilesFormRecord._init_map(self)
        self.my_osid_object_form._my_map['variables'] = \
            self._variables_metadata['default_object_values'][0]
        self.my_osid_object_form._my_map['expression'] = \
            self._expression_metadata['default_string_values'][0]

    def _init_metadata(self):
        """stub"""
        super(MultiLanguageCalculationInteractionQuestionFormRecord, self)._init_metadata()
        MultiLanguageQuestionFormRecord._init_metadata(self)
        QuestionFilesFormRecord._init_metadata(self)
        self._variables_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'variables'),
            'element_label': 'variables',
            'instructions': 'Enter the variables',
            'required': True,
            'read_only': False,
            'linked': False,
            'array': True,
            'default_object_values': [{}],
            'syntax': 'OBJECT',
            'object_set': []
        }
        self._expression_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'expression'),
            'element_label': 'expression',
            'instructions': 'enter the expression',
            'required': True,
            'read_only': False,
            'linked': False,
            'array': False,
            'default_string_values': [{
                'text': '',
                'languageTypeId': str(DEFAULT_LANGUAGE_TYPE),
                'scriptTypeId': str(DEFAULT_SCRIPT_TYPE),
                'formatTypeId': str(DEFAULT_FORMAT_TYPE),
            }],
            'syntax': 'STRING',
            'minimum_string_length': 0,
            'maximum_string_length': 1024,
            'string_set': []
        }

    def clear_variables(self):
        self.my_osid_object_form._my_map['variables'] = {}

    def add_variable(self, variable_name, variable_type, var_min, var_max, var_step=1, format=''):
        if variable_name in self.my_osid_object_form._my_map['variables']:
            raise IllegalState('variable already exists')
        if variable_type == 'integer':
            self.my_osid_object_form._my_map['variables'][variable_name] = {
                'type': variable_type,
                'min_value': int(var_min),
                'max_value': int(var_max),
                'step': int(var_step)
            }
        elif variable_type == 'float':
            self.my_osid_object_form._my_map['variables'][variable_name] = {
                'type': variable_type,
                'format': format,
                'min_value': float(var_min),
                'max_value': float(var_max)
            }

    def remove_variable(self, variable_name):
        if variable_name not in self.my_osid_object_form._my_map['variables']:
            raise IllegalState('variable not present')
        del self.my_osid_object_form._my_map['variables'][variable_name]

    def clear_expression(self):
        self.my_osid_object_form._my_map['expression'] = ''

    def set_expression(self, expression):
        # list of possible problems from
        # http://code.activestate.com/recipes/496746-restricted-safe-eval/
        if any(t in expression for t in ['import', 'os.', '__class__', 'raise', 'from', 'exec', 'eval',
                                         'try', 'except', 'finally', 'dir', 'compile', 'delattr', 'getattr',
                                         'file', 'locals', 'globals', 'open', 'setattr', 'vars',
                                         'input', 'raw_input', 'execFile', 'reload', 'im_class',
                                         'im_func', 'im_self', 'func_code', 'func_defaults', 'func_globals',
                                         'func_name', 'tb_frame', 'tb_next', 'f_back', 'f_builtins',
                                         'f_code', 'f_exc_traceback', 'f_exc_type', 'f_exc_value',
                                         'f_globals', 'f_locals']):
            raise IllegalState('bad expression')
        self.my_osid_object_form._my_map['expression'] = str(expression)


class MultiLanguageCalculationInteractionFeedbackAndFilesAnswerRecord(DecimalValuesRecord,
                                                                      IntegerValuesRecord,
                                                                      TextAnswerRecord):
    """answer record for numeric response"""
    _implemented_record_type_identifiers = [
        'item-decimal-values',
        'item-integer-values',
        'text-answer',
        'qti-numeric-response'
    ]

    def __init__(self, osid_object):
        self.my_osid_object = osid_object
        super(MultiLanguageCalculationInteractionFeedbackAndFilesAnswerRecord, self).__init__(osid_object)
        self._value = None

    def has_tolerance_value(self):
        """stub"""
        return 'tolerance' in self.my_osid_object._my_map['decimalValues']

    def get_tolerance_value(self):
        """stub"""
        if self.has_tolerance_value():
            return self.get_decimal_value('tolerance')
        raise IllegalState()

    tolerance = property(fget=get_tolerance_value)

    def get_object_map(self):
        obj_map = dict(self.my_osid_object._my_map)
        obj_map = osid_objects.OsidObject.get_object_map(self.my_osid_object, obj_map)
        for label, value in obj_map['decimalValues'].items():
            obj_map['decimalValues'][label] = float(value)
        return obj_map

    object_map = property(fget=get_object_map)

    def set_answer_value(self, value):
        self._value = value

    def is_match(self, response):
        if self._value is not None:
            try:
                return int(str(response)) == int(str(self._value))
            except ValueError:
                try:
                    int(str(self._value))
                    # expect an int; response is not
                    return False
                except ValueError:
                    try:
                        return float(str(response)) == float(str(self._value))
                    except Exception:
                        # response is empty string / not a float
                        return False
        else:
            return False


class MultiLanguageCalculationInteractionFeedbackAndFilesAnswerFormRecord(DecimalValuesFormRecord,
                                                                          IntegerValuesFormRecord,
                                                                          TextAnswerFormRecord):
    """answer form for numeric response"""
    _implemented_record_type_identifiers = [
        'item-decimal-values',
        'item-integer-values',
        'text-answer',
        'qti-numeric-response'
    ]

    def __init__(self, osid_object_form=None):
        if osid_object_form is not None:
            self.my_osid_object_form = osid_object_form
        self._init_metadata()
        if not self.my_osid_object_form.is_for_update():
            self._init_map()
        super(MultiLanguageCalculationInteractionFeedbackAndFilesAnswerFormRecord, self).__init__(
            osid_object_form=osid_object_form)

    def _init_map(self):
        """call these all manually because non-cooperative"""
        DecimalValuesFormRecord._init_map(self)
        IntegerValuesFormRecord._init_map(self)
        TextAnswerFormRecord._init_map(self)
        super(MultiLanguageCalculationInteractionFeedbackAndFilesAnswerFormRecord, self)._init_map()
        self.my_osid_object_form._my_map['toleranceMode'] = \
            self._tolerance_mode_metadata['default_string_values'][0]

    def _init_metadata(self):
        """stub"""
        DecimalValuesFormRecord._init_metadata(self)
        IntegerValuesFormRecord._init_metadata(self)
        TextAnswerFormRecord._init_metadata(self)
        super(MultiLanguageCalculationInteractionFeedbackAndFilesAnswerFormRecord, self)._init_metadata()
        self._tolerance_mode_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'tolerance_mode'),
            'element_label': 'tolerance_mode',
            'instructions': 'enter the tolerance mode',
            'required': True,
            'read_only': False,
            'linked': False,
            'array': False,
            'default_string_values': [{
                'text': '',
                'languageTypeId': str(DEFAULT_LANGUAGE_TYPE),
                'scriptTypeId': str(DEFAULT_SCRIPT_TYPE),
                'formatTypeId': str(DEFAULT_FORMAT_TYPE),
            }],
            'syntax': 'STRING',
            'minimum_string_length': 0,
            'maximum_string_length': 1024,
            'string_set': []
        }

    def get_tolerance_metadata(self):
        """stub"""
        return Metadata(**self._decimal_value_metadata)

    def set_tolerance_value(self, tolerance):
        """stub"""
        # include index because could be multiple response / tolerance pairs
        if not isinstance(tolerance, float):
            raise InvalidArgument('tolerance value must be a decimal')
        self.add_decimal_value(tolerance, 'tolerance')

    def clear_tolerance_value(self):
        self.clear_decimal_value('tolerance')

    def set_tolerance_mode(self, tolerance_mode):
        """stub"""
        # include index because could be multiple response / tolerance pairs
        self.my_osid_object_form._my_map['toleranceMode'] = str(tolerance_mode)

    def clear_tolerance_mode(self):
        self.my_osid_object_form._my_map['toleranceMode'] = ''
