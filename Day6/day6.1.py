import re
from functools import reduce
use_real_data = True

file = open('Day6/{}_data6.1.txt'.format('real' if use_real_data else 'example'))
raw_data = file.read()
file.close()

per_line_data = [list(filter(lambda x : x != '', line.replace('  ',' ').split(':')[-1].split(' '))) for line in re.split('\n', raw_data)]

allSolutions = []

for index, time in enumerate(per_line_data[0]):
    solutions = []
    for i in range(int(time)):
        result = i * (int(time) - i)
        if result > int(per_line_data[1][index]):
            solutions.append(result)
    allSolutions.append(solutions)

print(allSolutions)
print(reduce(lambda x, y: x * y, [len(solution) for solution in allSolutions]))