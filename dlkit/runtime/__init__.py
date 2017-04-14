from .managers import Runtime
from .impls.proxy.managers import ProxyManager

RUNTIME = Runtime()
PROXY_SESSION = ProxyManager().get_proxy_session()
