# Read the input.txt file

# Open the file in read mode
with open('input.txt', 'r') as file:
    # Read the file
    data = file.read()

# Split the data into by newline
data = data.split('\n')

# Part 1

data = data[0]
for index in range(len(data)):
    dt = data[index:index+4]
    
    if len(set(dt))==4:
        print(dt)
        print(index+4)
        break

# Part 2

# Read the input.txt file

# Open the file in read mode
with open('Advent-of-Code-2022/Day6 Tuning Trouble/input.txt', 'r') as file:
    # Read the file
    data = file.read()

# Split the data into by newline
data = data.split('\n')

data = data[0]
for index in range(len(data)):
    dt = data[index:index+14]
    
    if len(set(dt))==14:
        print(dt)
        print(index+14)
        break