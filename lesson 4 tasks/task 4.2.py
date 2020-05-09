def counting(number):
    number = str(number)
    summ = 0
    for i in number:
        summ += int(i)
    return summ
        
print(counting(1234))