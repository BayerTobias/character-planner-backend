from django.db import models


# Create your models here.
class CharClass(models.Model):
    name = models.CharField(max_length=25)
