import json, time

try:
    action = int (input('Choose action: 1 for enter a new contact, 2 for open the list of contacts, 3 for quit: '))
except ValueError:
    print('You chose nonexistent action. It will be open list of contacts')
    action = 2

def get_contact():
    name = input('Enter name: ')
    surname = input('Enter surname: ')
    try: 
        phone = int(input('Enter phone: '))
    except ValueError:
        print('You input wrong data. It was replaced to 123')
        phone = 123
    email = input('Enter email: ')
    t = time.strftime('%X', time.localtime())
    new_contact = {'time': t, 'name': name, 'surmane': surname, 'phone': phone, 'email': email}
    return new_contact

def write_json(new_contact):
    try:
        all_contacts = json.load(open('contact.json'))
    except OSError:
        all_contacts = []
    
    file_json = open('contact.json', 'w')
    all_contacts.append(new_contact)
    json.dump(all_contacts, file_json)
    file_json.close()


while action == 1:
    write_json(get_contact())
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
