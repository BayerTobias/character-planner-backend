from django.contrib import admin
from .models import CharRace


class CharRaceAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")


admin.site.register(CharRace, CharRaceAdmin)
