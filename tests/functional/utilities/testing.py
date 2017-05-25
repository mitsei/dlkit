"""useful utility methods"""
import os
import json
import envoy
import shutil
import unittest

from pymongo import MongoClient

from dlkit.runtime import RUNTIME, PROXY_SESSION
from dlkit.runtime.primordium import Id, DataInputStream, Type
from dlkit.runtime.proxy_example import SimpleRequest
from dlkit.records.registry import ASSESSMENT_RECORD_TYPES

import dlkit.runtime.configs

from .authorization import create_authz_superuser, add_user_authz_to_settings

SIMPLE_SEQUENCE_ASSESSMENT_RECORD = Type(**ASSESSMENT_RECORD_TYPES['simple-child-sequencing'])

PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))
ABS_PATH = os.path.abspath(os.path.join(PROJECT_PATH, os.pardir))
TEST_DATA_STORE_PATH = os.path.join(ABS_PATH, '../../test_datastore')

TEST_BANK_GENUS = Type('assessment.Bank%3Atest-catalog%40ODL.MIT.EDU')
TEST_BIN_GENUS = Type('resource.Bin%3Atest-catalog%40ODL.MIT.EDU')
TEST_GRADEBOOK_GENUS = Type('grading.Gradebook%3Atest-catalog%40ODL.MIT.EDU')
TEST_LOG_GENUS = Type('logging.Log%3Atest-catalog%40ODL.MIT.EDU')
TEST_OBJECTIVE_BANK_GENUS = Type('learning.ObjectiveBank%3Atest-catalog%40ODL.MIT.EDU')
TEST_REPOSITORY_GENUS = Type('repository.Repository%3Atest-catalog%40ODL.MIT.EDU')


