# let's make sure Filesystem adapter works -- files get sent there
import os

from dlkit.abstract_osid.osid import errors
from dlkit.primordium.locale.types import string as String
from dlkit.records.registry import COMPOSITION_GENUS_TYPES
from dlkit.runtime import configs
from dlkit.runtime.primordium import DataInputStream, Type, Id, DateTime

from .utilities.testing import DLKitTestCase


WORDIGNORECASE_STRING_MATCH_TYPE = Type(**String.get_type_data('WORDIGNORECASE'))

EDX_COMPOSITION_RECORD_TYPE = Type(**{
    'authority': 'EDX.ORG',
    'namespace': 'repository-composition',
    'identifier': 'edx-composition',
    'display_name': 'edX Composition',
    'display_label': 'edX Composition',
    'description': 'Wrapper for things like chapter / vertical / split_test',
    'domain': 'repository.Composition'
})

ENCLOSURE_RECORD_TYPE = Type(
    **{'identifier': 'enclosure',
       'namespace': 'osid-object',
       'authority': 'ODL.MIT.EDU'})

ENCLOSED_ASSESSMENT_TYPE = Type(
    **{'identifier': 'Assessment',
       'namespace': 'assessment',
       'authority': 'OSID.ORG'})


class FilesystemAdapterTests(DLKitTestCase):
    def create_asset_with_content(self):
        form = self._repo.get_asset_form_for_create([])

        form.display_name = 'My new asset'
        form.description = 'Asset container for'

        new_asset = self._repo.create_asset(form)

        asset_content_types = []
        try:
            config = self._repo._osid_object._runtime.get_configuration()
            parameter_id = Id('parameter:assetContentRecordTypeForFiles@mongo')
            asset_content_types.append(
                config.get_value_by_parameter(parameter_id).get_type_value())
        except AttributeError:
            pass

        content_form = self._repo.get_asset_content_form_for_create(new_asset.ident,
                                                                    asset_content_types)

        blob = DataInputStream(self.test_file1)

        content_form.set_data(blob)

        self._repo.create_asset_content(content_form)

        asset = self._repo.get_asset(new_asset.ident)
        return asset

    def file_exists(self, filepath):
        # check on the filesystem that the file is there
        return os.path.isfile(filepath)

    def get_asset_content_full_path(self, asset):
        # For these tests, assume first assetContent
        ac = next(asset.get_asset_contents())
        # this is super hacky
        return os.path.join(ac._config_map['data_store_full_path'],
                            ac._my_map['url'])

    def setUp(self):
        super(FilesystemAdapterTests, self).setUp()

        self._repo = self._get_test_repository()
        self._asset = self.create_asset_with_content()

    def tearDown(self):
        """
        Remove the test user from all groups in Membership
        Start from the smallest groupId because need to
        remove "parental" roles like for DepartmentAdmin / DepartmentOfficer
        """
        super(FilesystemAdapterTests, self).tearDown()

    def test_repository_assets_put_onto_disk(self):
        filepath = self.get_asset_content_full_path(self._asset)
        self.assertTrue(self.file_exists(filepath))

    def test_repository_assets_return_cloudfront_url_when_queried(self):
        asset_content = next(self._asset.get_asset_contents())
        url = asset_content.get_url()
        self.is_streamable_url(url)

    def test_files_deleted_when_asset_content_deleted(self):
        filepath = self.get_asset_content_full_path(self._asset)
        self.assertTrue(self.file_exists(filepath))

        asset_content = next(self._asset.get_asset_contents())

        self._repo.delete_asset_content(asset_content.ident)
        self.assertFalse(self.file_exists(filepath))


