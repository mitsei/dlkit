"""Implementations of mapping abstract base class primitives."""
# pylint: disable=invalid-name
#     Method names comply with OSID specification.
# pylint: disable=no-init
#     Abstract classes do not define __init__.
# pylint: disable=too-few-public-methods
#     Some interfaces are specified as 'markers' and include no methods.
# pylint: disable=too-many-public-methods
#     Number of methods are defined in specification
# pylint: disable=too-many-ancestors
#     Inheritance defined in specification
# pylint: disable=too-many-arguments
#     Argument signature defined in specification.
# pylint: disable=duplicate-code
#     All apparent duplicates have been inspected. They aren't.
import abc


class Coordinate:
    """A coordinate represents a position."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_coordinate_type(self):
        """Gets the ``Type`` of this ``Coordinate`` which indicates the format of the coordinate data.

        :return: the coordinate type
        :rtype: ``osid.type.Type``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.Type

    coordinate_type = abc.abstractproperty(fget=get_coordinate_type)

    @abc.abstractmethod
    def get_dimensions(self):
        """Gets the number of dimensions available in this coordinate.

        :return: the number of dimensions
        :rtype: ``cardinal``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # cardinal

    dimensions = abc.abstractproperty(fget=get_dimensions)

    @abc.abstractmethod
    def get_values(self):
        """Gets the values of this coordinate.

        The size of the returned array should equal ``getDimensions()``.

        :return: the coordinate values
        :rtype: ``decimal``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # decimal

    values = abc.abstractproperty(fget=get_values)

    @abc.abstractmethod
    def defines_uncertainty(self):
        """Tests if uncertainty is defined for this heading.

        :return: ``true`` if uncertainty is defined, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_uncertainty_minus(self):
        """Gets the uncertainty in the negtive direction for each value of this coordinate.

        The size of the returned array is typically one less than
        ``getDimensions()``.

        :return: the negative uncertainty values
        :rtype: ``decimal``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # decimal

    uncertainty_minus = abc.abstractproperty(fget=get_uncertainty_minus)

    @abc.abstractmethod
    def get_uncertainty_plus(self):
        """Gets the uncertainty in the positive direction for each value of this coordinate.

        The size of the returned array is typically one less than
        ``getDimensions()``.

        :return: the positive uncertainty values
        :rtype: ``decimal``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # decimal

    uncertainty_plus = abc.abstractproperty(fget=get_uncertainty_plus)


class Speed:
    """A speed is a distance traveled over a unit of time."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_distance(self):
        """Gets the distance.

        :return: the distance
        :rtype: ``osid.mapping.Distance``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.Distance

    distance = abc.abstractproperty(fget=get_distance)

    @abc.abstractmethod
    def get_time_unit(self):
        """Gets the time unit.

        :return: the time unit
        :rtype: ``osid.calendaring.DateTimeResolution``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.DateTimeResolution

    time_unit = abc.abstractproperty(fget=get_time_unit)


