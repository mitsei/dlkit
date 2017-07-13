# initialize with our default configs
from dlkit.app_configs.configs import *

# Try getting configs from the main app to override our defaults
try:
    from dlkit_configs.configs import *
except ImportError:
    pass
