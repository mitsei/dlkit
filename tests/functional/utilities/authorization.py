import pickle

from copy import deepcopy

from dlkit.primordium.id.primitives import Id
from dlkit.primordium.type.primitives import Type

from dlkit.runtime import PROXY_SESSION, RUNTIME
from dlkit.runtime.proxy_example import User, SimpleRequest
from dlkit.runtime import configs

BOOTSTRAP_VAULT_GENUS = Type(**{
    'identifier': 'bootstrap-vault',
    'namespace': 'authorization.Vault',
    'authority': 'ODL.MIT.EDU'
})

try:
    CONFIGURED_AUTHORITY = configs.JSON_1['parameters']['authority']['values'][0]['value']
except KeyError:
    CONFIGURED_AUTHORITY = ''

BASE_AUTHORIZATIONS = (
    ('assessment.Bank', 'lookup', 'assessment.Bank'),
    ('authorization.Vault', 'lookup', 'authorization.Vault'),
    ('commenting.Book', 'lookup', 'commenting.Book'),
    ('hierarchy.Hierarchy', 'lookup', 'hierarchy.Hierarchy'),
    ('learning.ObjectiveBank', 'lookup', 'learning.ObjectiveBank'),
    ('repository.Repository', 'lookup', 'repository.Repository'),
    ('resource.Bin', 'lookup', 'resource.Bin'),
)

SUPER_USER_FUNCTIONS = (
    ('create', 'authorization.Authorization'),
    ('delete', 'authorization.Authorization'),
    ('lookup', 'authorization.Authorization'),
    ('search', 'authorization.Authorization'),
    ('create', 'authorization.Vault'),
    ('delete', 'authorization.Vault'),
    ('search', 'authorization.Vault'),
)

PROXY_USER_FUNCTIONS = (
    ('proxy', 'users.Proxy'),
)