class Heading:
    """A heading represents a direction."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_heading_type(self):
        """Gets the ``Type`` of this ``Heading`` which indicates the format of the heading values.

        :return: the coordinate type
        :rtype: ``osid.type.Type``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.Type

    heading_type = abc.abstractproperty(fget=get_heading_type)

    @abc.abstractmethod
    def get_dimensions(self):
        """Gets the number of dimensions of motion.

        :return: the number of dimensions
        :rtype: ``cardinal``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # cardinal

    dimensions = abc.abstractproperty(fget=get_dimensions)

    @abc.abstractmethod
    def get_values(self):
        """Gets the values of this heading The size of the returned array is typically one less than ``getDimensions()``.

        :return: the heading values
        :rtype: ``decimal``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # decimal

    values = abc.abstractproperty(fget=get_values)

    @abc.abstractmethod
    def defines_uncertainty(self):
        """Tests if uncertainty is defined for this heading.

        :return: ``true`` if uncertainty is defined, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_uncertainty_minus(self):
        """Gets the uncertainty in the negtive direction for each value of this heading.

        The size of the returned array is typically one less than
        ``getDimensions()``.

        :return: the negative uncertainty values
        :rtype: ``decimal``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # decimal

    uncertainty_minus = abc.abstractproperty(fget=get_uncertainty_minus)

    @abc.abstractmethod
    def get_uncertainty_plus(self):
        """Gets the uncertainty in the positive direction for each value of this heading.

        The size of the returned array is typically one less than
        ``getDimensions()``.

        :return: the positive uncertainty values
        :rtype: ``decimal``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # decimal

    uncertainty_plus = abc.abstractproperty(fget=get_uncertainty_plus)


class SpatialUnit:
    """A spatial unit can represent a single position or an area constructed of multiple positions or shapes.

    The data describing the spatial unit is defined in the record
    indicated by the record type.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_center_coordinate(self):
        """Gets a single corrdinate to represent the center of this spatial unit.

        :return: the center coordinate
        :rtype: ``osid.mapping.Coordinate``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.Coordinate

    center_coordinate = abc.abstractproperty(fget=get_center_coordinate)

    @abc.abstractmethod
    def get_bounding_coordinates(self):
        """Gets a list of bounding coordinates of this spatial unit.

        :return: the bounding coordinates
        :rtype: ``osid.mapping.CoordinateList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.CoordinateList

    bounding_coordinates = abc.abstractproperty(fget=get_bounding_coordinates)

    @abc.abstractmethod
    def get_spatial_unit_record(self, spatial_unit_record_type):
        """Gets the spatial unit record corresponding to the given ``SpatialUnit`` record ``Type``.

        The ``spatial_unit_record_type`` may be the ``Type`` returned in
        ``get_record_types()`` or any of its parents in a ``Type``
        hierarchy where ``has_record_type(spatial_unit_record_type)`` is
        ``true`` .

        :param spatial_unit_record_type: the type of spatial unit record to retrieve
        :type spatial_unit_record_type: ``osid.type.Type``
        :return: the spatial unit record
        :rtype: ``osid.mapping.records.SpatialUnitRecord``
        :raise: ``NullArgument`` -- ``spatial_unit_record_type`` is ``null``
        :raise: ``Unsupported`` -- ``has_record_type(spatial_unit_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.records.SpatialUnitRecord


class Distance:
    """A distance."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_yotta_parsecs(self):
        """Gets the number of yottaparsecs.

        You should budget extra time to travel a yottaparsec.

        :return: the number of yottaparsecs
        :rtype: ``decimal``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # decimal

    yotta_parsecs = abc.abstractproperty(fget=get_yotta_parsecs)

    @abc.abstractmethod
    def get_exa_parsecs(self):
        """Gets the number of exaparsecs.

        An exaparsec is much shorter.

        :return: the number of exaparsecs
        :rtype: ``decimal``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # decimal

    exa_parsecs = abc.abstractproperty(fget=get_exa_parsecs)

    @abc.abstractmethod
    def get_giga_parsecs(self):
        """Get sthe number of gigaparsecs.

        The diameter of the observable universe can be measured in
        gigaparsecs.

        :return: the number of gigaparsecs
        :rtype: ``decimal``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # decimal

    giga_parsecs = abc.abstractproperty(fget=get_giga_parsecs)

    @abc.abstractmethod
    def get_yottameters(self):
        """Gets this distance in yottameters.

        A yottameter is 1 trillion terameters.

        :return: the number of yottameters
        :rtype: ``decimal``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # decimal

    yottameters = abc.abstractproperty(fget=get_yottameters)

    @abc.abstractmethod
    def get_zettameters(self):
        """Gets this distance in zettameters.

        A zettameter is one billion terameters.

        :return: the number of zettameters
        :rtype: ``decimal``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # decimal

    zettameters = abc.abstractproperty(fget=get_zettameters)

    @abc.abstractmethod
    def get_exameters(self):
        """Gets this distance in exameters.

        A exameter is 1BB meters.

        :return: the number of exameters
        :rtype: ``decimal``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # decimal

    exameters = abc.abstractproperty(fget=get_exameters)

    @abc.abstractmethod
    def get_parsecs(self):
        """Gets this distance in parsecs.

        A parsec is 30,857,000,000,000,000 meters.

        :return: the number of parsecs
        :rtype: ``decimal``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # decimal

    parsecs = abc.abstractproperty(fget=get_parsecs)

    @abc.abstractmethod
    def get_light_years(self):
        """Gets this distance in light years.

        A light year is 9,460,730,472,580,800 meters.

        :return: the number of light years
        :rtype: ``decimal``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # decimal

    light_years = abc.abstractproperty(fget=get_light_years)

    @abc.abstractmethod
    def get_petameters(self):
        """Gets this distance in petameters.

        A petameter is 1M gigameters.

        :return: the number of petameters
        :rtype: ``decimal``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # decimal

    petameters = abc.abstractproperty(fget=get_petameters)

    @abc.abstractmethod
    def get_terameters(self):
        """Gets this distance in terameters.

        A terameter is one trillion meters.

        :return: the number of terameters
        :rtype: ``decimal``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # decimal

    terameters = abc.abstractproperty(fget=get_terameters)

    @abc.abstractmethod
    def get_gigameters(self):
        """Gets this distance in gigameters.

        A gigameter is 1B meters.

        :return: the number of gigameters
        :rtype: ``decimal``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # decimal

    gigameters = abc.abstractproperty(fget=get_gigameters)

    @abc.abstractmethod
    def get_megameters(self):
        """Gets this distance in megameters.

        A megameter is longer than a megaman.

        :return: the number of megameters
        :rtype: ``decimal``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # decimal

    megameters = abc.abstractproperty(fget=get_megameters)

    @abc.abstractmethod
    def get_kilometers(self):
        """Gets this distance kilometers.

        A kilometer is 1,000 meters.

        :return: the number of kilometres
        :rtype: ``decimal``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # decimal

    kilometers = abc.abstractproperty(fget=get_kilometers)

    @abc.abstractmethod
    def get_meters(self):
        """Gets this distance in meters.

        A meter is 0.0049709695379 furlongs.

        :return: the number of meters
        :rtype: ``decimal``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # decimal

    meters = abc.abstractproperty(fget=get_meters)

    @abc.abstractmethod
    def get_atto_parsecs(self):
        """Gets this distance in attoparsecs.

        :return: the number of attoparsecs
        :rtype: ``decimal``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # decimal

    atto_parsecs = abc.abstractproperty(fget=get_atto_parsecs)

    @abc.abstractmethod
    def get_centimeters(self):
        """Gets this distance in centimeters.

        A centimeter is one hundreth of a meter.

        :return: the number of centimeters
        :rtype: ``decimal``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # decimal

    centimeters = abc.abstractproperty(fget=get_centimeters)

    @abc.abstractmethod
    def get_millimeters(self):
        """Gets this distance in millimeters.

        A millimeter is one thousandth of a meter.

        :return: the number of millimeters
        :rtype: ``decimal``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # decimal

    millimeters = abc.abstractproperty(fget=get_millimeters)

    @abc.abstractmethod
    def get_microns(self):
        """Gets this distance in micrometers.

        A micron is one millionth of a meter.

        :return: the number of microns
        :rtype: ``decimal``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # decimal

    microns = abc.abstractproperty(fget=get_microns)

    @abc.abstractmethod
    def get_nanometers(self):
        """Gets this distance in nanometers.

        A nanometer is one billionth of a meter.

        :return: the number of nanometers
        :rtype: ``decimal``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # decimal

    nanometers = abc.abstractproperty(fget=get_nanometers)

    @abc.abstractmethod
    def get_angstroms(self):
        """Gets this distance in angstroms.

        An angstrom is one ten billionth of a meter.

        :return: the number of angstroms
        :rtype: ``decimal``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # decimal

    angstroms = abc.abstractproperty(fget=get_angstroms)

    @abc.abstractmethod
    def get_picometers(self):
        """Gets this distance in picometers.

        A picometer is one trillionth of a meter.

        :return: the number of picometers
        :rtype: ``decimal``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # decimal

    picometers = abc.abstractproperty(fget=get_picometers)

    @abc.abstractmethod
    def get_femtometers(self):
        """Gets this distance in femotometers.

        A femoto is one quadrillionth of a meter.

        :return: the number of femtometers
        :rtype: ``decimal``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # decimal

    femtometers = abc.abstractproperty(fget=get_femtometers)

    @abc.abstractmethod
    def get_attometers(self):
        """Gets this distance in attometers.

        An attometer is one quintillionth of a meter.

        :return: the number of attometers
        :rtype: ``decimal``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # decimal

    attometers = abc.abstractproperty(fget=get_attometers)

    @abc.abstractmethod
    def get_zeptometers(self):
        """Gets this distance in zeptometers.

        A zeptometer is one sextillionth of a meter.

        :return: the number of zeptometers
        :rtype: ``decimal``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # decimal

    zeptometers = abc.abstractproperty(fget=get_zeptometers)

    @abc.abstractmethod
    def get_yoctometers(self):
        """Gets this distance in yoctometers.

        A yoctometer is one septillionth of a meter.

        :return: the number of yoctometers
        :rtype: ``decimal``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # decimal

    yoctometers = abc.abstractproperty(fget=get_yoctometers)

    @abc.abstractmethod
    def get_xoxxometers(self):
        """Gets this distance in xoxxometers.

        A xoxxometer is one octillionth of a meter.

        :return: the number of xoxxometers
        :rtype: ``decimal``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # decimal

    xoxxometers = abc.abstractproperty(fget=get_xoxxometers)

    @abc.abstractmethod
    def get_weebleometers(self):
        """Gets this distance in weeblemeters.

        A weeblemeter is one nonillionth of a meter.

        :return: the number of weeblemeters
        :rtype: ``decimal``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # decimal

    weebleometers = abc.abstractproperty(fget=get_weebleometers)

    @abc.abstractmethod
    def get_vatometers(self):
        """Gets this distance in vatometers.

        A vatometer is one decillionth of a meter.

        :return: the number of vatometers
        :rtype: ``decimal``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # decimal

    vatometers = abc.abstractproperty(fget=get_vatometers)

    @abc.abstractmethod
    def get_plancks(self):
        """Gets this distance in plancks.

        Plancks are really small.

        :return: the number of plancks
        :rtype: ``decimal``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # decimal

    plancks = abc.abstractproperty(fget=get_plancks)

    @abc.abstractmethod
    def get_granularity(self):
        """Gets the granularity of this distance.

        The granularity indicates the resolution of the yardstick. More
        precision than what is specified in this method cannot be
        inferred from the available data.

        :return: granularity
        :rtype: ``osid.mapping.DistanceResolution``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.DistanceResolution

    granularity = abc.abstractproperty(fget=get_granularity)

    @abc.abstractmethod
    def get_granularity_multiplier(self):
        """If the granularity of the measurement equals ``get_granularity(),`` then the multiplier is 1.

        This method may return a different number when the granularity
        differs from one of the defined resolutions.

        :return: granularity multiplier
        :rtype: ``cardinal``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # cardinal

    granularity_multiplier = abc.abstractproperty(fget=get_granularity_multiplier)

    @abc.abstractmethod
    def defines_uncertainty(self):
        """Tests if uncertainty is defined for this distance.

        :return: ``true`` if uncertainty is defined, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_uncertainty_units(self):
        """Gets the units of the uncertainty.

        :return: units of the uncertainty
        :rtype: ``osid.mapping.DistanceResolution``
        :raise: ``IllegalState`` -- ``defines_uncertainty()`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.DistanceResolution

    uncertainty_units = abc.abstractproperty(fget=get_uncertainty_units)

    @abc.abstractmethod
    def get_uncertainty_minus(self):
        """Gets the uncertainty of this distance in the negative direction in meters.

        :return: the uncertainty under this value
        :rtype: ``decimal``
        :raise: ``IllegalState`` -- ``defines_uncertainty()`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # decimal

    uncertainty_minus = abc.abstractproperty(fget=get_uncertainty_minus)

    @abc.abstractmethod
    def get_uncertainty_plus(self):
        """Gets the uncertainty of this distance in the positive direction in meters.

        :return: the uncertainty over this value
        :rtype: ``decimal``
        :raise: ``IllegalState`` -- ``defines_uncertainty()`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # decimal

    uncertainty_plus = abc.abstractproperty(fget=get_uncertainty_plus)
