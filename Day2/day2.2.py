from functools import reduce

use_real_data = True

file = open('Day2/{}_data2.2.txt'.format('real' if use_real_data else 'example'))
raw_data = file.read()
file.close()

per_line_data = raw_data.split('\n')

colors = ['red', 'blue', 'green']
total = 0

for line in per_line_data:
    game_split = line.split(':')
    game_pulls = game_split[1].split(';')
    max_count = [0, 0, 0]
    for pull in game_pulls:
        pull = pull.strip()
        per_cube  = pull.split(',')
        for cube in per_cube:
            for color in colors:
                if color in cube:
                    max_count[colors.index(color)] = max(max_count[colors.index(color)], int(cube.strip().split(' ')[0]))
    total += reduce(lambda x, y: x * y, max_count)
print(total)