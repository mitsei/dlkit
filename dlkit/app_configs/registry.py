# This file tells dlkit where to find / import each of the different
# managers from.
MANAGER_PATHS = {

    'service': {
        'ASSESSMENT': ('dlkit.services.assessment.AssessmentManager',
                       'dlkit.services.assessment.AssessmentManager'),
        'ASSESSMENT_AUTHORING': ('dlkit.services.assessment_authoring.AssessmentAuthoringManager',
                                 'dlkit.services.assessment_authoring.AssessmentAuthoringManager'),
        'AUTHENTICATION': ('dlkit.services.authentication.AuthenticationManager',
                           'dlkit.services.authentication.AuthenticationManager'),
        'AUTHORIZATION': ('dlkit.services.authorization.AuthorizationManager',
                          'dlkit.services.authorization.AuthorizationManager'),
        'REPOSITORY': ('dlkit.services.repository.RepositoryManager',
                       'dlkit.services.repository.RepositoryManager'),
        'LEARNING': ('dlkit.services.learning.LearningManager',
                     'dlkit.services.learning.LearningManager'),
        'LOGGING': ('dlkit.services.logging_.LoggingManager',
                    'dlkit.services.logging_.LoggingManager'),
        'CATALOGING': ('dlkit.services.cataloging.CatalogingManager',
                       'dlkit.services.cataloging.CatalogingManager'),
        'COMMENTING': ('dlkit.services.commenting.CommentingManager',
                       'dlkit.services.commenting.CommentingManager'),
        'RESOURCE': ('dlkit.services.resource.ResourceManager',
                     'dlkit.services.resource.ResourceManager'),
        'GRADING': ('dlkit.services.grading.GradingManager',
                    'dlkit.services.grading.GradingManager'),
        'TYPE': ('dlkit.services.type.TypeManager',
                 'dlkit.services.type.TypeManager')
    },
    'json': {
        'ASSESSMENT': ('dlkit.json_.assessment.managers.AssessmentManager',
                       'dlkit.json_.assessment.managers.AssessmentProxyManager'),
        'ASSESSMENT_AUTHORING': ('dlkit.json_.assessment_authoring.managers.AssessmentAuthoringManager',
                                 'dlkit.json_.assessment_authoring.managers.AssessmentAuthoringProxyManager'),
        'AUTHENTICATION': ('dlkit.json_.authentication.managers.AuthenticationManager',
                           'dlkit.json_.authentication.managers.AuthenticationProxyManager'),
        'AUTHORIZATION': ('dlkit.json_.authorization.managers.AuthorizationManager',
                          'dlkit.json_.authorization.managers.AuthorizationProxyManager'),
        'REPOSITORY': ('dlkit.json_.repository.managers.RepositoryManager',
                       'dlkit.json_.repository.managers.RepositoryProxyManager'),
        'LEARNING': ('dlkit.json_.learning.managers.LearningManager',
                     'dlkit.json_.learning.managers.LearningProxyManager'),
        'LOGGING': ('dlkit.json_.logging_.managers.LoggingManager',
                    'dlkit.json_.logging_.managers.LoggingProxyManager'),
        'CATALOGING': ('dlkit.json_.cataloging.managers.CatalogingManager',
                       'dlkit.json_.cataloging.managers.CatalogingProxyManager'),
        'COMMENTING': ('dlkit.json_.commenting.managers.CommentingManager',
                       'dlkit.json_.commenting.managers.CommentingProxyManager'),
        'RESOURCE': ('dlkit.json_.resource.managers.ResourceManager',
                     'dlkit.json_.resource.managers.ResourceProxyManager'),
        'GRADING': ('dlkit.json_.grading.managers.GradingManager',
                    'dlkit.json_.grading.managers.GradingProxyManager')
    },
    'authz_adapter': {
        'ASSESSMENT': ('dlkit.authz_adapter.assessment.managers.AssessmentManager',
                       'dlkit.authz_adapter.assessment.managers.AssessmentProxyManager'),
        'ASSESSMENT_AUTHORING': ('dlkit.authz_adapter.assessment_authoring.managers.AssessmentAuthoringManager',
                                 'dlkit.authz_adapter.assessment_authoring.managers.AssessmentAuthoringProxyManager'),
        'AUTHORIZATION': ('dlkit.authz_adapter.authorization.managers.AuthorizationManager',
                          'dlkit.authz_adapter.authorization.managers.AuthorizationProxyManager'),
        'REPOSITORY': ('dlkit.authz_adapter.repository.managers.RepositoryManager',
                       'dlkit.authz_adapter.repository.managers.RepositoryProxyManager'),
        'LEARNING': ('dlkit.authz_adapter.learning.managers.LearningManager',
                     'dlkit.authz_adapter.learning.managers.LearningProxyManager'),
        'LOGGING': ('dlkit.authz_adapter.logging_.managers.LoggingManager',
                    'dlkit.authz_adapter.logging_.managers.LoggingProxyManager'),
        'CATALOGING': ('dlkit.authz_adapter.cataloging.managers.CatalogingManager',
                       'dlkit.authz_adapter.cataloging.managers.CatalogingProxyManager'),
        'COMMENTING': ('dlkit.authz_adapter.commenting.managers.CommentingManager',
                       'dlkit.authz_adapter.commenting.managers.CommentingProxyManager'),
        'RESOURCE': ('dlkit.authz_adapter.resource.managers.ResourceManager',
                     'dlkit.authz_adapter.resource.managers.ResourceProxyManager'),
        'GRADING': ('dlkit.authz_adapter.grading.managers.GradingManager',
                    'dlkit.authz_adapter.grading.managers.GradingProxyManager')
    },
    'handcar': {
        'LEARNING': ('dlkit.handcar.learning.managers.LearningManager',
                     'dlkit.handcar.learning.managers.LearningProxyManager'),
        'TYPE': ('dlkit.handcar.type.managers.TypeManager',
                 'dlkit.handcar.type.managers.TypeManager'),
        'REPOSITORY': ('dlkit.handcar.repository.managers.RepositoryManager',
                       'dlkit.handcar.repository.managers.RepositoryProxyManager'),
    },
    'aws_adapter': {
        'REPOSITORY': ('dlkit.aws_adapter.repository.managers.RepositoryManager',
                       'dlkit.aws_adapter.repository.managers.RepositoryProxyManager')
    },
    'filesystem_adapter': {
        'REPOSITORY': ('dlkit.filesystem_adapter.repository.managers.RepositoryManager',
                       'dlkit.filesystem_adapter.repository.managers.RepositoryProxyManager')
    },
    'always_authz': {
        'AUTHORIZATION': ('tests.authz_impls.always_authz.AuthorizationManager',
                          'tests.authz_impls.always_authz.AuthorizationProxyManager')
    },
    'never_authz': {
        'AUTHORIZATION': ('tests.authz_impls.never_authz.AuthorizationManager',
                          'tests.authz_impls.never_authz.AuthorizationProxyManager')
    },

}
