from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect
from django.template import loader
from backend.models import Team, Tournament, CustomUser, Rozgrywki
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
    users = CustomUser.objects.filter()
    creator_mail = team.creator
    creator = CustomUser.objects.get(email=creator_mail)

    if request.method == 'POST':
        type = request.POST.get('type')
        email = request.POST.get('email')
        if type == "delete":
            user = get_user_model().objects.get(email=email)
            team.players.remove(user)
            return redirect('team_site', teamname=teamname)
        elif type == "add":
            user = get_user_model().objects.get(email=email)
            team.players.add(user)
            return redirect('team_site', teamname=teamname)

    new_users = []
    for user in users:
        nalezy = False
        for team_user in team.players.all():
            if user.nick == team_user.nick:
                nalezy = True
        if nalezy == False:
            if team.creator != user.email:
                new_users.append(user)

    template = loader.get_template('frontend/team.html')
    context = {
        "team":team,
        "users": new_users,
        "creator": creator,
    }
    return HttpResponse(template.render(context, request))
    


def tworzenie_rozgrywek(ilosc_faz, max_ilosc_druzyn, lista_druzyn, turniej, ilosc_druzyn):
    nazwa_turnieju=turniej.nazwa
    faza_0 = max_ilosc_druzyn/2
    roznica = ilosc_druzyn-faza_0
    i=0
    for y in range(int(faza_0)):
            if y<roznica:
                rozgrywka = Rozgrywki(nazwa_rozgrywki="Mecz "+str(y)+" faza 0",nazwa_turnieju=nazwa_turnieju, druzyna1=lista_druzyn[i], druzyna2=lista_druzyn[i+1], mecz=y ,faza=0)
                i=i+2
                rozgrywka.save()
                turniej.rozgrywki.add(rozgrywka)
            else:
                rozgrywka = Rozgrywki(nazwa_rozgrywki="Mecz "+str(y)+" faza 0",nazwa_turnieju=nazwa_turnieju, druzyna1=lista_druzyn[i], druzyna2="Walkower", mecz=y ,faza=0,winner=lista_druzyn[i])
                i=i+1
                rozgrywka.save()
                turniej.rozgrywki.add(rozgrywka)
    lista_rozgrywek = list(turniej.rozgrywki.all())
    for fazy in range(1,ilosc_faz):
        reszta_faz = int((max_ilosc_druzyn/2)/(2*fazy))
        for y in range(reszta_faz):
            druzyna1="Waiting"
            druzyna2="Waiting"
            if fazy == 1:
                if lista_rozgrywek[y*2].druzyna2 == "Walkower":
                    druzyna1 = lista_rozgrywek[y*2].druzyna1
                if lista_rozgrywek[y*2+1].druzyna2 == "Walkower":
                    druzyna2 = lista_rozgrywek[y*2+1].druzyna1
            rozgrywka = Rozgrywki(nazwa_rozgrywki="Mecz "+str(y)+" faza "+str(fazy),nazwa_turnieju=nazwa_turnieju, druzyna1=druzyna1, druzyna2=druzyna2, mecz=y ,faza=fazy)
            rozgrywka.save()
            turniej.rozgrywki.add(rozgrywka)



import random
def tournament_site(request, tournamentname):
    rozgrywki = Rozgrywki.objects.filter(nazwa_turnieju=tournamentname)
    tournament = Tournament.objects.get(nazwa=tournamentname)
    teams = Team.objects.filter(creator = request.user.email)
    template = loader.get_template('frontend/tournament.html')
    if request.method == 'POST':
        type = request.POST.get('type')
        if type == "add":
            tournament.druzyny.add(Team.objects.get(nazwa = request.POST.get("druzyna")))
            return redirect('tournament_site', tournamentname = tournament.nazwa)
        elif type == "remove":
            nazwa = request.POST.get('nazwa')
            tournament.druzyny.remove(Team.objects.get(nazwa=nazwa))
            return redirect('tournament_site', tournamentname = tournament.nazwa)
        elif type == "start":
            ilosc_druzyn = len(tournament.druzyny.all())
            druzyny = list(tournament.druzyny.all())
            random.shuffle(druzyny)
            if ilosc_druzyn == 4:
                tworzenie_rozgrywek(2,4, druzyny, tournament, 4)
                return redirect('tournament_site', tournamentname = tournament.nazwa)
            elif ilosc_druzyn<=8:
                tworzenie_rozgrywek(3,8, druzyny, tournament, ilosc_druzyn)
                return redirect('tournament_site', tournamentname = tournament.nazwa)
            elif ilosc_druzyn<=16:
                tworzenie_rozgrywek(4,16, druzyny, tournament, ilosc_druzyn)
                return redirect('tournament_site', tournamentname = tournament.nazwa)
            elif ilosc_druzyn<=32:
                tworzenie_rozgrywek(5,32, druzyny, tournament, ilosc_druzyn)
                return redirect('tournament_site', tournamentname = tournament.nazwa)
    context = {
        "tournament":tournament,
        "teams": teams,
        "rozgrywki": rozgrywki,
        "zapisana_druzyna": None,
    }
    for x in tournament.druzyny.all():
        if x.creator == request.user.email:
            context['zapisana_druzyna']=x
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