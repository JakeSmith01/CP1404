MIN_LENGTH = 8


def main():
    user_password = get_password()
    password_length = len(user_password)
    while password_length < MIN_LENGTH:
        print('Password is to short')
        get_password()
    asterisk_printer(password_length)


def get_password():
    password = input('Please enter a password')
    return password


def asterisk_printer(password_length):
    for i in range(0, password_length):
        print('*', end='')


main()