class AssetContentTests(DLKitTestCase):
    def create_asset_with_content(self):
        form = self._repo.get_asset_form_for_create([])

        form.display_name = 'My new asset'
        form.description = 'Asset container for'

        new_asset = self._repo.create_asset(form)

        asset_content_types = []
        try:
            config = self._repo._osid_object._runtime.get_configuration()
            parameter_id = Id('parameter:assetContentRecordTypeForFiles@mongo')
            asset_content_types.append(
                config.get_value_by_parameter(parameter_id).get_type_value())
        except AttributeError:
            pass

        content_form = self._repo.get_asset_content_form_for_create(new_asset.ident,
                                                                    asset_content_types)

        blob = DataInputStream(self.test_file1)
        content_form.display_name = "test_file_1"
        content_form.set_data(blob)
        content_form.set_genus_type(self._test_genus_type)

        self._repo.create_asset_content(content_form)

        asset = self._repo.get_asset(new_asset.ident)
        return asset

    def setUp(self):
        super(AssetContentTests, self).setUp()
        self._test_genus_type = Type('asset-content-genus-type%3Avtt%40ODL.MIT.EDU')
        self._repo = self._get_test_repository()
        self._asset = self.create_asset_with_content()

    def tearDown(self):
        """
        Remove the test user from all groups in Membership
        Start from the smallest groupId because need to
        remove "parental" roles like for DepartmentAdmin / DepartmentOfficer
        """
        super(AssetContentTests, self).tearDown()

    def test_can_get_asset_content_by_id(self):
        asset_content_id = self._asset.get_asset_contents().next().ident
        asset_content = self._repo.get_asset_content(asset_content_id)
        self.assertEqual(
            str(asset_content.ident),
            str(asset_content_id)
        )

    def test_can_query_asset_contents(self):
        querier = self._repo.get_asset_content_query()
        querier.match_display_name('test_file_1', match=True)
        asset_contents = self._repo.get_asset_contents_by_query(querier)
        self.assertEqual(
            asset_contents.available(),
            1
        )
        self.assertEqual(
            str(asset_contents.next().ident),
            str(self._asset.get_asset_contents().next().ident)
        )

    def test_can_get_null_results_from_asset_content_query(self):
        querier = self._repo.get_asset_content_query()
        querier.match_display_name('foo', match=True)
        asset_contents = self._repo.get_asset_contents_by_query(querier)
        self.assertEqual(
            asset_contents.available(),
            0
        )

    def test_can_get_asset_contents_by_ids(self):
        asset_content_id = self._asset.get_asset_contents().next().ident
        asset_contents = self._repo.get_asset_contents_by_ids([asset_content_id])
        self.assertEqual(asset_contents.available(), 1)
        self.assertEqual(
            str(asset_contents.next().ident),
            str(asset_content_id)
        )

    def test_can_get_null_results_of_asset_contents_by_ids(self):
        asset_contents = self._repo.get_asset_contents_by_ids([Id('foo%3A111111111111111111111111%40ODL.MIT.EDU')])
        self.assertEqual(asset_contents.available(), 0)

    def test_can_get_asset_contents_by_genus_type(self):
        asset_content_id = self._asset.get_asset_contents().next().ident
        asset_contents = self._repo.get_asset_contents_by_genus_type(self._test_genus_type)
        self.assertEqual(asset_contents.available(), 1)
        self.assertEqual(
            str(asset_contents.next().ident),
            str(asset_content_id)
        )

    def test_can_get_null_results_of_asset_contents_by_genus_type(self):
        asset_contents = self._repo.get_asset_contents_by_genus_type(Type('foo%3A1%40ODL.MIT.EDU'))
        self.assertEqual(asset_contents.available(), 0)

    def test_can_get_asset_contents_by_genus_type_and_asset(self):
        asset_content_id = self._asset.get_asset_contents().next().ident
        asset_contents = self._repo.get_asset_contents_by_genus_type_for_asset(self._test_genus_type,
                                                                               self._asset.ident)
        self.assertEqual(asset_contents.available(), 1)
        self.assertEqual(
            str(asset_contents.next().ident),
            str(asset_content_id)
        )

    def test_can_get_null_results_of_asset_contents_by_genus_type_and_asset(self):
        asset_contents = self._repo.get_asset_contents_by_genus_type_for_asset(Type('foo%3A1%40ODL.MIT.EDU'),
                                                                               self._asset.ident)
        self.assertEqual(asset_contents.available(), 0)

    def test_can_get_asset_contents_for_asset(self):
        asset_content_id = self._asset.get_asset_contents().next().ident
        asset_contents = self._repo.get_asset_contents_for_asset(self._asset.ident)
        self.assertEqual(asset_contents.available(), 1)
        self.assertEqual(
            str(asset_contents.next().ident),
            str(asset_content_id)
        )


