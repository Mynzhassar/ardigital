from django.http import Http404

from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView

from .. import serializers, models


@api_view(['GET'])
def list_services(request):
    objects = models.Service.objects.all()
    serializer = serializers.ServiceSerializer(objects, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes(permissions.IsAdminUser)
def add_service(request):
    serializer = serializers.ServiceSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EditService(APIView):
    permission_classes = permissions.IsAdminUser

    def get_object(self, pk):
        try:
            return models.Service.objects.get(pk=pk)
        except models.Service.DoesNotExist:
            raise Http404

    def put(self, request, pk):
        profit = self.get_object(pk)
        serializer = serializers.ServiceSerializer(profit, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        profit = self.get_object(pk)
        profit.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
