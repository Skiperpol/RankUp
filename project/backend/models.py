from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    nick = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    data_urodzenia = models.DateField(blank=True, null=True)
    avatar = models.ImageField(blank=True, default="images/1.png")
    opis = models.TextField('Opis', max_length=500, default='', blank=True)
    punkty = models.IntegerField(default=0)
    
    def __str__(self):
        return self.username


class Powiadomienia(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    tresc = models.TextField()
    druzyna = models.CharField(max_length=100, null=True, blank=True)
    volunteer = models.CharField(max_length=100, null=True, blank=True)
    data = models.DateTimeField(auto_now_add=True)




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

    ilosc_druzyn_format = (
        ('4','4'),
        ('8','8'),
        ('16','16'),
        ('32','32'),
    )

    nazwa = models.CharField(max_length=100, unique=True)
    opis = models.CharField(max_length=200, null=True, blank=True)
    zdjecie = models.ImageField(upload_to='images/', blank=True, default="images/defaulttournament.jpg")
    nagroda = models.CharField(max_length=100, null=True, blank=True)
    data = models.DateTimeField()
    ilosc_druzyn = models.CharField(choices=ilosc_druzyn_format, max_length=100)
    druzyny = models.ManyToManyField('Team',null=True, blank=True)
    # regulamin
    creator = models.EmailField()
    rodzaj_gry = models.CharField(choices=gry, max_length=100)
    format_rozgrywek = models.CharField(choices=formaty, max_length=10)
    rozgrywki = models.ManyToManyField('Rozgrywki',null=True, blank=True)
    started = models.BooleanField(default=False)
    finished = models.BooleanField(default=False)

    def __str__(self):
        return self.nazwa

class Rozgrywki(models.Model):
    nazwa_rozgrywki = models.CharField(max_length=100)
    nazwa_turnieju = models.CharField(max_length=100)
    druzyna1 = models.CharField(max_length=100, null=True, blank=True)
    druzyna2 = models.CharField(max_length=100, null=True, blank=True)
    winner = models.CharField(max_length=100, null=True, blank=True)
    mecz = models.IntegerField(null=True, blank=True)
    faza = models.IntegerField(null=True, blank=True)
    screen_druzyna1 = models.ImageField(upload_to='images/', null=True, blank=True)
    screen_druzyna2 = models.ImageField(upload_to='images/', null=True, blank=True)
    kto_wygral_druzyna1 = models.CharField(max_length=100, null=True, blank=True)
    kto_wygral_druzyna2 = models.CharField(max_length=100, null=True, blank=True)
    message = models.ManyToManyField('Message', null=True, blank=True)

    def __str__(self):
        return self.nazwa_rozgrywki

class Team(models.Model):
    nazwa = models.CharField(max_length=100)
    opis = models.CharField(max_length=200, null=True, blank=True)
    zdjecie = models.ImageField(upload_to='images/', null=True, blank=True, default="images/1.png")
    creator = models.EmailField()
    punkty = models.IntegerField(default=0)
    add_players = models.ManyToManyField('CustomUser', related_name="add_players", null=True, blank=True)
    waiting_list = models.ManyToManyField('CustomUser', related_name="waiting_list", null=True, blank=True)
    remove_players = models.ManyToManyField('CustomUser', related_name="remove_players", null=True, blank=True)
    volunteers = models.ManyToManyField('CustomUser', related_name="volunteers", null=True, blank=True)

    def __str__(self):
        return self.nazwa
    


class Message(models.Model):
    nazwa_rozgrywki = models.CharField(max_length=100, null=True, blank=True)
    kapitan = models.CharField(max_length=100, null=True, blank=True)
    wiadomosci = models.CharField(max_length=100, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date_added',)


        

