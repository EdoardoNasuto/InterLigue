from django.contrib import admin

from teams.models import Team
from teams.models import Player


class TeamAdmin(admin.ModelAdmin):
    """
    Admin configuration for the `Team` model in the Django Admin interface.

    Args:
        list_display (tuple): The fields to display in the list view of `Team` objects.
        list_filter (tuple): The fields to use for filtering the list view of `Team` objects.
        search_fields (tuple): The fields to use for searching `Team` objects.
        readonly_fields (tuple): The fields that should be displayed as read-only in the detail view of `Team` objects.
        fieldsets (tuple): The sections and fields to display in the detail view of `Team` objects.
    """

    list_display = (
        "name",
        "league",
        "matches_played",
        "wins",
        "lose",
        "bo_wins",
        "bo_lose",
        "bo_diff",
    )
    list_filter = ("split", "league")
    search_fields = ("name",)
    readonly_fields = (
        "matches_played",
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
    fieldsets = (
        (
            "Informations",
            {
                "fields": (
                    "name",
                    "number",
                    "acronym",
                    "split",
                    "league",
                    "staff",
                    "player1",
                    "player2",
                    "player3",
                    "player4",
                    "player5",
                ),
            },
        ),
        (
            "Statistiques",
            {
                "fields": (
                    "matches_played",
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
                ),
            },
        ),
    )


class PlayerAdmin(admin.ModelAdmin):
    """
    Admin configuration for the `Player` model in the Django Admin interface.

    Args:
        list_display (tuple): The fields to display in the list view of `Player` objects.
        list_filter (tuple): The fields to use for filtering the list view of `Player` objects.
        search_fields (tuple): The fields to use for searching `Player` objects.
        ordering (tuple): The fields to use for ordering `Player` objects.
        readonly_fields (tuple): The fields that should be displayed as read-only in the detail view of `Player` objects.
    """

    list_display = (
        "name",
        "get_team",
        "score",
        "goals",
        "saves",
        "assists",
        "shots",
    )
    list_filter = ("split",)
    search_fields = ("name",)
    ordering = ("name", "score", "goals", "saves", "assists", "shots")
    readonly_fields = ("score", "goals", "saves", "assists", "shots")


admin.site.register(Team, TeamAdmin)
admin.site.register(Player, PlayerAdmin)
