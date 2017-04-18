"""Implementations of type abstract base class primitives."""
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


class Type:
    """The Type is a form of identifier that is primarily used to identify interface specifications.

    The ``Type`` differs from ``Id`` in that it offers display
    information and ``Types`` may be arranged in hierarchies to indicate
    an extended interface. Semantically, an ``Id`` identifies any OSID
    object while the ``Type`` identifies a specification.

    The components of the Type that make up its identification are:

      * identifier: a unique key or guid
      * namespace: the namespace of the identifier
      * authority: the isuer of the identifier


    Persisting a type reference means to persist the above
    identification elements. In addition to these identifier components,
    A ``Type`` mai also provide some additional metadata such as a name,
    description and domain.

    """
    __metaclass__ = abc.ABCMeta

    def __hash__(self):
        return hash((self.get_authority(),
                     self.get_identifier_namespace(),
                     self.get_identifier()))

    def __eq__(self, other):
        if isinstance(other, Type):
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
    def get_display_name(self):
        """Gets the full display name of this ``Type``.

        :return: the display name of this ``Type``
        :rtype: ``osid.locale.DisplayText``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.locale.DisplayText

    display_name = property(fget=get_display_name)

    @abc.abstractmethod
    def get_display_label(self):
        """Gets the shorter display label for this ``Type``.

        Where a display name of a ``Type`` might be ``"`` Critical
        Logging Priority Type", the display label could be "critical".

        :return: the display label for this ``Type``
        :rtype: ``osid.locale.DisplayText``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.locale.DisplayText

    display_label = property(fget=get_display_label)

    @abc.abstractmethod
    def get_description(self):
        """Gets a description of this ``Type``.

        :return: the description of this ``Type``
        :rtype: ``osid.locale.DisplayText``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.locale.DisplayText

    description = property(fget=get_description)

    @abc.abstractmethod
    def get_domain(self):
        """Gets the domain.

        The domain can provide an information label about ths
        application space of this Type.

        :return: the domain of this ``Type``
        :rtype: ``osid.locale.DisplayText``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.locale.DisplayText

    domain = property(fget=get_domain)

    @abc.abstractmethod
    def get_authority(self):
        """Gets the authority of this ``Type``.

        The authority is a string used to ensure the uniqueness of this
        ``Type`` when using a non- federated identifier space.
        Generally, it is a domain name identifying the party responsible
        for this ``Type``. This method is used to compare one ``Type``
        to another.

        :return: the authority of this ``Type``
        :rtype: ``string``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # string

    authority = property(fget=get_authority)

    @abc.abstractmethod
    def get_identifier_namespace(self):
        """Gets the namespace of the identifier.

        This method is used to compare one ``Type`` to another.

        :return: the authority of this ``Type``
        :rtype: ``string``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # string

    identifier_namespace = property(fget=get_identifier_namespace)

    namespace = property(fget=get_identifier_namespace)

    @abc.abstractmethod
    def get_identifier(self):
        """Gets the identifier of this ``Type``.

        This method is used to compare one ``Type`` to another.

        :return: the identifier of this ``Type``
        :rtype: ``string``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # string

    identifier = property(fget=get_identifier)
