import json

from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

from transaction.models import Transaction
from users.models import UserToken


class UserLoginAPI(View):

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        username = data.get('email')
        password = data.get('password')
        try:
            credentials = {
                get_user_model().USERNAME_FIELD: username,
                'password': password
            }
            user = authenticate(**credentials)
            try:
                token = user.usertoken.key
            except UserToken.DoesNotExist:
                obj = UserToken(user=user)
                obj.save()
                token = obj.key
            return JsonResponse({"username": user.username, "token": token}, safe=False)
        except User.DoesNotExist:
           return JsonResponse({}, status=401)

class UserListAPI(View):
    def get(self, request, *args, **kwargs):
        return


class UserDetailAPI(View):
    def get(self, request, *args, **kwargs):
        return


class UserTransactionAPI(View):
    def get(self, request, *args, **kwargs):
        objs = Transaction.objects.filter(user=request.user).order_by('-created_at')
        json_list = [obj.get_json() for obj in objs]
        return JsonResponse(json_list, safe=False)
