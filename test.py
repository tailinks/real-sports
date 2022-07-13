from last_10_games import season
import pandas as pd
games = pd.read_csv('france-ligue-1-matches-2018-to-2019-stats.csv')
test = season(games)
print(max(test.matches['Game Week']))