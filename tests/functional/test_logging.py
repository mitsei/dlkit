import datetime
import json

from dlkit.records.registry import LOG_ENTRY_RECORD_TYPES
from dlkit.runtime.primordium import Type, DateTime

from .utilities.testing import DLKitTestCase, get_agent_id


TEXT_BLOB_LOG_ENTRY = Type(**LOG_ENTRY_RECORD_TYPES['text-blob'])


class LogEntryTests(DLKitTestCase):
    def create_log_entry(self):
        form = self._log.get_log_entry_form_for_create([TEXT_BLOB_LOG_ENTRY])
        form.set_text(self._text_blob)
        return self._log.create_log_entry(form)

    def num_entries(self, val):
        self.assertEqual(
            self._log.log_entries.available(),
            val
        )

    def setUp(self):
        super(LogEntryTests, self).setUp()

        self._log = self._get_test_log()
        self._text_blob = json.dumps({
            'user': 'Jane',
            'action': 'signed in',
            'timestamp': {
                'year': 2016,
                'month': 1,
                'day': 1
            }
        })

    def tearDown(self):
        """
        Remove the test user from all groups in Membership
        Start from the smallest groupId because need to
        remove "parental" roles like for DepartmentAdmin / DepartmentOfficer
        """
        super(LogEntryTests, self).tearDown()

    def test_can_create_text_blob_log_entry(self):
        self.create_log_entry()

    def test_can_update_text_blob_log_entry(self):
        self.num_entries(0)
        entry = self.create_log_entry()
        self.num_entries(1)
        form = self._log.get_log_entry_form_for_update(entry.ident)
        form.set_text('foo')
        new_entry = self._log.update_log_entry(form)
        entry = self._log.get_log_entry(new_entry.ident)
        self.assertEqual(
            entry.get_text().text,
            'foo'
        )
        self.num_entries(1)

    def test_can_delete_text_blob_log_entry(self):
        self.num_entries(0)
        entry = self.create_log_entry()
        self.num_entries(1)
        self._log.delete_log_entry(entry.ident)
        self.num_entries(0)

    def test_can_query_by_timestamp(self):
        self.num_entries(0)

        now = DateTime.now() - datetime.timedelta(minutes=5)
        past = now - datetime.timedelta(days=1)
        future = now + datetime.timedelta(days=1)
        more_future = future + datetime.timedelta(days=1)

        entry = self.create_log_entry()
        self.num_entries(1)

        log_entry_query = self._log.get_log_entry_query()
        log_entry_query.match_timestamp(past, now, True)
        results = self._log.get_log_entries_by_query(log_entry_query)
        self.assertEqual(
            results.available(),
            0
        )

        log_entry_query = self._log.get_log_entry_query()
        log_entry_query.match_timestamp(now, future, True)
        results = self._log.get_log_entries_by_query(log_entry_query)
        self.assertEqual(
            results.available(),
            1
        )
        self.assertEqual(
            str(results.next().ident),
            str(entry.ident)
        )

        log_entry_query = self._log.get_log_entry_query()
        log_entry_query.match_timestamp(future, more_future, True)
        results = self._log.get_log_entries_by_query(log_entry_query)
        self.assertEqual(
            results.available(),
            0
        )

    def test_can_query_by_agent_id(self):
        entry = self.create_log_entry()
        agent_id = get_agent_id(self.username)

        log_entry_query = self._log.get_log_entry_query()
        log_entry_query.match_agent_id(agent_id, True)
        results = self._log.get_log_entries_by_query(log_entry_query)
        self.assertEqual(
            results.available(),
            1
        )

        self.assertEqual(
            str(results.next().ident),
            str(entry.ident)
        )

        log_entry_query = self._log.get_log_entry_query()
        log_entry_query.match_agent_id('foobar', True)
        results = self._log.get_log_entries_by_query(log_entry_query)
        self.assertEqual(
            results.available(),
            0
        )
