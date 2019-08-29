def main():
    print('Temperature converter')
    choice = input('Convert from (C)elsius or (F)ahrenheit:').upper()
    if choice == 'C':
        celsius = int(input('Please enter a temperature in celsius'))
        fahrenheit = convert_celsius(celsius)
        print('This converts to', fahrenheit, 'Fahrenheit')
    elif choice == 'F':
        fahrenheit = int(input('Please enter a temperature in fahrenheit'))
        celsius = convert_fahrenheit(fahrenheit)
        print('This converts to', celsius, 'Celsius')
    else:
        print('Invalid Choice')


def convert_celsius(celsius):
    return (celsius * (9 / 5)) + 32


def convert_fahrenheit(fahrenheit):
    return (5 / 9) * (fahrenheit - 32)


main()
