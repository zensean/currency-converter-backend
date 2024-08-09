from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .models import CurrencyRate
from .serializers import CurrencyRateSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser

class CurrencyRateViewSet(viewsets.ModelViewSet):
    queryset = CurrencyRate.objects.all()
    serializer_class = CurrencyRateSerializer

    def get_permissions(self):
        if self.request.method in ['PUT', 'DELETE']:
            return [IsAdminUser()]
        return [IsAuthenticatedOrReadOnly()]
