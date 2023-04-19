from django.shortcuts import render
from teams.models import Team
from itertools import combinations


def calendar(request):
    teams = Team.objects.all()
    team_list = [team.name for team in teams]
    # convertir queryset en liste pour pouvoir utiliser la combinaison
    matches = []
    for match in combinations(team_list, 2):
        # générer toutes les combinaisons de deux équipes
        matches.append(match)
        # ajouter chaque match généré à la liste des matches

    context = {"matches": matches}
    return render(request, "calendar.html", context)
