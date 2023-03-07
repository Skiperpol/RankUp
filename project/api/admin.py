from django.contrib import admin
from api.models import Tournament, Team, Player

class TournamentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Tournament, TournamentAdmin)
class PlayerAdmin(admin.ModelAdmin):
    pass
admin.site.register(Player, PlayerAdmin)
class TeamAdmin(admin.ModelAdmin):
    pass
admin.site.register(Team, TeamAdmin)