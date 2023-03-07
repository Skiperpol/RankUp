from django.db import models

class Tournament(models.Model):
    nazwa = models.CharField(max_length=100)
    zdjecie = models.ImageField(upload_to='images/', null=True, blank=True)
   
    def __str__(self):
        return self.nazwa

class Team(models.Model):
    nazwa = models.CharField(max_length=100)
    opis = models.CharField(max_length=100, null=True, blank=True)
    zdjecie = models.ImageField(upload_to='images/', null=True, blank=True)
   
    def __str__(self):
        return self.nazwa

class Player(models.Model):
    imie = models.CharField(max_length=100)
    nazwisko = models.CharField(max_length=100)
    nick = models.CharField(max_length=100)
    druzyna = models.ManyToManyField(Team, null=True, blank=True)
    zdjecie = models.ImageField(upload_to='images/', null=True, blank=True)
   
    def __str__(self):
        return self.nick


        

