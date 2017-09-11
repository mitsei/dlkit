"""Unit tests of logging records."""


import pytest


from ..utilities.general import is_never_authz, is_no_authz, uses_cataloging, uses_filesystem_only


@pytest.mark.usefixtures("log_entry_record_class_fixture", "log_entry_record_test_fixture")
class TestLogEntryRecord(object):
    """Tests for LogEntryRecord"""


@pytest.mark.usefixtures("log_entry_query_record_class_fixture", "log_entry_query_record_test_fixture")
class TestLogEntryQueryRecord(object):
    """Tests for LogEntryQueryRecord"""


@pytest.mark.usefixtures("log_entry_form_record_class_fixture", "log_entry_form_record_test_fixture")
class TestLogEntryFormRecord(object):
    """Tests for LogEntryFormRecord"""


@pytest.mark.usefixtures("log_entry_search_record_class_fixture", "log_entry_search_record_test_fixture")
class TestLogEntrySearchRecord(object):
    """Tests for LogEntrySearchRecord"""


@pytest.mark.usefixtures("log_record_class_fixture", "log_record_test_fixture")
class TestLogRecord(object):
    """Tests for LogRecord"""


@pytest.mark.usefixtures("log_query_record_class_fixture", "log_query_record_test_fixture")
class TestLogQueryRecord(object):
    """Tests for LogQueryRecord"""


@pytest.mark.usefixtures("log_form_record_class_fixture", "log_form_record_test_fixture")
class TestLogFormRecord(object):
    """Tests for LogFormRecord"""


@pytest.mark.usefixtures("log_search_record_class_fixture", "log_search_record_test_fixture")
class TestLogSearchRecord(object):
    """Tests for LogSearchRecord"""
