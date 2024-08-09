from rest_framework import serializers
from .models import CurrencyRate, CustomUser

class CurrencyRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrencyRate
        fields = ['id', 'source_currency', 'target_currency', 'rate', 'is_public', 'owner']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'role']
