from django.db import models
from char_classes.models import CharClass


class Skill(models.Model):
    name = models.CharField(max_length=20)
    char_class = models.ForeignKey(CharClass, on_delete=models.SET_NULL, null=True)
    description = models.CharField(max_length=100)
    firstLevelCost = models.IntegerField(default=1)
    secondLevelCost = models.IntegerField(null=True, blank=True)
