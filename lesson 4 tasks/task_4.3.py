import random


def frequent_element(my_list):
    my_list = []
    for i in range(20):
        my_list.append(random.randint(1, 20))
    print(my_list)
    my_dict = {} 
    for element in my_list: 
        if element in my_dict:
            my_dict[element] += 1
        else:
            my_dict[element] = 1
        my_dict2 = {}
        max_v = max(my_dict.values()) #максимальное количество повторений
        my_dict2 = {k:v for k, v in my_dict.items() if v == max_v}
    # print(my_dict)
    # print(my_dict2)
    print(max(my_dict2))

my_list = []
frequent_element(my_list)
