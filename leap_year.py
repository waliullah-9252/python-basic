year = int(input('Enter a year: '))
if year % 4 == 0:
    print(year, 'is leap year')
elif year % 100 == 0:
    print(year, ' is not leap year')
elif year % 400 == 0:
    print(year, ' is leap year')
else:
    print(year, ' is not leap year')