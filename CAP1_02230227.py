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
# MY Solution Score is: 50169
##################################################

def read_input(input_file):    # defining a function to read the input file(input_7_cap1.txt), with argument "input_file"
    game_round = []
    with open(input_file, 'r') as python_file:    # It opens the specified file (input_file) in read mode  the 'with' statement
        for line in python_file:
            shape, scoreline = line.strip().split() # The splitting is done based on whitespace, resulting in two parts: shape and outcome
            game_round.append((shape, scoreline))
    return game_round  # Once all lines in the file have been processed, it returns the game_round list containing tuples of (shape, outcome) for each line in the input_file                            

def calculate_score(game_round):            # initiating the function to calculate the score of the game
    play_score = 0                          # initial  play_score is zero befor starting the game
    for shape, overview in game_round:
        if shape == "A":                    # coloum containing 'A' means Rock
            if overview == "X":             # game round with  'A' and 'X' means you have to lose so, we select scissor
                round_score = 3             # 3 + 0 = 3 (round score)  
            elif overview == "Y":           # now game round with 'A' and 'Y' so, we need to make it draw so, we select rock
                round_score = 4             # 1 + 3 =4 (round score)
            else:                           # if not X and Y(else) then it moves to Z means we have to win 
                round_score = 8             # 2 + 6 = 8(round score)


        elif shape == "B":                  # "B": Paper
            if overview == "X":             # round with 'B' and 'X', we have to lose with showing rock
                round_score = 1             # 1 + 0 = 1(round score)
            elif overview == "Y":           # round with 'B' and 'Y' we have to make it draw showing (B) Paper
                round_score = 5             # 2 + 3 = 5(round score)
            else:                           # round with 'B' and 'Z' so we have to win
                round_score = 9             # 3 + 6 = 9(round score)
        

        else:                               # else(C) = scissor
            if overview == "X":             # round with 'C' and 'X', we have to lose
                round_score = 2             # 2 + 0 = 2(round score)
            elif overview == "Y":           # round with 'C' and 'Y', we have to make it draw call
                round_score = 6             # 3 + 3 = 6(round score)
            else:                           # else here refers to round with 'C' and 'Z' so, we have to win
                round_score = 7             # 1 + 6 = 7(round score)
        

        play_score += round_score   # update score till the end of iteration
    
    return play_score               # Once all rounds have been processed, it returns the final score accumulated over all rounds

                                
                       

input_file = "input_7_cap1.txt"   # Replace with the 'input' to your input_file
game_round = read_input(input_file)    # calls a function read_input(), which is the name of the file containing the game data
total_round_score = calculate_score(game_round)  # The result is stored in the variable total_score
print("Total Score:", total_round_score)    # finally the  total score of the game round is been calculated 

