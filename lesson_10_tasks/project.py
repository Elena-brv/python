from tkinter import Tk, Toplevel, Button, Label, Entry, Listbox, END, SINGLE
import time, random, json

root = Tk()
root.title('Speed game')
root.geometry('800x200')

result = Toplevel()
result.title('Result of current game')
result.withdraw()

records = Toplevel()
records.title('Records of all games')
records.withdraw()

label_game = Label(text='Game', font='Arial 10')
entry_text = Entry(width=300)


def random_phrase():
    with open('random_phrases.txt', 'r') as file:
        lines = file.readlines()
    return random.choice(lines)

line_game = random_phrase()


def start_game(): 
    global start_time
    start_time = time.time()
    label_text = Label(text=f'{line_game}', font='Arial 15')
    label_text.pack()
    check()


def check(): 
    answer = entry_text.get()
    if answer.strip() == line_game.strip():
        game_time = time.time() - start_time
        result.deiconify()
        count_of_backspace = keypress('<BackSpace>')
        result_of_game = f'Your result: {game_time} sec, BackSpace was used {count_of_backspace} time(s)'
        label_result = Label(result, text=f'{result_of_game}')
        label_result.pack()
        t = time.strftime('%c', time.localtime())
        try:
            all_results = json.load(open('results.json'))
        except OSError:
            all_results = []
        file_json = open('results.json', 'w')
        all_results.append({t: result_of_game})
        json.dump(all_results, file_json)
        file_json.close()
    else: 
        root.after(500, check)


def decorator(func):
    decorator.count_bs = -1
    
    def wrapper(arg1):
        decorator.count_bs += 1
        return decorator.count_bs
    return wrapper

@decorator
def keypress(event):
    decorator.count_bs

entry_text.bind('<BackSpace>', keypress)


def show_records():
    records.deiconify()
    file_json = open('results.json', 'r')
    listbox = Listbox(records, width=100, selectmode=SINGLE)
    list_of_records = json.load(file_json)
    for record in list_of_records:
        listbox.insert(END, record)
    listbox.pack()
    file_json.close()


button_start = Button(root,
                    text='Start game',
                    bg='green',
                    fg='white',
                    width=15,
                    height=2,
                    command=start_game        
                )

button_history = Button(root,
                    text='Game history', 
                    bg='purple',
                    fg='white',
                    width=15,
                    height=2,
                    command=show_records
                )

label_game.pack()
button_start.pack()
entry_text.pack()
button_history.pack(side='bottom')
root.mainloop()