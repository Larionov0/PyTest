# Generated by Django 2.2.6 on 2019-10-31 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_pack_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='pack',
            name='pack_class',
            field=models.CharField(default='0', max_length=30),
        ),
    ]
