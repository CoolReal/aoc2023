import re
from functools import reduce

use_real_data = False

file = open('Day4/{}_data4.1.txt'.format('real' if use_real_data else 'example'))
raw_data = file.read()
file.close()

per_line_data = raw_data.split('\n')

sum = 0

cards = []

for index, line in enumerate(per_line_data):
    cards.append({'line': line, 'occurences': 1})

for index, card in enumerate(cards):
    numbers = card['line'].split(':')[-1].split('|')
    winning_numbers = re.split(r'\s+', numbers[0].strip())
    your_numbers = re.split(r'\s+', numbers[1].strip())
    found_numbers = 0
    for number in your_numbers:
        if number in winning_numbers:
            found_numbers += 1
            cards[index + found_numbers]['occurences'] += 1 * card['occurences']

print(reduce(lambda x, y: x + y['occurences'], cards, 0))