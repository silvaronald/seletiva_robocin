import pandas
import os
import glob
import matplotlib.pyplot as plt

def main():
    logs = list(glob.glob(os.path.join("logs",'*.*')))

    players = []

    # This list contains the number of tackles made by each player, where the index is the player's number - 1
    tackles = []

    for i in range(11):
        tackles.append(0)

        players.append(i + 1)

    for log in logs:
        result = log_result(log)

        for i in range(11):
            tackles[i] += result[i]
    
    # Plots a bar graph
    plt.bar(players, tackles)

    plt.title("Tackles Count")

    plt.xlabel("Player Number")
    plt.xticks(players)
    
    plt.ylabel("Tackles")

    plt.show()

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

    return tackles

main()