# populate with default registry
from dlkit.app_configs.registry import *

# try finding these from the main project to override our defaults
try:
    from dlkit_configs.registry import *
except ImportError:
    pass
