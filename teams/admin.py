from django.contrib import admin

from teams.models import Team
from teams.models import Player


class TeamAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "league",
        "get_average_mmr",
        "matches_played",
        "wins",
        "lose",
        "bo_wins",
        "bo_lose",
        "bo_diff",
    )
    list_filter = ("league",)
    search_fields = ("name",)
    ordering = (
        "name",
        "matches_played",
        "wins",
        "bo_wins",
        "bo_lose",
        "bo_diff",
        "matches_played",
    )
    readonly_fields = (
        "wins",
        "lose",
        "bo_wins",
        "bo_lose",
        "bo_diff",
        "score",
        "goals",
        "saves",
        "assists",
        "shots",
    )


class PlayerAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "get_team",
        "MMR",
        "score",
        "goals",
        "saves",
        "assists",
        "shots",
    )
    list_filter = []
    search_fields = ("name",)
    ordering = ("name", "MMR", "score", "goals", "saves", "assists", "shots")
    readonly_fields = ("score", "goals", "saves", "assists", "shots")


admin.site.register(Team, TeamAdmin)
admin.site.register(Player, PlayerAdmin)
