from django.contrib import admin
from .models import CharClass


class CharClassAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")


admin.site.register(CharClass, CharClassAdmin)
