"""
Generic implementions of Osid primitive.

Can be used by implementations and consumer applications alike.

"""
# pylint: disable=no-init, too-few-public-methods
#    This is a required marker interface

from dlkit.abstract_osid.osid import markers as abc_osid_markers


class OsidPrimitive(abc_osid_markers.OsidPrimitive):
    """A marker interface for an interface that behaves like a language primitive.

    Primitive types, such as numbers and strings, do not encapsulate
    behaviors supplied by an OSID Provider. More complex primitives are
    expressed through interface definitions but are treated in a similar
    fashion as a language primitive. OSID Primitives supplied by an OSID
    Consumer must be consumable by any OSID Provider.

    """
