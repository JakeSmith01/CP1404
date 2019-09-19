from prac_06.guitar import Guitar

example = Guitar('Gibson L-5 CES', 1922, 16035.40)
another_guitar = Guitar('Another Guitar', 2012, 2.50)
print(example)
print(another_guitar)
print('Example get_age() - Expected 97, Got', example.get_age())
print('Another_Guitar get_age() - Expected 7, Got', another_guitar.get_age())
print('Example is_vintage() - Expected True, Got', example.is_vintage())
print('Another_Guitar is_vintage() - Expected False, Got', another_guitar.is_vintage())
