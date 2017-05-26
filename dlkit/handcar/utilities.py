import re

from .primitives import Id, Type, DisplayText
from .osid.osid_errors import AlreadyExists, NotFound

from dlkit.runtime import PROXY_SESSION
from dlkit.runtime.managers import Runtime

CONDITION = PROXY_SESSION.get_proxy_condition()
PROXY = PROXY_SESSION.get_proxy(CONDITION)

LM = Runtime().get_service_manager('LEARNING',
                                   implementation='TEST_SERVICE_HANDCAR')
# not sure why Repository requires proxy...
RM = Runtime().get_service_manager('REPOSITORY',
                                   proxy=PROXY,
                                   implementation='TEST_SERVICE_HANDCAR')

SANDBOX_TYPE = Type({
    'id': 'mc3-objectivebank%3Amc3.learning.objectivebank.sandbox%40MIT-OEIT',
    'authority': 'MIT-OEIT',
    'identifierNamespace': 'mc3-objectivebank',
    'identifier': 'mc3.learning.objectivebank.sandbox',
    'domain': '',
    'displayName': '',
    'description': '',
    'displayLabel': ''})


class BankHierarchyUrls(object):
    """
    Set of URLs for access objective bank hierarchy
    """
    def __init__(self):
        self._root = '/handcar/services/learning/objectivebankhierarchies/'
        self._program = 'mc3-objectivebank%3Amc3.learning.objectivebank.mit.program%40MIT-OEIT'
        self._subject_area = 'mc3-objectivebank%3Amc3.learning.objectivebank.mit.subject.area%40MIT-OEIT'
        self._subject = 'mc3-objectivebank%3Amc3.learning.objectivebank.mit.subject%40MIT-OEIT'
        self._mitoces = 'mc3-objectivebank%3Amc3.learning.objectivebank.mitoces%40MIT-OEIT'

    def _safe_alias(self, alias):
        if '%40' in alias:
            return alias
        else:
            return re.sub(r'[ ]', '', alias.lower())

    def children(self, alias, bank_id):
        """
        URL for getting or setting child relationships for the specified bank
        :param alias:
        :param bank_id:
        :return:
        """
        return self._root + self._safe_alias(alias) + '/child/ids/' + str(bank_id)

    def hierarchy(self, alias=None):
        """
        return the URL for the bank hierarchy itself
        :param alias:
        :return:
        """
        if alias:
            return self._root + self._safe_alias(alias)
        else:
            return self._root

    def nodes(self, alias, depth=10, bank_id=None):
        """
        URL for getting bulk nodes in hierarchy
        :param alias:
        :param depth:
        :return:
        """
        if bank_id:
            return self._root + self._safe_alias(alias) + '/child/nodes/' + bank_id + '?descendentlevels=' + str(depth)
        else:
            return self._root + self._safe_alias(alias) + '/root/nodes?descendentlevels=' + str(depth)

    def parents(self, alias, bank_id):
        """
        URL for getting or setting parent relationships for the specified bank
        :param alias:
        :param bank_id:
        :return:
        """
        return self._root + self._safe_alias(alias) + '/parent/ids/' + bank_id

    def roots(self, alias):
        """
        URL for get or set root banks for the given alias / id
        :param alias:
        :return:
        """
        return self._root + self._safe_alias(alias) + '/root/ids/'


