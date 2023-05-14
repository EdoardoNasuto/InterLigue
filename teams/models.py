from django.db import models
from django.db.models import Q
from authentication.models import User
from django.core.exceptions import ValidationError


class Player(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, unique=True)
    tracker = models.URLField(null=False, blank=False)
    score = models.IntegerField(default=0, null=False, blank=False)
    goals = models.IntegerField(default=0, null=False, blank=False)
    assists = models.IntegerField(default=0, null=False, blank=False)
    saves = models.IntegerField(default=0, null=False, blank=False)
    shots = models.IntegerField(default=0, null=False, blank=False)

    def get_team(self):
        """
        Returns the team the player belongs to.

        Returns:
            Team: The team the player belongs to, or None if the player does not belong to any team.
        """

        try:
            team = Team.objects.get(
                Q(player1=self)
                | Q(player2=self)
                | Q(player3=self)
                | Q(player4=self)
                | Q(player5=self)
            )
            return team
        except Team.DoesNotExist:
            return None

    get_team.short_description = "Team"

    def set_statistics(self):
        """
        Computes and updates the player's statistics based on the matches they played.

        The statistics that are computed are:
        - score
        - goals
        - assists
        - saves
        - shots
        """

        # Import the Match model from the results app
        from results.models import Match

        # Retrieve all the matches in which the player has participated
        matches = Match.objects.filter(
            Q(team_A_player_1=self)
            | Q(team_A_player_2=self)
            | Q(team_A_player_3=self)
            | Q(team_A_player_4=self)
            | Q(team_A_player_5=self)
            | Q(team_B_player_1=self)
            | Q(team_B_player_2=self)
            | Q(team_B_player_3=self)
            | Q(team_B_player_4=self)
            | Q(team_B_player_5=self)
        )

        # Define a list of player fields for each team in a match
        player_fields = [
            "team_A_player_1",
            "team_A_player_2",
            "team_A_player_3",
            "team_A_player_4",
            "team_A_player_5",
            "team_B_player_1",
            "team_B_player_2",
            "team_B_player_3",
            "team_B_player_4",
            "team_B_player_5",
        ]

        # Initialize a dictionary to store the player's statistics
        player_stats = {
            "score": 0,
            "goals": 0,
            "assists": 0,
            "saves": 0,
            "shots": 0,
        }

        # Iterate over each match in which the player participated
        for match in matches:
            # Iterate over each player field in a match
            for player_field in player_fields:
                # Retrieve the player from the player field
                player = getattr(match, player_field)
                # Check if the player exists and is the same as the current player
                if player is not None and player.id == self:
                    # Iterate over each statistic and add it to the player's stats dictionary
                    for stat in player_stats:
                        player_stats[stat] += getattr(match, (f"{player_field}_{stat}"))

        # Update the player's stats in the database
        Player.objects.filter(id=self).update(**player_stats)

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    number = models.IntegerField(default=1, null=False, blank=False)
    acronym = models.CharField(max_length=4, null=False, blank=False)
    league = models.IntegerField(default=1, null=False, blank=False)
    staff = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)

    matches_played = models.IntegerField(default=0, null=False, blank=False)
    wins = models.IntegerField(default=0, null=False, blank=False)
    lose = models.IntegerField(default=0, null=False, blank=False)
    bo_wins = models.IntegerField(default=0, null=False, blank=False)
    bo_lose = models.IntegerField(default=0, null=False, blank=False)
    bo_diff = models.IntegerField(default=0, null=False, blank=False)

    score = models.IntegerField(default=0, null=False, blank=False)
    goals = models.IntegerField(default=0, null=False, blank=False)
    assists = models.IntegerField(default=0, null=False, blank=False)
    saves = models.IntegerField(default=0, null=False, blank=False)
    shots = models.IntegerField(default=0, null=False, blank=False)

    player1 = models.OneToOneField(
        Player,
        related_name="team_player1",
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )
    player2 = models.OneToOneField(
        Player,
        related_name="team_player2",
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )
    player3 = models.OneToOneField(
        Player,
        related_name="team_player3",
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )
    player4 = models.OneToOneField(
        Player,
        related_name="team_player4",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    player5 = models.OneToOneField(
        Player,
        related_name="team_player5",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    def clean(self):
        """
        Validates the team composition to ensure that it meets the necessary criteria.

        Raises a ValidationError if any of the following conditions are met:
            - a player appears twice in the team composition
            - a player is already part of another team's composition
        """

        # Call the parent class's clean method to ensure that it gets run
        super().clean()

        # Make a list of all the players in the team
        players = [self.player1, self.player2, self.player3, self.player4, self.player5]

        # Check that no player appears twice in the team composition
        seen_players = set()
        for player in players:
            if player in seen_players:
                raise ValidationError(
                    f"Le joueur {player} apparaît deux fois dans la composition de l'équipe."
                )
            elif player:
                seen_players.add(player)

        # Check that no player appears in the composition of another team
        for i in range(len(players)):
            player = getattr(self, f"player{i+1}")
            if (
                player
                and Team.objects.exclude(pk=self.pk)
                .filter(
                    Q(player1=player)
                    | Q(player2=player)
                    | Q(player3=player)
                    | Q(player4=player)
                    | Q(player5=player)
                )
                .exists()
            ):
                raise ValidationError(
                    f"Le joueur {player} a déjà une équipe attribuée."
                )

    def set_statistics(self):
        """
        Computes and updates the statistics of a team based on the statistics of its players.

        The following statistics are computed:
        - score: the total score of the team
        - goals: the total number of goals scored by the team
        - saves: the total number of saves made by the team
        - assists: the total number of assists made by the team
        - shots: the total number of shots made by the team
        """

        # Initialize dictionary with all keys initialized to 0
        stats = {
            "score": 0,
            "goals": 0,
            "saves": 0,
            "assists": 0,
            "shots": 0,
        }

        # Iterate through the team's players and add up their stats
        for player in [
            self.player1,
            self.player2,
            self.player3,
            self.player4,
            self.player5,
        ]:
            if player is not None:
                stats["score"] += player.score
                stats["goals"] += player.goals
                stats["saves"] += player.saves
                stats["assists"] += player.assists
                stats["shots"] += player.shots

        # Update the team's stats in the database
        Team.objects.filter(id=self.id).update(**stats)

    def set_teams_stats(self):
        """
        Calculates and updates various statistics for the team based on past matches.

        The following statistics are computed:
        - wins: the number of matches won
        - lose: the number of matches lost
        - bo_wins: the number of Best-of (BO) wins
        - bo_lose: the number of BO losses
        - bo_diff: the BO difference (BO wins minus BO losses)
        - matches_played: the total number of matches played
        """

        # Import the Match model from the results app
        from results.models import Match

        # Initialize dictionary with all keys initialized to 0
        stats = {
            "wins": 0,
            "lose": 0,
            "bo_wins": 0,
            "bo_lose": 0,
            "bo_diff": 0,
            "matches_played": 0,
        }

        # Iterate through all matches the team has played
        for match in Match.objects.filter(Q(team_A=self) | Q(team_B=self)):
            # Add up the BO wins and losses for the team
            stats["bo_wins"] += (
                match.team_A_score if match.team_A == self else match.team_B_score
            )
            stats["bo_lose"] += (
                match.team_B_score if match.team_A == self else match.team_A_score
            )

            # Determine if the team won or lost the match
            team_win = match.get_team_win()
            if team_win:
                if team_win == self:
                    stats["wins"] += 1
                else:
                    stats["lose"] += 1

        # Calculate the BO difference and matches played for the team
        stats["bo_diff"] = stats["bo_wins"] - stats["bo_lose"]
        stats["matches_played"] = stats["wins"] + stats["lose"]

        # Update the team's stats in the database
        Team.objects.filter(id=self.id).update(**stats)

    def __str__(self):
        return self.name
