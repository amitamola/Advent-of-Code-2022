# Read the input.txt file

# Open the file in read mode
with open('input.txt', 'r') as file:
    # Read the file
    data = file.read()

# Split the data into by newline
data = data.split('\n')

# Part 1
total = 0

for val in data:
    pair1, pair2 = val.split(',')

    # Create set of values in pair1 and pair2
    p1v1, p1v2 = tuple(map(lambda x: int(x), pair1.split('-')))
    pair1 = set(range(p1v1, p1v2+1))

    p2v1, p2v2 = tuple(map(lambda x: int(x), pair2.split('-')))
    pair2 = set(range(p2v1, p2v2+1))

    if len(pair1) > len(pair2):
        # Subtract pair2 from pair1
        output = pair2 - pair1
    else:
        # Subtract pair1 from pair2
        output = pair1 - pair2

    # If output lenght is 0 then add 1 to total
    if len(output) == 0:
        total += 1

print(total)

# Part 2
total = 0

for val in data:
    pair1, pair2 = val.split(',')

    # Create set of values in pair1 and pair2
    p1v1, p1v2 = tuple(map(lambda x: int(x), pair1.split('-')))
    pair1 = set(range(p1v1, p1v2+1))

    p2v1, p2v2 = tuple(map(lambda x: int(x), pair2.split('-')))
    pair2 = set(range(p2v1, p2v2+1))

    # Check intersection of pair1 and pair2
    output = pair1.intersection(pair2)

    if len(output)>0:
        total += 1

print(total)