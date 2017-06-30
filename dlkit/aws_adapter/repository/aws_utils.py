"""Utilies for dealing with amazon web services"""
from __future__ import unicode_literals

import boto3
import datetime
import rsa

from botocore.signers import CloudFrontSigner
from dlkit.aws_adapter import AWS_CLIENT


def get_aws_s3_handle(config_map):
    """Convenience function for getting AWS S3 objects

    Added by cjshaw@mit.edu, Jan 9, 2015
    Added to aws_adapter build by birdland@mit.edu, Jan 25, 2015, and
    added support for Configuration
    May 25, 2017: Switch to boto3

    """
    url = 'https://' + config_map['s3_bucket'] + '.s3.amazonaws.com'
    if not AWS_CLIENT.is_aws_s3_client_set():
        client = boto3.client(
            's3',
            aws_access_key_id=config_map['put_public_key'],
            aws_secret_access_key=config_map['put_private_key']
        )
        AWS_CLIENT.set_aws_s3_client(client)
    else:
        client = AWS_CLIENT.s3
    return client, url


def get_signed_url(url, config_map):
    """ Convenience function for getting cloudfront signed URL given a saved URL

    cjshaw, Jan 7, 2015

    Follows:
        http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/
            private-content-creating-signed-url-canned-policy.html#private-
            content-creating-signed-url-canned-policy-procedure
        http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/
            PrivateContent.html
        http://boto.readthedocs.org/en/latest/ref/cloudfront.html

    May 25, 2017: Switch to boto3

    """
    # From https://stackoverflow.com/a/34322915
    def rsa_signer(message):
        private_key = open(config_map['cloudfront_private_key_file'], 'r').read()
        return rsa.sign(
            message,
            rsa.PrivateKey.load_pkcs1(private_key.encode('utf8')),
            'SHA-1')  # CloudFront requires SHA-1 hash

    if any(config_map[key] == '' for key in ['s3_bucket', 'cloudfront_distro',
                                             'cloudfront_private_key_file', 'cloudfront_keypair_id']):
        # This is a test configuration
        return 'You are missing S3 and CF configs: https:///?Expires=X&Signature=X&Key-Pair-Id='

    expires = datetime.datetime.utcnow() + datetime.timedelta(days=7)
    s3_bucket = config_map['s3_bucket']

    url = url.replace(s3_bucket + '.s3.amazonaws.com', config_map['cloudfront_distro'])

    if not AWS_CLIENT.is_aws_cf_client_set():
        cf_signer = CloudFrontSigner(
            config_map['cloudfront_keypair_id'],
            rsa_signer
        )
        AWS_CLIENT.set_aws_cf_client(cf_signer)
    else:
        cf_signer = AWS_CLIENT.cf
    signed_url = cf_signer.generate_presigned_url(
        url,
        date_less_than=expires)
    return signed_url


def remove_file(config_map, file_key):
    """Convenience function for removing objects from AWS S3

    Added by cjshaw@mit.edu, Apr 28, 2015
    May 25, 2017: Switch to boto3

    """
    # for boto3, need to remove any leading /
    if file_key[0] == '/':
        file_key = file_key[1::]
    client = boto3.client(
        's3',
        aws_access_key_id=config_map['put_public_key'],
        aws_secret_access_key=config_map['put_private_key']
    )
    client.delete_object(
        Bucket=config_map['s3_bucket'],
        Key=file_key
    )
