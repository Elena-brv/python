from tkinter import Tk, Toplevel, Button, Label, Entry, Listbox
import requests, os

root = Tk()
root.title('Save file')
root.geometry('600x150')

label = Label(text='Enter link, path, file’s name with format', font='Arial 15')
entry_link = Entry(width=300)
entry_path = Entry(width=300)
entry_name = Entry(width=300)


def save_file():
    file_link = entry_link.get()
    responce = requests.get(file_link)
    file_path = entry_path.get()
    file_name = entry_name.get()
    if len(file_name) == 0:
        file_name = file_link.split("/")[-1]

    try:
        with open(os.path.join(file_path, file_name), 'wb') as file:
            file.write(responce.content)
    except FileNotFoundError:
        file_path = os.getcwd()
        with open(os.path.join(file_path, file_name), 'wb') as file:
            file.write(responce.content)

    root.withdraw()
 

button_save = Button (root,
                    text='Save file',
                    bg='green',
                    fg='white',
                    width=15,
                    height=2,
                    command = save_file
                    )

label.pack()
entry_link.pack()
entry_path.pack()
entry_name.pack()
button_save.pack()
root.mainloop()
