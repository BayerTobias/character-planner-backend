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
