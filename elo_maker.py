from elo import *
from last_10_games import *

games = pd.read_csv('france-ligue-1-matches-2018-to-2019-stats.csv')
test = season(games)

start_n = 0
end_n = max(test.matches['Game Week'])

teams = test.matches['away_team_name'].unique()

elo_df = pd.DataFrame(columns = teams)
elo_df.loc[0] = [1000] * len(teams)

for i in range(end_n):
    test.matches.loc
