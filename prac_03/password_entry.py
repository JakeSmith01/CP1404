MIN_LENGTH = 8
password = input('Please enter a password')
password_length = len(password)

while password_length < MIN_LENGTH:
    print('Password is to short')
    password = input('Please enter a password')

for i in range(0, password_length):
    print('*', end='')

