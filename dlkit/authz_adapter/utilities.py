"""helper utilities for the authz adapter implementation"""

from .primitives import Type
from dlkit.abstract_osid.osid.errors import NullArgument

BOOTSTRAP_VAULT_TYPE = Type(authority='ODL.MIT.EDU',
                            namespace='authorization.Vault',
                            identifier='bootstrap_vault')

OVERRIDE_VAULT_TYPE = Type(authority='ODL.MIT.EDU',
                           namespace='authorization.Vault',
                           identifier='override_vault')


class QueryWrapper(object):
    """Wrapper class to aid in QuerySessions"""
    def __init__(self, provider_query):
        self.__class__ = type(provider_query.__class__.__name__,
                              (self.__class__, provider_query.__class__),
                              {})
        self.__dict__ = provider_query.__dict__
        self._provider_query = provider_query
        self._cat_id_args_list = []


def raise_null_argument(func):
    """decorator, to intercept num argument TypeError and raise as NullArgument"""
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except TypeError as ex:
            if any(statement in ex.args[0] for statement in ['takes exactly',
                                                             'required positional argument']):
                raise NullArgument('Wrong number of arguments provided: ' + str(ex.args[0]))
            else:
                raise
    return wrapper
