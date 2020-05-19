from tkinter import Tk, Toplevel, Button, Label, Entry
import time

root = Tk()
root.title('Your contacts')
root.geometry('600x300')

tl = Toplevel()
tl.title('All contacts')
tl.geometry('600x300')
tl.withdraw()

def save_contact():
    file = open('My contacts.txt', 'a')
    t = time.strftime('%X', time.localtime())
    file.write(str(t)+ ': ')
    file.write('Name: ' + str(entry_name.get())+ ', ')
    file.write('Surname: '+ str(entry_surname.get())+ ', ')
    file.write('Phone: '+ str(entry_phone.get())+ ', ')
    file.write('E-mail: '+ str(entry_email.get())+ '\n')
    file.close()


label = Label(text= 'Enter name, surname, phone, email', font= 'Arial 15')
entry_name = Entry(width = 100)
entry_surname = Entry(width = 100)
entry_phone = Entry(width = 100)
entry_email = Entry(width = 100)
button_save = Button(root,
                        text= 'Save contact',
                        bg = 'orange',
                        fg = 'black',
                        width = 20,
                        height = 3,
                        command = save_contact
                        )

def open_contacts():
    tl.deiconify()
    file_cont = open('My contacts.txt', 'r')
    label_tl = Label(tl, text= str(file_cont.read()))
    label_tl.pack()
    file_cont.close()


button_contacts = Button(root,
                            text = 'My contacts',
                            bg = 'green',
                            fg = 'white',
                            width = 20,
                            height = 3,
                            command = open_contacts
                            )


def clear_list():
    open('My contacts.txt','w').close()
    tl.quit()

button_clear = Button(tl,
                        text = 'Clear the list',
                        bg = 'blue',
                        fg = 'white',
                        width = 20,
                        height = 3,
                        command = clear_list
                        )

label.pack()
entry_name.pack()
entry_surname.pack()
entry_phone.pack()
entry_email.pack()
button_save.pack()
button_contacts.pack()
button_clear.pack(side = 'bottom')
root.mainloop()
