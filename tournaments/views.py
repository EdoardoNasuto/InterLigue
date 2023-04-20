from django.shortcuts import render
from .calendars import calendars


def calendar(request):
    context = {"matches": calendars()}
    return render(request, "calendar.html", context)
