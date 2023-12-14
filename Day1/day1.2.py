use_real_data = True

file = open('Day1/{}_data1.2.txt'.format('real' if use_real_data else 'example'))
raw_data = file.read()
file.close()

per_line_data = raw_data.split('\n')

numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

total_sum = 0
for line in per_line_data:
    current_number = None
    previous_digit = None
    composite_string = ''
    for letter in line:
        if letter.isdigit():
            composite_string = ''
            previous_digit = letter
        else:
            composite_string += letter
            for number in numbers:
                if len(number) > len(composite_string):
                    continue
                if number in composite_string[-len(number):]:
                    previous_digit = numbers.index(number) + 1
                    break

        if current_number is None and previous_digit is not None:
            current_number = str(previous_digit)
    current_number += str(previous_digit)
    total_sum += int(current_number)

print(total_sum)
