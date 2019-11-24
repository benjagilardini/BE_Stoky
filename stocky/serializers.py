from rest_framework import serializers
from stocky.models import Stock

class StockSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Stock
        fields = '__all__'