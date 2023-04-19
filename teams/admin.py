from django.contrib import admin

from teams.models import Team
from teams.models import Player


class TeamAdmin(admin.ModelAdmin):
    list_display = ("name",)
    list_filter = ("league",)
    search_fields = ("name",)
    ordering = ("name",)


class PlayerAdmin(admin.ModelAdmin):
    list_display = ("name",)
    list_filter = []
    search_fields = ("name",)
    ordering = ("name",)


admin.site.register(Team, TeamAdmin)
admin.site.register(Player, PlayerAdmin)
