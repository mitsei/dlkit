try:
    # Try getting these at the project level
    from dlkit_configs.handcar_configs import *
except ImportError:
    # fall back to built-in configs
    from dlkit.app_configs.handcar_configs import *