def construct_url(type_, bank_id=None, obj_id=None, obj_ids=None, act_id=None, asset_id=None, genus_type=None, descendents=0):
    url = '/handcar/services/learning/objectivebanks/'
    if type_ == 'objective_banks':
        if bank_id:
            url += get_id_str(bank_id)
        else:
            pass
    elif type_ == 'objective_banks_by_genus':
        if genus_type:
            url += '?genustypeid={0}'.format(get_id_str(genus_type))
        else:
            raise ValueError()
    elif type_ == 'objectives':
        if obj_id and bank_id:
            url += get_id_str(bank_id) + '/objectives/' + get_id_str(obj_id)
        elif bank_id:
            url += get_id_str(bank_id) + '/objectives/'
        elif obj_id:
            url += '../objectives/' + get_id_str(obj_id)
        else:
            raise ValueError
    elif type_ == 'objectives_by_genus':
        if bank_id and genus_type:
            url += '{0}/objectives?genustypeid={1}'.format(get_id_str(bank_id),
                                                           get_id_str(genus_type))
        else:
            raise ValueError
    elif type_ == 'objectives_by_ids':
        if bank_id is not None and obj_ids is not None:
            url += '{0}/objectives/bulk/?{1}'.format(get_id_str(bank_id),
                                                     '&'.join(['id={0}'.format(get_id_str(i))
                                                               for i in obj_ids]))
        elif obj_ids is not None:
            url = '/handcar/services/learning/objectives/bulk/?{0}'.format('&'.join(['id={0}'.format(get_id_str(i))
                                                                           for i in obj_ids]))
    elif type_ == 'childids':
        if bank_id and obj_id:
            url += (get_id_str(bank_id) + '/objectives/' +
                    get_id_str(obj_id) + '/childids/')
        else:
            raise ValueError
    elif type_ == 'children':
        if bank_id and obj_id:
            url += (get_id_str(bank_id) + '/objectives/' +
                    get_id_str(obj_id) + '/children')
        else:
            raise ValueError
    elif type_ == 'dependents':
        if bank_id and obj_id:
            url += (get_id_str(bank_id) + '/objectives/' +
                    get_id_str(obj_id) + '/dependents')
        else:
            raise ValueError
    elif type_ == 'equivalents':
        if bank_id and obj_id:
            url += (get_id_str(bank_id) + '/objectives/' +
                    get_id_str(obj_id) + '/equivalents')
        else:
            raise ValueError
    elif type_ == 'parentids':
        if bank_id and obj_id:
            url += (get_id_str(bank_id) + '/objectives/' +
                    get_id_str(obj_id) + '/parentids/')
        else:
            raise ValueError
    elif type_ == 'parents':
        if bank_id and obj_id:
            url += (get_id_str(bank_id) + '/objectives/' +
                    get_id_str(obj_id) + '/parents/')
        else:
            raise ValueError
    elif type_ == 'requisites':
        if bank_id and obj_id:
            url += (get_id_str(bank_id) + '/objectives/' +
                    get_id_str(obj_id) + '/requisites/')
        else:
            raise ValueError
    elif type_ == 'requisiteids':
        if bank_id and obj_id:
            url += (get_id_str(bank_id) + '/objectives/' +
                    get_id_str(obj_id) + '/requisiteids/')
        else:
            raise ValueError
    elif type_ == 'rootids':
        if bank_id:
            url += get_id_str(bank_id) + '/objectives/rootids/'
        else:
            raise ValueError
    elif type_ == 'roots':
        if bank_id:
            url += get_id_str(bank_id) + '/objectives/roots?descendentlevels=' + str(descendents)
        else:
            raise ValueError
    elif type_ == 'activities':
        if act_id and bank_id and not obj_id:
            url += get_id_str(bank_id) + '/activities/' + get_id_str(act_id)
        elif obj_id and bank_id:
            url += (get_id_str(bank_id) + '/objectives/' + get_id_str(obj_id) +
                    '/activities/')
        elif bank_id:
            url += get_id_str(bank_id) + '/activities/'
        else:
            raise ValueError
    elif type_ == 'activities_by_genus':
        if bank_id and genus_type:
            url += (get_id_str(bank_id) + '/activities?genustypeid=' +
                    get_id_str(genus_type))
        else:
            raise ValueError
    elif type_ == 'assets':
        if asset_id and bank_id and not act_id:
            url += get_id_str(bank_id) + '/assets/' + get_id_str(asset_id)
        elif act_id and bank_id:
            url += (get_id_str(bank_id) + '/activities/' + get_id_str(act_id) +
                    '/assets/')
        elif bank_id:
            url += get_id_str(bank_id) + '/assets/'
        else:
            raise ValueError
    elif type_ == 'assets_by_genus':
        if bank_id and genus_type:
            url += (get_id_str(bank_id) + '/assets?genustypeid=' +
                    get_id_str(genus_type))
        else:
            raise ValueError
    elif type_ == 'authorization':
        if bank_id:
            url += get_id_str(bank_id) + '/authorization/'
        else:
            url = '/handcar/services/learning/authorization'  # yuck!
    elif type_ == 'objective_bank_types':
        url += 'types/genus/'
    elif type_ == 'extension_record':
        if bank_id:
            url += get_id_str(bank_id)
            if obj_id:
                url += '/objectives/' + get_id_str(obj_id) + '/extension'
            elif act_id:
                url += '/activities/' + get_id_str(act_id) + '/extension'
            elif asset_id:
                url += '/assets/' + get_id_str(asset_id) + '/extension'
            else:
                url += '/extension'
        else:
            raise ValueError
    elif type_ == 'objective_objective_bank_assignment':
        url += '../bankassignment/objective/' + get_id_str(obj_id) + '/' + get_id_str(bank_id) + '/'
    else:
        raise ValueError
    return url


def get_id_str(id_):
    if not is_string(id_):
        id_ = str(id_)
    return id_


def get_bank_by_name(name):
    obls = LM.get_objective_bank_lookup_session()
    for ob in obls.get_objective_banks():
        if ob.display_name.text == name:
            return ob
    raise NotFound()


