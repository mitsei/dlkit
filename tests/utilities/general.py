def is_never_authz(config):
    return config == 'TEST_SERVICE_NEVER_AUTHZ'


def is_no_authz(config):
    return config in ['TEST_SERVICE', 'TEST_SERVICE_MEMCACHE'] or uses_cataloging(config) or uses_filesystem_only(config)


def uses_cataloging(config):
    return config == 'TEST_SERVICE_CATALOGING'


def uses_filesystem_only(config):
    return config == 'TEST_SERVICE_FILESYSTEM'
