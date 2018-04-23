from django.urls import include
from django.urls import path
from .views import *

# category_urlpatterns = [
#     path('category/', CategoryListView.as_view(), name="category-list"),
#     path('category/add/', CategoryAddView.as_view(), name="category-add"),
#     path('category/<int:pk>/', CategoryDetailView.as_view(), name="category-detail"),
# ]

urlpatterns = [
    # path('', Dashboard.as_view(), name="dashboard"),
    path('transactions/', TransactionListAPI.as_view(), name="transaction-api-list"),
    path('transactions/add/', TransactionAddAPI.as_view(), name="transaction-api-add"),
    # path('transactions/<int:pk>/', TransactionDetailView.as_view(), name="transaction-detail"),
    # path('', include(category_urlpatterns)),
]
