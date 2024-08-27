from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import CharClass
from .serializers import CharClassSerializer, CharClassDetailsSerializer
from django.shortcuts import get_object_or_404


class CharClassView(APIView):

    def get(self, request):

        queryset = CharClass.objects.all()
        serializer = CharClassSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CharClassDetailsView(APIView):

    def get(self, request, id):

        char_class = get_object_or_404(CharClass, pk=id)
        serialiter = CharClassDetailsSerializer(char_class)
        return Response(serialiter.data, status=status.HTTP_200_OK)
