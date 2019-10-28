from django.db import models
from django.contrib.auth.models import User
from catalog.models import Pack


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    completed_packs = models.ManyToManyField(Pack)
    paisons = models.IntegerField(default=0)
