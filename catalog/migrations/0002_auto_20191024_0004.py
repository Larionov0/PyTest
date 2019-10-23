# Generated by Django 2.2.6 on 2019-10-23 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='count_of_correct',
            field=models.IntegerField(default=0, help_text='Count of correct answers'),
        ),
        migrations.AddField(
            model_name='question',
            name='count_of_incorrect',
            field=models.IntegerField(default=0, help_text='Count of incorrect answers'),
        ),
    ]
