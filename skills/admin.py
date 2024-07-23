from django.contrib import admin
from .models import Skill, CustomSkill

# Register your models here.


class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "char_class", "description")
    list_display_links = ("name", "char_class", "description")


class CustomSkillAdmin(admin.ModelAdmin):
    list_display = ("name", "character", "description")
    list_display_links = ("name", "character", "description")


admin.site.register(Skill, SkillAdmin)
admin.site.register(CustomSkill, CustomSkillAdmin)
