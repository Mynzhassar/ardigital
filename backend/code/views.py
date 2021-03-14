from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from . import models, serializers


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
    }
    serializer = serializers.ConsultationSerializer(data=data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)