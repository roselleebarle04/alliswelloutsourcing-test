from rest_framework import serializers
import datetime
from .models import *


class OrderSerializer(serializers.ModelSerializer):
    order_type = serializers.PrimaryKeyRelatedField(
        required=False,
        allow_null=True,
        queryset=OrderType.objects.all())

    class Meta:
        model = Order
        fields = '__all__'
        depth = 1


class OrderTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderType
        fields = '__all__'
        depth = 1
