from django.db import models


class CharClass(models.Model):
    STAT_CHOICES = [
        ("strength", "Strength"),
        ("agility", "Agility"),
        ("constitution", "Constitution"),
        ("intelligence", "Intelligence"),
        ("charisma", "Charisma"),
    ]

    name = models.CharField(max_length=25)
    base_lvl_hp = models.IntegerField(default=1)
    base_lvl_mana = models.IntegerField(null=True, blank=True)
    main_stat = models.CharField(
        max_length=20, choices=STAT_CHOICES, null=True, blank=True
    )
    color = models.CharField(max_length=25)

    def __str__(self):
        return self.name
