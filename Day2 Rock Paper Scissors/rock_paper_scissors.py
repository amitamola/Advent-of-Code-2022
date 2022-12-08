# Read the input.txt file

# Open the file in read mode
with open('input.txt', 'r') as file:
    # Read the file
    data = file.read()

# Split the data into by newline
data = data.split('\n')

# A for Rock, B for Paper, and C for Scissors and played by opponent
# X for Rock, Y for Paper, and Z for Scissors and played by you

# Points for selecting: 1 for Rock, 2 for Paper, and 3 for Scissors
# Points for winning: 6 points for winning, 3 points for draw, and 0 points for losing

# Get total points won

# Part 1
play_point = {'X': 1, 'Y': 2, 'Z': 3}

total_points = 0

for val in data:
    val = val.split(' ')
    opponent_play = val[0]
    your_play = val[1]

    total_points += play_point[your_play]

    if opponent_play == 'A':
        if your_play == 'X':
            total_points += 3
        elif your_play == 'Y':
            total_points += 6
        else:
            total_points += 0

    elif opponent_play == 'B':
        if your_play == 'X':
            total_points += 0
        elif your_play == 'Y':
            total_points += 3
        else:
            total_points += 6
    
    else:
        if your_play == 'X':
            total_points += 6
        elif your_play == 'Y':
            total_points += 0
        else:
            total_points += 3

print(total_points)


# Part 2
play_point = {'A': 1, 'B': 2, 'C': 3}

total_points = 0

for val in data:
    val = val.split(' ')
    opponent_play = val[0]
    outcome = val[1]

    if opponent_play == 'A':
        if outcome == 'X':
            your_play = 'C'
            total_points += 0
            total_points += play_point[your_play]
        elif outcome == 'Y':
            your_play = 'A'
            total_points += 3
            total_points += play_point[your_play]
        else:
            your_play = 'B'
            total_points += 6
            total_points += play_point[your_play]

    elif opponent_play == 'B':
        if outcome == 'X':
            your_play = 'A'
            total_points += 0
            total_points += play_point[your_play]
        elif outcome == 'Y':
            your_play = 'B'
            total_points += 3
            total_points += play_point[your_play]
        else:
            your_play = 'C'
            total_points += 6
            total_points += play_point[your_play]
        
    else:
        if outcome == 'X':
            your_play = 'B'
            total_points += 0
            total_points += play_point[your_play]
        elif outcome == 'Y':
            your_play = 'C'
            total_points += 3
            total_points += play_point[your_play]
        else:
            your_play = 'A'
            total_points += 6
            total_points += play_point[your_play]

print(total_points)