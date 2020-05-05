def suma_element(list_or_tuple):
    summa = 0
    for element in list_or_tuple:
        summa += element
    return summa

my_list = [12, 8, 12, 6, 9]
print(suma_element(my_list))