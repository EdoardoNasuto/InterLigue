from django.contrib import admin

from teams.models import Team
from teams.models import Player


class TeamAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "acronym",
        "league",
        "player1",
        "player2",
        "player3",
        "player4",
        "player5",
    )
    list_filter = ("league",)
    search_fields = ("name",)
    ordering = ("name",)


class PlayerAdmin(admin.ModelAdmin):
    list_display = ("name", "MMR")
    list_filter = []
    search_fields = ("name",)
    ordering = ("-MMR",)


admin.site.register(Team, TeamAdmin)
admin.site.register(Player, PlayerAdmin)
