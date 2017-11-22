"""
records.assessment.mecqbank.item_records.py
"""

import re
from dlkit.abstract_osid.osid.errors import IllegalState

from ..basic.base_records import ProvenanceItemRecord
from ..basic.simple_records import ItemTextsRecord,\
    ItemFilesRecord,\
    TextsAnswerRecord,\
    QuestionTextsFormRecord,\
    QuestionTextsRecord,\
    QuestionFilesFormRecord,\
    QuestionFilesRecord,\
    ItemTextsAndFilesMixin,\
    ProvenanceMixin,\
    QuestionTextsAndFilesMixin
from ...osid.base_records import QueryInitRecord

from .mecqbank_base_records import PDFPreviewFormRecord,\
    PDFPreviewRecord,\
    PublishedFormRecord,\
    SourceItemRecord,\
    SimpleDifficultyItemFormRecord,\
    SimpleDifficultyItemRecord,\
    MecQBankBaseMixin,\
    PublishedRecord


class MecQBankItemRecord(ItemTextsRecord,
                         ItemFilesRecord,
                         ProvenanceItemRecord,
                         PDFPreviewRecord,
                         SourceItemRecord,
                         SimpleDifficultyItemRecord,
                         PublishedRecord):
    """mecqbank base item"""
    _implemented_record_type_identifiers = [
        'mecqbank-item',
        'item-texts',
        'item-files',
        'provenance-item',
        'mecqbank-pdf-preview',
        'simple-difficulty',
        'mecqbank-source',
        'mecqbank-published'
    ]

    def _clean(self, label):
        """stub"""
        return re.sub(r'[^\w\d]', '_', label)

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

    def _update_object_map(self, obj_map):
        """stub"""
        super(MecQBankItemRecord, self)._update_object_map(obj_map)

    latex = property(fget=get_raw_latex)


class MecQBankItemFormRecord(ItemTextsAndFilesMixin,
                             MecQBankBaseMixin,
                             ProvenanceMixin):
    """form for mecqbank items"""
    _implemented_record_type_identifiers = [
        'mecqbank-item',
        'item-texts',
        'item-files',
        'provenance-item',
        'mecqbank-pdf-preview',
        'simple-difficulty',
        'mecqbank-source',
        'mecqbank-published'
    ]


class MecQBankItemQueryRecord(QueryInitRecord):
    """to make mecqbank items queryable"""


class MecQBankAssessmentRecord(PublishedRecord):
    """assessments for mecqbank"""
    _implemented_record_type_identifiers = [
        'mecqbank-assessment',
        'mecqbank-published'
    ]


class MecQBankAssessmentFormRecord(PublishedFormRecord):
    """form for mecqbank assessments"""
    _implemented_record_type_identifiers = [
        'mecqbank-assessment',
        'mecqbank-published'
    ]


class MecQBankAssessmentQueryRecord(QueryInitRecord):
    """for querying mecqbank assessments"""
    def match_mecqbank_item_id(self, item_id):
        """stub"""
        self._add_match('itemIds', str(item_id), True)

    def clear_mecqbank_item_id(self):
        """stub"""
        self._clear_terms('itemIds')


class MecQBankAnswerRecord(TextsAnswerRecord, ItemFilesRecord, PDFPreviewRecord):
    """mecqbank answers"""
    _implemented_record_type_identifiers = [
        'mecqbank-answer',
        'texts-answer',
        'mecqbank-pdf-preview'
    ]

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


class MecQBankAnswerFormRecord(ItemTextsAndFilesMixin,
                               PDFPreviewFormRecord):
    """forms for mecqbank answers"""
    _implemented_record_type_identifiers = [
        'mecqbank-answer',
        'texts-answer',
        'mecqbank-pdf-preview'
    ]


class MecQBankQuestionRecord(PDFPreviewRecord,
                             SimpleDifficultyItemRecord,
                             QuestionTextsRecord,
                             QuestionFilesRecord):
    """mecqbank questions"""
    _implemented_record_type_identifiers = [
        'mecqbank-question',
        'question-texts',
        'question-files',
        'mecqbank-pdf-preview',
        'simple-difficulty',
    ]

    def _clean(self, label):
        """stub"""
        return re.sub(r'[^\w\d]', '_', label)

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

    latex = property(fget=get_raw_latex)


class MecQBankQuestionFormRecord(PDFPreviewFormRecord,
                                 SimpleDifficultyItemFormRecord,
                                 QuestionTextsAndFilesMixin):
    """form for mecqbank questions"""
    _implemented_record_type_identifiers = [
        'mecqbank-question',
        'question-texts',
        'question-files',
        'mecqbank-pdf-preview',
        'simple-difficulty',
    ]
