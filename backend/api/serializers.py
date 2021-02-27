from rest_framework import serializers

from .models import Profit, Service


class ProfitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profit
        fields = ('image', 'description',)


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('title', 'image', 'description',)
