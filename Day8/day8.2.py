import re
from functools import cmp_to_key, reduce
import math
use_real_data = True

file = open('Day8/{}_data8.2.txt'.format('real' if use_real_data else 'example'))
raw_data = file.read()
file.close()

per_line_data = raw_data.split('\n')

instructions = per_line_data[0]
elements = []
for element in per_line_data[2:]:
    split = element.split('=')
    lrSplit = split[1].split(',')
    elements.append((split[0].strip(), lrSplit[0].strip()[-3:], lrSplit[1].strip()[:3]))

current_elements = list(filter(lambda x: x[0][-1] == 'A' ,elements))

all_steps = []

for element in current_elements:
    current_element = element
    steps = 0
    while current_element[0][-1] != 'Z':
        current_instruction = instructions[steps % len(instructions)]
        if current_instruction == 'L':
            current_element = list(filter(lambda x: x[0] == current_element[1] ,elements))[0]
        else:
            current_element = list(filter(lambda x: x[0] == current_element[2] ,elements))[0]
        steps += 1
    all_steps.append(steps)

print(all_steps)
print(math.lcm(*all_steps))