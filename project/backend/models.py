from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class CustomUser(AbstractUser):
    nick = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    data_urodzenia = models.DateField(blank=True, null=True)
    avatar = models.ImageField(blank=True)
    opis = models.TextField('Opis', max_length=500, default='', blank=True)
    punkty = models.IntegerField(default=0)
    
    def __str__(self):
        return self.username







class Tournament(models.Model):
    gry = (
        ('League of Legends', 'League of Legends'),
        ('Valorant', 'Valorant'),
        ('Counter-Strike: Global Offensive', 'Counter-Strike: Global Offensive'),
    )
    formaty = (
        ('5vs5','5vs5'),
        ('2vs2','2vs2'),
        ('1vs1','1vs1'),
    )

    nazwa = models.CharField(max_length=100, unique=True)
    opis = models.CharField(max_length=200, null=True, blank=True)
    zdjecie = models.ImageField(upload_to='images/', blank=True, default="images/1.png")
    nagroda = models.CharField(max_length=100, null=True, blank=True)
    data = models.DateTimeField()
    ilosc_druzyn = models.IntegerField(validators=[MaxValueValidator(32), MinValueValidator(4)])
    druzyny = models.ManyToManyField('Team',null=True, blank=True)
    # regulamin
    creator = models.EmailField()
    rodzaj_gry = models.CharField(choices=gry, max_length=100)
    format_rozgrywek = models.CharField(choices=formaty, max_length=10)

    def __str__(self):
        return self.nazwa

class Team(models.Model):
    nazwa = models.CharField(max_length=100)
    opis = models.CharField(max_length=200, null=True, blank=True)
    zdjecie = models.ImageField(upload_to='images/', null=True, blank=True)
    creator = models.EmailField()
    punkty = models.IntegerField(default=0)
    players = models.ManyToManyField('CustomUser')

    def __str__(self):
        return self.nazwa

        

