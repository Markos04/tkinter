from tkinter import *
import tkinter.messagebox as mb
import os
import time

root = Tk()
root.geometry('1024x600')
root.title('Aplikacija')
#root.resizable(0,0)

# Frames
mainMenu = Frame(root, bg='#ffdd99')
mainButtons = Frame(mainMenu, bg='#ffdd99')
other = Frame(root, bg='#ffdd99')


# Variables
label1img = PhotoImage(file = r'C:\Users\Stevanovic\Desktop\slike za programe\mainLabel1.png')

# Functions
def topLevel1():
    root1 = Toplevel()
    root1.geometry('800x600')

    pathEntry = Frame(root1, highlightbackground='black', highlightthickness=1, bg='#ffdd99')
    other = Frame(root1, highlightbackground='black', highlightthickness=1, bg='#ffdd99')

    lab1 = Label(pathEntry, text='Enter Path: ', font=('TkDefaultFont', 20))
    lab1.grid(row=0, column=0)
    global ent1
    ent1 = Entry(pathEntry, font=('TkDefaultFont', 20))
    ent1.grid(row=0, column=1)

    getPath1 = Button(other, command = setPATH, text='Set Path', font=('TkDefaultFont', 14))
    getPath1.grid(row=1, column=0)

    pathEntry.pack(side=TOP, anchor=SW, padx = 5, pady = 5)
    other.pack(side=TOP, anchor=SW, padx = 5, pady = 5)

def setPATH():
    global path
    path = ent1.get()
    os.chdir('{}'.format(path))


def forgetList():
    ListDirectories.grid_forget()
    
def dirList():
    global ListDirectories
    ListDirectories = Label(other)
    for f in os.listdir():
        if f == os.listdir()[-1]:
            ListDirectories["text"] += '{}'.format(f)
            break
        ListDirectories["text"] += '{}, \n'.format(f)
    ListDirectories.grid(row=3, column=0)
    
# mainMenu

mainLabel = Label(root, text='File Sorter', image = label1img, height = 50, compound = CENTER, font=('Comic Sans MS', 30, 'bold'), fg='white')
mainLabel.pack(fill=X)
mBtn1 = Button(mainButtons, text='Set Path', command = topLevel1, font=('TkDefaultFont', 14))
mBtn1.grid(row=1, column=0, padx = 79)
mBtn2 = Button(mainButtons, text='Window 2', command = topLevel1, font=('TkDefaultFont', 14))
mBtn2.grid(row=1, column=1, padx = 79)
mBtn3 = Button(mainButtons, text='Window 3', command = topLevel1, font=('TkDefaultFont', 14))
mBtn3.grid(row=1, column=2, padx = 79)
mBtn4 = Button(mainButtons, text='Window 4', command = topLevel1, font=('TkDefaultFont', 14))
mBtn4.grid(row=1, column=3, padx = 79)

# Other
listBtn = Button(other, text='List Directories', font=('TkDefaultFont', 14), command = dirList)
listBtn.grid(row=2, column=0, padx = 4, pady = 5)
forgetBtn = Button(other, text='Forget Directiories', font=('TkDefaultFont', 14), command = forgetList)
forgetBtn.grid(row=2, column=2, padx = 4, pady = 5)

# Frame Packing
mainMenu.pack(fill=Y)
mainButtons.pack(fill=X, pady = 10)
other.pack(fill = BOTH, expand=True)
root.mainloop()
