from django.shortcuts import render
from results.models import Match
from results.models import Team
from django.db.models import F


def standings(request):
    """Renders the standings page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object containing the rendered template.

    """

    # Get a list of all distinct leagues in the database
    leagues = Team.objects.values_list("league", flat=True).distinct()

    # Create an empty list to store the teams in each league
    teams_by_league = []

    # Loop through each league and get a queryset of all teams in that league,
    # sorted by various criteria
    for league in leagues:
        teams = Team.objects.filter(league=league).order_by(
            "-wins", "lose", "-bo_diff", "-bo_wins", "bo_lose"
        )
        # Add the league name and the teams in that league to the list of teams by league
        teams_by_league.append({"league": league, "teams": teams})

    # Create a dictionary containing the list of teams by league and render the standings page
    context = {"teams_by_league": teams_by_league}
    return render(request, "standings.html", context)


def calendar(request):
    """
    Renders a page with a calendar of upcoming matches, grouped by league.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: A response containing the rendered HTML template.
    """

    # Get a list of all the distinct leagues in the database
    leagues = (
        Match.objects.order_by("league").values_list("league", flat=True).distinct()
    )

    # Group all the matches by league and order them by week, ignoring null values
    matches = []
    for league in leagues:
        match = Match.objects.filter(league=league).order_by(
            F("week").asc(nulls_last=True), F("date").asc(nulls_last=True)
        )
        matches.append({"league": league, "match": match})

    # Render the template with the matches grouped by league
    context = {"matches": matches}
    return render(request, "calendar.html", context)
