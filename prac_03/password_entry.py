MIN_LENGTH = 8


def main():
    user_password = get_password()
    asterisk_printer(user_password)


def get_password():
    password = input('Please enter a password')
    while len(password) < MIN_LENGTH:
        print('Password is to short')
        password = input('Please enter a password')
    return password


def asterisk_printer(string):
    for i in range(len(string)):
        print('*', end='')


main()
