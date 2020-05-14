import random, math

my_list = []

for i in range(random.randint(1,10)):
    my_list.append(random.randint(1,1000))
print(my_list)

sorted_list = sorted(my_list)
print(sorted_list)

sqrt = map(lambda i: math.sqrt(i), sorted_list)
sqrt_list = list(sqrt)
print(sqrt_list)

#index_of_mediana 
lenght = len(sqrt_list)
if lenght%2 != 0:
    index_of_mediana = sqrt_list[lenght//2]
else:
    index_of_mediana = (sqrt_list[lenght//2-1] + sqrt_list[lenght//2]) / 2
print(index_of_mediana)

result = filter(lambda ind: ind > index_of_mediana, sqrt_list)
print(list(result))