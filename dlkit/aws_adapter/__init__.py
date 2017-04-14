from dlkit.abstract_osid.osid.errors import OperationFailed


class AWSClientContainer(object):

    def __init__(self):
        self._aws_s3_client = None
        self._aws_cf_client = None

    def is_aws_s3_client_set(self):
        return bool(self._aws_s3_client)

    def set_aws_s3_client(self, aws_s3_client):
        # if self.is_aws_s3_client_set():
        #     raise OperationFailed('AWS S3 Client already set')
        # this seems to cache poorly, resulting sometimes in
        # this claiming it is set, but then throwing 403 on subsequent requests
        # so just always set it, if it thinks it needs to ...
        self._aws_s3_client = aws_s3_client

    def get_aws_s3_client(self):
        if not self.is_aws_s3_client_set():
            raise OperationFailed('AWS S3 Client not set')
        return self._aws_s3_client

    s3 = property(fget=get_aws_s3_client, fset=set_aws_s3_client)

    def is_aws_cf_client_set(self):
        return bool(self._aws_cf_client)

    def set_aws_cf_client(self, aws_cf_client):
        # if self.is_aws_cf_client_set():
        #     raise OperationFailed('AWS CloudFront Client already set')
        # this seems to cache poorly, resulting sometimes in
        # this claiming it is set, but then throwing 403 on subsequent requests
        # so just always set it, if it thinks it needs to ...
        self._aws_cf_client = aws_cf_client

    def get_aws_cf_client(self):
        if not self.is_aws_cf_client_set():
            raise OperationFailed('AWS CloudFront Client not set')
        return self._aws_cf_client

    cf = property(fget=get_aws_cf_client, fset=set_aws_cf_client)

AWS_CLIENT = AWSClientContainer()
