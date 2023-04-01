from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login, authenticate
from .forms import userRegistrationForm, UserData, UserUpdate, TeamForm, TournamentForm
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from backend.models import Team, Tournament, CustomUser, Powiadomienia
from django.template import loader
from django.http import HttpResponse, JsonResponse

def main(request):
    return render(request, 'main.html')



def register(request):
    if request.method == "POST":
        form = userRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
        else:
            for error in list(form.errors.values()):
                print(request, error)

    else:
        form = userRegistrationForm()

    return render(
        request = request,
        template_name = "frontend/register.html",
        context={"form":form}
        )


def logout_view(request):
    logout(request)
    return redirect('/')


def login_web(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('/')

        else:
            for error in list(form.errors.values()):
                print(request, error)

    form = AuthenticationForm() 
    
    return render(
        request=request,
        template_name="frontend/login_web.html", 
        context={'form': form}
        )



def player_site(request, playernick):
    user = get_user_model().objects.filter(nick=playernick).first()
    if user:
        player = CustomUser.objects.get(nick=playernick)
        context = {
            'player': player,
            'teams': None,
            'team_member': None,
        }
        if Team.objects.filter(creator=user.email).exists():
            team_creator=Team.objects.filter(creator=user.email)
            context['team']=team_creator
        
        if Team.objects.filter(add_players__email=user.email).exists():
            team_member = Team.objects.filter(add_players__email=user.email)
            context['team_member']=team_member

        return render(request, 'frontend/player.html', context=context)

    return redirect("/")



def settings(request):
    user = request.user
    if user.is_authenticated:
        if request.method == 'POST':
            form = UserUpdate(request.POST, instance=user)
            if form.is_valid():
                form.save()
                return redirect('/')
        else:
            form = UserUpdate(instance=user)
        return render(request, 'frontend/settings.html', {'form': form})
    else:
        return redirect('/')
    

def player_list_site(request):
    players = CustomUser.objects.all()

    template = loader.get_template('frontend/players_list.html')
    context = {
        "players":players,
    }
    return HttpResponse(template.render(context, request))





def create_team(request):
    user = request.user
    if user.is_authenticated:
        if request.method == 'POST':
            form = TeamForm(request.POST, request.FILES)
            if form.is_valid():
                form.instance.creator=request.user.email
                form.save()
                return redirect('/teams')
        else:
            form = TeamForm()
        return render(request, 'frontend/create_team.html', {'form': form})
    else:
        return redirect('/')
    

def create_tournament(request):
    user = request.user
    if user.is_authenticated:
        if request.method == 'POST':
            form = TournamentForm(request.POST, request.FILES)
            if form.is_valid():
                form.instance.creator=request.user.email
                form.save()
                return redirect('/tournaments')
        else:
            form = TournamentForm()
            form.fields['data'].label = "Data rozpoczęcia turnieju"
            form.fields['ilosc_druzyn'].label = "Maksymalna ilość drużyn"
        return render(request, 'frontend/create_tournament.html', {'form': form})
    else:
        return redirect('/')
    
def powiadomienia(request):
    user = request.user
    if user.is_authenticated:
        powiadomienia = Powiadomienia.objects.filter(user=user)
        if request.method == 'POST':
            type = request.POST.get('type')
            team_name = request.POST.get('team')
            team = Team.objects.get(nazwa=team_name)
            print(type, team_name, team)
            if type == "add_invite":
                team.add_players.add(user)
                team.waiting_list.remove(user)
                team.remove_players.add(user)
                powiadomienie = powiadomienia.filter(druzyna=team_name)
                powiadomienie.delete()
                return redirect('powiadomienia')
            elif type == "cancel_invite":
                team.waiting_list.remove(user)
                team.add_players.remove(user)
                powiadomienie = powiadomienia.filter(druzyna=team_name)
                powiadomienie.delete()
                return redirect('powiadomienia')
            elif type == "add_volunteer":
                volunteer = request.POST.get('volunteer')
                new_volunteer = CustomUser.objects.get(nick = volunteer)
                team.add_players.add(new_volunteer)
                team.remove_players.add(new_volunteer)
                team.volunteers.remove(new_volunteer)
                powiadomienie = powiadomienia.filter(druzyna=team_name, volunteer=volunteer)
                powiadomienie.delete()
                return redirect('powiadomienia')
            elif type == "cancel_volunteer":
                volunteer = request.POST.get('volunteer')
                new_volunteer = CustomUser.objects.get(nick = volunteer)
                team.volunteers.remove(new_volunteer)
                powiadomienie = powiadomienia.filter(druzyna=team_name, volunteer=volunteer)
                powiadomienie.delete()
                return redirect('powiadomienia')
        return render(request, 'frontend/powiadomienia.html', {'powiadomienia': powiadomienia})
    else:
        return redirect('/')