INSTRUCTOR_FUNCTIONS = (
    ('assessment.Answer', 'lookup', 'assessment.Bank'),
    ('assessment.Answer', 'create', 'assessment.Bank'),
    ('assessment.Answer', 'delete', 'assessment.Bank'),
    ('assessment.Answer', 'update', 'assessment.Bank'),
    ('assessment.Assessment', 'author', 'assessment.Bank'),
    ('assessment.Assessment', 'lookup', 'assessment.Bank'),
    ('assessment.Assessment', 'create', 'assessment.Bank'),
    ('assessment.Assessment', 'delete', 'assessment.Bank'),
    ('assessment.Assessment', 'search', 'assessment.Bank'),
    ('assessment.Assessment', 'update', 'assessment.Bank'),
    ('assessment.Assessment', 'take', 'assessment.Bank'),
    ('assessment.AssessmentBank', 'assign', 'assessment.Bank'),
    ('assessment.AssessmentBank', 'lookup', 'assessment.Bank'),
    ('assessment.AssessmentOffered', 'lookup', 'assessment.Bank'),
    ('assessment.AssessmentOffered', 'create', 'assessment.Bank'),
    ('assessment.AssessmentOffered', 'delete', 'assessment.Bank'),
    ('assessment.AssessmentOffered', 'update', 'assessment.Bank'),
    ('assessment.AssessmentTaken', 'lookup', 'assessment.Bank'),
    ('assessment.AssessmentTaken', 'create', 'assessment.Bank'),
    ('assessment.AssessmentTaken', 'delete', 'assessment.Bank'),
    ('assessment.AssessmentTaken', 'search', 'assessment.Bank'),
    ('assessment.AssessmentTaken', 'update', 'assessment.Bank'),
    ('assessment.Item', 'lookup', 'assessment.Bank'),
    ('assessment.Item', 'create', 'assessment.Bank'),
    ('assessment.Item', 'delete', 'assessment.Bank'),
    ('assessment.Item', 'update', 'assessment.Bank'),
    ('assessment.Item', 'search', 'assessment.Bank'),
    ('assessment.Question', 'lookup', 'assessment.Bank'),
    ('assessment.Question', 'create', 'assessment.Bank'),
    ('assessment.Question', 'delete', 'assessment.Bank'),
    ('assessment.Question', 'update', 'assessment.Bank'),
    ('assessment.Bank', 'access', 'assessment.Bank'),
    ('assessment.Bank', 'create', 'assessment.Bank'),
    ('assessment.Bank', 'delete', 'assessment.Bank'),
    ('assessment.Bank', 'modify', 'assessment.Bank'),
    ('assessment.Bank', 'search', 'assessment.Bank'),
    ('assessment.Bank', 'update', 'assessment.Bank'),
    ('assessment_authoring.AssessmentPart', 'lookup', 'assessment_authoring.Bank'),
    ('assessment_authoring.AssessmentPart', 'create', 'assessment_authoring.Bank'),
    ('assessment_authoring.AssessmentPart', 'delete', 'assessment_authoring.Bank'),
    ('assessment_authoring.AssessmentPart', 'update', 'assessment_authoring.Bank'),
    ('commenting.Book', 'access', 'commenting.Book'),
    ('commenting.Book', 'create', 'commenting.Book'),
    ('commenting.Book', 'delete', 'commenting.Book'),
    ('commenting.Book', 'modify', 'commenting.Book'),
    ('commenting.Book', 'update', 'commenting.Book'),
    ('commenting.Comment', 'author', 'commenting.Book'),
    ('commenting.Comment', 'lookup', 'commenting.Book'),
    ('commenting.Comment', 'create', 'commenting.Book'),
    ('commenting.Comment', 'delete', 'commenting.Book'),
    ('commenting.Comment', 'update', 'commenting.Book'),
    ('hierarchy.Hierarchy', 'update', 'hierarchy.Hierarchy'),
    ('learning.ObjectiveBank', 'create', 'learning.ObjectiveBank'),
    ('learning.ObjectiveBank', 'delete', 'learning.ObjectiveBank'),
    ('learning.ObjectiveBank', 'update', 'learning.ObjectiveBank'),
    ('learning.Objective', 'create', 'learning.ObjectiveBank'),
    ('learning.Objective', 'delete', 'learning.ObjectiveBank'),
    ('learning.Objective', 'lookup', 'learning.ObjectiveBank'),
    ('learning.Objective', 'search', 'learning.ObjectiveBank'),
    ('learning.Objective', 'update', 'learning.ObjectiveBank'),
    ('learning.Proficiency', 'create', 'learning.ObjectiveBank'),
    ('learning.Proficiency', 'delete', 'learning.ObjectiveBank'),
    ('learning.Proficiency', 'lookup', 'learning.ObjectiveBank'),
    ('learning.Proficiency', 'search', 'learning.ObjectiveBank'),
    ('learning.Proficiency', 'update', 'learning.ObjectiveBank'),
    ('logging.Log', 'lookup', 'logging.Log'),
    ('logging.Log', 'create', 'logging.Log'),
    ('logging.Log', 'delete', 'logging.Log'),
    ('logging.Log', 'update', 'logging.Log'),
    ('logging.LogEntry', 'alias', 'logging.Log'),
    ('logging.LogEntry', 'create', 'logging.Log'),
    ('logging.LogEntry', 'delete', 'logging.Log'),
    ('logging.LogEntry', 'lookup', 'logging.Log'),
    ('logging.LogEntry', 'search', 'logging.Log'),
    ('logging.LogEntry', 'update', 'logging.Log'),
    ('repository.Repository', 'access', 'repository.Repository'),
    ('repository.Repository', 'author', 'repository.Repository'),
    ('repository.Repository', 'create', 'repository.Repository'),
    ('repository.Repository', 'delete', 'repository.Repository'),
    ('repository.Repository', 'modify', 'repository.Repository'),
    ('repository.Repository', 'search', 'repository.Repository'),
    ('repository.Repository', 'update', 'repository.Repository'),
    ('repository.Asset', 'author', 'repository.Repository'),
    ('repository.Asset', 'lookup', 'repository.Repository'),
    ('repository.Asset', 'create', 'repository.Repository'),
    ('repository.Asset', 'delete', 'repository.Repository'),
    ('repository.Asset', 'search', 'repository.Repository'),
    ('repository.Asset', 'update', 'repository.Repository'),
    ('repository.AssetComposition', 'access', 'repository.Repository'),
    ('repository.AssetComposition', 'lookup', 'repository.Repository'),
    ('repository.AssetComposition', 'compose', 'repository.Repository'),
    ('repository.AssetRepository', 'assign', 'repository.Repository'),
    ('repository.AssetRepository', 'lookup', 'repository.Repository'),
    ('repository.Composition', 'author', 'repository.Repository'),
    ('repository.Composition', 'lookup', 'repository.Repository'),
    ('repository.Composition', 'create', 'repository.Repository'),
    ('repository.Composition', 'delete', 'repository.Repository'),
    ('repository.Composition', 'search', 'repository.Repository'),
    ('repository.Composition', 'update', 'repository.Repository'),
    ('resource.Bin', 'access', 'resource.Bin'),
    ('resource.Bin', 'author', 'resource.Bin'),
    ('resource.Bin', 'create', 'resource.Bin'),
    ('resource.Bin', 'delete', 'resource.Bin'),
    ('resource.Bin', 'modify', 'resource.Bin'),
    ('resource.Bin', 'update', 'resource.Bin'),
    ('resource.Resource', 'author', 'resource.Bin'),
    ('resource.Resource', 'lookup', 'resource.Bin'),
    ('resource.Resource', 'create', 'resource.Bin'),
    ('resource.Resource', 'delete', 'resource.Bin'),
    ('resource.Resource', 'search', 'resource.Bin'),
    ('resource.Resource', 'update', 'resource.Bin'),
    ('resource.ResourceAgent', 'assign', 'resource.Bin'),
    ('resource.ResourceAgent', 'delete', 'resource.Bin'),
    ('resource.ResourceAgent', 'lookup', 'resource.Bin'),
    ('grading.Gradebook', 'lookup', 'grading.Gradebook'),
    ('grading.Gradebook', 'create', 'grading.Gradebook'),
    ('grading.Gradebook', 'delete', 'grading.Gradebook'),
    ('grading.Gradebook', 'update', 'grading.Gradebook'),
    ('grading.GradeEntry', 'create', 'grading.Gradebook'),
    ('grading.GradeEntry', 'delete', 'grading.Gradebook'),
    ('grading.GradeEntry', 'lookup', 'grading.Gradebook'),
    ('grading.GradeEntry', 'update', 'grading.Gradebook'),
    ('grading.GradeSystem', 'create', 'grading.Gradebook'),
    ('grading.GradeSystem', 'delete', 'grading.Gradebook'),
    ('grading.GradeSystem', 'lookup', 'grading.Gradebook'),
    ('grading.GradeSystem', 'update', 'grading.Gradebook'),
    ('grading.GradebookColumn', 'create', 'grading.Gradebook'),
    ('grading.GradebookColumn', 'delete', 'grading.Gradebook'),
    ('grading.GradebookColumn', 'lookup', 'grading.Gradebook'),
    ('grading.GradebookColumn', 'update', 'grading.Gradebook'),
)

