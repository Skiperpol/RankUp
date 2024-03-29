# Generated by Django 3.2.11 on 2023-03-31 08:59

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0010_powiadomienia_druzyna'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='players',
        ),
        migrations.AddField(
            model_name='team',
            name='add_players',
            field=models.ManyToManyField(related_name='add_players', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='team',
            name='remove_players',
            field=models.ManyToManyField(related_name='remove_players', to=settings.AUTH_USER_MODEL),
        ),
    ]
