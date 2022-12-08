# Read the input.txt file

# Open the file in read mode
with open('input.txt', 'r') as file:
    # Read the file
    data = file.read()

# Split the data into by newline
data = data.split('\n')

# Part 1

vals = [[] for _ in range(9)]
for each_row in data[:8]:
    for i, part in enumerate(range(0, len(each_row), 4)):
        it = each_row[part+1:part+2]
        if it==' ':
            pass
        else:
            vals[i].append(it)
            
for i, item in enumerate(vals):
    vals[i] = item[::-1]

import re

for moves in data[10:]:
    count, frm, to = tuple(map(int, re.findall(r'\d+', moves)))
    for _ in range(count):
        ite = vals[frm-1].pop()
        vals[to-1].append(ite)

print(''.join([last[-1] for last in vals]))

# Part 2

vals = [[] for _ in range(9)]
for each_row in data[:8]:
    for i, part in enumerate(range(0, len(each_row), 4)):
        it = each_row[part+1:part+2]
        if it==' ':
            pass
        else:
            vals[i].append(it)
            
for i, item in enumerate(vals):
    vals[i] = item[::-1]

import re

for moves in data[10:]:
    count, frm, to = tuple(map(int, re.findall(r'\d+', moves)))

    vals[to-1].extend(vals[frm-1][-count:])
    vals[frm-1] = vals[frm-1][:-count]


print(''.join([last[-1] for last in vals]))