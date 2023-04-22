from django.contrib import admin
from results.models import *


class MatchAdmin(admin.ModelAdmin):
    list_display = ("team_A", "team_B", "league")
    list_filter = ("league",)
    search_fields = []
    ordering = []


admin.site.register(Match, MatchAdmin)
