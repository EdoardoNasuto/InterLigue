from django.db import models
from django.db.models import Q
from authentication.models import User
from django.core.exceptions import ValidationError


class Player(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, unique=True)
    avatar = models.ImageField(null=True, blank=True)
    tracker = models.URLField(null=False, blank=False)
    MMR = models.IntegerField(default=0, null=False, blank=False)
    score = models.IntegerField(default=0, null=False, blank=False)
    goals = models.IntegerField(default=0, null=False, blank=False)
    assists = models.IntegerField(default=0, null=False, blank=False)
    saves = models.IntegerField(default=0, null=False, blank=False)
    shots = models.IntegerField(default=0, null=False, blank=False)

    def get_team(self):
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
        from results.models import Match

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

        player_stats = {
            "score": 0,
            "goals": 0,
            "assists": 0,
            "saves": 0,
            "shots": 0,
        }

        for match in matches:
            for player_field in player_fields:
                player = getattr(match, player_field)
                if player is not None:
                    if player.id == self:
                        for stat in player_stats:
                            player_stats[stat] += getattr(
                                match, (f"{player_field}_{stat}")
                            )

        Player.objects.filter(id=self).update(**player_stats)

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    number = models.IntegerField(default=1, null=False, blank=False)
    acronym = models.CharField(max_length=4, null=False, blank=False)
    league = models.IntegerField(default=1, null=False, blank=False)
    logo = models.ImageField(null=True, blank=True)
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
        super().clean()
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

    def get_average_mmr(self):
        players = [self.player1, self.player2, self.player3, self.player4, self.player5]
        total_mmr = sum(player.MMR for player in players if player)
        num_players = sum(1 for player in players if player)
        return total_mmr / num_players

    get_average_mmr.short_description = "MMR"

    def set_statistics(self):
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
            print(team_win)
            if team_win:
                print("yes")
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
