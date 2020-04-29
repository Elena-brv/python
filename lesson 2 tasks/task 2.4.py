value = float (input('Enter value in metres: '))
unit = str (input('Choose unit (mm,sm,km): '))

if value >= 0:
    if unit == 'mm':
        print(f'{value} m = {value * 1000} mm')
    elif unit == 'sm':
        print(f'{value} m = {value * 100} sm')
    elif unit == 'km':
        print(f'{value} m = {value / 1000} km')
else:
    print('You chose wrong unit or value. Try again.')