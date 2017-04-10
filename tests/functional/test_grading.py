import numpy as np

from decimal import Decimal

from .utilities.testing import DLKitTestCase, get_manager

from dlkit.runtime.proxy_example import SimpleRequest


class GradebookSummaryTests(DLKitTestCase):
    def add_item(self, bank):
        form = bank.get_item_form_for_create([])
        form.display_name = 'a test item!'
        form.description = 'for testing with'
        new_item = bank.create_item(form)

        question_form = bank.get_question_form_for_create(new_item.ident,
                                                          [])
        question_form.display_name = 'Question for ' + new_item.display_name.text
        question_form.description = ''
        new_question = bank.create_question(question_form)

        answer_form = bank.get_answer_form_for_create(new_item.ident,
                                                      [])
        answer_form.display_name = 'Answer for ' + new_item.display_name.text
        new_answer = bank.create_answer(answer_form)

        return new_item

    def create_grade_system(self, gradebook):
        create_form = gradebook.get_grade_system_form_for_create([])
        create_form.display_name = 'Test Grade System'
        create_form.description = 'Test Grade System for tests'
        create_form.based_on_grades = False
        create_form.lowest_numeric_score = 0
        create_form.highest_numeric_score = 100
        create_form.numeric_score_increment = 1
        return gradebook.create_grade_system(create_form)

    def create_gradebook_column(self, gradebook, grade_system):
        create_form = gradebook.get_gradebook_column_form_for_create([])
        create_form.display_name = 'Test GradebookColumn'
        create_form.description = 'Test GradebookColumn for tests'
        create_form.grade_system = grade_system.ident
        return gradebook.create_gradebook_column(create_form)

    def populate_grade_entries(self, gradebook, column):
        self._scores = []
        for num in range(0, 100):
            username = 'User_{0}'.format(num)
            request = SimpleRequest(username=username)
            gm = get_manager(request, 'grading')
            form = gradebook.get_grade_entry_form_for_create(column.ident,
                                                             gm.effective_agent_id,
                                                             [])
            form.set_score(float(num))
            gradebook.create_grade_entry(form)
            self._scores.append(Decimal(num))

    def setUp(self):
        super(GradebookSummaryTests, self).setUp()

        self._bank = self._get_test_bank()
        self._item = self.add_item(self._bank)
        self._taken = self.create_taken_for_items(self._bank, [self._item])

        self._gradebook = self._get_test_gradebook()
        self._grade_system = self.create_grade_system(self._gradebook)
        self._gradebook_column = self.create_gradebook_column(self._gradebook,
                                                              self._grade_system)

        self.populate_grade_entries(self._gradebook, self._gradebook_column)
        self.summary = self._gradebook.get_gradebook_column_summary(self._gradebook_column.ident)

    def tearDown(self):
        """
        Remove the test user from all groups in Membership
        Start from the smallest groupId because need to
        remove "parental" roles like for DepartmentAdmin / DepartmentOfficer
        """
        super(GradebookSummaryTests, self).tearDown()

    def test_can_get_mean(self):
        self.assertEqual(
            self.summary.get_mean(),
            np.mean(self._scores)
        )

    def test_can_get_median(self):
        self.assertEqual(
            self.summary.get_median(),
            np.median(self._scores)
        )

    def test_can_get_mode(self):
        self.assertEqual(
            self.summary.get_mode(),
            0
        )

    def test_can_get_rms(self):
        self.assertEqual(
            self.summary.get_rms(),
            np.sqrt(np.mean(np.square(self._scores)))
        )

    def test_can_get_standard_deviation(self):
        self.assertEqual(
            self.summary.get_standard_deviation(),
            np.std(self._scores)
        )

    def test_can_get_sum(self):
        self.assertEqual(
            self.summary.get_sum(),
            50 * 99
        )
