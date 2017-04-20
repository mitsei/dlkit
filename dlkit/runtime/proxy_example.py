

class ProxyExample:
    pass
# Do whatever you do to get an HTTPRequest object that includes an
# user authenticated via Touchstone.
# That object is assumed to be stored the 'request' variable below:

    # from dlkit_django import proxy_session
    # condition = proxy_session.get_proxy_condition()
    # condition.set_http_request(request)
    # proxy = proxy_session.get_proxy(condition)

# Or get an XBlockUser() object from the xblock runtime. That object
# is assumed to be stored the 'xblock_user' variable below:

    # from dlkit_django import proxy_session
    # condition = proxy_session.get_proxy_condition()
    # condition.set_xblock_user(xblock_user)
    # proxy = proxy_session.get_proxy(condition)

# Now you have a proxy object that holds the user data and eventually other
# stuff, like locale information, etc, that can be used to instantiate new
# Managers, which you will probably insert into your HttpRequest.session.

    # from dlkit_django import runtime
    # request.session.lm = runtime.get_service_manager('LEARNING', proxy)

# For the duration of the session you can use this for all the other things.
# that you normally do. My understanding is that your various Managers and
# all their state will be save (in default mode) as Pickled objets in the db.
# For anonomous users you can still just instantiate as LearningManager()


class SimpleRequest:

    def __init__(self, username='pwilkins@mit.edu', authenticated=True, META={}):
        self.user = User(username, authenticated)
        self.META = META
        self.session = {}

    def get_user(self):
        return self.user


class User:

    def __init__(self, username, authenticated):
        self.username = username
        self.authenticated = authenticated

    def get_username(self):
        return self.username

    def is_authenticated(self):
        return self.authenticated


class SimpleXBlockUser:

    def __init__(self, is_current_user=True, emails=None, full_name='Peter Wilkins',
                 is_authenticated=True, user_id='pwilkins@mit.edu', username='pwilkins'):
        self.is_current_user = is_current_user
        self.emails = emails or []
        self.full_name = full_name
        self.opt_attrs = {'proxy_example.is_authenticated': is_authenticated,
                          'proxy_example.user_id': user_id,
                          'proxy_example.username': username}
