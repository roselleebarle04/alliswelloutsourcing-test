from django.shortcuts import render

from rest_framework import viewsets

from .serializers import *


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderTypeViewSet(viewsets.ModelViewSet):
    queryset = OrderType.objects.all()
    serializer_class = OrderTypeSerializer
