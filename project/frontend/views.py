from django.http import HttpResponse, JsonResponse
from django.template import loader
from api.models import Team, Tournament, Player


def index(request):
    teams = Team.objects.all()[0:3]
    tournaments = Tournament.objects.all()[0:3]
    players = Player.objects.all()[0:3]

    template = loader.get_template('frontend/index.html')
    context = {
        "teams":teams,
        "tournaments":tournaments,
        "players":players,
    }
    return HttpResponse(template.render(context, request))


def team_site(request, teamname):
    team = Team.objects.get(nazwa=teamname)

    template = loader.get_template('frontend/team.html')
    context = {
        "team":team,
    }
    return HttpResponse(template.render(context, request))
    
def tournament_site(request, tournamentname):
    tournament = Tournament.objects.get(nazwa=tournamentname)

    template = loader.get_template('frontend/tournament.html')
    context = {
        "tournament":tournament,
    }
    return HttpResponse(template.render(context, request))
    
def player_site(request, playername):
    player = Player.objects.get(nick=playername)

    template = loader.get_template('frontend/player.html')
    context = {
        "player":player,
    }
    return HttpResponse(template.render(context, request))

       
def tournament_list_site(request):
    tournaments = Tournament.objects.all()

    template = loader.get_template('frontend/tournament_list.html')
    context = {
        "tournaments":tournaments,
    }
    return HttpResponse(template.render(context, request))     

def player_list_site(request):
    players = Player.objects.all()

    template = loader.get_template('frontend/players_list.html')
    context = {
        "players":players,
    }
    return HttpResponse(template.render(context, request))


def team_list_site(request):
    teams = Team.objects.all()

    template = loader.get_template('frontend/team_list_site.html')
    context = {
        "teams":teams,
    }
    return HttpResponse(template.render(context, request))