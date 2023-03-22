from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from backend.models import Team, Tournament, Message

class userRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    nick = forms.CharField(max_length=30, required=True)
    data_urodzenia = forms.DateField(required=False)
    avatar = forms.ImageField(required=False)
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['password1'].help_text = None
            self.fields['password2'].help_text = None

    class Meta:
        help_texts = {
            'username': None,
            'password1': None,
            'password2': None,
        }
        model = get_user_model()
        fields = ['first_name', 'last_name', 'username', 'nick', 'data_urodzenia', 'avatar', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super(userRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.nick = self.cleaned_data['nick']
        user.data_urodzenia = self.cleaned_data['data_urodzenia']
        user.avatar = self.cleaned_data['avatar']
        if commit:
            user.save()
        return user
    

class UserData(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email', 'nick', 'punkty']

class UserUpdate(forms.ModelForm):
    opis = forms.Textarea()
    avatar = forms.ImageField(widget=forms.FileInput)
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = get_user_model()
        help_texts = {
            'username': None,
        }
        fields = ['first_name', 'last_name', 'username', 'nick', 'data_urodzenia', 'avatar', 'email', 'opis', 'password']


class TeamForm(forms.ModelForm):
    creator = forms.EmailField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Team
        fields = ['nazwa', 'opis', 'zdjecie','punkty']
        widgets = {
            'punkty': forms.HiddenInput(),
        }


class TournamentForm(forms.ModelForm):
    creator = forms.EmailField(widget=forms.HiddenInput(), required=False)
    zdjecie = forms.ImageField(required=False)    

    class Meta:
        model = Tournament
        fields = ['nazwa', 'opis', 'nagroda', 'data', 'ilosc_druzyn', 'druzyny', 'rodzaj_gry', 'format_rozgrywek']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'datetime-local'}),
            'druzyny': forms.HiddenInput(),
        }



class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['nazwa_rozgrywki', 'kapitan', 'wiadomosci']
        widgets = {
            'nazwa_rozgrywki': forms.HiddenInput(),
            'wiadomosci': forms.TextInput(attrs={'id':'wiadomosci'}),
            'kapitan': forms.HiddenInput(),
        }