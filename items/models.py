from django.db import models
from django.conf import settings


class WeaponGroup(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class BaseWeapon(models.Model):
    name = models.CharField(max_length=50)
    group = models.ManyToManyField(WeaponGroup, blank=True)
    min_str = models.IntegerField(null=True, blank=True)
    dmg = models.IntegerField(null=True, blank=True)
    attribute = models.CharField(max_length=5, null=True, blank=True)
    weight = models.DecimalField(max_digits=5, decimal_places=1, null=True, blank=True)
    ini_bonus = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name


class CustomWeapon(models.Model):

    name = models.CharField(max_length=50)
    group = models.ManyToManyField(WeaponGroup, blank=True)
    min_str = models.IntegerField(null=True, blank=True)
    dmg = models.IntegerField(null=True, blank=True)
    attribute = models.CharField(max_length=5, null=True, blank=True)
    weight = models.DecimalField(max_digits=5, decimal_places=1, null=True, blank=True)
    ini_bonus = models.IntegerField(null=True, blank=True)
    special = models.CharField(max_length=250, blank=True, null=True)

    character = models.ForeignKey(
        "characters.Character", on_delete=models.CASCADE, related_name="custom_weapons"
    )

    def __str__(self):
        return self.name


class BaseArmor(models.Model):
    name = models.CharField(max_length=50)
    min_str = models.IntegerField(null=True, blank=True)
    armor_bonus = models.IntegerField(null=True, blank=True)
    maneuver_bonus = models.IntegerField(null=True, blank=True)
    weight = models.DecimalField(max_digits=5, decimal_places=1, null=True, blank=True)

    def __str__(self):
        return self.name


class Money(models.Model):
    gf = models.IntegerField(default=0)
    tt = models.IntegerField(default=0)
    kl = models.IntegerField(default=0)
    mu = models.IntegerField(default=0)

    character = models.OneToOneField(
        "characters.Character", on_delete=models.CASCADE, related_name="money"
    )
