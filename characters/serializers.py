from rest_framework import serializers
from .models import Character, CharacterSkill
from char_classes.serializers import CharClassDetailsSerializer
from char_races.serializers import CharRaceSerializer
from skills.serializers import CustomSkillSerializer


class CharacterSkillSerializer(serializers.ModelSerializer):

    class Meta:
        model = CharacterSkill
        fields = ("id", "skill", "nodes_skilled")


class CharacterSerializer(serializers.ModelSerializer):

    char_class = CharClassDetailsSerializer(read_only=True)
    char_skilled_skills = CharacterSkillSerializer(many=True, read_only=True)
    custom_skills = CustomSkillSerializer(many=True, read_only=True)
    race = CharRaceSerializer(read_only=True)

    class Meta:
        model = Character
        fields = "__all__"


class CharacterListSerializer(serializers.ModelSerializer):
    race_name = serializers.CharField(source="race.name", read_only=True)
    char_class_name = serializers.CharField(source="char_class.name", read_only=True)

    # evtl nur ids und im frontend verbinden
    class Meta:
        model = Character
        fields = ["id", "name", "race_name", "char_class_name"]