class CompositionTests(DLKitTestCase):
    def create_asset_with_content(self):
        form = self._repo.get_asset_form_for_create([])

        form.display_name = 'My new asset'
        form.description = 'Asset container for'

        new_asset = self._repo.create_asset(form)

        asset_content_types = []
        try:
            config = self._repo._osid_object._runtime.get_configuration()
            parameter_id = Id('parameter:assetContentRecordTypeForFiles@mongo')
            asset_content_types.append(
                config.get_value_by_parameter(parameter_id).get_type_value())
        except AttributeError:
            pass

        content_form = self._repo.get_asset_content_form_for_create(new_asset.ident,
                                                                    asset_content_types)

        blob = DataInputStream(self.test_file1)

        content_form.set_data(blob)

        self._repo.create_asset_content(content_form)

        asset = self._repo.get_asset(new_asset.ident)
        return asset

    def setup_composition(self, repository_id):
        repo = self.get_repo(repository_id)
        asset_form = repo.get_asset_form_for_create([])
        asset_form.display_name = 'test'
        asset_form.description = 'ing'
        new_asset = repo.create_asset(asset_form)

        # now add the new data
        asset_content_type_list = []
        try:
            config = repo._osid_object._runtime.get_configuration()
            parameter_id = Id('parameter:assetContentRecordTypeForFiles@mongo')
            asset_content_type_list.append(
                config.get_value_by_parameter(parameter_id).get_type_value())
        except AttributeError:
            pass

        asset_content_form = repo.get_asset_content_form_for_create(new_asset.ident,
                                                                    asset_content_type_list)

        asset_content_form.set_data(DataInputStream(self.test_file1))

        repo.create_asset_content(asset_content_form)

        form = repo.get_composition_form_for_create([])
        form.display_name = 'my test composition'
        form.description = 'foobar'
        form.set_children([new_asset.ident])
        composition = repo.create_composition(form)
        return composition.object_map

    def setUp(self):
        super(CompositionTests, self).setUp()

        self._repo = self._get_test_repository()
        self._asset = self.create_asset_with_content()

    def tearDown(self):
        """
        Remove the test user from all groups in Membership
        Start from the smallest groupId because need to
        remove "parental" roles like for DepartmentAdmin / DepartmentOfficer
        """
        super(CompositionTests, self).tearDown()

    def test_can_create_composition_with_asset_child(self):
        composition_map = self.setup_composition(self._repo.ident)

        asset_child_id = composition_map['childIds'][0]

        asset = self._repo.get_asset(Id(asset_child_id))

        self.assertEqual(
            asset.get_asset_contents().available(),
            1
        )

        self.is_streamable_url(asset.get_asset_contents().next().get_url())


