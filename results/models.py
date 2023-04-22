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
    def create_matches(sender, **kwargs):
        """
        Create matches for a newly created team or one that has changed leagues
        """
        match_objs = []
        # Get a list of all unique leagues
        for league in Team.objects.values_list("league", flat=True).distinct():
            # Get a list of matches between teams in the league
            matches = calendar(league)
            for team_a, team_b in matches:
                # Check if a match already exists with these teams
                if not Match.objects.filter(team_A=team_a, team_B=team_b).exists():
                    # Create a new match object
                    match_objs.append(
                        Match(
                            league=team_a.league,
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
                    )
        # Create all the new match objects in bulk
        Match.objects.bulk_create(match_objs)

    @receiver(post_save, sender=Team)
    def update_matches(sender, instance, **kwargs):
        """
        Update existing matches when a team is updated
        """
        # Update all matches involving the updated team
        for match in Match.objects.filter(team_A=instance) | Match.objects.filter(
            team_B=instance
        ):
            # Update the player information for the updated team
            match.team_A_player_1 = match.team_A.player1
            match.team_A_player_2 = match.team_A.player2
            match.team_A_player_3 = match.team_A.player3
            match.team_A_player_4 = match.team_A.player4
            match.team_A_player_5 = match.team_A.player5
            match.team_B_player_1 = match.team_B.player1
            match.team_B_player_2 = match.team_B.player2
            match.team_B_player_3 = match.team_B.player3
            match.team_B_player_4 = match.team_B.player4
            match.team_B_player_5 = match.team_B.player5
            match.save()

    @receiver(post_save, sender=Team)
    def delete_matches(sender, instance, **kwargs):
        """
        Delete matches involving a team when it is deleted or has changed leagues
        """
        # Find all matches that involve the deleted team
        for match in Match.objects.filter(team_A=instance) | Match.objects.filter(
            team_B=instance
        ):
            if match.league != instance.league:
                match.delete()
