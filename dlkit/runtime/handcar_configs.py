# initialize with built-in configs
from dlkit.app_configs.handcar_configs import *

# override with project-level ones if provided
try:
    from dlkit_configs.handcar_configs import *
except ImportError:
    pass
