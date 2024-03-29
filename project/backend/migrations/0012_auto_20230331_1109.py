# Generated by Django 3.2.11 on 2023-03-31 09:09

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0011_auto_20230331_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='add_players',
            field=models.ManyToManyField(blank=True, null=True, related_name='add_players', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='team',
            name='remove_players',
            field=models.ManyToManyField(blank=True, null=True, related_name='remove_players', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='team',
            name='waiting_list',
            field=models.ManyToManyField(blank=True, null=True, related_name='waiting_list', to=settings.AUTH_USER_MODEL),
        ),
    ]
