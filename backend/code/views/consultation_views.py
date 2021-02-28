from datetime import datetime
from django.http import Http404

from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView

from .. import serializers, models


@api_view(['GET'])
@permission_classes(permissions.IsAdminUser)
def list_consultations(request):
    objects = models.Consultation.objects.all()
    serializer = serializers.ConsultationSerializer(objects, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def add_consultation(request):
    serializer = serializers.ConsultationSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EditConsultation(APIView):
    permission_classes = permissions.IsAdminUser

    def get_object(self, pk):
        try:
            return models.Consultation.objects.get(pk=pk)
        except models.Consultation.DoesNotExist:
            raise Http404

    def put(self, request, pk):
        consultation = self.get_object(pk)
        serializer = serializers.ServiceSerializer(consultation, data=request.data)

        if serializer.is_valid():
            if serializer.data.status == 'PROCESSED':
                consultation.response_time = datetime.now()
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        consultation = self.get_object(pk)
        consultation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
