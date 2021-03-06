from django.utils import timezone
from rest_framework import serializers

from . import models, validators, constants


class ProfitSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    image = serializers.ImageField()
    description = serializers.CharField(max_length=255)

    class Meta:
        model = models.Profit
        fields = ('id', 'image', 'description',)


class ServiceSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=100)
    image = serializers.ImageField()
    description = serializers.CharField(max_length=255)

    class Meta:
        model = models.Service
        fields = ('id', 'title', 'image', 'description',)


class ConsultationSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    service_id = serializers.IntegerField(write_only=True)
    full_name = serializers.CharField(max_length=100,
                                      validators=[validators.validate_full_name])

    telephone_number = serializers.CharField(max_length=constants.VALID_PHONE_NUM_MAX_LEN,
                                             validators=[validators.validate_telephone_number])

    status = serializers.ChoiceField(choices=constants.CONSULTATION_STATUS_CHOICES,
                                     read_only=True)

    receipted_time = serializers.DateTimeField(default=timezone.now)

    class Meta:
        model = models.Consultation
        fields = ('id', 'service_id', 'full_name', 'telephone_number', 'status', 'receipted_time',
                  'response_time',)


class CaseSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    image = serializers.ImageField()
    description = serializers.CharField(max_length=255)
    link = serializers.URLField(max_length=100)

    class Meta:
        fields = ('image', 'description', 'link',)
        abstract = True

    def create(self, validated_data):
        case = models.Case(**validated_data)
        case.save()
        return case

    def update(self, instance, validated_data):
        instance.image = validated_data.get('image', instance.image)
        instance.description = validated_data.get('description', instance.description)
        instance.link = validated_data.get('link', instance.link)
        instance.save()
        return instance


class SiteSerializer(CaseSerializer):
    class Meta(CaseSerializer.Meta):
        model = models.Site
        fields = CaseSerializer.Meta.fields


class AdvertisementSerializer(CaseSerializer):
    class Meta(CaseSerializer.Meta):
        model = models.Advertisement
        fields = CaseSerializer.Meta.fields


class ApplicationSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    full_name = serializers.CharField(max_length=100,
                                      validators=[validators.validate_full_name])

    telephone_number = serializers.CharField(max_length=constants.VALID_PHONE_NUM_MAX_LEN,
                                             validators=[validators.validate_telephone_number])

    status = serializers.ChoiceField(choices=constants.APPLICATION_STATUS_CHOICES,
                                     read_only=True)

    receipted_time = serializers.DateTimeField(default=timezone.now)

    class Meta:
        model = models.Application
        fields = (
            'id', 'full_name', 'telephone_number', 'status', 'receipted_time', 'response_time',)
