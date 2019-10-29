from django.db import models
from django.contrib.auth.models import User
from catalog.models import Pack
from django.utils.timezone import now


class Achievement(models.Model):
    name = models.CharField(max_length=100, default="name")
    condition = models.TextField(default="text that describes achievement")

    def __str__(self):
        return self.name


class PacksAchievement(Achievement):
    pack_set = models.ManyToManyField(Pack)


class MoneyAchievement(Achievement):
    paisons = models.IntegerField(default=1000000)


class FailedPack(models.Model):
    pack = models.ForeignKey(Pack, on_delete=models.CASCADE, default=0)
    date = models.DateTimeField(default=now())

    def __str__(self):
        return self.pack.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=0)
    completed_packs = models.ManyToManyField(Pack, blank=True, related_name="completed_users")
    failed_packs = models.ManyToManyField(FailedPack, blank=True, related_name="failed_users")
    paisons = models.IntegerField(default=0)
    achievements = models.ManyToManyField(Achievement, blank=True)

    def __str__(self):
        return self.user.username + f"({self.paisons})"
