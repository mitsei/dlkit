# populate with default registry
from dlkit.app_configs.registry import MANAGER_PATHS

# try finding these from the main project to override our defaults
try:
    from dlkit_configs.registry import MANAGER_PATHS as USER_MANAGER_PATHS
    MANAGER_PATHS.update(USER_MANAGER_PATHS)
except ImportError:
    pass