STUDENT_FUNCTIONS = (
    ('assessment.AssessmentTaken', 'create', 'assessment.Bank'),
    ('assessment.AssessmentTaken', 'lookup', 'assessment.Bank'),
    ('assessment.Assessment', 'take', 'assessment.Bank'),
    ('commenting.Comment', 'lookup', 'commenting.Book'),
    ('repository.Asset', 'create', 'repository.Repository'),
    ('repository.Asset', 'delete', 'repository.Repository'),
    ('repository.Asset', 'lookup', 'repository.Repository'),
    ('repository.Asset', 'search', 'repository.Repository'),
    ('resource.Resource', 'lookup', 'resource.Bin'),
)

SUBPACKAGES = (
    ('assessment_authoring', 'assessment'),
)


def activate_managers(request):
    """
    Create initial managers and store them in the user session
    """
    managers = [('authzm', 'AUTHORIZATION'), ]

    for manager in managers:
        nickname = manager[0]
        service_name = manager[1]
        if nickname not in request.session:
            condition = PROXY_SESSION.get_proxy_condition()
            condition.set_http_request(request)
            proxy = PROXY_SESSION.get_proxy(condition)
            set_session_data(request, nickname, RUNTIME.get_service_manager(service_name,
                                                                            proxy=proxy))
    return request


