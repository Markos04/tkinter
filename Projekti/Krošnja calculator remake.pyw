import tkinter as tk
import os

class Buttons:
    def __init__(self, master, row, column, text, command, bg = '#25b05a', activebackground = '#25b05a', activeforeground= '#fcf2d2', padx = 1, pady = 1):
        self.btn = tk.Button(master, text = text, command = command, image = common_img, width = 45, height = 45, compound='c',
            font = ('Calibri', 30), bg= bg, fg = "#fcf2d2", activebackground=activebackground, activeforeground = '#fcf2d2', padx = 7, pady=7)
        self.btn.grid(row = row, column = column, padx=padx, pady=pady)

class Entrys:
    def __init__(self, master, textvariable, row = 0, column = 0, font=('calibri', 20)):
        self.numEntry = tk.Entry(master, font=font, textvariable = textvariable, bd=5, bg='#fffae8', justify='center', width = 23)
        self.numEntry.grid(row = row, column = column, columnspan = 5, ipady= 10, pady = 10, padx = 2)

class App(tk.Frame):

    def __init__(self, parent, title=None,bg = '#abe6ff', geometry=None, icon = None):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.parent.title(title)
        self.parent.resizable(0,0)
        self.parent.configure(bg = bg)
        
        mFrame = tk.Frame(parent, bd = 20, bg='#fcf2d2')

        self.e = Entrys(mFrame, textin)

        self.num_1 = Buttons(mFrame, 1, 1, '1', lambda:self.printBtn(1))
        self.num_2 = Buttons(mFrame, 1, 2, '2', lambda:self.printBtn(2))
        self.num_3 = Buttons(mFrame, 1, 3, '3', lambda:self.printBtn(3))

        self.pL = Buttons(mFrame, 2, 0, '(', lambda:self.printBtn('('))
        self.num_4 = Buttons(mFrame, 2, 1, '4', lambda:self.printBtn(4))
        self.num_5 = Buttons(mFrame, 2, 2, '5', lambda:self.printBtn(5))
        self.num_6 = Buttons(mFrame, 2, 3, '6', lambda:self.printBtn(6))

        self.Dot = Buttons(mFrame, 3, 0, '.', lambda:self.printBtn('.'))
        self.num_7 = Buttons(mFrame, 3, 1, '7', lambda:self.printBtn(7))
        self.num_8 = Buttons(mFrame, 3, 2, '8', lambda:self.printBtn(8))
        self.num_9 = Buttons(mFrame, 3, 3, '9', lambda:self.printBtn(9))

        self.pR = Buttons(mFrame, 2, 4, ')', lambda:self.printBtn(')'))
        self.num_C = Buttons(mFrame, 4, 1, 'C', self.Clear)
        self.num_0 = Buttons(mFrame, 4, 2, '0', lambda:self.printBtn(0))
        self.eq = Buttons(mFrame, 4, 3, '=', self.Equals)
        self.cc = Buttons(mFrame, 3, 4, '⌫', self.backsp)

        self.opAdd = Buttons(mFrame, 5, 2, '+', lambda:self.printBtn('+'), '#825437', '#825437', '#fcf2d2')
        self.opSub = Buttons(mFrame, 6, 2, '-', lambda:self.printBtn('-'), '#825437', '#825437', '#fcf2d2')
        self.opMul = Buttons(mFrame, 7, 2, '*', lambda:self.printBtn('*'), '#825437', '#825437', '#fcf2d2')
        self.opDiv = Buttons(mFrame, 8, 2, '/', lambda:self.printBtn('/'), '#825437', '#825437', '#fcf2d2')
        
        mFrame.grid(row = 0, column=0)

        self.parent.bind('<Key>', self.keyBind)

    def printBtn(self, number):
        global expression
        expression += str(number)
        textin.set(expression)
        
    def Clear(self):
        global expression
        expression = ""
        textin.set(expression)

    def backsp(self):
        global expression
        expression = expression[0:len(expression)-1]
        textin.set(expression)

    def Equals(self):
        global expression
        try:
            sumup = str(eval(expression))
            textin.set(sumup)
            expression = str(sumup)
        except SyntaxError:
            textin.set('Invalid Syntax')
        except ZeroDivisionError:
            textin.set("Can't divide by zero")

    def keyBind(self, val):
        global expression
        try:
            if val.keysym in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0'):
                self.printBtn(val.keysym)
            if val.keysym == 'plus':
                self.printBtn('+')
            if val.keysym == 'minus':
                self.printBtn('-')
            if val.keysym == 'asterisk':
                self.printBtn('*')
            if val.keysym == 'slash':
                self.printBtn('/')
            if val.keysym == 'parenright':
                self.printBtn(')')
            if val.keysym == 'parenleft':
                self.printBtn('(')
            if val.keysym == 'period':
                self.printBtn('.')
            if val.keysym in ('c', 'C'):
                self.Clear()
            if val.keysym in ('equal', 'Return'):
                self.Equals()
            if val.keysym == 'BackSpace':
                expression = expression[0:len(expression)-1]
                textin.set(expression)
            else:
                textin.set(expression)
        except:
            textin.set('Invalid Syntax')

if __name__ == "__main__":
    root = tk.Tk()
    textin = tk.StringVar()
    expression = ""
    common_img = tk.PhotoImage(width=1, height=1)
    app = App(root, "Krošnja calc")
    root.mainloop()