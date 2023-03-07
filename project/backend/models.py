from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    nick = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    data_urodzenia = models.DateField(blank=True, null=True)
    avatar = models.ImageField(blank=True)
    opis = models.TextField('Opis', max_length=500, default='', blank=True)
    punkty = models.IntegerField(default=0)
    
    def __str__(self):
        return self.username