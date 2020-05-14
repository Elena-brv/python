string = str(input('Input the string: '))
# print(string[::-1])

if string == string[::-1]:
    print('It’s a palindrome')
else:
    print('It’s not a palindrome')