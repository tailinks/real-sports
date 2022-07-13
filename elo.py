def new_elo_calculator(old_elo: float, match_won:bool, expected_outcome:float, match_weight: float)-> float:
    match_result = 0
    if match_won:
        match_result = 1
    new_elo = old_elo + match_importance * (match_result-expected_outcome)
    return new_elo

def home_elo_difference_calculator(home_elo: float, away_elo: float)-> float:
    dr = home_elo - away_elo + 100
    return dr

def home_expected_result(home_elo_difference: float)-> float:
    expected_outcome = 1/(10**(-home_elo_difference/400)+1)
    return expected_outcome

def match_goal_weight(goal_difference: float, match_importance=30)->float:
    goal_difference = abs(goal_difference)
    non_standard_diff = {0:0, 1:1, 2:1.5}
    if goal_difference in list(non_standard_diff.keys()):
        match_goal_weight = non_standard_diff[goal_difference] * match_importance
    else:
        match_goal_weight = (3/4+(goal_difference-3)/8) * match_importance
    return match_goal_weight