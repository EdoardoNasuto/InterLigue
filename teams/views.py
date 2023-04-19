from django.shortcuts import render
from teams.models import Team


def teams(request):
    teams = Team.objects.all()
    context = {"teams": teams}
    return render(request, "teams.html", context)
