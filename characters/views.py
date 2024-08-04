from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .models import Character
from .serializers import CharacterSerializer, CharacterListSerializer
from django.shortcuts import get_object_or_404


class CharactersView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, character_id=None):
        if character_id:
            character = get_object_or_404(Character, pk=character_id)
            serializer = CharacterSerializer(character)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            queryset = Character.objects.filter(user=request.user)
            serializer = CharacterListSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