class EdXCompositionTests(CompositionTests):
    def create_composition_of_type(self, comp_type):
        form = self._repo.get_composition_form_for_create([EDX_COMPOSITION_RECORD_TYPE])
        form.display_name = 'my test composition'
        form.description = 'foobar'
        form.set_genus_type(Type(**COMPOSITION_GENUS_TYPES[comp_type]))
        return self._repo.create_composition(form)

    def setUp(self):
        super(EdXCompositionTests, self).setUp()

    def tearDown(self):
        """
        Remove the test user from all groups in Membership
        Start from the smallest groupId because need to
        remove "parental" roles like for DepartmentAdmin / DepartmentOfficer
        """
        super(EdXCompositionTests, self).tearDown()

    def test_can_create_edx_composition_type(self):
        form = self._repo.get_composition_form_for_create([EDX_COMPOSITION_RECORD_TYPE])
        form.display_name = 'my test composition'
        form.description = 'foobar'
        composition = self._repo.create_composition(form)

        self.assertEqual(
            [str(EDX_COMPOSITION_RECORD_TYPE)],
            composition.object_map['recordTypeIds']
        )

    def test_can_set_start_date_for_chapters_and_sequentials(self):
        test_cases = ['chapter', 'sequential']
        start_date = DateTime(year=2015, day=1, month=1)
        for case in test_cases:
            try:
                comp = self.create_composition_of_type(case)
                form = self._repo.get_composition_form_for_update(comp.ident)
                form.set_start_date(start_date)
                self._repo.update_composition(form)

                form = self._repo.get_composition_form_for_update(comp.ident)
                form.clear_start_date()
                self._repo.update_composition(form)
            except errors.IllegalState:
                self.fail('This should have worked.')
            else:
                pass

    def test_cannot_set_start_date_for_courses_split_tests_and_verticals(self):
        test_cases = ['course', 'split_test', 'vertical']
        start_date = DateTime(year=2015, day=1, month=1)
        for case in test_cases:
            comp = self.create_composition_of_type(case)

            try:
                form = self._repo.get_composition_form_for_update(comp.ident)
                form.set_start_date(start_date)
                self._repo.update_composition(form)
            except errors.IllegalState:
                pass
            else:
                self.fail('This should have raised IllegalState().')

            try:
                form = self._repo.get_composition_form_for_update(comp.ident)
                form.clear_start_date()
                self._repo.update_composition(form)
            except errors.IllegalState:
                pass
            else:
                self.fail('This should have raised IllegalState().')

    def test_can_get_start_date_for_chapters_and_sequentials(self):
        test_cases = ['chapter', 'sequential']
        start_date = DateTime(year=2015, day=1, month=1)
        for case in test_cases:
            comp = self.create_composition_of_type(case)
            form = self._repo.get_composition_form_for_update(comp.ident)
            form.set_start_date(start_date)
            comp = self._repo.update_composition(form)

            try:
                self.assertEqual(
                    str(start_date),
                    str(comp.start_date)
                )
            except errors.IllegalState:
                self.fail('This should have worked.')
            else:
                pass

    def test_cannot_get_start_date_for_courses_split_tests_and_verticals(self):
        test_cases = ['course', 'split_test', 'vertical']
        start_date = DateTime(year=2015, day=1, month=1)
        for case in test_cases:
            comp = self.create_composition_of_type(case)

            try:
                self.assertEqual(
                    str(start_date),
                    str(comp.start_date)
                )
            except errors.IllegalState:
                pass
            else:
                self.fail('This should have thrown IllegalState().')

    def test_can_set_filename_for_non_course_compositions(self):
        test_cases = ['chapter', 'sequential', 'split_test', 'vertical']
        for case in test_cases:
            try:
                comp = self.create_composition_of_type(case)
                form = self._repo.get_composition_form_for_update(comp.ident)
                form.set_file_name('file for ' + case)
                comp = self._repo.update_composition(form)
                self.assertEqual(
                    comp.filename.text,
                    'file for ' + case
                )
            except errors.IllegalState:
                self.fail('This should have worked.')
            else:
                pass

    def test_course_has_default_filename(self):
        test_cases = ['course']
        for case in test_cases:
            try:
                comp = self.create_composition_of_type(case)
                form = self._repo.get_composition_form_for_update(comp.ident)
                form.set_file_name('file for ' + case)
                comp = self._repo.update_composition(form)
                self.assertEqual(
                    comp.filename.text,
                    'course.xml'
                )
            except errors.IllegalState:
                self.fail('This should have worked.')
            else:
                pass

    def test_can_set_visible_to_students_for_chapters_and_sequentials(self):
        test_cases = ['chapter', 'sequential']
        for case in test_cases:
            try:
                comp = self.create_composition_of_type(case)

                self.assertTrue(comp.visible_to_students)

                form = self._repo.get_composition_form_for_update(comp.ident)
                form.set_visible_to_students(False)
                comp = self._repo.update_composition(form)

                self.assertFalse(comp.visible_to_students)

                form = self._repo.get_composition_form_for_update(comp.ident)
                form.clear_visible_to_students()
                comp = self._repo.update_composition(form)

                self.assertTrue(comp.visible_to_students)
            except errors.IllegalState:
                self.fail('This should have worked.')
            else:
                pass

    def test_cannot_set_visible_to_students_for_courses_split_tests_and_verticals(self):
        test_cases = ['course', 'split_test', 'vertical']
        for case in test_cases:
            comp = self.create_composition_of_type(case)
            try:
                self.assertTrue(comp._my_map['visibleToStudents'])

                form = self._repo.get_composition_form_for_update(comp.ident)
                form.set_visible_to_students(False)
                comp = self._repo.update_composition(form)
            except errors.IllegalState:
                comp = self._repo.get_composition(comp.ident)
                self.assertTrue(comp._my_map['visibleToStudents'])
            else:
                self.fail('This should have thrown IllegalState().')

            try:
                self.assertTrue(comp._my_map['visibleToStudents'])

                form = self._repo.get_composition_form_for_update(comp.ident)
                form.clear_visible_to_students()
                comp = self._repo.update_composition(form)
            except errors.IllegalState:
                comp = self._repo.get_composition(comp.ident)
                self.assertTrue(comp._my_map['visibleToStudents'])
            else:
                self.fail('This should have thrown IllegalState().')

            try:
                self.assertTrue(comp.visible_to_students)
            except errors.IllegalState:
                pass
            else:
                self.fail('This should have thrown IllegalState().')

    def test_can_set_draft_on_verticals(self):
        test_cases = ['vertical']
        for case in test_cases:
            try:
                comp = self.create_composition_of_type(case)

                self.assertFalse(comp.draft)

                form = self._repo.get_composition_form_for_update(comp.ident)
                form.set_draft(True)
                comp = self._repo.update_composition(form)

                self.assertTrue(comp.draft)

                form = self._repo.get_composition_form_for_update(comp.ident)
                form.clear_draft()
                comp = self._repo.update_composition(form)

                self.assertFalse(comp.draft)
            except errors.IllegalState:
                self.fail('This should have worked.')
            else:
                pass

    def test_cannot_set_draft_on_non_verticals(self):
        test_cases = ['course', 'chapter', 'sequential', 'split_test']
        for case in test_cases:
            comp = self.create_composition_of_type(case)
            try:
                self.assertFalse(comp._my_map['draft'])

                form = self._repo.get_composition_form_for_update(comp.ident)
                form.set_draft(True)
                comp = self._repo.update_composition(form)
            except errors.IllegalState:
                comp = self._repo.get_composition(comp.ident)
                self.assertFalse(comp._my_map['draft'])
            else:
                self.fail('This should have thrown IllegalState().')

            try:
                self.assertFalse(comp._my_map['draft'])

                form = self._repo.get_composition_form_for_update(comp.ident)
                form.clear_draft()
                comp = self._repo.update_composition(form)
            except errors.IllegalState:
                comp = self._repo.get_composition(comp.ident)
                self.assertFalse(comp._my_map['draft'])
            else:
                self.fail('This should have thrown IllegalState().')

            try:
                comp.draft
            except errors.IllegalState:
                self.assertFalse(comp._my_map['draft'])
            else:
                self.fail('This should have thrown IllegalState().')


