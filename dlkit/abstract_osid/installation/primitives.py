"""Implementations of installation abstract base class primitives."""
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


class Version:
    """A ``Version`` represents a version in a scheme."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_scheme(self):
        """Gets the versioining scheme as a type.

        :return: the versioning scheme type
        :rtype: ``osid.type.Type``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.Type

    scheme = property(fget=get_scheme)

    @abc.abstractmethod
    def get_components(self):
        """Gets the components of the version.

        In a major.minor[.maintenance[.build]] scheme, an example is {3,
        0, 0}.

        :return: the version components
        :rtype: ``string``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # string

    components = property(fget=get_components)
