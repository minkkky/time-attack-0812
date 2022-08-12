from rest_framework import serializers
from .models import Product, SubscribeLog

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

class SubscribeLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscribeLog
        fields = "__all__"