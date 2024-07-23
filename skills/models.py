from django.db import models
from char_classes.models import CharClass


class Skill(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    first_level_cost = models.IntegerField(default=1)
    second_level_cost = models.IntegerField(null=True, blank=True)
    char_class = models.ForeignKey(
        CharClass, on_delete=models.SET_NULL, null=True, related_name="skills"
    )

    def __str__(self):
        return f"{self.name} - {self.char_class.name}"


class CustomSkill(models.Model):
    skill_type_choices = [
        ("knowledge", "Knowledge"),
        ("weapon", "Weapon"),
        ("spell_list", "Spell List"),
    ]

    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    first_level_cost = models.IntegerField(default=1)
    second_level_cost = models.IntegerField(null=True, blank=True)
    skill_type = models.CharField(max_length=20, choices=skill_type_choices)
    nodes_skilled = models.IntegerField(null=True, blank=True)
    character = models.ForeignKey(
        "characters.Character", models.CASCADE, related_name="custom_skills"
    )

    def __str__(self) -> str:
        return self.name
