from django.contrib import admin
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeView,
    PasswordChangeDoneView,
)
from django.urls import path

import authentication.views
import teams.views
import results.views

urlpatterns = [
    path("", authentication.views.home, name="home"),
    path("admin/", admin.site.urls, name="admin"),
    path("teams/", teams.views.teams, name="teams"),
    path("calendar/", results.views.calendar, name="calendar"),
    path("standings/", results.views.standings, name="standings"),
]
