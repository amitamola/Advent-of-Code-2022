# Read the input.txt file

# Open the file in read mode
with open('input.txt', 'r') as file:
    # Read the file
    data = file.read()

# Split the data into by newline
data = data.split('\n')

# Part 1
total = 0

def return_val(val):
    if val.isupper():
        return ord(val)-64+26
    else:
        return ord(val)-96

for string in data:
    #Split the string in two equal half of same length
    string1 = string[:len(string)//2]
    string2 = string[len(string)//2:]

    #Get common characters in both the strings using set intersection
    common = set(string1).intersection(set(string2))
    total+=return_val(common.pop())

print(total)

# Part 2
new_total = 0

# Loop through the data where each set of 3 items three strings to get common characters
for i in range(0, len(data), 3):
    # Get the common characters in all the three strings
    common = set(data[i]).intersection(set(data[i+1]), set(data[i+2]))
    new_total+=return_val(common.pop())

print(new_total)