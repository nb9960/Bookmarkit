from django.contrib.auth.models import User
class EmailAuthBackend(object):
    """
    Authenticate using an e-mail address.
    """
    def authenticate(self, request, username=None, password=None):
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            return None
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

# User credentials will be checked using the ModelBackend authentication backend, and if no user is returned, the credentials will be checked using your custom EmailAuthBackend backend.
# The order of the backends listed in the AUTHENTICATION_BACKENDS setting matters. If the same credentials are valid for multiple backends, Django will stop at the first backend that successfully authenticates the user.

