import pandas
import os
import glob
import matplotlib.pyplot as plt

def main():
    logs = list(glob.glob(os.path.join("logs",'*.*')))

    stats = {"stamina_spent": 0,
    "effort": 0,
    "tackles": 0,
    }

    players = []
    player_stats = []

    for i in range(2, 12):
        player_stats.append(stats)
        players.append(i)

    print(player_stats)

def log_result(log):
    match_log = pandas.read_csv(log)

    log_len = len(match_log.index) - 1

    # This list contains the number of tackles made by each player, where the index is the player's number - 1
    tackles = []

    # Finds out if RoboCIn is on left or right side
    robocin_side = ""

    if (match_log["team_name_l"][0] == "RoboCIn"):
        robocin_side = "l"
        
    else:
        robocin_side = "r"

    # Filters the columns which will be used
    filter = []

    for i in range(1, 12):
        filter.append(str("player_" + robocin_side + str(i) + "_counting_tackle"))

    for item in filter:
        tackles.append(match_log[item][log_len])

    if (tackles[0] > 0):
        print(log)

    return tackles

main()