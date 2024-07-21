from rest_framework import serializers
from .models import Character
from char_classes.serializers import CharClassDetailsSerializer
from char_races.serializers import CharRaceSerializer


class CharacterSerializer(serializers.ModelSerializer):

    char_class = CharClassDetailsSerializer(read_only=True)
    race = CharRaceSerializer(read_only=True)

    class Meta:
        model = Character
        fields = "__all__"
