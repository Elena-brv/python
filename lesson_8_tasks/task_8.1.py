import json, time

try:
    action = int (input('Choose action: 1 for enter a new contact, 2 for open the list of contacts, 3 for quit: '))
except ValueError:
    print('You chose nonexistent action. It will be open list of contacts')
    action = 2

if action == 1:
    file_json = open('contact.json', 'a')
    name = input('Enter name: ')
    surname = input('Enter surname: ')
    try: 
        phone = int(input('Enter phone: '))
    except ValueError:
        print('You input wrong data. It was replaced to 123')
        phone = 123
    email = input('Enter email: ')
    t = time.strftime('%X', time.localtime())
    contact = {'time': t, 'name': name, 'surmane': surname, 'phone': phone, 'email': email}
    json.dump(contact, file_json)
    file_json.close() 
    try: 
        action = int (input('Choose action: 1 for enter a new contact, 2 for open the list of contacts, 3 for quit: '))
    except ValueError:
        print('You chose nonexistent action. It will be open list of contacts')
        action = 2

if action == 2:
    file_json = open('contact.json', 'r')
    contacts = json.load(file_json)
    file_json.close()
    print(contacts)
    try: 
        list_action = int (input('Choose action: 1 for clear the list, 2 for quit: '))
    except ValueError:
        print('You chose nonexistent action. Program quit')
        list_action = 2


if action == 3 or list_action == 2:
    quit()

if list_action == 1:
    open('contact.json','w').close()
    quit()
