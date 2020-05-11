import random

my_list = []
summ = 0

for i in range(random.randint(1,5)): #i - списки в главном списке
    row = [] #вложенный список
    for j in range(random.randint(1,5)): # j - элементы во вложенных списках
        row.append(random.randint(1,10))
    my_list.append(row)
    for element in row:
        summ += element

print(my_list)
print(summ)
