from rest_framework import serializers
from .models import CharClass
from skills.serializers import SkillSerializer


class CharClassDetailsSerializer(serializers.ModelSerializer):

    skills = SkillSerializer(many=True, read_only=True)

    class Meta:
        model = CharClass
        fields = ["id", "name", "base_lvl_hp", "base_lvl_mana", "skills"]


class CharClassSerializer(serializers.ModelSerializer):

    class Meta:
        model = CharClass
        fields = ["id", "name", "base_lvl_hp", "base_lvl_mana"]
