"""Stupid authz impl that asks user for permission"""

# pylint: disable=too-many-public-methods,too-many-ancestors

# from dlkit.abstract_osid.authorization import managers as abc_authorization_managers
from dlkit.abstract_osid.authorization import sessions as abc_authorization_sessions
from dlkit.manager_impls.authorization import managers as authorization_managers
from .osid_errors import Unimplemented, OperationFailed
from . import profile
from . import osid_managers
from . import osid_sessions


class AuthorizationSession(abc_authorization_sessions.AuthorizationSession, osid_sessions.OsidSession):
    """Stupid authz session impl that asks user for permission"""

    _session_name = 'AuthorizationSession'

    def get_vault_id(self):
        raise Unimplemented()

    vault_id = property(fget=get_vault_id)

    def get_vault(self):
        raise Unimplemented()

    vault = property(fget=get_vault)

    def can_access_authorizations(self):
        return True

    def is_authorized(self, agent_id=None, function_id=None, qualifier_id=None):
        authz = raw_input('Do you want to be authorized? (y or n) ')
        if authz in ['y', 'Y', 'yes', 'Yes', 'YES', 'sure', 'Sure', 'SURE', 'of course']:
            return True
        else:
            print 'Enter either y or n.  If you don\'t follow instructions, you won\'t be authorized!!!'
            return False

    def get_authorization_condition(self, function_id=None):
        raise Unimplemented()

    def is_authorized_on_condition(self, agent_id=None, function_id=None, qualifier_id=None, condition=None):
        raise Unimplemented()


class AuthorizationManager(authorization_managers.AuthorizationManager):

    def supports_authorization(self):
        """Override default method in authorization_managers"""
        return True

    def get_authorization_session(self):
        """Override default method in authorization_managers"""
        if not self.supports_authorization():
            raise Unimplemented()
        return AuthorizationSession()


class AuthorizationProxyManager(authorization_managers.AuthorizationProxyManager):

    def supports_authorization(self):
        """Override default method in authorization_managers"""
        return True

    def get_authorization_session(self, proxy):
        """Override default method in authorization_managers"""
        if not self.supports_authorization():
            raise Unimplemented()
        return AuthorizationSession()
