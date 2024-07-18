from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import CharClass
from .serializers import CharClassSerializer


class CharClassView(APIView):

    def get(self, request):

        queryset = CharClass.objects.all()
        serializer = CharClassSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
