OUTPUT_FILE = 'name.txt'
INPUT_FILE = 'numbers.txt'

user_name = input('Please enter your name:')
out_file = open(OUTPUT_FILE, 'w')
print('Your name is {}'.format(user_name), file=out_file)

out_file.close()

in_file = open(INPUT_FILE, 'r')
number1 = int(in_file.readline())
number2 = int(in_file.readline())
in_file.close()
print(number1 + number2)

in_file = open(INPUT_FILE, 'r')
total = 0
for line in in_file:
    number = int(line)
    total = total + number
print(total)
in_file.close()
