from stocky.models import Stock
from stocky.serializers import StockSerializer
from rest_framework import viewsets
from django.shortcuts import render, redirect
from rest_framework import filters

class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

    filter_backends = (filters.SearchFilter,)
    search_fields = ('nombre', 'descripcion', 'cantidad')