# Generated by Django 3.2.14 on 2023-03-12 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_auto_20230312_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='zdjecie',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='zdjecie',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
