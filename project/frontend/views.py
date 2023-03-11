from django.http import HttpResponse, JsonResponse
from django.template import loader
from backend.models import Team, Tournament, CustomUser
from backend.forms import TeamForm


def index(request):
    teams = Team.objects.all()[0:3]
    tournaments = Tournament.objects.all()[0:3]
    players = CustomUser.objects.all()[0:3]

    template = loader.get_template('frontend/index.html')
    context = {
        "teams":teams,
        "tournaments":tournaments,
        "players":players,
    }
    return HttpResponse(template.render(context, request))


from django.contrib.auth import get_user_model
def team_site(request, teamname):
    team = Team.objects.get(nazwa=teamname)

    uzytkownik = get_user_model()
    team2 = Team.objects.get(nazwa=teamname)
    user = uzytkownik.objects.get(email = "dawid@dawid.pl")
    team2.players.add(user)


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
    

       
def tournament_list_site(request):
    tournaments = Tournament.objects.all()

    template = loader.get_template('frontend/tournament_list.html')
    context = {
        "tournaments":tournaments,
    }
    return HttpResponse(template.render(context, request))     



def team_list_site(request):
    teams = Team.objects.all()

    template = loader.get_template('frontend/team_list_site.html')
    context = {
        "teams":teams,
    }
    return HttpResponse(template.render(context, request))

    
def contact_site(request):
    template = loader.get_template('frontend/contact.html')
    context = {
    }
    return HttpResponse(template.render(context, request))