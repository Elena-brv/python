import string, random
print(string.printable)

def generator_password():
    sequence = string.printable
    password = list()
    for i in range(8):
        password.append(random.choice(sequence))
    password = (''.join(password))
    return password

file = open('passwords.txt', 'a')
password = generator_password()
print(password)
file.write(str(password)+ '\n')

file.close()