class EnclosureTests(DLKitTestCase):
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

        item = bank.get_item(new_item.ident)
        return item

    def create_asset_with_content(self):
        form = self._repo.get_asset_form_for_create([])

        form.display_name = 'My new asset'
        form.description = 'Asset container for'

        new_asset = self._repo.create_asset(form)

        asset_content_types = []
        try:
            config = self._repo._osid_object._runtime.get_configuration()
            parameter_id = Id('parameter:assetContentRecordTypeForFiles@mongo')
            asset_content_types.append(
                config.get_value_by_parameter(parameter_id).get_type_value())
        except AttributeError:
            pass

        content_form = self._repo.get_asset_content_form_for_create(new_asset.ident,
                                                                    asset_content_types)

        blob = DataInputStream(self.test_file1)

        content_form.set_data(blob)

        self._repo.create_asset_content(content_form)

        asset = self._repo.get_asset(new_asset.ident)
        return asset

    def setup_composition(self, repository_id):
        repo = self.get_repo(repository_id)
        asset_form = repo.get_asset_form_for_create([])
        asset_form.display_name = 'test'
        asset_form.description = 'ing'
        new_asset = repo.create_asset(asset_form)

        # now add the new data
        asset_content_type_list = []
        try:
            config = repo._osid_object._runtime.get_configuration()
            parameter_id = Id('parameter:assetContentRecordTypeForFiles@mongo')
            asset_content_type_list.append(
                config.get_value_by_parameter(parameter_id).get_type_value())
        except AttributeError:
            pass

        asset_content_form = repo.get_asset_content_form_for_create(new_asset.ident,
                                                                    asset_content_type_list)

        asset_content_form.set_data(DataInputStream(self.test_file1))

        repo.create_asset_content(asset_content_form)

        form = repo.get_composition_form_for_create([])
        form.display_name = 'my test composition'
        form.description = 'foobar'
        form.set_children([new_asset.ident])
        composition = repo.create_composition(form)
        return composition.object_map

    def setUp(self):
        super(EnclosureTests, self).setUp()

        self._repo = self._get_test_repository()
        self._bank = self._get_test_bank()
        self._item = self.add_item(self._bank)
        self._assessment = self.create_assessment_for_items(self._bank, [self._item])
        self._asset = self.create_asset_with_content()

    def tearDown(self):
        """
        Remove the test user from all groups in Membership
        Start from the smallest groupId because need to
        remove "parental" roles like for DepartmentAdmin / DepartmentOfficer
        """
        super(EnclosureTests, self).tearDown()

    def test_create_enclosed_assessment(self):
        """Tests creating an assessment enclosed in an asset"""
        create_form = self._repo.get_asset_form_for_create([ENCLOSURE_RECORD_TYPE])
        create_form.set_enclosed_object(self._assessment.ident)
        with self.assertRaises(errors.NoAccess):
            create_form.set_display_name('This should fail')
        with self.assertRaises(errors.NoAccess):
            create_form.set_description('This should also fail')
        with self.assertRaises(errors.NoAccess):
            create_form.set_genus_type(ENCLOSURE_RECORD_TYPE)
        asset = self._repo.create_asset(create_form)
        self.assertEqual(asset.get_display_name().text, self._assessment.get_display_name().text)
        self.assertEqual(asset.get_description().text, self._assessment.get_description().text)
        self.assertEqual(str(asset.get_genus_type()), str(ENCLOSED_ASSESSMENT_TYPE))

    # def test_update_asset_with_assessment(self):
    #     """
    #     Tests silently creating an assessment enclosed in an asset through update
    #
    #     And that if one already exists, that we get it instead.
    #
    #     """
    #     update_form = self._repo.get_asset_form_for_update(self._assessment.ident)
    #     update_form.set_title('This is the Asset Title')
    #     updated_asset = self._repo.update_asset(update_form)
    #     updated_asset_assessment_id = updated_asset.enclosed_object_id
    #     self.assertEqual(updated_asset.title.text, 'This is the Asset Title')
    #     new_update_form = self._repo.get_asset_form_for_update(self._assessment.ident)
    #     new_updated_asset = self._repo.update_asset(new_update_form)
    #     self.assertEqual(new_updated_asset.enclosed_object_id, updated_asset_assessment_id)
    #     self.assertEqual(updated_asset.title.text, 'This is the Asset Title')

    def test_assessment_asset_composition(self):
        """Tests silently creating an enclosure through asset composition design."""

        create_form = self._repo.get_composition_form_for_create([])
        create_form.display_name = 'Test Composition'
        create_form.description = 'Test Composition for Enclosure tests'
        composition = self._repo.create_composition(create_form)
        self._repo.add_asset(self._assessment.ident, composition.ident)
        asset_list = self._repo.get_composition_assets(composition.ident)
        self.assertEqual(asset_list.available(), 1)
        self.assertEqual(asset_list.next().display_name.text, 'a test assessment')


