def main(converted_celsius, converted_fahrenheit):
    print('Temperature converter')
    choice = input('Convert from (C)elsius or (F)ahrenheit:').upper()
    if choice == 'C':
        celsius_temp = int(input('Please enter a temperature in celsius'))
        convert_celsius(celsius_temp)
        print('This converts to', converted_celsius, 'Fahrenheit')
    elif choice == 'F':
        fahrenheit_temp = int(input('Please enter a temperature in fahrenheit'))
        convert_fahrenheit(fahrenheit_temp)
        print('This converts to', converted_fahrenheit, 'Celsius')
    else:
        print('Invalid Choice')


def convert_celsius(celsius_temp):
    converted_celsius = (celsius_temp * (9/5)) + 32
    return converted_celsius


def convert_fahrenheit(fahrenheit_temp):
    converted_fahrenheit = ((fahrenheit_temp - 32) / (5/9))
    return converted_fahrenheit


main()

