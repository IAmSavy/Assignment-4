Year = int(input('Enter a year:'))
if Year % 100 == 0:
    if Year % 400 == 0: print('The year ', Year, ' is a leap year.')
    else: print('The year ', Year, ' is not a leap year.')
elif Year % 4 == 0: print('The year ', Year, ' is a leap year.')
else: print('The year ', Year, ' is not a leap year.')