class SearchAssetPaginationTests(DLKitTestCase):
    def create_asset(self, name="my new asset"):
        form = self._repo.get_asset_form_for_create([])

        form.display_name = str(name)
        form.description = 'Test asset'

        return self._repo.create_asset(form)

    def setUp(self):
        super(SearchAssetPaginationTests, self).setUp()

        self._repo = self._get_test_repository()
        for i in range(1, 20):
            self.create_asset(name=str(i))

    def tearDown(self):
        """
        Remove the test user from all groups in Membership
        Start from the smallest groupId because need to
        remove "parental" roles like for DepartmentAdmin / DepartmentOfficer
        """
        super(SearchAssetPaginationTests, self).tearDown()

    def test_specifying_start_and_end_returns_right_objects(self):
        querier = self._repo.get_asset_query()
        querier.match_keyword('1', WORDIGNORECASE_STRING_MATCH_TYPE, True)

        searcher = self._repo.get_asset_search()
        searcher.limit_result_set(1, 5)  # should return 5 results, numbered 1, 10, 11, 12, 13

        results = self._repo.get_assets_by_search(querier, searcher)
        self.assertEqual(
            results.get_result_size(),
            5
        )
        assets_found = results.get_assets()
        self.assertEqual(
            assets_found.available(),
            5
        )

        expected_names = ['1', '10', '11', '12', '13']
        for expected_name in expected_names:
            self.assertEqual(
                assets_found.next().display_name.text,
                expected_name
            )

    def test_null_start_and_end_throws_exception(self):
        searcher = self._repo.get_asset_search()

        self.assertRaises(errors.NullArgument, searcher.limit_result_set, 1, None)
        self.assertRaises(errors.NullArgument, searcher.limit_result_set, None, 5)
        self.assertRaises(errors.NullArgument, searcher.limit_result_set, None, None)

    def test_end_less_than_start_throws_exception(self):
        searcher = self._repo.get_asset_search()

        self.assertRaises(errors.InvalidArgument, searcher.limit_result_set, 5, 1)

    def test_end_equal_to_start_throws_exception(self):
        searcher = self._repo.get_asset_search()

        self.assertRaises(errors.InvalidArgument, searcher.limit_result_set, 5, 5)

    def test_end_greater_than_total_docs_returns_everything(self):
        querier = self._repo.get_asset_query()
        querier.match_keyword('1', WORDIGNORECASE_STRING_MATCH_TYPE, True)

        searcher = self._repo.get_asset_search()
        searcher.limit_result_set(1, 25)  # should return 11 results, 1 + 10-19

        results = self._repo.get_assets_by_search(querier, searcher)
        assets_found = results.get_assets()
        self.assertEqual(
            assets_found.available(),
            11
        )

        expected_names = ['1', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19']
        for expected_name in expected_names:
            self.assertEqual(
                assets_found.next().display_name.text,
                expected_name
            )

    def test_can_search_within_an_id_list(self):
        querier = self._repo.get_asset_query()
        querier.match_keyword('1', WORDIGNORECASE_STRING_MATCH_TYPE, True)

        searcher = self._repo.get_asset_search()
        searcher.limit_result_set(1, 5)  # should return 5 results, numbered 1, 10, 11, 12, 13

        results = self._repo.get_assets_by_search(querier, searcher)
        self.assertEqual(
            results.get_result_size(),
            5
        )
        assets_found = results.get_assets()
        self.assertEqual(
            assets_found.available(),
            5
        )

        expected_names = ['1', '10', '11', '12', '13']
        new_id_to_search_on = []
        for expected_name in expected_names:
            if expected_name == '12':
                new_id_to_search_on.append(assets_found.next().ident)
            else:
                next(assets_found)

        querier = self._repo.get_asset_query()
        querier.match_keyword('2', WORDIGNORECASE_STRING_MATCH_TYPE, True)

        searcher = self._repo.get_asset_search()
        searcher.search_among_assets(new_id_to_search_on)

        results = self._repo.get_assets_by_search(querier, searcher)  # should only return "12", and not "2"
        self.assertEqual(
            results.get_result_size(),
            1
        )
        assets_found = results.get_assets()
        self.assertEqual(
            assets_found.available(),
            1
        )

        self.assertEqual(
            str(assets_found.next().ident),
            str(new_id_to_search_on[0])
        )


class SearchCompositionPaginationTests(DLKitTestCase):
    def create_composition(self, name="my new composition"):
        form = self._repo.get_composition_form_for_create([])

        form.display_name = str(name)
        form.description = 'Test composition'

        return self._repo.create_composition(form)

    def setUp(self):
        super(SearchCompositionPaginationTests, self).setUp()

        self._repo = self._get_test_repository()
        for i in range(1, 20):
            self.create_composition(name=str(i))

    def tearDown(self):
        """
        Remove the test user from all groups in Membership
        Start from the smallest groupId because need to
        remove "parental" roles like for DepartmentAdmin / DepartmentOfficer
        """
        super(SearchCompositionPaginationTests, self).tearDown()

    def test_specifying_start_and_end_returns_right_objects(self):
        querier = self._repo.get_composition_query()
        querier.match_keyword('1', WORDIGNORECASE_STRING_MATCH_TYPE, True)

        searcher = self._repo.get_composition_search()
        searcher.limit_result_set(1, 5)  # should return 5 results, numbered 1, 10, 11, 12, 13

        results = self._repo.get_compositions_by_search(querier, searcher)
        self.assertEqual(
            results.get_result_size(),
            5
        )
        compositions_found = results.get_compositions()
        self.assertEqual(
            compositions_found.available(),
            5
        )

        expected_names = ['1', '10', '11', '12', '13']
        for expected_name in expected_names:
            self.assertEqual(
                compositions_found.next().display_name.text,
                expected_name
            )

    def test_null_start_and_end_throws_exception(self):
        searcher = self._repo.get_composition_search()

        self.assertRaises(errors.NullArgument, searcher.limit_result_set, 1, None)
        self.assertRaises(errors.NullArgument, searcher.limit_result_set, None, 5)
        self.assertRaises(errors.NullArgument, searcher.limit_result_set, None, None)

    def test_end_less_than_start_throws_exception(self):
        searcher = self._repo.get_composition_search()

        self.assertRaises(errors.InvalidArgument, searcher.limit_result_set, 5, 1)

    def test_end_equal_to_start_throws_exception(self):
        searcher = self._repo.get_composition_search()

        self.assertRaises(errors.InvalidArgument, searcher.limit_result_set, 5, 5)

    def test_end_greater_than_total_docs_returns_everything(self):
        querier = self._repo.get_composition_query()
        querier.match_keyword('1', WORDIGNORECASE_STRING_MATCH_TYPE, True)

        searcher = self._repo.get_composition_search()
        searcher.limit_result_set(1, 25)  # should return 11 results, 1 + 10-19

        results = self._repo.get_compositions_by_search(querier, searcher)
        compositions_found = results.get_compositions()
        self.assertEqual(
            compositions_found.available(),
            11
        )

        expected_names = ['1', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19']
        for expected_name in expected_names:
            self.assertEqual(
                compositions_found.next().display_name.text,
                expected_name
            )

    def test_can_search_within_an_id_list(self):
        querier = self._repo.get_composition_query()
        querier.match_keyword('1', WORDIGNORECASE_STRING_MATCH_TYPE, True)

        searcher = self._repo.get_composition_search()
        searcher.limit_result_set(1, 5)  # should return 5 results, numbered 1, 10, 11, 12, 13

        results = self._repo.get_compositions_by_search(querier, searcher)
        self.assertEqual(
            results.get_result_size(),
            5
        )
        compositions_found = results.get_compositions()
        self.assertEqual(
            compositions_found.available(),
            5
        )

        expected_names = ['1', '10', '11', '12', '13']
        new_id_to_search_on = []
        for expected_name in expected_names:
            if expected_name == '12':
                new_id_to_search_on.append(compositions_found.next().ident)
            else:
                next(compositions_found)

        querier = self._repo.get_composition_query()
        querier.match_keyword('2', WORDIGNORECASE_STRING_MATCH_TYPE, True)

        searcher = self._repo.get_composition_search()
        searcher.search_among_compositions(new_id_to_search_on)

        results = self._repo.get_compositions_by_search(querier, searcher)  # should only return "12", and not "2"
        self.assertEqual(
            results.get_result_size(),
            1
        )
        compositions_found = results.get_compositions()
        self.assertEqual(
            compositions_found.available(),
            1
        )

        self.assertEqual(
            str(compositions_found.next().ident),
            str(new_id_to_search_on[0])
        )
