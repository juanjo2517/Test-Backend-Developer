from django.contrib import admin

# Models 
from apps.fifa_api.models import Player, Team, IntegrationServices

admin.site.register(Player)
admin.site.register(Team)
admin.site.register(IntegrationServices)

