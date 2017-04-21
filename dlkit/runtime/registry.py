try:
    # try finding these from the main project
    from dlkit_configs.registry import *
except ImportError:
    # fall back to default configs
    from dlkit.app_configs.registry import *
