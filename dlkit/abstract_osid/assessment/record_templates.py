"""Implementations of assessment abstract base class records."""
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


class QuestionRecord:
    """A record for a ``Question``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class QuestionQueryRecord:
    """A record for a ``QuestionQuery``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class QuestionQueryInspectorRecord:
    """A record for a ``QuestionQueryInspector``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class QuestionFormRecord:
    """A record for a ``QuestionForm``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class QuestionSearchOrderRecord:
    """A record for a ``QuestionSearchOrder``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class AnswerRecord:
    """A record for an ``Answer``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class AnswerQueryRecord:
    """A record for an ``AnswerQuery``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class AnswerQueryInspectorRecord:
    """A record for an ``AnswerQueryInspector``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class AnswerFormRecord:
    """A record for an ``AnswerForm``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class AnswerSearchOrderRecord:
    """A record for an ``AnswerSearchOrder``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class ItemRecord:
    """A record for an ``Item``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class ItemQueryRecord:
    """A record for an ``ItemQuery``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class ItemQueryInspectorRecord:
    """A record for an ``ItemQueryInspector``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class ItemFormRecord:
    """A record for an ``ItemForm``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class ItemSearchOrderRecord:
    """A record for an ``ItemSearchOrder``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class ItemSearchRecord:
    """A record for an ``ItemSearch``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class ItemSearchResultsRecord:
    """A record for an ``ItemSearchResults``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class AssessmentRecord:
    """A record for an ``Assessment``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class AssessmentQueryRecord:
    """A record for an ``AssessmentQuery``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class AssessmentQueryInspectorRecord:
    """A record for an ``AssessmentQueryInspector``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class AssessmentFormRecord:
    """A record for an ``AssessmentForm``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class AssessmentSearchOrderRecord:
    """A record for an ``AssessmentSearchOrder``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class AssessmentSearchRecord:
    """A record for an ``AssessmentSearch``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class AssessmentSearchResultsRecord:
    """A record for an ``AssessmentSearchResults``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class AssessmentOfferedRecord:
    """A record for an ``AssessmentOffered``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class AssessmentOfferedQueryRecord:
    """A record for an ``AssessmentOfferedQuery``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class AssessmentOfferedQueryInspectorRecord:
    """A record for an ``AssessmentOfferedQueryInspector``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class AssessmentOfferedFormRecord:
    """A record for an ``AssessmentOfferedForm``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class AssessmentOfferedSearchOrderRecord:
    """A record for an ``AssessmentOfferedSearchOrder``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class AssessmentOfferedSearchRecord:
    """A record for an ``AssessmentOfferedSearch``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class AssessmentOfferedSearchResultsRecord:
    """A record for an ``AssessmentOfferedSearchResults``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class AssessmentTakenRecord:
    """A record for an ``AssessmentTaken``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class AssessmentTakenQueryRecord:
    """A record for an ``AssessmentTakenQuery``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class AssessmentTakenQueryInspectorRecord:
    """A record for an ``AssessmentTakenQueryInspector``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class AssessmentTakenFormRecord:
    """A record for an ``AssessmentTakenForm``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class AssessmentTakenSearchOrderRecord:
    """A record for an ``AssessmentTakenSearchOrder``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class AssessmentTakenSearchRecord:
    """A record for an ``AssessmentTakenSearch``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class AssessmentTakenSearchResultsRecord:
    """A record for an ``AssessmentTakenSearchResults``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class AssessmentSectionRecord:
    """A record for an ``AssessmentSection``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class BankRecord:
    """A record for a ``Bank``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class BankQueryRecord:
    """A record for a ``BankQuery``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class BankQueryInspectorRecord:
    """A record for a ``BankQueryInspector``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class BankFormRecord:
    """A record for a ``BankForm``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class BankSearchOrderRecord:
    """A record for a ``BankSearchOrder``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class BankSearchRecord:
    """A record for a ``BankSearch``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class BankSearchResultsRecord:
    """A record for a ``BankSearchResults``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class ResponseRecord:
    """A record for a ``Response``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta
