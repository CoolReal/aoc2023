use_real_data = True

file = open('Day3/{}_data3.2.txt'.format('real' if use_real_data else 'example'))
raw_data = file.read()
file.close()

per_line_data = raw_data.split('\n')

def pad_data(data):
    per_line_data.insert(0, '.' * len(per_line_data[0]))
    per_line_data.insert(len(per_line_data), '.' * len(per_line_data[0]))
    for index, line in enumerate(per_line_data):
        per_line_data[index] = '.' + line + '.'

pad_data(per_line_data)

def restore_number(line, index):
    original_index = index
    number = ''
    while index >= 0 and line[index].isdigit():
        number = line[index] + number
        index -= 1
    index = original_index + 1
    while index < len(line) and line[index].isdigit():
        number += line[index]
        index += 1
    return int(number)

def get_adjacent_numbers(lines, index):
    digit_indexes = [[False for x in range(3)] for y in range(3)]
    start_index = index - 1 if index > 0 else 0
    end_index = index + 1 if index < len(lines[0]) - 1 else len(lines[0]) - 1
    for line_index, line in enumerate(lines):
        for character_index, character in enumerate(line[start_index:end_index + 1]):
            digit_indexes[line_index][character_index] = character.isdigit()
    
    for row in digit_indexes:
        if row.count(True) == 2:
            row[1] = False
        if row.count(True) == 3:
            row[1] = False
            row[2] = False

    numbers = []

    for row_index, row in enumerate(digit_indexes):
        for digit_index, digit in enumerate(row):
            if digit:
                numbers.append(restore_number(lines[row_index], digit_index + start_index))

    return numbers

sum = 0

for index, line in enumerate(per_line_data):
    for character_index, character in enumerate(line):
        if character == '*':
            numbers = get_adjacent_numbers(per_line_data[index - 1:index + 2], character_index)
            if (len(numbers) == 2):
                sum += numbers[0] * numbers[1]        
            
print(sum)