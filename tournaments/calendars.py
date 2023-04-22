from teams.models import Team
from itertools import combinations


def calendar(league):
    teams = Team.objects.filter(league=league)
    team_list = list(teams)
    # Convert queryset to list to be able to use combination
    matches = []
    for match in combinations(team_list, 2):
        # Generate all combinations of two teams
        matches.append(match)
        # Add each generated match to the match list
    return matches
