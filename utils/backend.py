from django.conf import settings
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User

from users.models import UserToken


def get_auth_header(request):
    return request.META.get('HTTP_AUTHORIZATION', b'')


class TokenBackend:
    def authenticate(self, request, **kwargs):
        auth = get_auth_header(request).split()
        if not auth or auth[0].lower() != b'bearer':
            return None
        token_key = auth[1]

        try:
            user_token = UserToken.objects.select_related('user').get(key=token_key)
        except UserToken.DoesNotExist:
            return None

        return user_token.user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
