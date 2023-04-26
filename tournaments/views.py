from django.shortcuts import render
from results.models import Match


def calendar(request):
    context = {"matches": Match.objects.all()}
    return render(request, "calendar.html", context)


def rules(request):
    return render(request, "rules.html")
