from django.contrib import admin
from .models import CustomUser, Tournament, Team, Rozgrywki, Message, Powiadomienia,Problemy


admin.site.register(CustomUser)
admin.site.register(Tournament)
admin.site.register(Team)
admin.site.register(Rozgrywki)
admin.site.register(Message)
admin.site.register(Powiadomienia)
admin.site.register(Problemy)

# @admin.register(Tournament)
# class TournamentAdmin(admin.ModelAdmin):
#     list_display = ("gry", "formaty", "ilosc_druzyn_format", "nazwa", "opis", "zdjecie", "nagroda", "data", "ilosc_druzyn", "creator", "rodzaj_gry", "format_rozgrywek", "winner", "started", "finished")
#     list_filter = ("nazwa", "opis", "zdjecie", "nagroda", "data", "ilosc_druzyn", "druzyny", "creator", "rodzaj_gry", "format_rozgrywek", "rozgrywki", "winner", "started", "finished")

