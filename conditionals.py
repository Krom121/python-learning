# CONDITIONALS

x = 7 

# Basic if 

if x < 6:
    print('this is true')

# if else 

if x < 6:
    print('this is true')
else:
    print('this is false')

# elif 

color = 'red'

if color == 'red':
    print('Color is red')
elif color == 'blue':
    print('Color is blue')
else:
    print('color is not red or blue')

# nesting if 

if color == 'red':
    if x < 10:
        print('color is red and x is less than ten')

# Logical operators

if color == 'red' and x < 10:
     print('color is red and x is less than ten')