def get_objective_by_bank_id_and_name(objective_bank_id, name):
    ols = LM.get_objective_lookup_session_for_objective_bank(objective_bank_id)
    for o in ols.get_objectives():
        if o.display_name.text == name:
            return o
    raise NotFound()


def is_string(string_):
    try:
        # python 2
        return isinstance(string_, basestring)
    except NameError:
        # python 3
        return isinstance(string_, str)


def create_sandbox_bank(display_name, description=None):
    if description is None:
        description = 'Catalog for ' + display_name
    lm = LM
    obas = lm.get_objective_bank_admin_session()
    obls = lm.get_objective_bank_lookup_session()
    for ob in obls.get_objective_banks():
        if ob.display_name.text == display_name:
            print('A sandbox bank named', display_name, 'already exists.')
            return None
    obfc = obas.get_objective_bank_form_for_create()
    obfc.display_name = display_name
    obfc.description = description
    obfc.genus_type = SANDBOX_TYPE
    return obas.create_objective_bank(obfc)


def delete_bank_by_name(display_name):
    lm = LM
    obas = lm.get_objective_bank_admin_session()
    obls = lm.get_objective_bank_lookup_session()
    found = False
    for ob in obls.get_objective_banks():
        if ob.display_name.text == display_name:
            found = True
            ols = lm.get_objective_lookup_session_for_objective_bank(ob.ident)
            als = lm.get_activity_lookup_session_for_objective_bank(ob.ident)
            if ols.get_objectives().available() != 0:
                print('can not delete objective bank \'' + ob.display_name.text + '\'. It still contains objectives.')
            elif als.get_activities().available() != 0:
                print('can not delete objective bank \'' + ob.display_name.text + '\'. It still contains activities.')
            else:
                print('deleting objective bank', ob)
                obas.delete_objective_bank(ob.ident)
    if not found:
        print('objective bank \'' + display_name + '\' not found.')


def create_objective(bank_id, display_name, description=None):
    if description is None:
        description = display_name + ' objective'
    lm = LM
    ols = lm.get_objective_lookup_session_for_objective_bank(bank_id)
    oas = lm.get_objective_admin_session_for_objective_bank(bank_id)
    for o in ols.get_objectives():
        if o.display_name.text == display_name:
            return o
    ofc = oas.get_objective_form_for_create([])
    ofc.display_name = display_name
    ofc.description = description
    return oas.create_objective(ofc)


def get_repository_by_name(name):
    rls = RM.get_repository_lookup_session(proxy=PROXY)
    for r in rls.get_repositories():
        if r.display_name.text == name:
            return r
    raise NotFound()


def get_asset_by_repository_id_and_name(repository_id, name):
    als = RM.get_asset_lookup_session_for_repository(repository_id,
                                                     proxy=PROXY)
    for a in als.get_assets():
        if a.display_name.text == name:
            return a
    raise NotFound()


def create_sandbox_repository(display_name, description=None):
    if description is None:
        description = 'Catalog for ' + display_name
    rm = RM
    ras = rm.get_repository_admin_session()
    rls = rm.get_repository_lookup_session()
    for r in rls.get_repositories():
        if r.display_name.text == display_name:
            print('A sandbox repository named', display_name, 'already exists.')
            return None
    rfc = ras.get_repository_form_for_create()
    rfc.display_name = display_name
    rfc.description = description
    rfc.genus_type = SANDBOX_TYPE
    return ras.create_repository(rfc)


def delete_repository_by_name(display_name):
    rm = RM
    ras = rm.get_repository_admin_session()
    rls = rm.get_repository_lookup_session()
    found = False
    for r in rls.get_repositories():
        if r.display_name.text == display_name:
            found = True
            als = rm.get_asset_lookup_session_for_repository(r.ident)
            if als.get_assets().available() != 0:
                print('can not delete repository \'' + r.display_name.text + '\'. It still contains assets.')
            else:
                print('deleting repository', r)
                ras.delete_repository(r.ident)
    if not found:
        print('repository \'' + display_name + '\' not found.')


def create_asset(repository_id, display_name, description=None):
    if description is None:
        description = display_name + ' asset'
    rm = RM
    als = rm.get_asset_lookup_session_for_repository(repository_id,
                                                     proxy=PROXY)
    aas = rm.get_asset_admin_session_for_repository(repository_id,
                                                    proxy=PROXY)
    for a in als.get_assets():
        if a.display_name.text == display_name:
            return a
    afc = aas.get_asset_form_for_create([])
    afc.display_name = display_name
    afc.description = description
    return aas.create_asset(afc)
