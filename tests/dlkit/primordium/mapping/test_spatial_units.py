# NOTE: most of this file is tested in tests/other/test_mapping_primitives.py
# So these tests only cover the lines not included in the other tests

import pytest

from dlkit.abstract_osid.osid import errors
from dlkit.primordium.mapping.coordinate_primitives import BasicCoordinate
from dlkit.primordium.mapping.spatial_units import RectangularSpatialUnit, SpatialUnitFactory
from dlkit.primordium.type.primitives import Type


@pytest.fixture(scope="function")
def rectangular_spatial_unit_test_wrapper(request):
    request.cls.unit = RectangularSpatialUnit(spatial_unit_map={
        'coordinateValues': [0, 1],
        'width': 5,
        'height': 5
    })
    request.cls.coordinate = BasicCoordinate([1, 1])


@pytest.mark.usefixtures("rectangular_spatial_unit_test_wrapper")
class TestRectangularSpatialUnit(object):
    def test_non_coordinate_throws_invalid_argument(self):
        with pytest.raises(errors.InvalidArgument):
            RectangularSpatialUnit(coordinate=[1, 2])

    def test_negative_width_throws_invalid_argument(self):
        with pytest.raises(errors.InvalidArgument):
            RectangularSpatialUnit(coordinate=self.coordinate,
                                   width=-0.1,
                                   height=0)

    def test_negative_height_throws_invalid_argument(self):
        with pytest.raises(errors.InvalidArgument):
            RectangularSpatialUnit(coordinate=self.coordinate,
                                   width=0,
                                   height=-0.1)

    def test_non_numeric_width_throws_invalid_argument(self):
        with pytest.raises(errors.InvalidArgument):
            RectangularSpatialUnit(coordinate=self.coordinate,
                                   width='0',
                                   height=0)

    def test_non_numeric_height_throws_invalid_argument(self):
        with pytest.raises(errors.InvalidArgument):
            RectangularSpatialUnit(coordinate=self.coordinate,
                                   width=0,
                                   height='0')

    def test_none_args_throws_null_argument(self):
        with pytest.raises(errors.NullArgument):
            RectangularSpatialUnit()

    def test_none_height_with_coordinate_throws_null_argument(self):
        with pytest.raises(errors.NullArgument):
            RectangularSpatialUnit(coordinate=self.coordinate,
                                   width=1)

    def test_none_width_with_coordinate_throws_null_argument(self):
        with pytest.raises(errors.NullArgument):
            RectangularSpatialUnit(coordinate=self.coordinate,
                                   height=1)

    def test_get_bounding_coordinates_returns_list_of_coordinates(self):
        result = self.unit.get_bounding_coordinates()
        assert isinstance(result, list)
        assert len(result) == 4
        for value in result:
            assert isinstance(value, BasicCoordinate)
        assert result[0].values == [0, 1]
        assert result[1].values == [5, 1]
        assert result[2].values == [5, 6]
        assert result[3].values == [0, 6]

    def test_get_spatial_unit_record_passes(self):
        self.unit.get_spatial_unit_record()

    def test_contains_throws_type_error_for_non_coordinate(self):
        with pytest.raises(TypeError):
            [1, 2] in self.unit

    def test_can_check_record_type(self):
        assert self.unit.is_of_record_type(self.unit.get_record_types()[0])
        assert not self.unit.is_of_record_type(Type('osid.mapping.SpatialUnit%3Acircle%40ODL.MIT.EDU'))


@pytest.fixture(scope="function")
def factory_test_wrapper(request):
    request.cls.factory = SpatialUnitFactory()


@pytest.mark.usefixtures("factory_test_wrapper")
class TestSpatialUnitFactory(object):
    def test_get_spatial_unit_throws_invalid_argument_for_non_supported_namespace(self):
        test_map = {
            'recordTypes': ['foo.Bar%3Arectangle%40ODL.MIT.EDU']
        }
        with pytest.raises(errors.InvalidArgument):
            self.factory.get_spatial_unit(test_map)

    def test_get_spatial_unit_throws_invalid_argument_for_non_supported_authority(self):
        test_map = {
            'recordTypes': ['osid.mapping.SpatialUnit%3Arectangle%40WWW.MIT.EDU']
        }
        with pytest.raises(errors.InvalidArgument):
            self.factory.get_spatial_unit(test_map)

    def test_get_spatial_unit_throws_invalid_argument_for_non_rectangle(self):
        test_map = {
            'recordTypes': ['osid.mapping.SpatialUnit%3Acircle%40ODL.MIT.EDU']
        }
        with pytest.raises(errors.InvalidArgument):
            self.factory.get_spatial_unit(test_map)
