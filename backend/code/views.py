import logging

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from . import models, serializers, constants, notifications

LOGGER = logging.getLogger(__name__)


@api_view(['GET'])
def list_profits(request):
    objects = models.Profit.objects.all()
    serializer = serializers.ProfitSerializer(objects, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def list_services(request):
    objects = models.Service.objects.all()
    serializer = serializers.ServiceSerializer(objects, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def add_consultation(request, pk):
    data = {
        'service_id': pk,
        'full_name': request.data['full_name'],
        'telephone_number': request.data['telephone_number'],
        'email': request.data['email'],
    }
    serializer = serializers.ConsultationSerializer(data=data)

    if serializer.is_valid():
        serializer.save()
        notifications.send_email(constants.CONSULTATION_EMAIL_CONTENT, request.data['email'])
        LOGGER.info('consultation_email_sent')
        return Response(status=status.HTTP_201_CREATED)

    LOGGER.error('failed_to_add_consultation', extra={
        'errors': serializer.errors,
    })
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def list_sites(request):
    objects = models.Site.objects.all()
    serializer = serializers.SiteSerializer(objects, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def list_advertisements(request):
    objects = models.Advertisement.objects.all()
    serializer = serializers.AdvertisementSerializer(objects, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def add_application(request):
    serializer = serializers.ApplicationSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        notifications.send_email(constants.APPLICATION_EMAIL_CONTENT, request.data['email'])
        LOGGER.info('application_email_sent')
        return Response(status=status.HTTP_201_CREATED)

    LOGGER.error('failed_to_add_application', extra={
        'errors': serializer.errors,
    })
    return Response(status=status.HTTP_400_BAD_REQUEST)
