"""
Generic implementions of osid.id.Id primitive.

Can be used by implementations and consumer applications alike.

"""
from dlkit.abstract_osid.id.primitives import Id as abc_id
from dlkit.abstract_osid.osid.errors import NullArgument
from ..osid.primitives import OsidPrimitive


class Id(abc_id, OsidPrimitive):
    """``Id`` represents an identifier object.

    Ids are designated by the following elements:

      * ``identifier:`` a unique key or guid
      * ``namespace:`` the namespace of the identifier
      * ``authority:`` the issuer of the identifier


    Two Ids are equal if their namespace, identifier and authority
    strings are equal. Only the identifier is case-sensitive. Persisting
    an ``Id`` means persisting the above components.

    """

    def __init__(self, idstr=None, authority=None, namespace=None, identifier=None, **kwargs):
        self._idstr = idstr
        if idstr is not None:
            idstr = self._unescape(idstr)
            self._authority = self._unescape(idstr.split('@')[-1])
            self._namespace = self._unescape(idstr.split(':')[0])
            self._identifier = self._unescape(idstr.split('@')[0].split(':')[-1])
        elif authority is not None and namespace is not None and identifier is not None:
            self._authority = authority
            self._namespace = namespace
            self._identifier = identifier
        else:
            raise NullArgument()

    def __str__(self):
        if self._idstr is not None:
            return self._idstr
        else:
            return super(Id, self).__str__()

    def get_authority(self):
        return self._authority

    def get_identifier_namespace(self):
        return self._namespace

    def get_identifier(self):
        return self._identifier

    authority = property(get_authority)
    identifier_namespace = property(get_identifier_namespace)
    namespace = property(get_identifier_namespace)
    identifier = property(get_identifier)
