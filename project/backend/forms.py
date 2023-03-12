from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from backend.models import Team

class userRegistrationForm(UserCreationForm):
    email = forms.EmailField(help_text="Podaj prawidłowy email", required=True)
    nick = forms.CharField(help_text="Podaj prawidłowy email",max_length=30, required=True)
    data_urodzenia = forms.DateField(help_text="Podaj prawidłowy email",required=False)
    avatar = forms.ImageField(help_text="Podaj prawidłowy email",required=False)


    class Meta:
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

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'username', 'nick', 'data_urodzenia', 'avatar', 'email', 'opis', 'password']


class TeamForm(forms.ModelForm):
    creator = forms.EmailField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Team
        fields = ['nazwa', 'opis', 'zdjecie','punkty']
        widgets = {
            'punkty': forms.HiddenInput(),
        }
