from rest_framework import serializers
from .models import BaseWeapon, CustomWeapon, WeaponGroup, BaseArmor, Money


class WeaponGroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = WeaponGroup
        fields = "__all__"


class BaseWeaponSerializer(serializers.ModelSerializer):
    group = WeaponGroupSerializer(many=True, read_only=True)

    class Meta:
        model = BaseWeapon
        fields = "__all__"


class CustomWeaponSerializer(serializers.ModelSerializer):
    group = WeaponGroupSerializer(many=True, read_only=True)

    class Meta:
        model = CustomWeapon
        fields = "__all__"


class BaseArmorSerializer(serializers.ModelSerializer):

    class Meta:
        model = BaseArmor
        fields = "__all__"


class MoneySerializer(serializers.ModelSerializer):

    class Meta:
        model = Money
        fields = "__all__"
