from rest_framework import serializers
from .models import BaseWeapon, CustomWeapon, WeaponGroup


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
