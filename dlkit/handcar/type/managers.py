# -*- coding: utf-8 -*-

# This module contains all the Manager classes used by the MIT Core Concept
# Catalog (MC3) Handcar based implementation of the OSID Learning Service.
# Note that it includes the core OsidProfile typically found in the osid
# package as well as the learning package managers.

from ...abstract_osid.type import managers as abc_type_managers
from ..osid import managers as osid_managers
from .. import profile
from ..primitives import Id, DisplayText, Type
from ..osid.osid_errors import NotFound, NullArgument, OperationFailed, Unimplemented


class TypeProfile(abc_type_managers.TypeProfile, osid_managers.OsidProfile):
    """The TypeProfile describes the interoperability among type services."""

    def supports_type_lookup(self):
        """Tests if Type lookup is supported.

        return: (boolean) - true if Type lookup is supported, false
                otherwise
        compliance: mandatory - This method must be implemented.

        """
        return 'supports_type_lookup' in profile.SUPPORTS

    def supports_type_admin(self):
        """Tests if a Type administrative service is supported.

        return: (boolean) - true if Type administration is supported,
                false otherwise
        compliance: mandatory - This method must be implemented.

        """
        return 'supports_type_admin' in profile.SUPPORTS


class TypeManager(abc_type_managers.TypeManager, osid_managers.OsidManager, TypeProfile):
    """This manager provides access to the available sessions of the type
    service.

    The TypeLookupSession is used for looking up Types and the
    TypeAdminSession is used for managing and registering new Types.

    """

    def get_type_lookup_session(self):
        """Gets the OsidSession associated with the type lookup service.

        return: (osid.type.TypeLookupSession) - a TypeLookupSession
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - supports_type_lookup() is false
        compliance: optional - This method must be implemented if
                    supports_type_lookup() is true.

        """
        if not self.supports_type_lookup():
            raise Unimplemented()
        try:
            from . import sessions
        except ImportError:
            raise  # OperationFailed()
        try:
            session = sessions.TypeLookupSession(runtime=self._runtime)
        except AttributeError:
            raise  # OperationFailed()
        return session

    type_lookup_session = property(fget=get_type_lookup_session)

    def get_type_admin_session(self):
        """Gets the OsidSession associated with the type admin service.

        return: (osid.type.TypeAdminSession) - a TypeAdminSession
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - supports_type_admin() is false
        compliance: optional - This method must be implemented if
                    supports_type_admin() is true.

        """
        pass
        if not self.supports_type_admin():
            raise Unimplemented()
        try:
            from . import sessions
        except ImportError:
            raise  # OperationFailed()
        try:
            session = sessions.TypeAdminSession()
        except AttributeError:
            raise  # OperationFailed()
        return session

    type_admin_session = property(fget=get_type_admin_session)
