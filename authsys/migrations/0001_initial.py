# Generated by Django 2.2.6 on 2019-10-28 21:43

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catalog', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='name', max_length=100)),
                ('condition', models.TextField(default='text that describes achievement')),
            ],
        ),
        migrations.CreateModel(
            name='FailedPack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=datetime.datetime(2019, 10, 28, 23, 43, 27, 54674))),
                ('pack', models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to='catalog.Pack')),
            ],
        ),
        migrations.CreateModel(
            name='MoneyAchievement',
            fields=[
                ('achievement_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='authsys.Achievement')),
                ('paisons', models.IntegerField(default=1000000)),
            ],
            bases=('authsys.achievement',),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paisons', models.IntegerField(default=0)),
                ('achievements', models.ManyToManyField(blank=True, to='authsys.Achievement')),
                ('completed_packs', models.ManyToManyField(blank=True, related_name='completed_users', to='catalog.Pack')),
                ('failed_packs', models.ManyToManyField(blank=True, related_name='failed_users', to='authsys.FailedPack')),
                ('user', models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PacksAchievement',
            fields=[
                ('achievement_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='authsys.Achievement')),
                ('pack_set', models.ManyToManyField(to='catalog.Pack')),
            ],
            bases=('authsys.achievement',),
        ),
    ]
