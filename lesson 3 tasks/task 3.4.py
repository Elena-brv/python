import random

a = random.randint(0, 50)
# print(a)
attempts = 4 #количество попыток

while attempts >= 1:
    number = int(input('Enter the integer from 0 till 50: '))
    if number == a:
        print('You win!')
        break
    elif number > a: 
        print('The number must be less')
    elif number < a:
        print('The number must be greater')
    attempts -= 1
    print(f'attempts left: {attempts}')
if attempts == 0:
    print('You lose!')
        

