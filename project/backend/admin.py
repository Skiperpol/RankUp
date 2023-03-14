from django.contrib import admin
from .models import CustomUser, Tournament, Team, Rozgrywki, Message

admin.site.register(CustomUser)
admin.site.register(Tournament)
admin.site.register(Team)
admin.site.register(Rozgrywki)
admin.site.register(Message)
