from rest_framework import serializers

from models import Profit


class ProfitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profit
        fields = ('image', 'description',)
