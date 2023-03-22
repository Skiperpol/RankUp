from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect
from django.template import loader
from backend.models import Team, Tournament, CustomUser, Rozgrywki, Message
from backend.forms import TeamForm, MessageForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

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
            nazwa_rozgrywki="Mecz_"+str(y)+"_faza_0"
            if y<roznica:
                rozgrywka = Rozgrywki(nazwa_rozgrywki=nazwa_rozgrywki,nazwa_turnieju=nazwa_turnieju, druzyna1=lista_druzyn[i], druzyna2=lista_druzyn[i+1], mecz=y ,faza=0)
                i=i+2
                rozgrywka.save()
                turniej.rozgrywki.add(rozgrywka)
            else:
                rozgrywka = Rozgrywki(nazwa_rozgrywki=nazwa_rozgrywki,nazwa_turnieju=nazwa_turnieju, druzyna1=lista_druzyn[i], druzyna2="Walkower", mecz=y ,faza=0,winner=lista_druzyn[i])
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
            nazwa_rozgrywki="Mecz_"+str(y)+"_faza_"+str(fazy)
            rozgrywka = Rozgrywki(nazwa_rozgrywki=nazwa_rozgrywki,nazwa_turnieju=nazwa_turnieju, druzyna1=druzyna1, druzyna2=druzyna2, mecz=y ,faza=fazy)
            rozgrywka.save()
            turniej.rozgrywki.add(rozgrywka)



import random
def tournament_site(request, tournamentname):
    teams = []
    rozgrywki = Rozgrywki.objects.filter(nazwa_turnieju=tournamentname)
    tournament = Tournament.objects.get(nazwa=tournamentname)
    creator = CustomUser.objects.get(email=tournament.creator)
    template = loader.get_template('frontend/tournament.html')
    if request.user.is_authenticated:
        teams = Team.objects.filter(creator = request.user.email)
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
    rozgrywki = Rozgrywki.objects.filter(nazwa_turnieju=tournament.nazwa)
    context = {
        "tournament":tournament,
        "teams": teams,
        "rozgrywki": rozgrywki,
        "creator": creator,
        "zapisana_druzyna": None,
        "rozgrywki": None,
    }
    if request.user.is_authenticated:
        if rozgrywki != "":
            context["rozgrywki"]=rozgrywki
        context['teams']=teams
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

    
@login_required
def room(request, nazwa_turnieju, nazwa_rozgrywki, druzyna):
    team = Team.objects.get(nazwa=druzyna)
    if team.creator != request.user.email:
        return redirect('index')
    room = Rozgrywki.objects.get(nazwa_rozgrywki=nazwa_rozgrywki, nazwa_turnieju=nazwa_turnieju)
    if room.druzyna1 == druzyna:
        form = MessageForm()
    elif room.druzyna2 == druzyna:
        form = MessageForm()
    else:
        return redirect('index')

    return render(
        request=request,
        template_name="frontend/room.html",
        context={
            'room': room,
            'form': form,
            'druzyna': druzyna,
        }
    )
    


def get_messages(request):
    room = request.GET.get('room')
    messages = Message.objects.filter(nazwa_rozgrywki=room)
    return JsonResponse({"messages":list(messages.values())})

def send(request):
    wiadomosci = request.POST['wiadomosci']
    kapitan = request.POST['kapitan']
    nazwa_rozgrywki = request.POST['nazwa_rozgrywki']

    new_message = Message.objects.create(kapitan=kapitan, wiadomosci=wiadomosci, nazwa_rozgrywki=nazwa_rozgrywki)
    new_message.save()
    return HttpResponse('Message sent successfully')

def check(obiekt_rozgrywki):
    if obiekt_rozgrywki.kto_wygral_druzyna1 !=None and obiekt_rozgrywki.kto_wygral_druzyna2 !=None:
        if obiekt_rozgrywki.kto_wygral_druzyna1 == obiekt_rozgrywki.kto_wygral_druzyna2:
            obiekt_rozgrywki.winner = obiekt_rozgrywki.kto_wygral_druzyna1
            print(obiekt_rozgrywki.winner)
            print(obiekt_rozgrywki.kto_wygral_druzyna1)
            obiekt_rozgrywki.save()
            
            nowa_nazwa_rozgrywki = "Mecz_"+str(int(obiekt_rozgrywki.mecz)//2)+"_faza_"+str(int(obiekt_rozgrywki.faza)+1)
            nowa_rozgrywka = Rozgrywki.objects.get(nazwa_rozgrywki=nowa_nazwa_rozgrywki)
            print("-------------------------------")
            print(nowa_nazwa_rozgrywki)
            print(nowa_rozgrywka)
            if obiekt_rozgrywki.mecz % 2 == 0:
                nowa_rozgrywka.druzyna1 = obiekt_rozgrywki.winner
                nowa_rozgrywka.save()
            else:
                nowa_rozgrywka.druzyna2 = obiekt_rozgrywki.winner
                nowa_rozgrywka.save()
        else:
            print("sprzeczność")


def winner(request):
    druzyna=request.POST['druzyna']
    nazwa_rozgrywki=request.POST['nazwa_rozgrywki']
    winner = request.POST['winner']
    img = request.FILES.get('image')
    rozgrywka = Rozgrywki.objects.get(nazwa_rozgrywki=nazwa_rozgrywki)
    if rozgrywka.druzyna1 == druzyna:
        rozgrywka.screen_druzyna1 = img
        rozgrywka.kto_wygral_druzyna1 = winner
        rozgrywka.save()
        check(rozgrywka)
    elif rozgrywka.druzyna2 == druzyna:
        rozgrywka.screen_druzyna2 = img
        rozgrywka.kto_wygral_druzyna2 = winner
        rozgrywka.save()
        check(rozgrywka)
    print(winner)
    print(img)
    return HttpResponse('Message sent successfully')
