import time

file = open('task_5.2_results.txt', 'a', encoding='utf-8')

while True:
    smth = str(input('Input smth: '))
    t = time.strftime('%H.%M.%S', time.localtime())
    # print(t,': ', smth)
    file.write(str(t)+ ': ')
    file.write(str(smth)+ '\n')

file.close()