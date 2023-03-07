from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login, authenticate
from .forms import userRegistrationForm, UserData, UserUpdate
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm

def main(request):
    return render(request, 'main.html')



def register(request):
    if request.method == "POST":
        form = userRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/backend/main')
        else:
            for error in list(form.errors.values()):
                print(request, error)

    else:
        form = userRegistrationForm()

    return render(
        request = request,
        template_name = "register.html",
        context={"form":form}
        )


def logout_view(request):
    logout(request)
    return redirect('/backend/main')


def login_web(request):
    if request.user.is_authenticated:
        return redirect('/backend/main')

    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('/backend/main')

        else:
            for error in list(form.errors.values()):
                print(request, error)

    form = AuthenticationForm() 
    
    return render(
        request=request,
        template_name="login_web.html", 
        context={'form': form}
        )



def profile(request, nick):
    if request.method == 'POST':
        pass

    user = get_user_model().objects.filter(nick=nick).first()
    if user:
        form = UserData(instance=user)
        return render(request, 'profile.html', context={'form': form})

    return redirect("/backend/main")



def settings(request):
    user = request.user
    if user.is_authenticated:
        if request.method == 'POST':
            form = UserUpdate(request.POST, instance=user)
            if form.is_valid():
                form.save()
                return redirect('/backend/main')
        else:
            form = UserUpdate(instance=user)
        return render(request, 'settings.html', {'form': form})
    else:
        return redirect('/backend/main')