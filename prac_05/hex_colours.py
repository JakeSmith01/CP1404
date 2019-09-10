COLOURS_DICT = {'AliceBlue': '#f0f8ff', 'AntiqueWhite1': '#faebd7', 'Azure1': '#f0ffff', 'Beige': '#f5f5dc'}

colour = input('Please enter a colour name: ').lower()
while colour != '':
    if colour in COLOURS_DICT:
        print(colour, 'is', COLOURS_DICT[colour])
    else:
        print('Invalid Colour')
    colour = input('Please enter a colour name:').lower()
