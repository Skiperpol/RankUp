# Generated by Django 3.2.11 on 2023-03-28 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20230328_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournament',
            name='ilosc_druzyn',
            field=models.CharField(choices=[('League of Legends', 'League of Legends'), ('Valorant', 'Valorant'), ('Counter-Strike: Global Offensive', 'Counter-Strike: Global Offensive')], max_length=100),
        ),
    ]
