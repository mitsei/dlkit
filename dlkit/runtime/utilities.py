"""utility methods"""


def impl_key_dict(value, priority=1):
    """to reduce duplicate code in configs.py and handcar_configs.py"""
    return {
        'syntax': 'STRING',
        'displayName': 'Implementation Key',
        'description': 'Implementation key used by Runtime for class loading',
        'values': [
            {'value': value, 'priority': priority}
        ]
    }
