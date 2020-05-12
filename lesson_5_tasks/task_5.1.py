# with open('script_copy.py', 'w+') as output, open('task_5.1.py', 'r') as input: output.write(input.read())

file = open('script_copy.py', 'w')

file2 = open('task_5.1.py', 'r')

file.write(file2.read())

file.close()
file2.close()
