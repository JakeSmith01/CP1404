"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""

MIN_LENGTH = 2
MAX_LENGTH = 6
SPECIAL_CHARS_REQUIRED = True
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH,
          "characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if SPECIAL_CHARS_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print("Your {}-character password is valid: {}".format(len(password),
                                                           password))


def is_valid_password(password):
    """Determine if the provided password is valid."""
    password_length = 0
    lower_case = 0
    upper_case = 0
    numbers = 0
    special_check = 0
    for char in password:

        password_length = password_length + 1

        if char.islower():
            lower_case = lower_case + 1

        elif char.isupper():
            upper_case = upper_case + 1

        elif char.isdigit():
            numbers = numbers + 1

        elif char in SPECIAL_CHARACTERS:
            special_check = special_check + 1

    if password_length < MIN_LENGTH or password_length > MAX_LENGTH:
        return False

    elif lower_case < 1:
        return False

    elif upper_case < 1:
        return False

    elif numbers < 1:
        return False

    elif SPECIAL_CHARS_REQUIRED == True:
        if special_check < 1:
            return False

    else:
        return True


main()
