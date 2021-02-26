from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('addTransaction', views.addTransaction_view, name="addTransaction"),
    path('transactions', views.transactions_view, name="transactions"),
    path('transactionTypes',views.transactionTypes_view, name="transactionTypes"),
    path('login',views.login_view, name="login"),
    path('logout', views.logout_view, name="logout"),
    path('pie-chart',views.pie_chart_view, name="pieChart")
    
]