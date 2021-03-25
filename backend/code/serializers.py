from rest_framework import serializers

from . import models, validators, constants


class ProfitSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = models.Profit
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = models.Service
        fields = '__all__'


class ConsultationSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    service_id = serializers.IntegerField(write_only=True)
    full_name = serializers.CharField(validators=[validators.validate_full_name])
    telephone_number = serializers.CharField(validators=[validators.validate_telephone_number])
    email = serializers.CharField(validators=[validators.validate_email_address])
    status = serializers.ChoiceField(read_only=True,
                                     choices=constants.APPLICATION_STATUS_CHOICES,)

    class Meta:
        model = models.Consultation
        fields = ('id', 'service_id', 'full_name', 'telephone_number', 'email', 'status',
                  'receipted_time', 'response_time',)


class CaseSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    image = serializers.ImageField()
    description = serializers.CharField()
    link = serializers.URLField()

    class Meta:
        fields = '__all__'
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
    full_name = serializers.CharField(validators=[validators.validate_full_name])
    telephone_number = serializers.CharField(validators=[validators.validate_telephone_number])
    email = serializers.CharField(validators=[validators.validate_email_address])
    status = serializers.ChoiceField(read_only=True,
                                     choices=constants.APPLICATION_STATUS_CHOICES,)

    class Meta:
        model = models.Application
        fields = '__all__'
