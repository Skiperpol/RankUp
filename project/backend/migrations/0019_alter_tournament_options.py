# Generated by Django 3.2.14 on 2023-04-01 22:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0018_auto_20230401_2124'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tournament',
            options={'ordering': ['finished', 'started', 'nazwa']},
        ),
    ]