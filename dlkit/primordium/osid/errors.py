"""
Additional exceptions not defined in osid spec.

Can be used by implementations and consumer applications alike.

"""


class BlockIteration(Exception):
    """An exception to be raised by osid lists that support blocking.

    This is provided in an effort to allow more pythonic iteration in
    For loops. Iteration on osid lists that may support blocking should
    be embedded in a try block:

    try:
        for item in osid_list:
            <do something with the item>
    except BlockIteration:
        <go ahead and do other things>

    In the above scenario, the osid_list may not be exhausted, and may
    be able to continue iteration at a later time. Per certain osid
    spec, this can occur if osid_list.has_next_object() == True, but
    osid_list.avaiable() == 0.

    """
