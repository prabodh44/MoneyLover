from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('addTransaction', views.addTransaction_view, name="addTransaction"),
    path('transactions', views.transactions_view, name="transactions"),
    path('transactionTypes',views.transactionTypes_view, name="transactionTypes"),
]