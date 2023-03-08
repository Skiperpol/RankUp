from django.urls import path
from .views import index, team_site, tournament_site, player_site, tournament_list_site, player_list_site, team_list_site, contact_site

urlpatterns = [
    path('', index, name='index'),
    path("team/<teamname>/", team_site, name="team_site"),
    path("tournament/<tournamentname>/", tournament_site, name="tournament_site"),
    path("player/<playername>/", player_site, name="player_site"),
    path("tournaments/", tournament_list_site, name="tournament_list_site"),
    path("players/", player_list_site, name="player_list_site"),
    path("teams/", team_list_site, name="team_list_site"),
    path("contact/", contact_site, name="contact_site"),
]