def is_never_authz(config):
    return config == 'TEST_SERVICE_NEVER_AUTHZ'


def is_no_authz(config):
    return config == 'TEST_SERVICE' or uses_cataloging(config)


def uses_cataloging(config):
    return config == 'TEST_SERVICE_CATALOGING'
