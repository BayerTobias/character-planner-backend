from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .models import Character
from .serializers import (
    CharacterSerializer,
    CharacterListSerializer,
    CreateCharacterSerializer,
)
from django.shortcuts import get_object_or_404


class CharactersView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = CreateCharacterSerializer(
            data=request.data, context={"request": request}
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, character_id=None):
        if character_id:
            character = get_object_or_404(Character, pk=character_id)
            serializer = CharacterSerializer(character)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            queryset = Character.objects.filter(user=request.user)
            serializer = CharacterListSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
