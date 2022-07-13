import time
import pandas as pd
import numpy as np

def goal_difference(home_goal: int, away_goal: int) -> int:
    difference = home_goal - away_goal
    return difference

def labelwin(goal_difference: int) -> float:
    if goal_difference > 0:
        return 1
    if goal_difference < 0:
        return 0
    else:
        return 0.5

class season:
    def __init__(self, season_matches: pd.DataFrame):
        self.matches = season_matches
        self.matches['goal_difference'] = np.vectorize(goal_difference)(self.matches['home_team_goal_count'], self.matches['away_team_goal_count'])
        self.matches['match_result'] = np.vectorize(labelwin)(self.matches['goal_difference'])

    def games_from_team(self, team_name: str) -> pd.DataFrame:
        result = self.matches.loc[(self.matches['home_team_name'] == team_name) | (self.matches['away_team_name'] == team_name)]
        return result
    
    def last_n_game_week(self, n:int, from_game_week: int)-> pd.DataFrame:
        array = list(range(from_game_week-n, from_game_week+1))
        result = self.matches.loc[self.matches["Game Week"].isin(array)]
        return result

    def last_n_games_for_team(self, team_name: str, n:int)-> pd.DataFrame:
        team_games = self.matches.loc[(self.matches['home_team_name'] == team_name) | (self.matches['away_team_name'] == team_name)]
        result = team_games.tail(n)
        return result

    def get_game_week(self, week:int) -> pd.DataFrame:
        result = self.matches.loc[(self.matches['Game Week'] == week)]
        return result



    
    

    