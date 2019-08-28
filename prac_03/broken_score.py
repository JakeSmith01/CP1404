def main():
    score = int(input('Enter score:'))
    grade = calculate_grade(score)
    print('Your grade is', grade)


def calculate_grade(score):
    if score < 0 or score > 100:
        return 'Invalid Score'
    elif score >= 90:
        return 'Excellent'
    elif score >= 50:
        return 'Passable'
    else:
        return 'Bad'


main()
