from rest_framework import serializers
from .models import Skill, CustomSkill


class SkillSerializer(serializers.ModelSerializer):

    class Meta:
        model = Skill
        fields = ["id", "name", "description", "first_level_cost", "second_level_cost"]


class CustomSkillSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomSkill
        fields = [
            "id",
            "name",
            "description",
            "first_level_cost",
            "second_level_cost",
            "skill_type",
            "nodes_skilled",
            "character",
        ]
