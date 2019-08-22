user_name = input('Please enter your name:')
print('(H)ello \n(G)oodbye \n(Q)uit')
user_choice = input('>>>').upper()

while user_choice != 'Q':

    if user_choice == 'H':
        print('Hello', user_name)

    elif user_choice == 'G':
        print('Gooodbye', user_name)

    else:
        print('Invalid choice')

    print('(H)ello \n(G)oodbye \n(Q)uit')
    user_choice = input('>>>').upper()

print('Finished')
