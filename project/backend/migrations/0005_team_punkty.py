# Generated by Django 3.2.11 on 2023-03-11 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_alter_team_creator'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='punkty',
            field=models.IntegerField(default=0),
        ),
    ]