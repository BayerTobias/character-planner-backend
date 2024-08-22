from django.contrib import admin
from .models import BaseWeapon, CustomWeapon, WeaponGroup, BaseArmor, Money


class BaseWeaponAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")


class CustomWeaponAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")


class BaseArmorAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")


class WeaponGroupAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")


class MoneyAdmin(admin.ModelAdmin):
    list_display = ("id", "character")
    list_display_links = ("id", "character")


admin.site.register(BaseWeapon, BaseWeaponAdmin)
admin.site.register(CustomWeapon, CustomWeaponAdmin)
admin.site.register(BaseArmor, BaseArmorAdmin)
admin.site.register(WeaponGroup, WeaponGroupAdmin)
admin.site.register(Money, MoneyAdmin)
