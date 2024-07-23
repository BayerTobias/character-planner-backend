from django.contrib import admin
from .models import Skill

# Register your models here.


class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "char_class", "description")
    list_display_links = ("name", "char_class", "description")


admin.site.register(Skill, SkillAdmin)
