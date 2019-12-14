# Generated by Django 2.2.6 on 2019-10-31 10:11

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authsys', '0002_auto_20191029_1856'),
    ]

    operations = [
        migrations.CreateModel(
            name='CountOfPacksAchievement',
            fields=[
                ('achievement_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='authsys.Achievement')),
                ('count', models.IntegerField(default=10, help_text='This is count of packs you need to earn')),
            ],
            bases=('authsys.achievement',),
        ),
        migrations.AlterField(
            model_name='failedpack',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 31, 10, 11, 24, 44192, tzinfo=utc)),
        ),
    ]
