from django.contrib import admin
from .models import Character


class CharacterAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "user")
    list_display_links = ("id", "name", "user")


admin.site.register(Character, CharacterAdmin)
