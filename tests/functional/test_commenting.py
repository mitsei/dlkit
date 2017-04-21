from .utilities.testing import DLKitTestCase

from dlkit.runtime.primordium import DataInputStream, Type, Id
from dlkit.records.registry import ANSWER_RECORD_TYPES, QUESTION_RECORD_TYPES, ITEM_GENUS_TYPES

UOC_PROBLEM_TYPE = Type(**ITEM_GENUS_TYPES['multi-file-submission'])
FILES_SUBMISSION_ANSWER_TYPE = Type(**ANSWER_RECORD_TYPES['files-submission'])
FILES_SUBMISSION_QUESTION_TYPE = Type(**QUESTION_RECORD_TYPES['files-submission'])

FILE_COMMENT_RECORD_TYPE = Type(**{
    'authority': 'ODL.MIT.EDU',
    'namespace': 'comment-type',
    'identifier': 'file-comment',
    'display_name': 'File Comment',
    'display_label': 'File Comment',
    'description': 'Comment via file',
    'domain': 'commenting.Comment'
})


class ResponseCommentingTests(DLKitTestCase):
    def add_item(self, bank):
        form = bank.get_item_form_for_create([])
        form.display_name = 'a test item!'
        form.description = 'for testing with'
        form.set_genus_type(UOC_PROBLEM_TYPE)
        new_item = bank.create_item(form)

        question_form = bank.get_question_form_for_create(new_item.ident,
                                                          [FILES_SUBMISSION_QUESTION_TYPE])
        question_form.display_name = 'Question for ' + new_item.display_name.text
        question_form.description = ''
        new_question = bank.create_question(question_form)

        answer_form = bank.get_answer_form_for_create(new_item.ident,
                                                      [FILES_SUBMISSION_ANSWER_TYPE])
        answer_form.display_name = 'Answer for ' + new_item.display_name.text
        new_answer = bank.create_answer(answer_form)

        return new_item

    def send_comment(self, with_files=False):
        first_section = self._bank.get_first_assessment_section(self._taken.ident)
        response = self._bank.get_response(first_section.ident, self._item.ident)
        comment_type = [FILE_COMMENT_RECORD_TYPE]

        book = self.get_book(self._bank.ident)
        form = book.get_comment_form_for_create(response.ident,
                                                comment_type)

        form.set_text('Good job')

        if with_files:
            form.set_file(DataInputStream(self.test_file1),
                          asset_name='my comments')

        book.create_comment(form)

    def setUp(self):
        super(ResponseCommentingTests, self).setUp()

        self._bank = self._get_test_bank()
        self._item = self.add_item(self._bank)
        self._taken = self.create_taken_for_items(self._bank, [self._item])

        self.student_submits_response()

    def student_submits_response(self):
        first_section = self._bank.get_first_assessment_section(self._taken.ident)
        response_form = self._bank.get_response_form(assessment_section_id=first_section.ident,
                                                     item_id=self._item.ident)
        response_form.add_file(DataInputStream(self.test_file1), 'my answers')
        self._bank.submit_response(first_section.ident, self._item.ident, response_form)

    def tearDown(self):
        """
        Remove the test user from all groups in Membership
        Start from the smallest groupId because need to
        remove "parental" roles like for DepartmentAdmin / DepartmentOfficer
        """
        super(ResponseCommentingTests, self).tearDown()

    def test_can_add_comment_to_response(self):
        first_section = self._bank.get_first_assessment_section(self._taken.ident)
        response = self._bank.get_response(first_section.ident, self._item.ident)
        comment_type = [FILE_COMMENT_RECORD_TYPE]

        book = self.get_book(self._bank.ident)
        form = book.get_comment_form_for_create(response.ident,
                                                comment_type)

        form.set_text('Good job')
        form.set_file(DataInputStream(self.test_file1),
                      asset_name='my comments')

        new_comment = book.create_comment(form)

        data = new_comment.object_map

        self.assertEqual(
            data['text']['text'],
            'Good job'
        )

        self.assertIn(
            'fileId',
            data
        )

        repo = self.get_repo(book.ident)
        asset = repo.get_asset(Id(data['fileId']['assetId']))

        self.assertIn(
            '/stream',
            asset.object_map['assetContents'][0]['url']
        )

    def test_can_send_text_only_comment(self):
        first_section = self._bank.get_first_assessment_section(self._taken.ident)
        response = self._bank.get_response(first_section.ident, self._item.ident)
        comment_type = []

        book = self.get_book(self._bank.ident)
        form = book.get_comment_form_for_create(response.ident,
                                                comment_type)

        form.set_text('Good job')

        new_comment = book.create_comment(form)

        data = new_comment.object_map

        self.assertEqual(
            data['text']['text'],
            'Good job'
        )

        self.assertNotIn(
            'fileId',
            data
        )

    def test_can_get_all_comments_for_response(self):
        self.send_comment(with_files=True)
        book = self.get_book(self._bank.ident)

        # should probably use something like get_comments_for_reference(), but
        # for now, just loop through...
        comments = book.get_comments()

        first_section = self._bank.get_first_assessment_section(self._taken.ident)
        response = self._bank.get_response(first_section.ident, self._item.ident)

        comments = [comment for comment in comments if comment.get_reference_id() == response.ident]

        self.assertEqual(
            len(comments),
            1
        )

    def test_learners_can_view_comments(self):
        self.send_comment(with_files=True)

        self.req = self.student_req

        book = self.get_book(self._bank.ident)

        # should probably use something like get_comments_for_reference(), but
        # for now, just loop through...
        comments = book.get_comments()

        first_section = self._bank.get_first_assessment_section(self._taken.ident)
        response = self._bank.get_response(first_section.ident, self._item.ident)

        comments = [comment for comment in comments if comment.get_reference_id() == response.ident]

        self.assertEqual(
            len(comments),
            1
        )
