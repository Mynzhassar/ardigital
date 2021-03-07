from django.http import Http404

from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView

from .. import models, serializers


@api_view(['GET'])
def list_advertisements(request):
    objects = models.Advertisement.objects.all()
    serializer = serializers.AdvertisementSerializer(objects, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([permissions.IsAdminUser])
def add_advertisement(request):
    serializer = serializers.AdvertisementSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EditAdvertisement(APIView):
    permission_classes = (permissions.IsAdminUser, )

    def get_object(self, pk):
        try:
            return models.Advertisement.objects.get(pk=pk)
        except models.Advertisement.DoesNotExist:
            raise Http404

    def put(self, request, pk):
        advertisement = self.get_object(pk)
        serializer = serializers.AdvertisementSerializer(advertisement, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        advertisement = self.get_object(pk)
        advertisement.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
