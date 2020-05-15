import time, random

def elements():
    for i in range(100000):
        print(random.randint(0,1000))

start_time = time.time()
elements()
print(time.strftime('%S'),'\n',(time.time() - start_time),'sec')
