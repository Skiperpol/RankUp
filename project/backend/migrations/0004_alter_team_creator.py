# Generated by Django 3.2.14 on 2023-03-11 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_auto_20230311_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='creator',
            field=models.EmailField(max_length=254),
        ),
    ]
