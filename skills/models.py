from django.db import models
from char_classes.models import CharClass


class Skill(models.Model):
    name = models.CharField(max_length=20)
    char_class = models.ForeignKey(
        CharClass, on_delete=models.SET_NULL, null=True, related_name="skills"
    )
    description = models.CharField(max_length=100)
    first_level_cost = models.IntegerField(default=1)
    second_level_cost = models.IntegerField(null=True, blank=True)
