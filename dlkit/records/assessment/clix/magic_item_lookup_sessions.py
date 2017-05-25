import json

from dlkit.json_.assessment.sessions import ItemLookupSession
from dlkit.json_.assessment.objects import ItemList

from dlkit.primordium.id.primitives import Id

from ..qti.numeric_response_records import MagicNumericResponseItemLookupSession
from ..qti.inline_choice_records import RandomizedInlineChoiceItemLookupSession
from ...adaptive.multi_choice_questions.randomized_questions import RandomizedMCItemLookupSession

try:
    # python 2
    from urllib import unquote
except ImportError:
    # python 3
    from urllib.parse import unquote


class CLIxMagicItemLookupSession(MagicNumericResponseItemLookupSession,
                                 RandomizedMCItemLookupSession,
                                 RandomizedInlineChoiceItemLookupSession,
                                 ItemLookupSession):
    """ to federate across multiple item lookup sessions, because otherwise there
    is no way to figure out which magic session is needed (since get_item_lookup_session
    doesn't have the item_id passed to it)
    """
    def __init__(self, *args, **kwargs):
        super(CLIxMagicItemLookupSession, self).__init__(*args, **kwargs)

    def get_item(self, item_id):
        authority = item_id.authority
        if authority in ['magic-randomize-choices-question-record',
                         'magic-randomize-inline-choices-question-record',
                         'qti-numeric-response']:
            # for now, this will not work with aliased IDs...
            magic_identifier = unquote(item_id.identifier)
            original_identifier = magic_identifier.split('?')[0]
            choice_ids = json.loads(magic_identifier.split('?')[-1])
            original_item_id = Id(identifier=original_identifier,
                                  namespace=item_id.namespace,
                                  authority=self._catalog.ident.authority)
            orig_item = super(CLIxMagicItemLookupSession, self).get_item(original_item_id)
            orig_item.set_params(choice_ids)
            return orig_item
        else:
            return super(CLIxMagicItemLookupSession, self).get_item(item_id)

    def get_items_by_ids(self, item_ids):
        item_list = []
        for item_id in item_ids:
            item_list.append(super(CLIxMagicItemLookupSession, self).get_item(item_id))
        return ItemList(item_list, runtime=self._runtime, proxy=self._proxy)
