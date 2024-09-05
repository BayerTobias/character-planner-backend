from rest_framework import serializers
from .models import Character, CharacterSkill, CharRace, CharClass
from char_classes.serializers import CharClassDetailsSerializer
from char_races.serializers import CharRaceSerializer
from skills.serializers import CustomSkillSerializer
from items.models import BaseWeapon, CustomWeapon, WeaponGroup, BaseArmor, Money
from items.serializers import (
    BaseWeaponSerializer,
    CustomWeaponSerializer,
    BaseArmorSerializer,
    MoneySerializer,
)


class CharacterSkillSerializer(serializers.ModelSerializer):

    class Meta:
        model = CharacterSkill
        fields = ("id", "skill", "nodes_skilled")


class CharacterSerializer(serializers.ModelSerializer):

    char_class = CharClassDetailsSerializer(read_only=True)
    char_skilled_skills = CharacterSkillSerializer(many=True, read_only=True)
    custom_skills = CustomSkillSerializer(many=True, read_only=True)
    race = CharRaceSerializer(read_only=True)
    base_weapons = BaseWeaponSerializer(many=True, read_only=True)
    custom_weapons = CustomWeaponSerializer(many=True, read_only=True)
    armor = BaseArmorSerializer(read_only=True)
    money = MoneySerializer(read_only=True)

    class Meta:
        model = Character
        fields = "__all__"

    # def get_custom_weapons(self, obj):

    #     custom_weapons = obj.custom_weapons.all()
    #     return CustomWeaponSerializer(custom_weapons, many=True).data


class CreateCharacterSerializer(serializers.ModelSerializer):

    race = serializers.PrimaryKeyRelatedField(queryset=CharRace.objects.all())
    char_class = serializers.PrimaryKeyRelatedField(queryset=CharClass.objects.all())
    base_weapons = serializers.PrimaryKeyRelatedField(
        queryset=BaseWeapon.objects.all(), many=True, allow_null=True, required=False
    )
    armor = serializers.PrimaryKeyRelatedField(
        queryset=BaseArmor.objects.all(), allow_null=True, required=False
    )
    user = serializers.PrimaryKeyRelatedField(read_only=True)  # User als read-only
    # money = MoneySerializer()

    class Meta:
        model = Character
        fields = "__all__"

    def create(self, validated_data):

        base_weapons_data = validated_data.pop("base_weapons", [])
        user = self.context["request"].user
        character = Character.objects.create(user=user, **validated_data)
        character.base_weapons.set(base_weapons_data)

        return character


class CharacterListSerializer(serializers.ModelSerializer):
    race_name = serializers.CharField(source="race.name", read_only=True)
    char_class_name = serializers.CharField(source="char_class.name", read_only=True)

    # evtl nur ids und im frontend verbinden
    class Meta:
        model = Character
        fields = ["id", "name", "race_name", "char_class_name"]
