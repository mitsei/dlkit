from dlkit.abstract_osid.authentication import objects as abc_authentication_objects
from ..osid import objects as osid_objects
from .. import settings


class Agent(abc_authentication_objects.Agent, osid_objects.OsidObject):
    """An ``Agent`` represents an authenticatable identity.

    Like all OSID objects, an ``Agent`` is identified by its ``Id`` and
    any persisted references should use the ``Id``.

    """

    def __init__(self, identifier, namespace, authority,
                 display_name=None, description=None, genus_type=None):
        self._identifier = identifier
        self._namespace = namespace
        self._authority = authority
        if display_name is None:
            display_name = 'Agent: ' + identifier
        if description is None:
            description = 'The Agent identified by ' + identifier
        if genus_type is None:
            genus_type = settings.DEFAULT_GENUS_TYPES['authentication.Agent']
        self._display_name = {
            'languageTypeId': settings.LANGUAGE_TYPE_ID,
            'scriptTypeId': settings.SCRIPT_TYPE_ID,
            'formatTypeId': settings.FORMAT_TYPE_ID,
            'text': display_name
        }
        self._description = {
            'languageTypeId': settings.LANGUAGE_TYPE_ID,
            'scriptTypeId': settings.SCRIPT_TYPE_ID,
            'formatTypeId': settings.FORMAT_TYPE_ID,
            'text': description
        }
        self._genus_type = genus_type

    def get_agent_record(self, agent_record_type):
        """Gets the agent record corresponding to the given ``Agent`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``agent_record_type`` may be the ``Type``
        returned in ``get_record_types()`` or any of its parents in a
        ``Type`` hierarchy where ``has_record_type(agent_record_type)``
        is ``true`` .

        :param agent_record_type: the type of the record to retrieve
        :type agent_record_type: ``osid.type.Type``
        :return: the agent record
        :rtype: ``osid.authentication.records.AgentRecord``
        :raise: ``NullArgument`` -- ``agent_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(agent_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authentication.records.AgentRecord
