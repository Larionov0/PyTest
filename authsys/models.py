from django.db import models
from django.contrib.auth.models import User
from catalog.models import Pack
from django.utils.timezone import now
from json import loads


class Achievement(models.Model):
    name = models.CharField(max_length=100, default="name")
    condition = models.TextField(default="text that describes achievement")
    reward_json = models.CharField(default="[]", max_length=500, help_text="json rewards")

    def __str__(self):
        return self.name


class PacksAchievement(Achievement):
    pack_set = models.ManyToManyField(Pack)


class MoneyAchievement(Achievement):
    paisons = models.IntegerField(default=1000000)


class CountOfPacksAchievement(Achievement):
    count = models.IntegerField(default=10, help_text="This is count of packs you need to earn")


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

    def check_achievements(self):
        # Checking Count of packs achievements
        for achievement in CountOfPacksAchievement.objects.all():
            if achievement not in self.achievements.all():
                print(1)
                if achievement.count <= self.completed_packs.count():
                    print(2)
                    self.achievements.add(achievement)
                    self.add_reward(achievement.reward_json)

    def add_reward(self, reward_json):
        rewards = loads(reward_json)
        for reward in rewards:
            pass
