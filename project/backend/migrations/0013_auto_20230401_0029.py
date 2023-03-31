# Generated by Django 3.2.11 on 2023-03-31 22:29

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0012_auto_20230331_1109'),
    ]

    operations = [
        migrations.AddField(
            model_name='powiadomienia',
            name='volunteer',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='volunteers',
            field=models.ManyToManyField(blank=True, null=True, related_name='volunteers', to=settings.AUTH_USER_MODEL),
        ),
    ]
