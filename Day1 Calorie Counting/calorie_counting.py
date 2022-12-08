# Read the input.txt file

# Open the file in read mode
with open('input.txt', 'r') as file:
    # Read the file
    data = file.read()

# Split the data into by newline
data = data.split('\n')

# Part 1
# Loop through the data and add values till there is empty string and store the max sum
max_sum = 0
summation = 0
for i in data:
    if i == '':
        if summation > max_sum:
            max_sum = summation
        summation = 0
    else:
        summation += int(i)

# Print the max sum
print(max_sum)

# Part 2
# Loop through the data and add values till there is empty string and store the sum in a list
summation = 0
sum_list = []
for i in data:
    if i != '':
        summation += int(i)
    else:
        sum_list.append(summation)
        summation = 0

# Add the maximum 3 values in sum_list
sum_list.sort(reverse=True)
print(sum_list[0] + sum_list[1] + sum_list[2])