from django.db import models


class CharRace(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name
