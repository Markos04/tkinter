import tkinter as tk
import math

# Variables

orange = '#df861d'
bgblue = '#2d3a4c'
btnbg = '#626c74'
btnfg = '#f5f0e1'
btnbg2 = '#99a4ad'
red = '#aa3d01'

# Classes
class Buttons:
	def __init__(self, master, text, row, column, command=None, padx=10, pady=10, columnspan=None, width=50, height=40,
				 bgcolor=btnbg, activebackground=btnbg, font=('Verdana', 28)):
		self.btn = tk.Button(master, text=text, command=command, image=commonImage, height=height, width=width,
							 compound='c', font=font,
							 bg=bgcolor, fg=btnfg, activebackground=activebackground, activeforeground=btnfg, padx=11,
							 pady=11, bd=2)
		self.btn.grid(row=row, column=column, padx=1, pady=1, columnspan=columnspan)

class Entrys:
	def __init__(self, master, textariable, row, column, justify, columnspan = None, width=None):
		self.entry = tk.Entry(master, textvariable = textariable, justify=justify, width = width, font = ('Calibri', 20), bg ='#ecf0f1',bd=3)
		self.entry.grid(row = row, column = column, columnspan = columnspan,ipady=10, pady=4)

class App(tk.Frame):

	def __init__(self, parent, title, configure=None, resizable=None, iconbitmap=None):
		tk.Frame.__init__(self, parent)
		self.parent = parent
		self.parent.title(title)
		
		mainframe = tk.Frame(parent, bg=bgblue, border=5, pady=2, padx=10)

		self.e = Entrys(mainframe, textin, 0, 0, 'right', 5, 28)
		self.num1 = Buttons(mainframe, '1', 1, 0, lambda: self.printBtn(1))
		self.num2 = Buttons(mainframe, '2', 1, 1, lambda: self.printBtn(2))
		self.num3 = Buttons(mainframe, '3', 1, 2, lambda: self.printBtn(3))

		self.num4 = Buttons(mainframe, '4', 2, 0, lambda: self.printBtn(4))
		self.num5 = Buttons(mainframe, '5', 2, 1, lambda: self.printBtn(5))
		self.num6 = Buttons(mainframe, '6', 2, 2, lambda: self.printBtn(6))

		self.num7 = Buttons(mainframe, '7', 3, 0, lambda: self.printBtn(7))
		self.num8 = Buttons(mainframe, '8', 3, 1, lambda: self.printBtn(8))
		self.num9 = Buttons(mainframe, '9', 3, 2, lambda: self.printBtn(9))

		self.lP = Buttons(mainframe, '(', 4, 0, lambda: self.printBtn('('), 10, 10, None, 50, 40, btnbg2, btnbg2)
		self.num0 = Buttons(mainframe, '0', 4, 1, lambda: self.printBtn(0))
		self.rP = Buttons(mainframe, ')', 4, 2, lambda: self.printBtn(')'), 10, 10, None, 50, 40, btnbg2, btnbg2)
		self.num00 = Buttons(mainframe, '00', 5, 2, lambda: self.printBtn('00'), 10, 10, None, 50, 40)

		self.numC = Buttons(mainframe, 'C', 5, 0, self.clsc, 10, 10, None, 50, 40, red, red)
		self.Dot = Buttons(mainframe, '.', 5, 1, lambda: self.printBtn('.'), 10, 10, None, 50, 40, btnbg2, btnbg2)
		self.numE = Buttons(mainframe, '=', 5, 3, self.equals, 10, 10, 2, 130, 40, red, red)

		self.opAdd = Buttons(mainframe, '+', 1, 3, lambda: self.printBtn('+'), 10, 10, None, 50, 40, orange, orange)
		self.opSub = Buttons(mainframe, '-', 2, 3, lambda: self.printBtn('-'), 10, 10, None, 50, 40, orange, orange)
		self.opMul = Buttons(mainframe, '*', 3, 3, lambda: self.printBtn('*'), 10, 10, None, 50, 40, orange, orange)
		self.opDiv = Buttons(mainframe, '/', 4, 3, lambda: self.printBtn('/'), 10, 10, None, 50, 40, orange, orange)

		self.opBack = Buttons(mainframe, '⌫', 1, 4, self.back, 10, 10, None, 50, 40, orange, orange, ('Verdana', 24))
		self.opSqrt = Buttons(mainframe, '√', 2, 4, self.squert, 10, 10, None, 50, 40, orange, orange, ('Verdana', 24))
		self.opPow = Buttons(mainframe, 'x^2', 3, 4, self.power, 10, 10, None, 50, 40, orange, orange, ('Verdana', 24))
		self.opExp = Buttons(mainframe, 'e^x', 4, 4, lambda: self.printBtn('**'), 10, 10, None, 50, 40, orange, orange, ('Verdana', 24))

		mainframe.grid(row=0, column=0)
		parent.bind("<Key>", self.keyBind)

	def printBtn(self, num):
		global expression

		expression += str(num)
		textin.set(expression)

	def equals(self):
		global expression
		try:
			total = str(eval(expression))
			textin.set(total)
			expression = str(total)
		except SyntaxError:
			textin.set("Invalid Syntax")
		except ZeroDivisionError:
			textin.set("Can't divide by zero")

	def clsc(self):
		global expression
		expression = ""
		textin.set(expression)

	def back(self):
		global expression
		expression = expression[0:len(expression) - 1]
		textin.set(expression)

	def power(self):
		try:
			global expression
			expression = str(float(expression) ** 2)
			textin.set(expression)
		except ValueError:
			textin.set('Invalid Syntax')

	def squert(self):
		try:
			global expression
			expression = str(math.sqrt(float(expression)))
			textin.set(expression)
		except ValueError:
			textin.set('Invalid Syntax')

	def keyBind(self, event):
		global expression
		try:
			if event.keysym in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0"):
				self.printBtn(event.keysym)
			elif event.keysym == "plus":
				self.printBtn("+")
			elif event.keysym == "minus":
				self.printBtn("-")
			elif event.keysym == "asterisk":
				self.printBtn("*")
			elif event.keysym == "slash":
				self.printBtn("/")
			elif event.keysym == "period":
				self.printBtn(".")
			elif event.keysym == "parenleft":
				self.printBtn("(")
			elif event.keysym == "parenright":
				self.printBtn(")")
			elif event.keysym in ("c", "C"):
				self.clsc()
			elif event.keysym in ("Return", "equal"):
				self.equals()
			elif event.keysym in ("s", "S"):
				self.squert()
			elif event.keysym == "at":
				self.power()
			elif event.keysym == "BackSpace":
				expression = expression[0:len(expression) - 1]
				textin.set(expression)
			else:
				textin.set(expression)
		except:
			textin.set("Invalid Syntax")

if __name__ == "__main__":
	root = tk.Tk()
	textin = tk.StringVar()
	expression = ""
	commonImage = tk.PhotoImage(width=1, height=1)
	root.configure(bg='#f5f0e1')
	root.resizable(0, 0)
	app = App(root, "Fancy Calc")
	root.mainloop()