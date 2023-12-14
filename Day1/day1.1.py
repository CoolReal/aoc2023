use_real_data = True

file = open('Day1/{}_data1.1.txt'.format('real' if use_real_data else 'example'))
raw_data = file.read()
file.close()

per_line_data = raw_data.split('\n')

total_sum = 0
for line in per_line_data:
    number = None
    previous_digit = None
    for letter in line:
        if letter.isdigit():
            previous_digit = letter
        if number is None:
            number = previous_digit
    number += previous_digit
    total_sum += int(number)

print(total_sum)
