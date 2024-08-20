from django.contrib import admin
from .models import BaseWeapon, CustomWeapon, WeaponGroup


class BaseWeaponAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")


class CustomWeaponAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")


class WeaponGroupAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")


admin.site.register(BaseWeapon, BaseWeaponAdmin)
admin.site.register(CustomWeapon, CustomWeaponAdmin)
admin.site.register(WeaponGroup, WeaponGroupAdmin)
