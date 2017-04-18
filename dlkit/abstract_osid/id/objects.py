"""Implementations of id abstract base class objects."""
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


class IdForm:
    """This form provides a means of creating an ``Id``."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_authority_metadata(self):
        """Gets the metadata for the authority.

        :return: metadata for the authority
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.Metadata

    authority_metadata = property(fget=get_authority_metadata)

    @abc.abstractmethod
    def set_authority(self, authority):
        """Sets the authority.

        :param authority: the authority
        :type authority: ``string``
        :raise: ``InvalidArgument`` -- ``authority`` is invalid
        :raise: ``NoAccess`` -- ``authority`` cannot be modified
        :raise: ``NullArgument`` -- ``authority`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_authority(self):
        """Clears the authority.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` is ``true`` or ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    authority = property(fset=set_authority, fdel=clear_authority)

    @abc.abstractmethod
    def get_identifier_namespace_metadata(self):
        """Gets the metadata for the identifier namespace.

        :return: metadata for the namespace
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.Metadata

    identifier_namespace_metadata = property(fget=get_identifier_namespace_metadata)

    @abc.abstractmethod
    def set_identifier_namespace(self, namespace):
        """Seta the identifier namespace.

        :param namespace: the namespace
        :type namespace: ``string``
        :raise: ``InvalidArgument`` -- ``namespace`` is invalid
        :raise: ``NoAccess`` -- ``namespace`` cannot be modified
        :raise: ``NullArgument`` -- ``namespace`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_identifier_namespace(self):
        """Clears the identifier namespace.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` is ``true`` or ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    identifier_namespace = property(fset=set_identifier_namespace, fdel=clear_identifier_namespace)

    @abc.abstractmethod
    def get_identifier_prefix_metadata(self):
        """Gets the metadata for the identifier prefix.

        :return: metadata for the prefix
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.Metadata

    identifier_prefix_metadata = property(fget=get_identifier_prefix_metadata)

    @abc.abstractmethod
    def set_identifier_prefix(self, prefix):
        """Seta the identifier prefix.

        An identifier will be generated with this prefix.

        :param prefix: the prefix
        :type prefix: ``string``
        :raise: ``InvalidArgument`` -- ``prefix`` is invalid
        :raise: ``NoAccess`` -- ``prefix`` cannot be modified
        :raise: ``NullArgument`` -- ``prefix`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_identifier_prefix(self):
        """Clears the identifier prefix.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` is ``true`` or ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    identifier_prefix = property(fset=set_identifier_prefix, fdel=clear_identifier_prefix)

    @abc.abstractmethod
    def get_identifier_suffix_metadata(self):
        """Gets the metadata for the identifier suffix.

        :return: metadata for the suffix
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.Metadata

    identifier_suffix_metadata = property(fget=get_identifier_suffix_metadata)

    @abc.abstractmethod
    def set_identifier_suffix(self, suffix):
        """Seta the identifier prefix.

        An identifier will be generated with this suffix.

        :param suffix: the suffix
        :type suffix: ``string``
        :raise: ``InvalidArgument`` -- ``suffix`` is invalid
        :raise: ``NoAccess`` -- ``suffix`` cannot be modified
        :raise: ``NullArgument`` -- ``suffix`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_identifier_suffix(self):
        """Clears the identifier suffix.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` is ``true`` or ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    identifier_suffix = property(fset=set_identifier_suffix, fdel=clear_identifier_suffix)

    @abc.abstractmethod
    def get_identifier_metadata(self):
        """Gets the metadata for the identifier.

        :return: metadata for the identifier
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.Metadata

    identifier_metadata = property(fget=get_identifier_metadata)

    @abc.abstractmethod
    def set_identifier(self, identifier):
        """Seta the identifier.

        :param identifier: the identifier
        :type identifier: ``string``
        :raise: ``InvalidArgument`` -- ``identifier`` is invalid
        :raise: ``NoAccess`` -- ``identifier`` cannot be modified
        :raise: ``NullArgument`` -- ``identifier`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_identifier(self):
        """Clears the identifier.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` is ``true`` or ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    identifier = property(fset=set_identifier, fdel=clear_identifier)


class IdList:
    """Like all ``OsidLists,``  ``IdList`` provides a means for accessing ``Id`` elements sequentially either one at a time or many at a time.

    Examples: while (il.hasNext()) { Id id = il.getNextId(); }

    or
      while (il.hasNext()) {
           Id[] ids = il.getNextIds(il.available());
      }

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_next_id(self):
        """Gets the next ``Id`` in this list.

        :return: the next ``Id`` in this list. The ``has_next()`` method should be used to test that a next ``Id`` is available before calling this method.
        :rtype: ``osid.id.Id``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    next_id = property(fget=get_next_id)

    @abc.abstractmethod
    def get_next_ids(self, n):
        """Gets the next set of ``Ids`` in this list.

        The specified amount must be less than or equal to the return
        from ``available()``.

        :param n: the number of ``Id`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``Id`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.id.Id``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id
