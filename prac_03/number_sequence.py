def main():
    print('Number Sequence Menu')
    print('(E)ven \n(O)dd \n(S)quares \n(Q)uit')
    user_choice = input('>>>').upper()

    while user_choice != 'Q':
        if user_choice == 'E':
            print_evens()

        elif user_choice == 'O':
            print_odds()

        elif user_choice == 'S':
            print_squares()

        else:
            print('Invalid choice')

    print('Thanks for using the program!')


def print_evens():
    lower_number = int(input('Please enter the lower number:'))
    upper_number = int(input('Please enter the upper number:'))

    for i in range(lower_number, upper_number+1):
        even_check = i % 2

        if even_check == 0:
            print(i)

    main()


def print_odds():
    lower_number = int(input('Please enter the lower number:'))
    upper_number = int(input('Please enter the upper number:'))

    for i in range(lower_number, upper_number+1):
        odd_check = i % 2

        if odd_check != 0:
            print(i)

    main()


def print_squares():
    lower_number = int(input('Please enter the lower number:'))
    upper_number = int(input('Please enter the upper number:'))

    for i in range(lower_number, upper_number + 1):
        squared_number = i * i
        print(squared_number)

    main()


main()
