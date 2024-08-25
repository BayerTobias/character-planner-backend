from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import CharRace
from .serializers import CharRaceSerializer


class RaceListView(APIView):

    def get(self, request):

        queryset = CharRace.objects.all()
        serializer = CharRaceSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
