# import boto
#
# from boto.s3.key import Key
import boto3

from botocore.exceptions import ClientError

import dlkit.runtime.configs
from dlkit.runtime.primordium import DataInputStream, Type, Id, DateTime
from dlkit.runtime.configs import S3_TEST_BUCKET, S3_TEST_PUBLIC_KEY,\
    S3_TEST_PRIVATE_KEY, CLOUDFRONT_TEST_DISTRO,\
    CLOUDFRONT_SIGNING_KEYPAIR_ID
from dlkit.runtime import RUNTIME, PROXY_SESSION

from .utilities.testing import DLKitTestCase, TEST_REPOSITORY_GENUS


class AWSAdapterTests(DLKitTestCase):
    def _get_aws_manager(self, manager_type):
        condition = PROXY_SESSION.get_proxy_condition()
        condition.set_http_request(self.req)
        proxy = PROXY_SESSION.get_proxy(condition)
        return RUNTIME.get_service_manager(manager_type.upper(),
                                           implementation='TEST_SERVICE_AWS',
                                           proxy=proxy)

    def _get_test_repository(self):
        rm = self._get_aws_manager('repository')
        querier = rm.get_repository_query()
        querier.match_genus_type(TEST_REPOSITORY_GENUS, True)
        repo = next(rm.get_repositories_by_query(querier))
        return rm.get_repository(repo.ident)  # to make sure we get a services repository

    def create_asset_with_content(self):
        form = self._repo.get_asset_form_for_create([])

        form.display_name = 'My new asset'
        form.description = 'Asset container for'

        new_asset = self._repo.create_asset(form)

        asset_content_types = []
        try:
            config = self._repo._osid_object._runtime.get_configuration()
            parameter_id = Id('parameter:assetContentRecordTypeForFiles@json')
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

    def is_cloudfront_url(self, _url):
        self.assertIn(
            'https://{0}/'.format(CLOUDFRONT_TEST_DISTRO),
            _url
        )

        expected_params = ['?Expires=',
                           '&Signature=',
                           '&Key-Pair-Id={0}'.format(CLOUDFRONT_SIGNING_KEYPAIR_ID)]

        for param in expected_params:
            self.assertIn(
                param,
                _url
            )

    def s3_file_exists(self, key):
        client = boto3.client(
            's3',
            aws_access_key_id=S3_TEST_PUBLIC_KEY,
            aws_secret_access_key=S3_TEST_PRIVATE_KEY
        )
        try:
            client.get_object(
                Bucket=S3_TEST_BUCKET,
                Key=key
            )
        except ClientError as ex:
            if ex.response['Error']['Code'] == 'NoSuchKey':
                return False
            raise ex
        return True

    def setUp(self):
        super(AWSAdapterTests, self).setUp()

        self._repo = self._get_test_repository()
        self._asset = self.create_asset_with_content()

    def tearDown(self):
        """
        Remove the test user from all groups in Membership
        Start from the smallest groupId because need to
        remove "parental" roles like for DepartmentAdmin / DepartmentOfficer
        """
        super(AWSAdapterTests, self).tearDown()

    def test_repository_assets_put_into_s3(self):
        expected_filekey = self._repo.ident.identifier + '/' + self.test_file1.name.split('/')[-1]
        self.assertTrue(self.s3_file_exists(expected_filekey))

    def test_repository_assets_return_cloudfront_url_when_queried(self):
        asset_content = next(self._asset.get_asset_contents())
        url = asset_content.get_url()
        self.is_cloudfront_url(url)

    def test_s3_files_deleted_when_asset_content_deleted(self):
        expected_filekey = self._repo.ident.identifier + '/' + self.test_file1.name.split('/')[-1]
        self.assertTrue(self.s3_file_exists(expected_filekey))

        asset_content = next(self._asset.get_asset_contents())

        self._repo.delete_asset_content(asset_content.ident)
        self.assertFalse(self.s3_file_exists(expected_filekey))
