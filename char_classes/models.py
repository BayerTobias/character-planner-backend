from django.db import models


# Create your models here.
class CharClass(models.Model):
    name = models.CharField(max_length=25)
    base_lvl_hp = models.IntegerField(default=1)
    base_lvl_mana = models.IntegerField(default=1)

    def __str__(self):
        return self.name
