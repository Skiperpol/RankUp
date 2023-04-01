# Generated by Django 3.2.11 on 2023-03-31 08:02

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0008_merge_20230331_0933'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='waiting_list',
            field=models.ManyToManyField(related_name='waiting_list', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='team',
            name='players',
            field=models.ManyToManyField(related_name='players', to=settings.AUTH_USER_MODEL),
        ),
    ]