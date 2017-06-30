# Pytest fixtures to get different DLKit configs during tests
# Implemented from documentation here:
#   https://docs.pytest.org/en/latest/unittest.html

import pytest


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_FUNCTIONAL'])
def dlkit_service_config(request):
    request.cls.service_cfg = request.param