class DLKitTestCase(unittest.TestCase):
    """
    """
    dbs_to_delete = ['test_dlkit_assessment',
                     'test_dlkit_assessment_authoring',
                     'test_dlkit_authorization',
                     'test_dlkit_commenting',
                     'test_dlkit_hierarchy',
                     'test_dlkit_id',
                     'test_dlkit_learning',
                     'test_dlkit_logging',
                     'test_dlkit_grading',
                     'test_dlkit_relationship',
                     'test_dlkit_repository',
                     'test_dlkit_resource']

    @staticmethod
    def _delete_database(db_name):
        MongoClient().drop_database(db_name)

    # def _pre_setup(self):
        # MockTestCase.setUp(self)

    # def _post_teardown(self):
        # MockTestCase.tearDown(self)

    def code(self, _req, _code):
        self.assertEqual(_req.status_code, _code)

    def create_assessment_for_items(self, bank, item_list):
        form = bank.get_assessment_form_for_create([SIMPLE_SEQUENCE_ASSESSMENT_RECORD])
        form.display_name = 'a test assessment'
        form.description = 'for testing with'
        new_assessment = bank.create_assessment(form)

        for item in item_list:
            bank.add_item(new_assessment.ident, item.ident)

        return new_assessment

    def _get_test_bank(self):
        am = get_manager(self.req, 'assessment')
        querier = am.get_bank_query()
        querier.match_genus_type(TEST_BANK_GENUS, True)
        bank = next(am.get_banks_by_query(querier))
        return am.get_bank(bank.ident)  # to make sure we get a services bank

    def create_new_bank(self, name="my new assessment bank"):
        am = get_manager(self.req, 'assessment')
        form = am.get_bank_form_for_create([])
        form.display_name = name
        form.description = 'for testing with'
        form.set_genus_type(TEST_BANK_GENUS)
        bank = am.create_bank(form)

        add_user_authz_to_settings('instructor',
                                   self.username,
                                   catalog_id=bank.ident)
        add_user_authz_to_settings('student',
                                   self.student_name,
                                   catalog_id=bank.ident)

        return bank

    def _get_test_bin(self):
        # assume the first one -- we're missing permissions to query?
        rm = get_manager(self.req, 'resource')
        return next(rm.get_bins())

    def create_new_bin(self):
        rm = get_manager(self.req, 'resource')
        form = rm.get_bin_form_for_create([])
        form.display_name = 'my new bin'
        form.description = 'for testing with'
        form.set_genus_type(TEST_BIN_GENUS)
        bin = rm.create_bin(form)

        add_user_authz_to_settings('instructor',
                                   self.username,
                                   catalog_id=bin.ident)
        add_user_authz_to_settings('student',
                                   self.student_name,
                                   catalog_id=bin.ident)

        return bin

    def _get_test_gradebook(self):
        # no gradebook query, so assume first gradebook
        gm = get_manager(self.req, 'grading')
        return next(gm.get_gradebooks())

    def create_new_gradebook(self):
        gm = get_manager(self.req, 'grading')
        form = gm.get_gradebook_form_for_create([])
        form.display_name = 'my new grade book'
        form.description = 'for testing with'
        form.set_genus_type(TEST_GRADEBOOK_GENUS)
        gradebook = gm.create_gradebook(form)

        add_user_authz_to_settings('instructor',
                                   self.username,
                                   catalog_id=gradebook.ident)
        add_user_authz_to_settings('student',
                                   self.student_name,
                                   catalog_id=gradebook.ident)

        return gradebook

    def _get_test_log(self):
        # we don't have log query enabled ... so assume first log found
        logm = get_manager(self.req, 'logging')
        return next(logm.get_logs())

    def create_new_log(self):
        logm = get_manager(self.req, 'logging')
        form = logm.get_log_form_for_create([])
        form.display_name = 'my new log'
        form.description = 'for testing with'
        form.set_genus_type(TEST_LOG_GENUS)
        log = logm.create_log(form)

        add_user_authz_to_settings('instructor',
                                   self.username,
                                   catalog_id=log.ident)
        add_user_authz_to_settings('student',
                                   self.student_name,
                                   catalog_id=log.ident)

        return log

    def _get_test_objective_bank(self):
        # get the first one because no objective bank query
        lm = get_manager(self.req, 'learning')
        return next(lm.get_objective_banks())

    def create_new_objective_bank(self):
        lm = get_manager(self.req, 'learning')
        form = lm.get_objective_bank_form_for_create([])
        form.display_name = 'my new objective bank'
        form.description = 'for testing with'
        form.set_genus_type(TEST_OBJECTIVE_BANK_GENUS)
        objective_bank = lm.create_objective_bank(form)

        add_user_authz_to_settings('instructor',
                                   self.username,
                                   catalog_id=objective_bank.ident)
        add_user_authz_to_settings('student',
                                   self.student_name,
                                   catalog_id=objective_bank.ident)

        return objective_bank

    def _get_test_repository(self):
        rm = get_manager(self.req, 'repository')
        querier = rm.get_repository_query()
        querier.match_genus_type(TEST_REPOSITORY_GENUS, True)
        repo = next(rm.get_repositories_by_query(querier))
        return rm.get_repository(repo.ident)  # to make sure we get a services repository

    def create_new_repo(self):
        rm = get_manager(self.req, 'repository')
        form = rm.get_repository_form_for_create([])
        form.display_name = 'my new repository'
        form.description = 'for testing with'
        form.set_genus_type(TEST_REPOSITORY_GENUS)
        repo = rm.create_repository(form)

        add_user_authz_to_settings('instructor',
                                   self.username,
                                   catalog_id=repo.ident)
        add_user_authz_to_settings('student',
                                   self.student_name,
                                   catalog_id=repo.ident)

        return repo

    def create_taken_for_items(self, bank, item_list):
        new_assessment = self.create_assessment_for_items(bank, item_list)

        form = bank.get_assessment_offered_form_for_create(new_assessment.ident, [])
        new_offered = bank.create_assessment_offered(form)

        form = bank.get_assessment_taken_form_for_create(new_offered.ident, [])
        taken = bank.create_assessment_taken(form)
        return taken

    def created(self, _req):
        self.code(_req, 201)

    def deleted(self, _req):
        self.code(_req, 204)

    def filename(self, file_):
        try:
            return file_.name.split('/')[-1].split('.')[0]
        except AttributeError:
            return file_.split('/')[-1].split('.')[0]

    def get_book(self, book_id):
        cm = get_manager(self.req, 'commenting')
        if is_string(book_id):
            book_id = Id(book_id)
        book = cm.get_book(book_id)

        add_user_authz_to_settings('instructor',
                                   self.username,
                                   catalog_id=book.ident)
        add_user_authz_to_settings('student',
                                   self.student_name,
                                   catalog_id=book.ident)

        return book

    def get_repo(self, repo_id):
        rm = get_manager(self.req, 'repository')
        if isinstance(repo_id, str):
            repo_id = Id(repo_id)
        repo = rm.get_repository(repo_id)

        add_user_authz_to_settings('instructor',
                                   self.username,
                                   catalog_id=repo.ident)
        add_user_authz_to_settings('student',
                                   self.student_name,
                                   catalog_id=repo.ident)

        return repo

    def is_streamable_url(self, _url):
        self.assertIn('/stream', _url)

    def json(self, _req):
        return json.loads(_req.content)

    def message(self, _req, _msg):
        self.assertIn(_msg, str(_req.content))

    def ok(self, _req):
        self.assertEqual(_req.status_code, 200)

    def setUp(self):
        for db in self.dbs_to_delete:
            self._delete_database(db)

        load_fixtures()
        self.url = '/api/v2/repository/'
        self.username = 'instructor@mit.edu'
        self.instructor_req = SimpleRequest(self.username)

        self.student_name = 'student@mit.edu'
        self.student_req = SimpleRequest(self.student_name)

        self.unauthenticated_req = SimpleRequest(self.username, authenticated=False)

        self.req = self.instructor_req

        self.test_file1 = open(ABS_PATH + '/files/test_file_1.txt', 'rb')
        self.test_file2 = open(ABS_PATH + '/files/test_file_2.txt', 'rb')
        if os.path.isdir(TEST_DATA_STORE_PATH):
            shutil.rmtree(TEST_DATA_STORE_PATH)

        if not os.path.isdir(TEST_DATA_STORE_PATH):
            os.makedirs(TEST_DATA_STORE_PATH)
        # add_user_authz_to_settings('instructor',
        #                            self.username)
        # add_user_authz_to_settings('student',
        #                            self.student_name)
        #
        # import pdb
        # pdb.set_trace()
        # self.create_new_bank()
        # self.create_new_bin()
        # self.create_new_gradebook()
        # self.create_new_log()
        # self.create_new_objective_bank()
        # self.create_new_repo()
        # pdb.set_trace()

    def setup_asset(self, repository_id):
        test_file = '/functional/files/test_file_1.txt'

        repo = self.get_repo(repository_id)
        asset_form = repo.get_asset_form_for_create([])
        asset_form.display_name = 'test'
        asset_form.description = 'ing'
        new_asset = repo.create_asset(asset_form)

        # now add the new data
        asset_content_type_list = []
        try:
            config = repo._runtime.get_configuration()
            parameter_id = Id('parameter:assetContentRecordTypeForFiles@json')
            asset_content_type_list.append(
                config.get_value_by_parameter(parameter_id).get_type_value())
        except AttributeError:
            pass

        asset_content_form = repo.get_asset_content_form_for_create(new_asset.ident,
                                                                    asset_content_type_list)

        self.default_asset_file = ABS_PATH + test_file
        with open(self.default_asset_file, 'r') as file_:
            asset_content_form.set_data(DataInputStream(file_))

        repo.create_asset_content(asset_content_form)

        new_asset = repo.get_asset(new_asset.ident)
        return new_asset.object_map

    def tearDown(self):
        for db in self.dbs_to_delete:
            self._delete_database(db)

        self.test_file1.close()
        self.test_file2.close()

        if os.path.isdir(TEST_DATA_STORE_PATH):
            shutil.rmtree(TEST_DATA_STORE_PATH)

    def updated(self, _req):
        self.code(_req, 202)


