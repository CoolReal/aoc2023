import re
use_real_data = True

file = open('Day5/{}_data5.2.txt'.format('real' if use_real_data else 'example'))
raw_data = file.read()
file.close()

per_line_data = re.split(r'\n\n', raw_data)

seed_line = per_line_data[0].split(' ')[1:]
seed_ranges = [[int(seed_line[i]), int(seed_line[i + 1])] for i in range(0, len(seed_line), 2)]
maps = []

for line in per_line_data[1:]:
    data = line.split(':')[1].split('\n')[1:]
    maps.append(data)


def segment_ranges(search_range, source, range):
    last_value = source + range - 1

    if search_range[1] < source or search_range[0] > last_value:
        return [[], [search_range]]

    if (search_range[0] >= source and search_range[1] <= last_value):
        return [search_range, []]

    if (search_range[0] <= source and search_range [1] >= last_value):
        return [[source, last_value], [[search_range[0], source - 1], [last_value + 1, search_range[1]]]]

    if (search_range[0] <= source and search_range[1] <= last_value):
        return [[source, search_range[1]], [[search_range[0], source - 1]]]

    if (search_range[0] >= source and search_range[1] >= last_value):
        return [[search_range[0], last_value], [[last_value + 1, search_range[1]]]]

current_ranges = [[range[0], range[0] + range[1] - 1] for range in seed_ranges]
next_ranges = []

for index, map in enumerate(maps):
    next_ranges = []
    while len(current_ranges) > 0:
        found = False
        current_range = current_ranges.pop(0)
        new_ranges = []
        for line in map: 
            destination, source, range = [int(value) for value in line.split(' ')]
            segments = segment_ranges(current_range, source, range)
            if len(segments[0]) == 0:
                continue
            else:
                found = True
                next_ranges.append([segments[0][0] + destination - source, segments[0][1] + destination - source])
                for seg in segments[1]:
                    current_ranges.append(seg)
                
        if not found:
            next_ranges.append(current_range)
    current_ranges = next_ranges

lowest_location = None

for range in current_ranges:
    lowest_location = range[0] if not lowest_location else min(lowest_location, range[0])


print(lowest_location)