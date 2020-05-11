import random
N = int(input('Input the count of list’s elements: '))

list_N = []
matches = 0 #количество четных чисел

for i in range(N):
    list_N.append(random.randint(-100, 100))
print(list_N)

for element in list_N:
    if element%2 == 0:
        print(element)
        matches += 1   
if matches < 1:
    print('There are no any even number in the list')
