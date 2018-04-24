from django.conf import settings
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User

from users.models import UserToken


class TokenBackend(object):
    def authenticate(self, token=None):
        """
        Try to find a user with the given token
        """
        try:
            t = UserToken.objects.get(key=token)
            return t.user
        except UserToken.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
