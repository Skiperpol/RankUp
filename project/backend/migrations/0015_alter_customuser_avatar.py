# Generated by Django 3.2.11 on 2023-04-01 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0014_merge_20230401_0107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='avatar',
            field=models.ImageField(blank=True, default='images/1.png', null=True, upload_to=''),
        ),
    ]
