from django.contrib import admin
from results.models import *


class MatchAdmin(admin.ModelAdmin):
    """
    Admin interface for managing Match instances.

    Args:
        list_display (tuple): The fields to display in the list view.
        list_filter (tuple): The fields to filter by in the list view.
        search_fields (tuple): The fields to search by in the list view.
        ordering (tuple): The fields to order by in the list view.
        fieldsets (tuple): The fields to display in the detail view and how they are grouped.
        readonly_fields (tuple): The fields that are read-only in the detail view.
    """

    list_display = ("week", "date", "team_A", "team_B", "league")
    list_filter = ("league",)
    search_fields = []
    ordering = ("week",)
    fieldsets = (
        (
            "Match information",
            {
                "fields": (
                    "week",
                    "date",
                    "league",
                    "team_A",
                    "team_B",
                ),
            },
        ),
        (
            "Results",
            {
                "fields": (
                    "team_A_score",
                    "team_B_score",
                ),
            },
        ),
        (
            "Team A Player 1",
            {
                "fields": (
                    "team_A_player_1",
                    "team_A_player_1_score",
                    "team_A_player_1_goals",
                    "team_A_player_1_assists",
                    "team_A_player_1_saves",
                    "team_A_player_1_shots",
                ),
                "classes": ("collapse",),
            },
        ),
        (
            "Team A Player 2",
            {
                "fields": (
                    "team_A_player_2",
                    "team_A_player_2_score",
                    "team_A_player_2_goals",
                    "team_A_player_2_assists",
                    "team_A_player_2_saves",
                    "team_A_player_2_shots",
                ),
                "classes": ("collapse",),
            },
        ),
        (
            "Team A Player 3",
            {
                "fields": (
                    "team_A_player_3",
                    "team_A_player_3_score",
                    "team_A_player_3_goals",
                    "team_A_player_3_assists",
                    "team_A_player_3_saves",
                    "team_A_player_3_shots",
                ),
                "classes": ("collapse",),
            },
        ),
        (
            "Team A Player 4",
            {
                "fields": (
                    "team_A_player_4",
                    "team_A_player_4_score",
                    "team_A_player_4_goals",
                    "team_A_player_4_assists",
                    "team_A_player_4_saves",
                    "team_A_player_4_shots",
                ),
                "classes": ("collapse",),
            },
        ),
        (
            "Team A Player 5",
            {
                "fields": (
                    "team_A_player_5",
                    "team_A_player_5_score",
                    "team_A_player_5_goals",
                    "team_A_player_5_assists",
                    "team_A_player_5_saves",
                    "team_A_player_5_shots",
                ),
                "classes": ("collapse",),
            },
        ),
        (
            "Team B Player 1",
            {
                "fields": (
                    "team_B_player_1",
                    "team_B_player_1_score",
                    "team_B_player_1_goals",
                    "team_B_player_1_assists",
                    "team_B_player_1_saves",
                    "team_B_player_1_shots",
                ),
                "classes": ("collapse",),
            },
        ),
        (
            "Team B Player 2",
            {
                "fields": (
                    "team_B_player_2",
                    "team_B_player_2_score",
                    "team_B_player_2_goals",
                    "team_B_player_2_assists",
                    "team_B_player_2_saves",
                    "team_B_player_2_shots",
                ),
                "classes": ("collapse",),
            },
        ),
        (
            "Team B Player 3",
            {
                "fields": (
                    "team_B_player_3",
                    "team_B_player_3_score",
                    "team_B_player_3_goals",
                    "team_B_player_3_assists",
                    "team_B_player_3_saves",
                    "team_B_player_3_shots",
                ),
                "classes": ("collapse",),
            },
        ),
        (
            "Team B Player 4",
            {
                "fields": (
                    "team_B_player_4",
                    "team_B_player_4_score",
                    "team_B_player_4_goals",
                    "team_B_player_4_assists",
                    "team_B_player_4_saves",
                    "team_B_player_4_shots",
                ),
                "classes": ("collapse",),
            },
        ),
        (
            "Team B Player 5",
            {
                "fields": (
                    "team_B_player_5",
                    "team_B_player_5_score",
                    "team_B_player_5_goals",
                    "team_B_player_5_assists",
                    "team_B_player_5_saves",
                    "team_B_player_5_shots",
                ),
                "classes": ("collapse",),
            },
        ),
    )
    readonly_fields = (
        "league",
        "team_A",
        "team_B",
        "team_A_player_1",
        "team_A_player_2",
        "team_A_player_3",
        "team_A_player_4",
        "team_A_player_5",
        "team_B_player_1",
        "team_B_player_2",
        "team_B_player_3",
        "team_B_player_4",
        "team_B_player_5",
    )

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        else:
            return False


admin.site.register(Match, MatchAdmin)