def add_user_authz_to_settings(role, username, catalog_id=None, authority='MIT-ODL'):
    from .testing import is_string
    if is_string(catalog_id):
        catalog_id = Id(catalog_id)
    agent = create_agent_id(username, authority=authority)

    if catalog_id is None:
        qualifiers = ('ROOT', 24 * '0')
        catalog_id = create_qualifier_id(24 * '0', 'authorization.Vault')
    else:
        qualifiers = (catalog_id,)

    # first, add the base authorizations to the user for the catalog_id and ROOT / '0' * 24
    req = get_super_authz_user_request()
    vault = get_vault(req)

    create_base_authorizations(vault,
                               agent,
                               qualifiers=qualifiers)

    # then, depending on role, add additional functions
    if role == 'instructor':
        authorization_iterator(vault,
                               agent,
                               qualifiers,
                               INSTRUCTOR_FUNCTIONS)
    elif role == 'student':
        authorization_iterator(vault,
                               agent,
                               qualifiers,
                               STUDENT_FUNCTIONS)


def authorization_iterator(vault, agent, qualifiers, authz_list):
    def first(namespace):
        return str(namespace).split('.')[0]

    for qualifier in qualifiers:
        for function_tuple in authz_list:
            namespace = function_tuple[0]
            function_name = function_tuple[1]
            function = create_function_id(function_name, namespace)

            if not isinstance(qualifier, Id):
                qualifier_id = create_qualifier_id(qualifier, function_tuple[2])
            else:
                qualifier_id = qualifier

            # also need to handle subpackages!!
            is_subpackage = False
            for subpackage in SUBPACKAGES:
                sub = subpackage[0]
                parent = subpackage[1]
                if first(qualifier_id.namespace) == parent and first(function.namespace) == sub:
                    is_subpackage = True

            if (first(qualifier_id.namespace) == first(function.namespace) or
                    is_subpackage):
                create_authz(vault, agent, function, qualifier_id)


def create_agent_id(username, authority='MIT-ODL'):
    return Id(identifier=username,
              namespace='osid.agent.Agent',
              authority=authority)


def create_authz(vault, agent, function, qualifier):
    form = vault.get_authorization_form_for_create_for_agent(agent, function, qualifier, [])
    vault.create_authorization(form)


def create_authz_superuser():
    original_config = open_up_services_config()

    req = get_super_authz_user_request()
    authzm = get_session_data(req, 'authzm')
    vault = create_vault(req)

    create_base_authorizations(vault, authzm.effective_agent_id)
    create_super_authz_authorizations(vault)

    restore_services_config(original_config)


def create_base_authorizations(vault, agent, qualifiers=()):
    if len(qualifiers) == 0:
        qualifiers = ('ROOT', 24 * '0')
    authorization_iterator(vault, agent, qualifiers, BASE_AUTHORIZATIONS)


def create_function_id(function, namespace):
    return Id(identifier=function,
              namespace=namespace,
              authority='ODL.MIT.EDU')


def create_qualifier_id(identifier, namespace, authority=CONFIGURED_AUTHORITY):
    if identifier == 'ROOT':
        authority = 'ODL.MIT.EDU'
    return Id(identifier=identifier,
              namespace=namespace,
              authority=authority)


def create_super_authz_authorizations(vault):
    req = get_super_authz_user_request()
    authzm = get_session_data(req, 'authzm')

    agent_id = authzm.effective_agent_id

    for function_tuple in SUPER_USER_FUNCTIONS:
        function = create_function_id(function_tuple[0],
                                      function_tuple[1])

        create_authz(vault, agent_id, function, vault.ident)


def create_test_request(test_user):
    # from django.http import HttpRequest
    # from django.conf import settings
    # from django.utils.importlib import import_module
    # #http://stackoverflow.com/questions/16865947/django-httprequest-object-has-no-attribute-session
    # test_request = HttpRequest()
    # engine = import_module(settings.SESSION_ENGINE)
    # session_key = None
    # test_request.user = test_user
    # test_request.session = engine.SessionStore(session_key)
    # return test_request
    return SimpleRequest(username=test_user.username)


