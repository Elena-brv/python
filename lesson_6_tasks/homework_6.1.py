import time

def decorator(func):

    def wrapper(a, b):
        file = open('logs.txt', 'a')
        t = time.strftime('%c')
        file.write(str(t)+ ': ')
        result = func(a, b)
        file.write(str(result)+ '\n')
        file.close()
        return result
    
    return wrapper

@decorator
def my_sum(a, b):
    suma = a + b
    return suma

print(my_sum(5, 3))