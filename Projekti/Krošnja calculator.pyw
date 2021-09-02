from tkinter import *
import tkinter.messagebox as mb
import os

root = Tk()
root.geometry('310x500')
root.title('Krošnja Calc')
#root.iconbitmap(r'C:/Users/Stevanovic/Downloads/tree_gLw_icon.ico')
root.resizable(0,0)
root.configure(bg='#b3ecff')

#Frames
buttons123 = Frame(root, bg='#b3ecff')
buttons456 = Frame(root, bg='#b3ecff')
buttons789 = Frame(root, bg='#b3ecff')
buttonsOP = Frame(root, bg='#b3ecff')
buttons0CS = Frame(root, bg='#b3ecff')
entryFrame = Frame(root, bg='#b3ecff')


# Functions
operator = ""
textin = StringVar()

def printButt(number):
    global operator
    operator += str(number)
    textin.set(operator)
    
def ClearSpaceBtn():
    global operator
    operator = ""
    textin.set("")

def EqualsInputBtn():
    try:
        global operator
        sumup = eval(operator)
        textin.set(sumup)
        operator = ""
    except SyntaxError:
        print('')
        ClearSpaceBtn()

# Making Buttons
numEntry = Entry(entryFrame, font=('arial', 20, 'bold'), textvariable = textin, bd=4, bg='#b3ecff', justify='center')
common_img = PhotoImage(width=1, height=1)
	# 123
num_1 = Button(buttons123, text='1', command = lambda:printButt(1), image = common_img, width = 45, height = 45, compound='c', font = ('TkDefaultFont', 30), bg = 'lightgreen', activebackground = 'lightgreen')
num_2 = Button(buttons123, text='2', command = lambda:printButt(2), image = common_img, width = 45, height = 45, compound='c', font = ('TkDefaultFont', 30), bg = 'lightgreen', activebackground = 'lightgreen')
num_3 = Button(buttons123, text='3', command = lambda:printButt(3), image = common_img, width = 45, height = 45, compound='c', font = ('TkDefaultFont', 30), bg = 'lightgreen', activebackground = 'lightgreen')
	# 456
num_4 = Button(buttons456, text='4', command = lambda:printButt(4), image = common_img, width = 45, height = 45, compound='c', font = ('TkDefaultFont', 30), bg = 'lightgreen', activebackground = 'lightgreen')
num_5 = Button(buttons456, text='5', command = lambda:printButt(5), image = common_img, width = 45, height = 45, compound='c', font = ('TkDefaultFont', 30), bg = 'lightgreen', activebackground = 'lightgreen')
num_6 = Button(buttons456, text='6', command = lambda:printButt(6), image = common_img, width = 45, height = 45, compound='c', font = ('TkDefaultFont', 30), bg = 'lightgreen', activebackground = 'lightgreen')
	# 789
num_7 = Button(buttons789, text='7', command = lambda:printButt(7), image = common_img, width = 45, height = 45, compound='c', font = ('TkDefaultFont', 30), bg = 'lightgreen', activebackground = 'lightgreen')
num_8 = Button(buttons789, text='8', command = lambda:printButt(8), image = common_img, width = 45, height = 45, compound='c', font = ('TkDefaultFont', 30), bg = 'lightgreen', activebackground = 'lightgreen')
num_9 = Button(buttons789, text='9', command = lambda:printButt(9), image = common_img, width = 45, height = 45, compound='c', font = ('TkDefaultFont', 30), bg = 'lightgreen', activebackground = 'lightgreen')
	# +-*/
op_add = Button(buttonsOP, text='+', command = lambda:printButt('+'), image = common_img, width = 45, height = 45, compound='c', font = ('TkDefaultFont', 30), bg = 'brown', activebackground = 'brown')
op_subtract = Button(buttonsOP, text='-', command = lambda:printButt('-'), image = common_img, width = 45, height = 45, compound='c', font = ('TkDefaultFont', 30), bg = 'brown', activebackground = 'brown')
op_multiply = Button(buttonsOP, text='*', command = lambda:printButt('*'), image = common_img, width = 45, height = 45, compound='c', font = ('TkDefaultFont', 30), bg = 'brown', activebackground = 'brown')
op_divide = Button(buttonsOP, text='/', command = lambda:printButt('/'), image = common_img, width = 45, height = 45, compound='c', font = ('TkDefaultFont', 30), bg = 'brown', activebackground = 'brown')
	# 0C=
num_0 = Button(buttons0CS, text='0', command = lambda:printButt(0), image = common_img, width = 45, height = 45, compound='c', font = ('TkDefaultFont', 30), bg = 'lightgreen', activebackground = 'lightgreen')
EqualsBtn = Button(buttons0CS, text='=', command = EqualsInputBtn, image = common_img, width = 45, height = 45, compound='c', font = ('TkDefaultFont', 30), bg = 'lightgreen', activebackground = 'lightgreen')
op_C = Button(buttons0CS, text='C', command = ClearSpaceBtn, image = common_img, width = 45, height = 45, compound='c', font = ('TkDefaultFont', 30), bg = 'lightgreen', activebackground = 'lightgreen')

buttList = [0, num_1, num_2, num_3, num_4, num_5, num_6, num_7, num_8, num_9, op_add, op_subtract, op_multiply, op_divide]

# Packing Buttons
numEntry.pack(side=LEFT, anchor=NE)
num_1.grid(row = 1, column = 0)
num_2.grid(row = 1, column = 1, padx = 5)
num_3.grid(row = 1, column = 2)
num_4.grid(row = 2, column = 0)
num_5.grid(row = 2, column = 1, padx = 5)
num_6.grid(row = 2, column = 2)
num_7.grid(row = 3, column = 0)
num_8.grid(row = 3, column = 1, padx = 5)
num_9.grid(row = 3, column = 2)
num_0.grid(row = 4, column = 0)
op_C.grid(row = 4, column = 1, padx = 5)
EqualsBtn.grid(row = 4, column = 2)
op_add.grid(row = 4, column = 0, pady = 2)
op_subtract.grid(row = 5, column = 0)
op_multiply.grid(row = 6, column = 0, pady = 2)
op_divide.grid(row = 7, column = 0)

entryFrame.grid(row = 0, column = 0)
buttons123.grid(row = 1, column = 0, padx = 5, pady = 2)
buttons456.grid(row = 2, column = 0, padx = 5)
buttons789.grid(row = 3, column = 0, padx = 5, pady = 2)
buttons0CS.grid(row = 4, column = 0, padx = 5)
buttonsOP.grid(row = 5, column = 0)

root.mainloop()



