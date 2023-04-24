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

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    number = models.IntegerField(default=1, null=False, blank=False)
    acronym = models.CharField(max_length=4, null=False, blank=False)
    league = models.IntegerField(default=1, null=False, blank=False)
    logo = models.ImageField(null=True, blank=True)
    staff = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
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

    def get_total_goals(self):
        return sum(
            p.goals
            for p in [
                self.player1,
                self.player2,
                self.player3,
                self.player4,
                self.player5,
            ]
            if p
        )

    get_total_goals.short_description = "Goals"

    def get_total_saves(self):
        return sum(
            p.saves
            for p in [
                self.player1,
                self.player2,
                self.player3,
                self.player4,
                self.player5,
            ]
            if p
        )

    get_total_saves.short_description = "Saves"

    def get_total_assists(self):
        return sum(
            p.assists
            for p in [
                self.player1,
                self.player2,
                self.player3,
                self.player4,
                self.player5,
            ]
            if p
        )

    get_total_assists.short_description = "Assists"

    def get_total_shots(self):
        return sum(
            p.shots
            for p in [
                self.player1,
                self.player2,
                self.player3,
                self.player4,
                self.player5,
            ]
            if p
        )

    get_total_shots.short_description = "Shots"

    def get_total_score(self):
        from results.models import Match
        from django.db.models import Sum

        return (
            Match.objects.filter(Q(team_A=self) | Q(team_B=self))
            .filter(team_A=self)
            .aggregate(Sum("team_A_score"))
            .get("team_A_score__sum")
            or 0
        ) + (
            Match.objects.filter(Q(team_A=self) | Q(team_B=self))
            .filter(team_B=self)
            .aggregate(Sum("team_B_score"))
            .get("team_B_score__sum")
            or 0
        )

    get_total_score.short_description = "score"

    def __str__(self):
        return self.name
