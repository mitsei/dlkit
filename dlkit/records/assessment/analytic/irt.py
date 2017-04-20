"""
Basic IRT support for assessment items
"""

from dlkit.json_.osid.metadata import Metadata

from dlkit.abstract_osid.assessment import record_templates as abc_assessment_records
from dlkit.abstract_osid.osid.errors import IllegalState, InvalidArgument

from ...osid.base_records import DecimalValuesRecord,\
    DecimalValuesFormRecord,\
    QueryInitRecord


class ItemDecimalValuesRecord(abc_assessment_records.ItemRecord, DecimalValuesRecord):
    """actual assessment item record"""

    _implemented_record_type_identifiers = [
        'item-decimal-values'
    ]


class ItemDecimalValuesFormRecord(DecimalValuesFormRecord,
                                  abc_assessment_records.ItemFormRecord):
    """an assessment item with decimal values attached"""

    _implemented_record_type_identifiers = [
        'item-decimal-values'
    ]

    def __init__(self, osid_object_form=None):
        if osid_object_form is not None:
            self.my_osid_object_form = osid_object_form
        self._init_metadata()
        if not self.my_osid_object_form.is_for_update():
            self._init_map()
        super(ItemDecimalValuesFormRecord, self).__init__(osid_object_form=osid_object_form)


class IRTItemRecord(DecimalValuesRecord):
    """include 3 basic IRT values"""

    _implemented_record_type_identifiers = [
        'irt-item',
        'item-decimal-values'
    ]

    def has_difficulty_value(self):
        """stub"""
        return 'difficulty' in self.my_osid_object._my_map['decimalValues']

    def get_difficulty_value(self):
        """stub"""
        if self.has_difficulty_value():
            return self.my_osid_object._my_map['decimalValues']['difficulty']
        raise IllegalState()

    def has_discrimination_value(self):
        """stub"""
        return 'discrimination' in self.my_osid_object._my_map['decimalValues']

    def get_discrimination_value(self):
        """stub"""
        if self.has_discrimination_value():
            return self.my_osid_object._my_map['decimalValues']['discrimination']
        raise IllegalState()

    def has_pseudo_guessing_value(self):
        """stub"""
        return 'pseudoGuessing' in self.my_osid_object._my_map['decimalValues']

    def get_pseudo_guessing_value(self):
        """stub"""
        if self.has_pseudo_guessing_value():
            return self.my_osid_object._my_map['decimalValues']['pseudoGuessing']
        raise IllegalState()

    difficulty = property(fget=get_difficulty_value)
    discrimination = property(fget=get_discrimination_value)
    guessing = property(fget=get_pseudo_guessing_value)


class IRTItemFormRecord(ItemDecimalValuesFormRecord):
    """form to create / update the 3 IRT values we support"""

    _implemented_record_type_identifiers = [
        'irt-item',
        'item-decimal-values'
    ]

    def __init__(self, osid_object_form=None):
        if osid_object_form is not None:
            self.my_osid_object_form = osid_object_form
        self._init_metadata()
        if not self.my_osid_object_form.is_for_update():
            self._init_map()
        super(IRTItemFormRecord, self).__init__(osid_object_form=osid_object_form)

    def _init_map(self):
        """stub"""
        super(IRTItemFormRecord, self)._init_map()
        self.my_osid_object_form._my_map['decimalValues']['difficulty'] = \
            self._decimal_value_metadata['default_decimal_values'][1]
        self.my_osid_object_form._my_map['decimalValues']['discrimination'] = \
            self._decimal_value_metadata['default_decimal_values'][1]
        self.my_osid_object_form._my_map['decimalValues']['pseudoGuessing'] = \
            self._decimal_value_metadata['default_decimal_values'][1]

    def get_difficulty_value_metadata(self):
        """stub"""
        return Metadata(**self._decimal_value_metadata)

    def get_discrimination_value_metadata(self):
        """stub"""
        return Metadata(**self._decimal_value_metadata)

    def get_pseudo_guessing_value_metadata(self):
        """stub"""
        return Metadata(**self._decimal_value_metadata)

    def set_difficulty_value(self, difficulty):
        """stub"""
        if not isinstance(difficulty, float):
            raise InvalidArgument('difficulty value must be a decimal')
        self.add_decimal_value(difficulty, 'difficulty')

    def set_discrimination_value(self, discrimination):
        """stub"""
        if not isinstance(discrimination, float):
            raise InvalidArgument('discrimination value must be a decimal')
        self.add_decimal_value(discrimination, 'discrimination')

    def set_pseudo_guessing_value(self, pseudo_guessing):
        """stub"""
        if not isinstance(pseudo_guessing, float):
            raise InvalidArgument('pseudo-guessing value must be a decimal')
        self.add_decimal_value(pseudo_guessing, 'pseudoGuessing')


class IRTItemQueryRecord(QueryInitRecord):
    """query items by IRT attributes"""

    def match_minimum_difficulty(self, value, match):
        """stub"""
        self._my_osid_query._match_minimum_decimal('decimalValues.difficulty',
                                                   value,
                                                   match)

    def clear_minimum_difficulty_terms(self):
        """stub"""
        self._my_osid_query._clear_minimum_terms('decimalValues.difficulty')

    def match_maximum_difficulty(self, value, match):
        """stub"""
        self._my_osid_query._match_maximum_decimal('decimalValues.difficulty',
                                                   value,
                                                   match)

    def clear_maximum_difficulty_terms(self):
        """stub"""
        self._my_osid_query._clear_maximum_terms('decimalValues.difficulty')

    def match_minimum_discrimination(self, value, match):
        """stub"""
        self._my_osid_query._match_minimum_decimal('decimalValues.discrimination',
                                                   value,
                                                   match)

    def clear_miniumum_discrimination_terms(self):
        """stub"""
        self._my_osid_query._clear_minimum_terms('decimalValues.discrimination')

    def match_maximum_discrimination(self, value, match):
        """stub"""
        self._my_osid_query._match_maximum_decimal('decimalValues.discrimination',
                                                   value,
                                                   match)

    def clear_maximum_discrimination_terms(self):
        """stub"""
        self._my_osid_query._clear_maximum_terms('decimalValues.discrimination')

    def match_minimum_pseudo_guessing(self, value, match):
        """stub"""
        self._my_osid_query._match_minimum_decimal('decimalValues.pseudo_guessing',
                                                   value,
                                                   match)

    def clear_miniumum_pseudo_guessing_terms(self):
        """stub"""
        self._my_osid_query._clear_minimum_terms('decimalValues.pseudo_guessing')

    def match_maximum_pseudo_guessing(self, value, match):
        """stub"""
        self._my_osid_query._match_maximum_decimal('decimalValues.pseudo_guessing',
                                                   value,
                                                   match)

    def clear_maximum_pseudo_guessing_terms(self):
        """stub"""
        self._my_osid_query._clear_maximum_terms('decimalValues.pseudo_guessing')
