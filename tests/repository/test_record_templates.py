"""Unit tests of repository records."""


import pytest


from ..utilities.general import is_never_authz, is_no_authz, uses_cataloging, uses_filesystem_only


@pytest.mark.usefixtures("asset_record_class_fixture", "asset_record_test_fixture")
class TestAssetRecord(object):
    """Tests for AssetRecord"""


@pytest.mark.usefixtures("asset_query_record_class_fixture", "asset_query_record_test_fixture")
class TestAssetQueryRecord(object):
    """Tests for AssetQueryRecord"""


@pytest.mark.usefixtures("asset_form_record_class_fixture", "asset_form_record_test_fixture")
class TestAssetFormRecord(object):
    """Tests for AssetFormRecord"""


@pytest.mark.usefixtures("asset_search_record_class_fixture", "asset_search_record_test_fixture")
class TestAssetSearchRecord(object):
    """Tests for AssetSearchRecord"""


@pytest.mark.usefixtures("asset_content_record_class_fixture", "asset_content_record_test_fixture")
class TestAssetContentRecord(object):
    """Tests for AssetContentRecord"""


@pytest.mark.usefixtures("asset_content_query_record_class_fixture", "asset_content_query_record_test_fixture")
class TestAssetContentQueryRecord(object):
    """Tests for AssetContentQueryRecord"""


@pytest.mark.usefixtures("asset_content_form_record_class_fixture", "asset_content_form_record_test_fixture")
class TestAssetContentFormRecord(object):
    """Tests for AssetContentFormRecord"""


@pytest.mark.usefixtures("composition_record_class_fixture", "composition_record_test_fixture")
class TestCompositionRecord(object):
    """Tests for CompositionRecord"""


@pytest.mark.usefixtures("composition_query_record_class_fixture", "composition_query_record_test_fixture")
class TestCompositionQueryRecord(object):
    """Tests for CompositionQueryRecord"""


@pytest.mark.usefixtures("composition_form_record_class_fixture", "composition_form_record_test_fixture")
class TestCompositionFormRecord(object):
    """Tests for CompositionFormRecord"""


@pytest.mark.usefixtures("composition_search_record_class_fixture", "composition_search_record_test_fixture")
class TestCompositionSearchRecord(object):
    """Tests for CompositionSearchRecord"""


@pytest.mark.usefixtures("repository_record_class_fixture", "repository_record_test_fixture")
class TestRepositoryRecord(object):
    """Tests for RepositoryRecord"""


@pytest.mark.usefixtures("repository_query_record_class_fixture", "repository_query_record_test_fixture")
class TestRepositoryQueryRecord(object):
    """Tests for RepositoryQueryRecord"""


@pytest.mark.usefixtures("repository_form_record_class_fixture", "repository_form_record_test_fixture")
class TestRepositoryFormRecord(object):
    """Tests for RepositoryFormRecord"""


@pytest.mark.usefixtures("repository_search_record_class_fixture", "repository_search_record_test_fixture")
class TestRepositorySearchRecord(object):
    """Tests for RepositorySearchRecord"""
