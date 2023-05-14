from django.shortcuts import render
from teams.models import Team


def teams(request):
    """
    A view that retrieves all teams from the database and renders them in the teams.html template.

    Args:
        request (HttpRequest): The HTTP request.

    Returns:
        HttpResponse: The HTTP response containing the rendered HTML.
    """

    # Retrieve all teams from the database
    teams = Team.objects.all().order_by("name")

    # Create a context dictionary containing the teams
    context = {"teams": teams}

    # Render the template with the context
    return render(request, "teams.html", context)
