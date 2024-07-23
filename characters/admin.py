from django.contrib import admin
from .models import Character, CharacterSkill


class CharacterAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "user")
    list_display_links = ("id", "name", "user")


class CharacterSkillAdmin(admin.ModelAdmin):
    list_display = ("character", "skill", "nodes_skilled")
    list_display_links = ("character", "skill", "nodes_skilled")


admin.site.register(Character, CharacterAdmin)
admin.site.register(CharacterSkill, CharacterSkillAdmin)
