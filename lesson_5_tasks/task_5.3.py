import time, random

def elements(i):
    for i in range(1000):
        print(random.randint(0,1000))

start_time = time.time()
elements(0)
print(time.strftime('%S'),'\n',(time.time() - start_time),'sec')