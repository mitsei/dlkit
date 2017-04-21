try:
    # Try getting configs from the main app
    from dlkit_configs.configs import *
except ImportError:
    # fallback to our default dlkit configs
    from dlkit.app_configs.configs import *
