use_real_data = True

file = open('Day2/{}_data2.1.txt'.format('real' if use_real_data else 'example'))
raw_data = file.read()
file.close()

per_line_data = raw_data.split('\n')

colors = ['red', 'blue', 'green']
color_count = [12, 14, 13]
possible_games = 0

for line in per_line_data:
    game_split = line.split(':')
    game_index = game_split[0][4:].strip()
    game_pulls = game_split[1].split(';')
    possible = True
    for pull in game_pulls:
        pull = pull.strip()
        per_cube  = pull.split(',')
        if not possible:
            break
        for cube in per_cube:
            if not possible:
                break
            for color in colors:
                if color not in cube:
                    continue
                if color_count[colors.index(color)] < int(cube.strip().split(' ')[0]):
                    possible = False
                    break
    if possible:
        possible_games += int(game_index)

print(possible_games)