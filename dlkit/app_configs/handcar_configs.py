import os

MC3_HOST = ''
MC3_HANDCAR_APP_KEY = None

try:
    from django.conf import settings
except ImportError:
    try:
        from dlkit.handcar import settings
        MC3_HOST = getattr(settings, 'HOST', '')
        # Keep the app_key None, since there are none in the
        # settings file.
    except ImportError:
        if 'MC3_HOST' in os.environ:
            MC3_HOST = os.environ['MC3_HOST']
        if 'MC3_HANDCAR_APP_KEY' in os.environ:
            MC3_HANDCAR_APP_KEY = os.environ['MC3_HANDCAR_APP_KEY']
else:
    from django.core.exceptions import ImproperlyConfigured
    try:
        settings.configure()
    except RuntimeError:
        pass  # already configured
    else:
        # This should always be called from here (not configs.py), if it is needed
        import django
        if django.VERSION < (1, 8):
            settings._setup()
        else:
            django.setup()
    try:
        MC3_HOST = getattr(settings, 'MC3_HOST', '')
        MC3_HANDCAR_APP_KEY = getattr(settings, 'MC3_HANDCAR_APP_KEY', None)
    except ImproperlyConfigured:
        pass


HANDCAR_MC3 = {
    'id': 'handcar_mc3',
    'displayName': 'Handcar MC3 Configuration',
    'description': 'Configuration for Handcar MC3 Production Service',
    'parameters': {
        'implKey': {
            'syntax': 'STRING',
            'displayName': 'Implementation Key',
            'description': 'Implementation key used by Runtime for class loading',
            'values': [
                {'value': 'handcar', 'priority': 1}
            ]
        },
        'hostName': {
            'syntax': 'STRING',
            'displayName': 'Host Name',
            'description': 'Host Name for Handcar RESTFul Service Provider',
            'values': [
                {'value': MC3_HOST, 'priority': 1}
            ]
        },
        'appKey': {
            'syntax': 'STRING',
            'displayName': 'App Key',
            'description': 'Agent Key for Handcar service provider',
            'values': [
                {'value': MC3_HANDCAR_APP_KEY, 'priority': 1}
            ]
        }
    }
}
