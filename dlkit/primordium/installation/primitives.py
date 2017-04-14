"""
Generic implementions of osid.installation.Version primitive.

Can be used by implementations and consumer applications alike.

"""
from dlkit.abstract_osid.installation.primitives import Version as abc_version
from dlkit.abstract_osid.osid.errors import InvalidArgument
from ..osid.primitives import OsidPrimitive


class Version(abc_version, OsidPrimitive):
    """A ``Version`` represents a version in a scheme."""

    def __init__(self, components=None):
        if components is None:
            self._components = []
        elif isinstance(components, list):
            self._components = components
        else:
            raise InvalidArgument()

    def get_scheme(self):
        """Gets the versioining scheme as a type.

        :return: the versioning scheme type
        :rtype: ``osid.type.Type``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.Type

    scheme = property(fget=get_scheme)

    def get_components(self):
        """Gets the components of the version.

        In a major.minor[.maintenance[.build]] scheme, an example is {3,
        0, 0}.

        :return: the version components
        :rtype: ``string``


        *compliance: mandatory -- This method must be implemented.*

        """
        return self._components

    components = property(fget=get_components)
