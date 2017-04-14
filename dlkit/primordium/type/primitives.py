"""
Generic implementions of osid.type.Type primitive.

Can be used by implementations and consumer applications alike.

"""
# pylint: disable=no-init, too-many-public-methods
#    Number of public methods are defined in spec
# pylint: disable=too-many-arguments
#    Number of arguments are defined in spec

from dlkit.abstract_osid.type.primitives import Type as abc_type
from dlkit.abstract_osid.osid.errors import NullArgument
from ..osid.primitives import OsidPrimitive
from .. import default_types


class Type(abc_type, OsidPrimitive):
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

    def __init__(self,
                 idstr=None,
                 identifier=None,
                 authority=None,
                 namespace=None,
                 display_name='',
                 display_label='',
                 description='',
                 domain='',
                 **kwargs):
        if (idstr is not None and display_name is not None and
                description is not None and domain is not None):
            idstr = self._unescape(idstr)
            self._authority = self._unescape(idstr.split('@')[-1])
            self._namespace = self._unescape(idstr.split(':')[0])
            self._identifier = self._unescape(idstr.split('@')[0].split(':')[-1])
        elif (authority is not None and namespace is not None and identifier is not None and
              display_name is not None and description is not None and domain is not None):
            self._authority = authority
            self._namespace = namespace
            self._identifier = identifier
        else:
            raise NullArgument()
        self._display_name = display_name
        self._display_label = display_label
        self._description = description
        self._domain = domain

    def get_display_name(self):
        from ..locale.primitives import DisplayText
        return DisplayText(text=self._display_name,
                           language_type=Type(**default_types.Language().get_type_data('DEFAULT')),
                           script_type=Type(**default_types.Script().get_type_data('DEFAULT')),
                           format_type=Type(**default_types.Format().get_type_data('DEFAULT')))

    def get_display_label(self):
        from ..locale.primitives import DisplayText
        return DisplayText(text=self._display_label,
                           language_type=Type(**default_types.Language().get_type_data('DEFAULT')),
                           script_type=Type(**default_types.Script().get_type_data('DEFAULT')),
                           format_type=Type(**default_types.Format().get_type_data('DEFAULT')))

    def get_description(self):
        from ..locale.primitives import DisplayText
        return DisplayText(text=self._description,
                           language_type=Type(**default_types.Language().get_type_data('DEFAULT')),
                           script_type=Type(**default_types.Script().get_type_data('DEFAULT')),
                           format_type=Type(**default_types.Format().get_type_data('DEFAULT')))

    def get_domain(self):
        from ..locale.primitives import DisplayText
        return DisplayText(text=self._domain,
                           language_type=Type(**default_types.Language().get_type_data('DEFAULT')),
                           script_type=Type(**default_types.Script().get_type_data('DEFAULT')),
                           format_type=Type(**default_types.Format().get_type_data('DEFAULT')))

    def get_authority(self):
        return self._authority

    def get_identifier_namespace(self):
        return self._namespace

    def get_identifier(self):
        return self._identifier

    display_name = property(get_display_name)
    display_label = property(get_display_label)
    description = property(get_description)
    domain = property(get_domain)
    authority = property(get_authority)
    identifier_namespace = property(get_identifier_namespace)
    namespace = property(get_identifier_namespace)
    identifier = property(get_identifier)
