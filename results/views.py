from django.shortcuts import render
from results.models import Team


def standings(request):
    leagues = Team.objects.values_list("league", flat=True).distinct()
    teams_by_league = []
    for league in leagues:
        teams = Team.objects.filter(league=league).order_by("-wins", "score")
        teams_by_league.append({"league": league, "teams": teams})
    context = {"teams_by_league": teams_by_league}
    return render(request, "standings.html", context)
