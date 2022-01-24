import pandas
import os
import glob
import matplotlib.pyplot as plt

def main():
    logs = list(glob.glob(os.path.join("logs",'*.*')))

    logs_results = []

    for log in logs:
        logs_results.append(log_result(log))

    # Plots graph with the logs results
    y_axis = []
    x_axis = []

    for item in logs_results:
        y_axis.append(item[0])
        x_axis.append(item[1])

    plt.scatter(y_axis, x_axis)

    plt.title("Possession Distribution")

    plt.xlabel("Match result")
    plt.ylabel("Possession percentage")

    plt.show()

# Returns RoboCIn's control percentage in the given match and if the team won, lost or drawed
def log_result(log):
    match_log = pandas.read_csv(log)

    total = 0
    robocin_control = 0

    # Finds out if RoboCIn is on left or right side
    robocin_side = ""

    if (match_log["team_name_l"][0] == "RoboCIn"):
        robocin_side = "l"
        
    else:
        robocin_side = "r"

    # Finds out if RoboCIn won, drawed or lost
    result = None

    left_score = match_log["team_score_l"][len(match_log.index) - 1]
    right_score = match_log["team_score_r"][len(match_log.index) - 1]

    if (right_score == left_score):
        result = "Draw"

    elif ((right_score > left_score and robocin_side == "r") or (left_score > right_score and robocin_side == "l")):
        result = "Win"

    else:
        result = "Lose"

    # Creates a list with the columns that will be used
    filter = ['playmode', 'ball_x', 'ball_y']

    for i in range(1, 12):
        player_l_x = "player_l" + str(i) + "_x"

        player_l_y = "player_l" + str(i) + "_y"

        player_r_x = "player_r" + str(i) + "_x"

        player_r_y = "player_r" + str(i) + "_y"

        filter.append(player_l_x)
        filter.append(player_l_y)
        filter.append(player_r_x)
        filter.append(player_r_y)

    match_log = match_log.filter(filter).where(match_log.playmode == "play_on").dropna()

    # Iterates through each row and matches ball's position to a player position (the closest player to the ball is 
    # chosen), incrementing control by 1 if it's an ally 
    for index, row in match_log.iterrows():
        min_distance = None

        control_side = ""

        # Iterates through players' positions
        for i in range(3, len(filter), 2):
            dist = distance(row["ball_x"], row["ball_y"], row[filter[i]], row[filter[i + 1]])

            if (min_distance == None or dist < min_distance):
                min_distance = dist

                control_side = filter[i][7]

        if (control_side == robocin_side):
            robocin_control += 1
        
        total += 1

    robocin_control = robocin_control / total * 100

    return [result, round(robocin_control)]

# Given the coordinates, calculates the distance (to the power of 2) between two objects
def distance(x1, y1, x2, y2):
    dist = ((x1 - x2) ** 2 + (y1 - y2) ** 2) 

    return dist

main()