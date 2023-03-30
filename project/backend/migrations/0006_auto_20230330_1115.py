# Generated by Django 3.2.14 on 2023-03-30 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_rename_powiadomienie_powiadomienia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='avatar',
            field=models.ImageField(blank=True, default='images/1.png', upload_to=''),
        ),
        migrations.AlterField(
            model_name='team',
            name='zdjecie',
            field=models.ImageField(blank=True, default='images/1.png', null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='zdjecie',
            field=models.ImageField(blank=True, default='images/defaulttournament.jpg', upload_to='images/'),
        ),
    ]