def is_string(string_):
    try:
        # python 2
        return isinstance(string_, basestring)
    except NameError:
        # python 3
        return isinstance(string_, str)


def load_fixtures():
    """use test settings, not the production settings"""
    # create a super-user who can create authorizations
    # create_authz_superuser()
    envoy.run('mongorestore --db test_dlkit_assessment --drop tests/functional/fixtures/test_dlkit_assessment')
    envoy.run('mongorestore --db test_dlkit_authorization --drop tests/functional/fixtures/test_dlkit_authorization')
    envoy.run('mongorestore --db test_dlkit_grading --drop tests/functional/fixtures/test_dlkit_grading')
    envoy.run('mongorestore --db test_dlkit_learning --drop tests/functional/fixtures/test_dlkit_learning')
    envoy.run('mongorestore --db test_dlkit_logging --drop tests/functional/fixtures/test_dlkit_logging')
    envoy.run('mongorestore --db test_dlkit_repository --drop tests/functional/fixtures/test_dlkit_repository')
    envoy.run('mongorestore --db test_dlkit_resource --drop tests/functional/fixtures/test_dlkit_resource')


def create_test_bank(test_instance):
    """
    helper method to create a test assessment bank
    """
    test_endpoint = '/api/v2/assessment/banks/'
    test_instance.login()
    payload = {
        "name": "a test bank",
        "description": "for testing"
    }
    req = test_instance.client.post(test_endpoint, payload, format='json')
    return json.loads(req.content)


def create_test_request(test_user):
    # from django.http import HttpRequest
    # from django.conf import settings
    # from django.utils.importlib import import_module
    # #http://stackoverflow.com/questions/16865947/django-httprequest-object-has-no-attribute-session
    # test_request = HttpRequest()
    # engine = import_module(settings.SESSION_ENGINE)
    # session_key = None
    # test_request.user = test_user
    # test_request.session = engine.SessionStore(session_key)
    # return test_request
    return SimpleRequest(username=test_user.username)


def get_agent_id(agent_id):
    """Not a great hack...depends too much on internal DLKit knowledge"""
    if '@mit.edu' not in agent_id:
        agent_id += '@mit.edu'
    test_request = SimpleRequest(agent_id)
    condition = PROXY_SESSION.get_proxy_condition()
    condition.set_http_request(test_request)
    proxy = PROXY_SESSION.get_proxy(condition)
    resm = RUNTIME.get_service_manager('RESOURCE',
                                       implementation='TEST_SERVICE_FUNCTIONAL',
                                       proxy=proxy)
    return resm.effective_agent_id


def get_manager(request, manager_type):
    condition = PROXY_SESSION.get_proxy_condition()
    condition.set_http_request(request)
    proxy = PROXY_SESSION.get_proxy(condition)
    return RUNTIME.get_service_manager(manager_type.upper(),
                                       implementation='TEST_SERVICE_FUNCTIONAL',
                                       proxy=proxy)


def serialize_date(date):
    return {
        'day': date.day,
        'month': date.month,
        'year': date.year,
        'hour': date.hour,
        'minute': date.minute,
        'second': date.second,
        'microsecond': date.microsecond
    }
