from django.shortcuts import render
from results.models import Match


def calendar(request):
    context = {"matches": Match.objects.order_by("week")}
    return render(request, "calendar.html", context)


def rules(request):
    return render(request, "rules.html")
