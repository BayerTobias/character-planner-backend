from django.db import models


class Skill(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    firstLevelCost = models.IntegerField(default=1)
    secondLevelCost = models.IntegerField(default=2, null=True)
