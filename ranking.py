import pandas
import os
import glob
import matplotlib.pyplot as plt

def main():
    logs = list(glob.glob(os.path.join("logs",'*.*')))

    logs_len = len(logs)

    # The score is based on stamina spent, tackles count and effort
    players = []
    scores = []

    for i in range(2, 12):
        players.append(i)
        scores.append(0)

    for log in logs:
        results = log_result(log)

        for i in range(10):
            # The formula used to calculate the score is: (stamina + tackles) * effort
            # The final score is the mean of all matches scores
            scores[i] += results[i][0] * results[i][2] * results[i][1] / logs_len

    # Plots graph with players' scores
    plt.bar(players, scores)

    plt.title("Players rating")

    plt.xlabel("Player number")
    plt.ylabel("Player score")

    plt.xticks(players)
    plt.yticks([])

    plt.show()

def log_result(log):
    match_log = pandas.read_csv(log)

    log_len = len(match_log.index) - 1

    # Finds out if RoboCIn is on left or right side
    robocin_side = ""

    if (match_log["team_name_l"][0] == "RoboCIn"):
        robocin_side = "l"
        
    else:
        robocin_side = "r"

    # Calculate players' tackle count
    tackles = []

    filter = []

    for i in range(2, 12):
        filter.append(str("player_" + robocin_side + str(i) + "_counting_tackle"))

    for item in filter:
        tackles.append(match_log[item][log_len])

    # Calculate players' effort
    efforts = []

    filter = []

    for i in range(2, 12):
        filter.append(str("player_" + robocin_side + str(i) + "_attribute_effort"))

    for item in filter:
        efforts.append(match_log[item][0])

    # Calculate players' spent stamina (being (inicial stamina capacity - final stamina capacity) / inicial stamina capacity)
    stamina = []

    filter = []

    for i in range(2, 12):
        filter.append(str("player_" + robocin_side + str(i) + "_attribute_stamina_capacity"))

    for item in filter:
        stamina.append((match_log[item][0] - match_log[item][log_len]) / match_log[item][0])

    # Returns a list with each player's statistics
    stats = []

    for i in range(10):
        player_stats = [stamina[i], efforts[i], tackles[i]]

        stats.append(player_stats)
    
    return stats

main()