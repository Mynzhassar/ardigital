from rest_framework import serializers

from . import models, validators


class ProfitSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Profit
        fields = ('image', 'description',)


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Service
        fields = ('title', 'image', 'description',)


class ConsultationSerializer(ServiceSerializer):
    full_name = serializers.CharField(validators=[validators.validate_full_name])
    telephone_number = serializers.CharField(validators=[validators.validate_telephone_number])

    class Meta(ServiceSerializer.Meta):
        model = models.Consultation
        fields = ServiceSerializer.Meta.fields + (
            'service', 'full_name', 'telephone_number', 'status', 'receipted_time',
            'response_time',)
