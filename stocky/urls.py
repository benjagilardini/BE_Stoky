from django.urls import path
from stocky.views import *

urlpatterns = [
    path('Stock/', StockList.as_view(), name = 'stocky')
]