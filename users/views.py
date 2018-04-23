from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

from transaction.models import Transaction


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
