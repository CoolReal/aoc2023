import re

use_real_data = True

file = open('Day4/{}_data4.1.txt'.format('real' if use_real_data else 'example'))
raw_data = file.read()
file.close()

per_line_data = raw_data.split('\n')

sum = 0

for line in per_line_data:
    numbers = line.split(':')[-1].split('|')
    winning_numbers = re.split(r'\s+', numbers[0].strip())
    your_numbers = re.split(r'\s+', numbers[1].strip())
    card_value = 0
    for number in your_numbers:
        if number in winning_numbers:
            card_value = 1 if card_value == 0 else card_value * 2
    sum += card_value

print(sum)