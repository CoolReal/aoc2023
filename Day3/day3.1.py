use_real_data = True

file = open('Day3/{}_data3.1.txt'.format('real' if use_real_data else 'example'))
raw_data = file.read()
file.close()

per_line_data = raw_data.split('\n')

sum = 0

def pad_data(data):
    per_line_data.insert(0, '.' * len(per_line_data[0]))
    per_line_data.insert(len(per_line_data), '.' * len(per_line_data[0]))
    for index, line in enumerate(per_line_data):
        per_line_data[index] = '.' + line + '.'

def check_for_symbol(lines, index):
    start_index = index - 1 if index > 0 else 0
    end_index = index + 1 if index < len(lines[0]) - 1 else len(lines[0]) - 1
    for line in lines:
        for i in range(start_index, end_index + 1):
            if not line[i].isdigit() and line[i] != '.':
                return True

pad_data(per_line_data)
for index, line in enumerate(per_line_data):
    number = None
    valid = False    
    for character_index, character in enumerate(line):
        if not character.isdigit():
            if number and valid:
                sum += int(number)
            number = None
            valid = False
            continue

        number = number + character if number else character
        valid = valid if valid else check_for_symbol(per_line_data[index - 1:index + 2], character_index)
            
print(sum)