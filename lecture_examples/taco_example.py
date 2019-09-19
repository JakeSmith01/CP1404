class User:
    number_of_tacos = 5
    score = 0

    def __init__(self, name):
        self.name = name

    def give_taco(self):
        User.number_of_tacos = User.number_of_tacos - 1

    def __str__(self):
        return '{}, {} points, {} tacos left'.format(self.name, User.number_of_tacos, User.score)


print('Taco Rewards')
user_name_1 = input('Enter the name of user 1')
user_name_2 = input('Enter the name of user 2')
u1 = User(user_name_1)
u2 = User(user_name_2)
print('''(G)ive Taco
(S)core
(Q)uit''')
choice = input('>>>').lower()
while choice != 'q':
    if choice == 'g':




