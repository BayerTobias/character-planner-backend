from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser


class CustomUser(AbstractUser):
    test = models.CharField(max_length=15, null=True, blank=True)
