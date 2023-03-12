from django.urls import path
from .views import index, team_site, tournament_site, tournament_list_site, team_list_site, contact_site
from backend.views import register, main, login_web, logout_view, settings, player_site, player_list_site, create_team, create_tournament

urlpatterns = [
    path('', index, name='index'),
    path("team/<teamname>/", team_site, name="team_site"),
    path("tournament/<tournamentname>/", tournament_site, name="tournament_site"),
    path("player/<playernick>/", player_site, name="player_site"),
    path("tournaments/", tournament_list_site, name="tournament_list_site"),
    path("players/", player_list_site, name="player_list_site"),
    path("teams/", team_list_site, name="team_list_site"),
    path("contact/", contact_site, name="contact_site"),
    path("create_team/", create_team, name="create_team"),
    path("create_tournament/", create_tournament, name="create_tournament"),



    path('main/', main, name='main'),
    path('login_web/', login_web, name='login_web'),
    path('register/', register, name='register'),

    path('logout/', logout_view, name='logout'),
    path('profile/<nick>', player_site, name='profile'),
    path('settings', settings, name='settings'),
]







