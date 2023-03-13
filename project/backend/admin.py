from django.contrib import admin
from .models import CustomUser, Tournament, Team, Rozgrywki

admin.site.register(CustomUser)
admin.site.register(Tournament)
admin.site.register(Team)
admin.site.register(Rozgrywki)
