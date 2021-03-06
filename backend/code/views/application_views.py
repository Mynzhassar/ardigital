from datetime import datetime
from django.http import Http404

from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView

from .. import serializers, models


@api_view(['GET'])
@permission_classes([permissions.IsAdminUser])
def list_applications(request):
    objects = models.Application.objects.all()
    serializer = serializers.ApplicationSerializer(objects, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def add_application(request):
    serializer = serializers.ApplicationSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EditApplication(APIView):
    permission_classes = (permissions.IsAdminUser,)

    def get_object(self, pk):
        try:
            return models.Application.objects.get(pk=pk)
        except models.Application.DoesNotExist:
            raise Http404

    def put(self, request, pk):
        application = self.get_object(pk)
        serializer = serializers.ApplicationSerializer(application, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        application = self.get_object(pk)
        application.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
