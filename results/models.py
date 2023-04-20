from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from teams.models import *
from tournaments.calendars import calendar


class Match(models.Model):
    league = models.IntegerField(default=1, null=False, blank=False)
    team_A = models.ForeignKey(
        Team, related_name="team_A", on_delete=models.CASCADE, null=False, blank=False
    )
    team_B = models.ForeignKey(
        Team, related_name="team_B", on_delete=models.CASCADE, null=False, blank=False
    )
    team_A_score = models.IntegerField(default=0, null=False, blank=False)
    team_B_score = models.IntegerField(default=0, null=False, blank=False)
    team_A_player_1 = models.ForeignKey(
        Player,
        related_name="team_A_player_1",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    team_A_player_2 = models.ForeignKey(
        Player,
        related_name="team_A_player_2",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    team_A_player_3 = models.ForeignKey(
        Player,
        related_name="team_A_player_3",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    team_A_player_4 = models.ForeignKey(
        Player,
        related_name="team_A_player_4",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    team_A_player_5 = models.ForeignKey(
        Player,
        related_name="team_A_player_5",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    team_B_player_1 = models.ForeignKey(
        Player,
        related_name="team_B_player_1",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    team_B_player_2 = models.ForeignKey(
        Player,
        related_name="team_B_player_2",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    team_B_player_3 = models.ForeignKey(
        Player,
        related_name="team_B_player_3",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    team_B_player_4 = models.ForeignKey(
        Player,
        related_name="team_B_player_4",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    team_B_player_5 = models.ForeignKey(
        Player,
        related_name="team_B_player_5",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    @receiver(post_save, sender=Team)
    def create_matches(sender, instance, created, **kwargs):
        matches = calendar()
        if created:
            for team_a, team_b in matches:
                # Check if a match already exists with these teams
                if not Match.objects.filter(team_A=team_a, team_B=team_b).exists():
                    match = Match.objects.create(
                        team_A=team_a,
                        team_B=team_b,
                        team_A_player_1=team_a.player1,
                        team_A_player_2=team_a.player2,
                        team_A_player_3=team_a.player3,
                        team_A_player_4=team_a.player4,
                        team_A_player_5=team_a.player5,
                        team_B_player_1=team_b.player1,
                        team_B_player_2=team_b.player2,
                        team_B_player_3=team_b.player3,
                        team_B_player_4=team_b.player4,
                        team_B_player_5=team_b.player5,
                    )
                    match.save()