def create_vault(request):
    authzm = get_session_data(request, 'authzm')
    form = authzm.get_vault_form_for_create([])
    form.display_name = "System Vault"
    form.description = "Created during bootstrapping"
    form.set_genus_type(BOOTSTRAP_VAULT_GENUS)
    return authzm.create_vault(form)


def get_authz_user_request(username):
    authz_user = User(username=username, authenticated=True)
    req = create_test_request(authz_user)
    activate_managers(req)
    return req


def get_session_data(request, item_type):
    # get a manager
    try:
        if item_type in request.session:
            return pickle.loads(request.session[item_type])
        else:
            return None
    except Exception as ex:
        print("Exception! {0}".format(ex))


def get_super_authz_user_request():
    return get_authz_user_request('dlkit-functional-tester')


def get_vault(request):
    authzm = get_session_data(request, 'authzm')
    return next(authzm.get_vaults_by_genus_type(BOOTSTRAP_VAULT_GENUS))


def open_up_services_config():
    previous_version = deepcopy(configs.SERVICE)

    configs.SERVICE = {
        'id': 'dlkit.runtime_bootstrap_configuration',
        'displayName': 'DLKit Runtime Bootstrap Configuration',
        'description': 'Bootstrap Configuration for DLKit Runtime',
        'parameters': {
            'implKey': {
                'syntax': 'STRING',
                'displayName': 'Implementation Key',
                'description': 'Implementation key used by Runtime for class loading',
                'values': [
                    {'value': 'service', 'priority': 1}
                ]
            },
            'assessmentProviderImpl': {
                'syntax': 'STRING',
                'displayName': 'Assessment Provider Implementation',
                'description': 'Implementation for assessment service provider',
                'values': [
                    {'value': 'JSON_1', 'priority': 1}
                ]
            },
            'assessment_authoringProviderImpl': {
                'syntax': 'STRING',
                'displayName': 'Assessment Authoring Provider Implementation',
                'description': 'Implementation for assessment authoring service provider',
                'values': [
                    {'value': 'JSON_1', 'priority': 1}
                ]
            },
            'authorizationProviderImpl': {
                'syntax': 'STRING',
                'displayName': 'Authorization Provider Implementation',
                'description': 'Implementation for authorization service provider',
                'values': [
                    {'value': 'JSON_1', 'priority': 1}
                ]
            },
            'learningProviderImpl': {
                'syntax': 'STRING',
                'displayName': 'Learning Provider Implementation',
                'description': 'Implementation for learning service provider',
                'values': [
                    {'value': 'JSON_1', 'priority': 1}
                ]
            },
            'repositoryProviderImpl': {
                'syntax': 'STRING',
                'displayName': 'Repository Provider Implementation',
                'description': 'Implementation for repository service provider',
                'values': [
                    {'value': 'JSON_1', 'priority': 1}
                ]
            },
            'commentingProviderImpl': {
                'syntax': 'STRING',
                'displayName': 'Commenting Provider Implementation',
                'description': 'Implementation for commenting service provider',
                'values': [
                    {'value': 'JSON_1', 'priority': 1}
                ]
            },
            'resourceProviderImpl': {
                'syntax': 'STRING',
                'displayName': 'Resource Provider Implementation',
                'description': 'Implementation for resource service provider',
                'values': [
                    {'value': 'JSON_1', 'priority': 1}
                ]
            },
            'gradingProviderImpl': {
                'syntax': 'STRING',
                'displayName': 'Grading Provider Implementation',
                'description': 'Implementation for grading provider',
                'values': [
                    {'value': 'JSON_1', 'priority': 1}
                ]
            },
            'loggingProviderImpl': {
                'syntax': 'STRING',
                'displayName': 'Logging Provider Implementation',
                'description': 'Implementation for logging provider',
                'values': [
                    {'value': 'JSON_1', 'priority': 1}
                ]
            },
        }
    }

    return previous_version


def restore_services_config(original_version):
    configs.SERVICE = original_version


def set_session_data(request, item_type, data):
    request.session[item_type] = pickle.dumps(data)
    # request.session.modified = True
