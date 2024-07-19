from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Character
from .serializers import CharacterSerializer
from django.shortcuts import get_object_or_404


class CharactersView(APIView):

    def get(self, request):
        # user_id = 1
        character = get_object_or_404(Character, pk=1)
        # queryset = Character.objects.filter(user_id=user_id)
        serializer = CharacterSerializer(character)
        return Response(serializer.data, status=status.HTTP_200_OK)
