This repo is a generic DLKit runtime.

It currently supports edX user (`set_xblock_user`) or Django request (`set_http_request`) objects.

The runtime assumes that your DLKit configurations are located in a
`app_configs` directory, like:

  dlkit_runtime/
  app_configs/
    __init__.py
    configs.py
    handcar_configs.py
    registry.py

Example files are located in the `.skel` files in this repository.