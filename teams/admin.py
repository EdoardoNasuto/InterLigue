from django.contrib import admin

from teams.models import Team
from teams.models import Player


class TeamAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "get_average_mmr",
        "get_total_score",
    )
    list_filter = ("league",)
    search_fields = ("name",)
    ordering = ("name",)


class PlayerAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "MMR",
        "get_team",
    )
    list_filter = []
    search_fields = ("name",)
    ordering = ("-MMR",)
    readonly_fields = ("score", "goals", "saves", "assists", "shots")


admin.site.register(Team, TeamAdmin)
admin.site.register(Player, PlayerAdmin)
