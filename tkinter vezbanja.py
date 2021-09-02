from tkinter import *
import os
root = Tk()
root.geometry('400x400')
root.title('Vezbanje')


# Scales and Scrollbars
'''
def select():
    selected = real_val.get()
    print(selected)
real_val = IntVar()
scale = Scale(root, label = 'range', from_ = 1, to = 200, orient=HORIZONTAL, length = 200,
              troughcolor = 'red', variable = real_val)
scale.pack(anchor = CENTER)

btn1 = Button(root, text='Submit', command = select)
btn1.pack()
lab1 = Label(root, text = 'Scrolls are Weird')
lab1.pack(side = TOP, anchor = NW)

scr_bar = Scrollbar(root)
scr_bar.pack(side = RIGHT)

items = Listbox(root, yscrollcommand = scr_bar.set)
for x in range(100):
    items.insert(END, 'Item: {}'.format(str(x))

    items.pack(side=LEFT)

scr_bar.config(command = items.yview))
'''
# Text Widget

# Menubar and Menum
'''
bar = Menu(root)
def new():
    print('New Clicked')
def open_file():
    print('Open File Clicked')
file = Menu(bar)
file.add_command(label="New", command = new)
file.add_command(label="Open", command = open_file)
file.add_command(label="Save", command = new)
file.add_command(label="Save as", command = new)
file.add_command(label="Close", command = new)
file.add_command(label="Exit", command = new)

bar.add_cascade(label = 'File', menu = file)

root.config(menu=bar)
'''
# Radiobuttons
'''
def selected():
    selected= realStuff.get()
    if selected == 1:
        olab["text"] = "Python"
    elif selected == 2:
        olab["text"] = "C++"
    elif selected == 3:
        olab["text"] = "Java"


rlab = Label(root, text = 'Radio Buttons...')
rlab.pack(anchor = W)

realStuff = IntVar()
rb1 = Radiobutton(root, text='Python', variable = realStuff, value = 1, command = selected)
rb1.pack(anchor = W)
rb2 = Radiobutton(root, text='C++', variable = realStuff, value = 2, command = selected)
rb2.pack(anchor = W)
rb3 = Radiobutton(root, text='Java', variable = realStuff, value = 3, command = selected)
rb3.pack(anchor = W)


olab = Label(root, text = 'Button:')
olab.pack(anchor = W)
'''
# Checkbuttons
'''
def printBoost():
    status10 = turbo_10.get()
    status20 = turbo_20.get()

    if status10 == 1:
        print('Boost: {}'.format(1))
    elif status20 == 1:
        print('Boost: {}'.format(1))
    elif status10 == 1 and status20 == 1:
        print('Boosts: {}, {}'.format(1, 1))

turbo_10 = IntVar()
turbo_20 = IntVar()
lab1 = Label(root, text='Hello everyone!')
lab1.grid(row = 0, column = 0)
cb1 = Checkbutton(root, text = 'turbo 10', variable = turbo_10)
cb1.grid(row = 1, column = 0)
cb2 = Checkbutton(root, text = 'turbo 20', variable = turbo_20)
cb2.grid(row = 2, column = 0)

boostBtn = Button(root, text = 'Boost...', command = printBoost)
boostBtn.grid(row = 3, column = 0)
'''

# Listbox
'''
def insertItem():
    for i in range(5):
        ws.insert(0, 'koji je teeeeeekst')

def deleteItem():
    current = ws.curselection()
    ws.delete(current)

def itemFromEntry():
    ws.insert(0, itemEntry.get())
    itemEntry.delete(0, END)
ws = Listbox(root)
ws.grid(row = 0, column = 0)

itemEntry = Entry(root)
itemEntry.grid(row = 0, column = 2)

insertBtn = Button(root, text='Insert item', command = insertItem)
insertBtn.grid(row = 1, column = 0, pady = 5)

deleteBtn = Button(root, text='Delete item', command = deleteItem)
deleteBtn.grid(row = 1, column = 1, pady = 5)

getBtn = Button(root, text='Get item', command = itemFromEntry)
getBtn.grid(row = 1, column = 2, pady = 5)
'''

root.mainloop()