file = open('script_copy.py', 'w')
file2 = open('task_5.1.py', 'r')
file.write(file2.read())

file.close()
file2.close()
