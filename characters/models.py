from django.db import models
from django.conf import settings


class Character(models.Model):
    # SETUP AS MODEL
    RACE_CHOICES = [
        ("gnome", "Gnome"),
        ("dwarf", "Dwarf"),
        ("elf", "Elf"),
        ("human", "Human"),
        # Weitere Rassen hier hinzufügen
    ]

    # SETUP AS MODEL
    CLASS_CHOICES = [("mage", "Mage")]

    name = models.CharField(max_length=25)
    race = models.CharField(max_length=50, choices=RACE_CHOICES)
    char_class = models.CharField(max_length=50, choices=CLASS_CHOICES)

    strength_value = models.IntegerField()
    agility_value = models.IntegerField()
    constitution_value = models.IntegerField()
    intelligence_value = models.IntegerField()
    charisma_value = models.IntegerField()

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="characters"
    )

    def __str__(self):
        return self.name
