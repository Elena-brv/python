def compare(a, b):
    if a == b or a + b == 5 or max(a, b) - min(a, b) == 5:
        print('True')
    else:
        print('False')

first_number = 15
second_number = 20
compare(first_number, second_number)
