from rest_framework import serializers
from .models import CharRace


class CharRaceSerializer(serializers.ModelSerializer):

    class Meta:
        model = CharRace
        fields = "__all__"
