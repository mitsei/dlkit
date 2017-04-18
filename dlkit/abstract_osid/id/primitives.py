"""Implementations of id abstract base class primitives."""
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


class Id:
    """``Id`` represents an identifier object.

    Ids are designated by the following elements:

      * ``identifier:`` a unique key or guid
      * ``namespace:`` the namespace of the identifier
      * ``authority:`` the issuer of the identifier


    Two Ids are equal if their namespace, identifier and authority
    strings are equal. Only the identifier is case-sensitive. Persisting
    an ``Id`` means persisting the above components.

    """
    __metaclass__ = abc.ABCMeta

    def __hash__(self):
        return hash((self.get_authority(),
                     self.get_identifier_namespace(),
                     self.get_identifier()))

    def __eq__(self, other):
        if isinstance(other, Id):
            return (
                self.get_authority() == other.get_authority() and
                self.get_identifier_namespace() == other.get_identifier_namespace() and
                self.get_identifier() == other.get_identifier()
            )
        return NotImplemented

    def __ne__(self, other):
        result = self.__eq__(other)
        if result is NotImplemented:
            return result
        return not result

    def __str__(self):
        """Provides serialized version of Id"""
        return self._escape(self._escape(self.get_identifier_namespace()) + ':' +
                            self._escape(self.get_identifier()) + '@' +
                            self._escape(self.get_authority()))

    def _escape(self, string):
        """Private method for escaping : and @"""
        return string.replace("%", "%25").replace(":", "%3A").replace("@", "%40")

    def _unescape(self, string):
        """Private method for un-escaping : and @"""
        return string.replace("%40", "@").replace("%3A", ":").replace("%25", "%")

    @abc.abstractmethod
    def get_authority(self):
        """Gets the authority of this ``Id``.

        The authority is a string used to ensure the uniqueness of this
        ``Id`` when using a non- federated identifier space. Generally,
        it is a service name identifying the provider of this ``Id``.
        This method is used to compare one ``Id`` to another.

        :return: the authority of this ``Id``
        :rtype: ``string``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # string

    authority = property(fget=get_authority)

    @abc.abstractmethod
    def get_identifier_namespace(self):
        """Gets the namespace of the identifier.

        The namespace reflects the domain in which the identifier is
        unique. When using a global identifier schema, the namespace may
        indicate the name of the scheme. When using a local
        identification scheme, the namespace may be more specific, such
        as the name of a database or file in which the identifiers
        exist. Federating adapters may use a custom namespace to include
        information for routing. This method is used to compare one
        ``Id`` to another.

        :return: the authority of this ``Id``
        :rtype: ``string``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # string

    identifier_namespace = property(fget=get_identifier_namespace)

    namespace = property(fget=get_identifier_namespace)

    @abc.abstractmethod
    def get_identifier(self):
        """Gets the identifier of this ``Id``.

        This method is used to compare one ``Id`` to another.

        :return: the identifier of this ``Id``
        :rtype: ``string``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # string

    identifier = property(fget=get_identifier)
