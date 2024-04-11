##################################################
# Tandin Penjor
# 1st Year, ICE(semester-II)
# Std.no: 02230227
##################################################
# References used while solving this problem are: 
# https://www.geeksforgeeks.org/taking-input-in-python/
# https://youtu.be/UmgE0DaNXKw(video:13min,53sec)
# https://stackoverflow.com/questions/67955658/rock-paper-scissors-game-python-count-feature-not-counting-full-session-using?newreg=2cf738509c8e402ab0d7f239fd2692f8
# https://www.dataquest.io/blog/read-file-python/#:~:text=Python%20provides%20a%20built%2Din,we%20can%20manipulate%20its%20content
##################################################
# SOLUTION:
# MY Solution Score is: 50259 
##################################################

def read_input(input_file):    # defining a function to read the input file(input_7_cap1.txt), argument "input_file"
    game_round = []
    with open(input_file, 'r') as python_file:       # It opens the specified file (input_file) in read mode using 'with' statement
        for line in python_file:
            shape, scoreline = line.strip().split() # The splitting is done based on whitespace, resulting in two parts: shape and outcome
            game_round.append((shape, scoreline))
    return game_round  # Once all lines in the file have been processed, it returns the game_round list containing tuples of (shape, outcome) for each line in the input_file                            

def calculate_score(game_round):            # initiating the function to calculate the score of the game
    score = 0                               # initial score is zero befor starting the game
    for shape, outcome in game_round:
        if shape == "A":
            shape_s = 1                     # shape_s here refers to shape_score
        elif shape == "B":
            shape_s = 2
        elif shape == "C":                  # For each tuple, it checks the value of shape and assigns a corresponding shape_score according to the rules provided
            shape_s = 3

        if outcome == "X":
            outcome_score = 0             
        elif outcome == "Y":               
            outcome_score = 3              
        elif outcome == "Z":
            outcome_score = 6

        score += shape_s + outcome_score  # update score till the end of iteration

    return score                          # Once all rounds have been processed, it returns the final score accumulated over all rounds


input_file = "input_7_cap1.txt"   # Replace with the 'input' to your input_file
game_round = read_input(input_file)       # calls a function read_input(), which is the name of the file containing the game data
total_score = calculate_score(game_round)  # The result is stored in the variable total_score
print("Total Score:", total_score)    # finally the  total score of the game round is calculated 

