import re
from functools import reduce
use_real_data = True

file = open('Day6/{}_data6.2.txt'.format('real' if use_real_data else 'example'))
raw_data = file.read()
file.close()

per_line_data = [line.split(':')[1].replace(' ', '') for line in re.split('\n', raw_data)]
per_line_data[0] = [per_line_data[0]]
per_line_data[1] = [per_line_data[1]]

allSolutions = []

for index, time in enumerate(per_line_data[0]):
    solutions = []
    for i in range(int(time)):
        result = i * (int(time) - i)
        if result > int(per_line_data[1][index]):
            solutions.append(result)
    allSolutions.append(solutions)

print(reduce(lambda x, y: x * y, [len(solution) for solution in allSolutions]))