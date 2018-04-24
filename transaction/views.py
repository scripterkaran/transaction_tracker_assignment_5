from django.core import serializers
from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

from transaction.models import Transaction, Category


class TransactionListAPI(View):
    def get(self, request, *args, **kwargs):
        objs = Transaction.objects.all()
        json_obj_list = [instance.get_json() for instance in objs]
        return JsonResponse(json_obj_list, safe=False)


class TransactionAddAPI(View):
    def post(self, request, *args, **kwargs):
        transaction = Transaction(**request.data, user=self.request.user)
        transaction.save()
        return JsonResponse(transaction.get_json())

class CategoryListAPI(View):
    def get(self, request, *args, **kwargs):
        objs = Category.objects.all()
        json_obj_list = [instance.get_json() for instance in objs]
        return JsonResponse(json_obj_list, safe=False)

class CategoryAddAPI(View):
    def post(self, request, *args, **kwargs):
        category = Category(**request.data)
        category.save()
        return JsonResponse(category.get_json())