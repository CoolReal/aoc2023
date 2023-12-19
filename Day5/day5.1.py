import re
use_real_data = True

file = open('Day5/{}_data5.1.txt'.format('real' if use_real_data else 'example'))
raw_data = file.read()
file.close()

per_line_data = re.split(r'\n\n', raw_data)

seeds = per_line_data[0].split(' ')[1:]
maps = []
for line in per_line_data[1:]:
    data = line.split(':')[1].split('\n')[1:]
    maps.append(data)

lowest_location = None
for seed in seeds:
    search_value = int(seed)
    for index, map in enumerate(maps):
        for line in map:
            destination, source, range = [int(value) for value in line.split(' ')]
            offset = 0
            if search_value >= source and search_value <= source + range - 1:
                offset = search_value - source 
                search_value = destination + offset
                break
    lowest_location = search_value if not lowest_location else min(lowest_location, search_value)
print(lowest_location)    
