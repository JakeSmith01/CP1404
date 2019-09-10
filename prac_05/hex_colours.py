COLOURS_DICT = {'aliceblue': '#f0f8ff', 'antiquewhite1': '#faebd7', 'azure1': '#f0ffff', 'beige': '#f5f5dc'}

colour = input('Please enter a colour name: ').lower()
while colour != '':
    if colour in COLOURS_DICT:
        print(colour, 'is', COLOURS_DICT[colour])
    else:
        print('Invalid Colour')
    colour = input('Please enter a colour name:').lower()
