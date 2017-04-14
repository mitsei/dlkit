# how do we inject this into records registry?
# for now, hardcode the import to this from AssessmentSession and AssessmentResultsSession...
# perhaps handle it in a runtime config, later.

from ..osid import registry as osid_registry

ASSESSMENT_PART_GENUS_TYPES = {
    'fbw-specify-lo': {
        'authority': 'ODL.MIT.EDU',
        'namespace': 'assessment-part-genus-type',
        'identifier': 'fbw-specify-lo',
        'display_name': 'Specify the LO only',
        'display_label': 'Specify the LO only',
        'description': 'Specify the LO only for this section',
        'domain': 'assessment_authoring.AssessmentPart'},
}

ASSESSMENT_PART_RECORD_TYPES = {
    'scaffold-down': {
        'authority': 'ODL.MIT.EDU',
        'namespace': 'assessment-part-record-type',
        'identifier': 'scaffold-down',
        'display_name': 'Assessment Part that scaffolds down when given incorrect item responses',
        'display_label': 'Assessment Part that scaffolds down when given incorrect item responses',
        'description': 'Assessment Part that scaffolds down when given incorrect item responses',
        'domain': 'assessment_authoring.AssessmentPart',
        'module_path': 'dlkit.records.adaptive.magic_parts.assessment_part_records',
        'object_record_class_name': 'ScaffoldDownAssessmentPartRecord',
        'form_record_class_name': 'ScaffoldDownAssessmentPartFormRecord'},
}

ASSESSMENT_PART_RECORD_TYPES.update(osid_registry.__dict__.get('OSID_OBJECT_RECORD_TYPES', {}))

ITEM_RECORD_TYPES = {
    'multi-choice-randomized': {
        'authority': 'ODL.MIT.EDU',
        'namespace': 'item-record-type',
        'identifier': 'multi-choice-randomized',
        'display_name': 'Item with randomized choice order',
        'display_label': 'Item with randomized choice order',
        'description': 'Assessment MultipleChoice Item record with randomized choice order',
        'domain': 'assessment.Item',
        'module_path': 'dlkit.records.adaptive.multi_choice_questions.randomized_questions',
        'object_record_class_name': 'MagicRandomizedMCItemRecord',
        'form_record_class_name': 'MagicRandomizedMCItemFormRecord'},
}

ITEM_RECORD_TYPES.update(osid_registry.__dict__.get('OSID_OBJECT_RECORD_TYPES', {}))

QUESTION_RECORD_TYPES = {
    'multi-choice-randomized': {
        'authority': 'ODL.MIT.EDU',
        'namespace': 'question-record-type',
        'identifier': 'multi-choice-randomized',
        'display_name': 'Question with randomized choice order',
        'display_label': 'Question with randomized choice order',
        'description': 'Assessment Question record with randomized choice order',
        'domain': 'assessment.Question',
        'module_path': 'dlkit.records.adaptive.multi_choice_questions.randomized_questions',
        'object_record_class_name': 'MultiChoiceRandomizeChoicesQuestionRecord',
        'form_record_class_name': 'MultiChoiceRandomizeChoicesQuestionFormRecord'},

}

QUESTION_RECORD_TYPES.update(osid_registry.__dict__.get('OSID_OBJECT_RECORD_TYPES', {}))
