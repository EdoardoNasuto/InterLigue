from django.db import models
from authentication.models import User


class Player(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    avatar = models.ImageField(null=True, blank=True)
    tracker = models.URLField(null=False, blank=False)
    MMR = models.IntegerField(default=0, null=False, blank=False)
    goals = models.IntegerField(default=0, null=False, blank=False)
    saves = models.IntegerField(default=0, null=False, blank=False)
    assists = models.IntegerField(default=0, null=False, blank=False)
    shots = models.IntegerField(default=0, null=False, blank=False)


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

    def get_average_mmr(self):
        players = [self.player1, self.player2, self.player3, self.player4, self.player5]
        total_mmr = sum(player.MMR for player in players if player)
        num_players = sum(1 for player in players if player)
        return total_mmr / num_players

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
