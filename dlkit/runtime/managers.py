"""
This module containg the OSID RuntimeManager class implementation for Django
"""
import importlib
from .impls.osid.managers import OsidRuntimeManager
from .impls.configuration.objects import Configuration
from .impls.configuration.sessions import ValueRetrievalSession
from .impls.primitives import Id
from . import configs
from .registry import MANAGER_PATHS
NO_PROXY = 0
PROXY = 1


class Runtime(OsidRuntimeManager):

    def __init__(self, config=None):
        if config is None:
            self._configuration = Configuration((getattr(configs, 'BOOTSTRAP')))
        else:
            self._configuration = config
        self._managers = {}
        self._proxy_managers = {}

    def get_service_manager(self, osid, implementation='SERVICE', proxy=None, version=[3, 0, 0]):
        if proxy is None:
            proxy_key = NO_PROXY
        else:
            proxy_key = PROXY
        return self._load_mgr(osid, implementation, version, proxy_key, proxy)

    def get_manager(self, osid, implementation, version=[3, 0, 0]):
        if implementation + osid not in self._managers:
            self._managers[implementation + osid] = self._load_mgr(osid, implementation, version, 0)
        return self._managers[implementation + osid]

    def get_proxy_manager(self, osid, implementation, version=[3, 0, 0], proxy=None):
        if implementation + osid not in self._proxy_managers:
            self._proxy_managers[implementation + osid] = self._load_mgr(osid, implementation, version, 1)
        return self._proxy_managers[implementation + osid]

    def get_configuration(self):
        return ValueRetrievalSession(self._configuration)

    def _load_mgr(self, osid, implementation, version, proxy_key, proxy=None):
        new_configuration = Configuration(getattr(configs, implementation))
        parameter_id = Id('parameter:implKey@dlkit_runtime')
        impl_key = ValueRetrievalSession(new_configuration).get_value_by_parameter(parameter_id).get_string_value()
        module_path = '.'.join(MANAGER_PATHS[impl_key][osid][proxy_key].split('.')[:-1])
        class_name = MANAGER_PATHS[impl_key][osid][proxy_key].split('.')[-1]
        module = importlib.import_module(module_path)
        if proxy is None:
            manager = getattr(module, class_name)()
        else:
            manager = getattr(module, class_name)(proxy=proxy)
        manager.initialize(Runtime(new_configuration))
        return manager

    configuration = property(fget=get_configuration)
