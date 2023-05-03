from django.shortcuts import render
from results.models import Match


def calendar(request):
    leagues = (
        Match.objects.order_by("league").values_list("league", flat=True).distinct()
    )
    matches = []
    for league in leagues:
        match = Match.objects.filter(league=league).order_by("week")
        matches.append({"league": league, "match": match})
    context = {
        "matches": matches,
    }
    return render(request, "calendar.html", context)


def rules(request):
    return render(request, "rules.html")
