from django.db import models
from django.conf import settings
from char_classes.models import CharClass
from char_races.models import CharRace
from skills.models import Skill


class Character(models.Model):

    name = models.CharField(max_length=25)
    race = models.ForeignKey(CharRace, on_delete=models.SET_NULL, null=True)
    char_class = models.ForeignKey(CharClass, on_delete=models.SET_NULL, null=True)

    strength_value = models.IntegerField()
    strength_bonus = models.IntegerField()
    agility_value = models.IntegerField()
    agility_bonus = models.IntegerField()
    constitution_value = models.IntegerField()
    constitution_bonus = models.IntegerField()
    intelligence_value = models.IntegerField()
    intelligence_bonus = models.IntegerField()
    charisma_value = models.IntegerField()
    charisma_bonus = models.IntegerField()

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="characters"
    )

    def __str__(self):
        return self.name


class CharacterSkill(models.Model):
    character = models.ForeignKey(
        Character, on_delete=models.CASCADE, related_name="char_skilled_skills"
    )
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    nodes_skilled = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.character.name} - {self.skill.name} (Level {self.nodes_skilled})"
