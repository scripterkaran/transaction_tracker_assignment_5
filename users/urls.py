from django.urls import include
from django.urls import path
from .views import *

urlpatterns = [
    path('users/', UserListAPI.as_view(), name="user-list-api"),
    path('users/<int:pk>/', UserDetailAPI.as_view(), name="user-detail-api"),
    path('users/<int:pk>/transactions/', UserTransactionAPI.as_view(), name="user-transaction-api-list"),
]
