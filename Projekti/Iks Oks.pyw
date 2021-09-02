import tkinter as tk
import tkinter.messagebox
from tkinter import filedialog
import os

class Buttons(tk.Button):
	def __init__(self, master, row, column, command, textvariable = None, width=19, height = 9, 
		bd=2, bdcolor= 'black', padx=None, pady=None, bg='white', activebg = 'white',relief='groove'):
		self.btnvar = tk.StringVar()
		self.btn = tk.Button(master, command=command, textvariable = self.btnvar, activebackground = activebg,
		highlightcolor = activebg, bd=3, width = width, height = height, bg=bg, relief=relief)
		self.btn.grid(row=row, column=column)

	def setState(self):
		self.btn['state'] = 'disabled'

class App(tk.Frame):
	click = True
	count = 0

	def __init__(self, master, title=None, icon=None, geometry=None, bg="white"):
		tk.Frame.__init__(self, master)
			
		self.master = master
		self.master.title(title)
		self.master.geometry(geometry)
		self.master.config(bg=bg)
		self.master.resizable(False, False)

		self.scoreFrame = tk.Frame(self.master, bg=bg)
		self.gameFrame = tk.Frame(self.master, bd = 50, bg=bg)
		self.scoreFrame.grid(row=0, column=0)
		self.gameFrame.grid(row=1, column=0)

		
		# Textvariables
		self.btn1var = tk.StringVar()
		self.btn2var = tk.StringVar()
		self.btn3var = tk.StringVar()
		self.btn4var = tk.StringVar()
		self.btn5var = tk.StringVar()
		self.btn6var = tk.StringVar()
		self.btn7var = tk.StringVar()
		self.btn8var = tk.StringVar()
		self.btn9var = tk.StringVar()
		self.btnVars = [0, self.btn1var, self.btn2var, self.btn3var, self.btn4var, self.btn5var, self.btn6var, self.btn7var, self.btn8var, self.btn9var]
		self.xScore = 0
		self.oScore = 0

		self.play()

	def play(self):
		self.xLab = tk.Label(self.scoreFrame, text="X: {}".format(self.xScore), padx = 10, pady = 10, font = ("Comic Sans MS", 20), bg='white')
		self.xLab.grid(row=0, column=0, padx=(0, 100))
		self.oLab = tk.Label(self.scoreFrame, text="O: {}".format(self.oScore), padx = 10, pady = 10, font = ("Comic Sans MS", 20), bg='white')
		self.oLab.grid(row=0, column=1, padx=(100, 0))
		self.btn1 = Buttons(self.gameFrame, 0, 0, lambda: self.press(1,0,0), self.btn1var)
		self.btn2 = Buttons(self.gameFrame, 0, 1, lambda: self.press(2,0,1), self.btn2var)
		self.btn3 = Buttons(self.gameFrame, 0, 2, lambda: self.press(3,0,2), self.btn3var)
		self.btn4 = Buttons(self.gameFrame, 1, 0, lambda: self.press(4,1,0), self.btn4var)
		self.btn5 = Buttons(self.gameFrame, 1, 1, lambda: self.press(5,1,1), self.btn5var)
		self.btn6 = Buttons(self.gameFrame, 1, 2, lambda: self.press(6,1,2), self.btn6var)
		self.btn7 = Buttons(self.gameFrame, 2, 0, lambda: self.press(7,2,0), self.btn7var)
		self.btn8 = Buttons(self.gameFrame, 2, 1, lambda: self.press(8,2,1), self.btn8var)
		self.btn9 = Buttons(self.gameFrame, 2, 2, lambda: self.press(9,2,2), self.btn9var)

		self.btns = [0, self.btn1, self.btn2, self.btn3, self.btn4, self.btn5, self.btn6, self.btn7, self.btn8, self.btn9]

	def press(self, num, r, c):
		global count, click

		for i in range(1, 10):
			if num == i:
				if self.count % 2 == 0:
					self.labph = tk.Label(self.gameFrame, image=xph, bd=0)
					self.labph.grid(row=r, column=c)
					self.btnVars[i].set('X')
					self.count += 1
					Buttons.setState(self.btns[i])
					break

				elif self.count % 2 == 1:
					self.labph = tk.Label(self.gameFrame, image=oph, bd=0)
					self.labph.grid(row=r, column=c)
					self.btnVars[i].set('O')
					self.count += 1
					Buttons.setState(self.btns[i])
					break
		self.check()

	def check(self):
		global count, click
		if (self.btn1var.get() == 'X' and self.btn2var.get() == 'X' and self.btn3var.get() == 'X' or
			self.btn4var.get() == 'X' and self.btn5var.get() == 'X' and self.btn6var.get() == 'X' or
			self.btn7var.get() == 'X' and self.btn8var.get() == 'X' and self.btn9var.get() == 'X' or
			self.btn1var.get() == 'X' and self.btn4var.get() == 'X' and self.btn7var.get() == 'X' or
			self.btn2var.get() == 'X' and self.btn5var.get() == 'X' and self.btn8var.get() == 'X' or
			self.btn3var.get() == 'X' and self.btn6var.get() == 'X' and self.btn9var.get() == 'X' or
			self.btn1var.get() == 'X' and self.btn5var.get() == 'X' and self.btn9var.get() == 'X' or
			self.btn3var.get() == 'X' and self.btn5var.get() == 'X' and self.btn7var.get() == 'X' or
			self.btn1var.get() == 'X' and self.btn2var.get() == 'X' and self.btn3var.get() == 'X'):
			tkinter.messagebox.showinfo("Tic Tac Toe", "Player X Won!")
			self.count = 0
			self.xScore+=1
			self.clear()
			self.play()

		elif (self.btn1var.get() == 'O' and self.btn2var.get() == 'O' and self.btn3var.get() == 'O' or
			self.btn4var.get() == 'O' and self.btn5var.get() == 'O' and self.btn6var.get() == 'O' or
			self.btn7var.get() == 'O' and self.btn8var.get() == 'O' and self.btn9var.get() == 'O' or
			self.btn1var.get() == 'O' and self.btn4var.get() == 'O' and self.btn7var.get() == 'O' or
			self.btn2var.get() == 'O' and self.btn5var.get() == 'O' and self.btn8var.get() == 'O' or
			self.btn3var.get() == 'O' and self.btn6var.get() == 'O' and self.btn9var.get() == 'O' or
			self.btn1var.get() == 'O' and self.btn5var.get() == 'O' and self.btn9var.get() == 'O' or
			self.btn3var.get() == 'O' and self.btn5var.get() == 'O' and self.btn7var.get() == 'O' or
			self.btn1var.get() == 'O' and self.btn2var.get() == 'O' and self.btn3var.get() == 'O'):
			tkinter.messagebox.showinfo("Tic Tac Toe", "Player O Won!")
			self.count = 0
			self.oScore += 1
			self.clear()
			self.play()

		elif self.count == 9:
			tkinter.messagebox.showinfo("Tic Tac Toe", "Tie Game!")
			self.count = 0
			self.clear()
			self.play()

	def clear(self):
		for i in self.btnVars[1:]:
			i.set('')

if __name__ == "__main__":
	root = tk.Tk()
	xph = tk.PhotoImage(file=r'C:\Users\Stevanovic\Desktop\tkinter\svi ostali fajlovi za projekte\x.png')
	oph = tk.PhotoImage(file=r'C:\Users\Stevanovic\Desktop\tkinter\svi ostali fajlovi za projekte\o.png')
	app = App(root, "Tic Tac Toe")
	root.mainloop()
