from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from teams.models import *
from tournaments.calendars import *


class Match(models.Model):
    league = models.IntegerField(default=1, null=False, blank=False)
    date = models.DateField(null=True, blank=True)
    week = models.IntegerField(null=True, blank=True)
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

    team_A_player_1_score = models.IntegerField(default=0, null=False, blank=False)
    team_A_player_1_goals = models.IntegerField(default=0, null=False, blank=False)
    team_A_player_1_assists = models.IntegerField(default=0, null=False, blank=False)
    team_A_player_1_saves = models.IntegerField(default=0, null=False, blank=False)
    team_A_player_1_shots = models.IntegerField(default=0, null=False, blank=False)

    team_A_player_2_score = models.IntegerField(default=0, null=False, blank=False)
    team_A_player_2_goals = models.IntegerField(default=0, null=False, blank=False)
    team_A_player_2_assists = models.IntegerField(default=0, null=False, blank=False)
    team_A_player_2_saves = models.IntegerField(default=0, null=False, blank=False)
    team_A_player_2_shots = models.IntegerField(default=0, null=False, blank=False)

    team_A_player_3_score = models.IntegerField(default=0, null=False, blank=False)
    team_A_player_3_goals = models.IntegerField(default=0, null=False, blank=False)
    team_A_player_3_assists = models.IntegerField(default=0, null=False, blank=False)
    team_A_player_3_saves = models.IntegerField(default=0, null=False, blank=False)
    team_A_player_3_shots = models.IntegerField(default=0, null=False, blank=False)

    team_A_player_4_score = models.IntegerField(default=0, null=False, blank=False)
    team_A_player_4_goals = models.IntegerField(default=0, null=False, blank=False)
    team_A_player_4_assists = models.IntegerField(default=0, null=False, blank=False)
    team_A_player_4_saves = models.IntegerField(default=0, null=False, blank=False)
    team_A_player_4_shots = models.IntegerField(default=0, null=False, blank=False)

    team_A_player_5_score = models.IntegerField(default=0, null=False, blank=False)
    team_A_player_5_goals = models.IntegerField(default=0, null=False, blank=False)
    team_A_player_5_assists = models.IntegerField(default=0, null=False, blank=False)
    team_A_player_5_saves = models.IntegerField(default=0, null=False, blank=False)
    team_A_player_5_shots = models.IntegerField(default=0, null=False, blank=False)

    team_B_player_1_score = models.IntegerField(default=0, null=False, blank=False)
    team_B_player_1_goals = models.IntegerField(default=0, null=False, blank=False)
    team_B_player_1_assists = models.IntegerField(default=0, null=False, blank=False)
    team_B_player_1_saves = models.IntegerField(default=0, null=False, blank=False)
    team_B_player_1_shots = models.IntegerField(default=0, null=False, blank=False)

    team_B_player_2_score = models.IntegerField(default=0, null=False, blank=False)
    team_B_player_2_goals = models.IntegerField(default=0, null=False, blank=False)
    team_B_player_2_assists = models.IntegerField(default=0, null=False, blank=False)
    team_B_player_2_saves = models.IntegerField(default=0, null=False, blank=False)
    team_B_player_2_shots = models.IntegerField(default=0, null=False, blank=False)

    team_B_player_3_score = models.IntegerField(default=0, null=False, blank=False)
    team_B_player_3_goals = models.IntegerField(default=0, null=False, blank=False)
    team_B_player_3_assists = models.IntegerField(default=0, null=False, blank=False)
    team_B_player_3_saves = models.IntegerField(default=0, null=False, blank=False)
    team_B_player_3_shots = models.IntegerField(default=0, null=False, blank=False)

    team_B_player_4_score = models.IntegerField(default=0, null=False, blank=False)
    team_B_player_4_goals = models.IntegerField(default=0, null=False, blank=False)
    team_B_player_4_assists = models.IntegerField(default=0, null=False, blank=False)
    team_B_player_4_saves = models.IntegerField(default=0, null=False, blank=False)
    team_B_player_4_shots = models.IntegerField(default=0, null=False, blank=False)

    team_B_player_5_score = models.IntegerField(default=0, null=False, blank=False)
    team_B_player_5_goals = models.IntegerField(default=0, null=False, blank=False)
    team_B_player_5_assists = models.IntegerField(default=0, null=False, blank=False)
    team_B_player_5_saves = models.IntegerField(default=0, null=False, blank=False)
    team_B_player_5_shots = models.IntegerField(default=0, null=False, blank=False)

    def get_team_win(self):
        if self.team_A_score > self.team_B_score:
            return self.team_A
        elif self.team_A_score < self.team_B_score:
            return self.team_B
        else:
            return None

    def get_match_play(self):
        if self.team_A_score and self.team_B_score == 0:
            return False
        else:
            return True

    def calculate_player_stats(sender, instance, **kwargs):
        """
        Update the statistics of players involved in a match
        """
        # Loop over the fields corresponding to each team in the match
        for teams in [
            "team_A",
            "team_B",
        ]:
            # Loop over the fields corresponding to each player in the team
            for players in [
                "player_1",
                "player_2",
                "player_3",
                "player_4",
                "player_5",
            ]:
                player_field = f"{teams}_{players}"
                # Get the Player object corresponding to the current player field
                player = getattr(instance, player_field)
                if player is not None:
                    Player.set_statistics(player.id)
            team = getattr(instance, teams)
            Team.set_statistics(team)
            Team.set_teams_stats(team)

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
                # Loop over the fields corresponding to each player in the match
                for player_field in [
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
                ]:
                    # Get the Player object corresponding to the current player field
                    player = getattr(match, player_field)
                    if player is not None:
                        player = Player.objects.select_related().get(id=player.id)
                        # Copy the player's current statistics into a dictionary
                        player_stats = {
                            "score": player.score,
                            "goals": player.goals,
                            "assists": player.assists,
                            "saves": player.saves,
                            "shots": player.shots,
                        }

                        # Loop over the statistics and update the player's stats
                        for stat in player_stats:
                            field_name = f"{player_field}_{stat}"
                            player_stats[stat] += -getattr(match, field_name)

                        # Update the player's statistics in the database
                        Player.objects.update_or_create(
                            id=player.id,
                            defaults=player_stats,
                        )
                match.delete()


@receiver(post_save, sender=Match)
def match_post_save(sender, instance, **kwargs):
    Match.calculate_player_stats(sender, instance, **kwargs)
