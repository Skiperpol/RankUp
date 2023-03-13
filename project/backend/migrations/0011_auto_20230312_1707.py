# Generated by Django 3.2.11 on 2023-03-12 16:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0010_merge_20230312_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournament',
            name='ilosc_druzyn',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(32), django.core.validators.MinValueValidator(4)]),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='zdjecie',
            field=models.ImageField(blank=True, default='images/1.png', upload_to='images/'),
        ),
    ]
