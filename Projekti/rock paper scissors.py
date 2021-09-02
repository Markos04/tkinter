import tkinter as tk
import random
#from PIL import ImageTk, Image

class Btns:

	def __init__(self, master, row, column, text, command):
		self.btn = tk.Button(master, text=text, command = command)
		self.btn.grid(row=row,column=column)

	def config(self, image):
		self.btn.configure(image=image)
class App(tk.Frame):
	click = True
	chList = ['rock','paper','scissors']
	def __init__(self, master, title=None, icon=None, geometry=None):
		tk.Frame.__init__(self, master)
		# Window
		self.master = master
		self.master.title(title)
		self.master.geometry(geometry)
		self.master.iconphoto(False, icon)

		self.frame = tk.Frame(self.master, bd=30, bg='lightgreen')
		self.frame.grid(row=0,column=0)

		self.one = ''
		self.two = ''
		self.three = ''

		self.play()


	# Functions
	def play(self):
		global rock, paper, scissors
		self.one = Btns(self.frame, 0, 0, "Rock", lambda :self.yourPick('rock'))
		self.two = Btns(self.frame, 0, 1, "Paper", lambda :self.yourPick('paper'))
		self.three = Btns(self.frame, 0, 2, "Scissors", lambda :self.yourPick('scissors'))

	def computerPick(self):
		self.choice = random.choice(self.chList)
		return self.choice

	def yourPick(self, yourChoice):
		global click

		self.compPick = self.computerPick()

		if self.click == True:

			if yourChoice == 'rock':
				Btns.config(self.one, rockph)
				if self.compPick == 'rock':
					Btns.config(self.two, rockph)
					Btns.config(self.three, tieph)
					self.click = False
				elif self.compPick == 'paper':
					Btns.config(self.two, paperph)
					Btns.config(self.three, loseph)
					self.click = False
				else:
					Btns.config(self.two, scissorsph)
					Btns.config(self.three, winph)
					self.click = False

			elif yourChoice == 'paper':
				Btns.config(self.two, paperph)
				if self.compPick == 'paper':
					Btns.config(self.one, paperph)
					Btns.config(self.three, tieph)
					self.click = False
				elif self.compPick == 'rock':
					Btns.config(self.one, scissorsph)
					Btns.config(self.three, loseph)
					self.click = False
				else:
					Btns.config(self.one, rockph)
					Btns.config(self.three, winph)
					self.click = False

			elif yourChoice == 'scissors':
				Btns.config(self.three, scissorsph)
				if self.compPick == 'scissors':
					Btns.config(self.two, scissorsph)
					Btns.config(self.one, tieph)
					self.click = False
				elif self.compPick == 'rock':
					Btns.config(self.two, rockph)
					Btns.config(self.one, loseph)
					self.click = False
				else:
					Btns.config(self.two, paperph)
					Btns.config(self.one, winph)
					self.click = False
		else:
			if yourChoice == 'rock' or yourChoice == 'paper' or yourChoice == 'scissors':
				Btns.config(self.one, rockph)
				Btns.config(self.two, paperph)
				Btns.config(self.three, scissorsph)
				self.click = True

if __name__ == "__main__":
	root = tk.Tk()
	
	rockph = tk.PhotoImage(file=r'C:\Users\Stevanovic\Desktop\tkinter\Svi ostali fajlovi za projekte\rock.png')
	paperph = tk.PhotoImage(file=r'C:\Users\Stevanovic\Desktop\tkinter\Svi ostali fajlovi za projekte\paper.png')
	scissorsph = tk.PhotoImage(file=r'C:\Users\Stevanovic\Desktop\tkinter\Svi ostali fajlovi za projekte\scissors.png')
	winph = tk.PhotoImage(file=r'C:\Users\Stevanovic\Desktop\tkinter\Svi ostali fajlovi za projekte\win.png')
	loseph = tk.PhotoImage(file=r'C:\Users\Stevanovic\Desktop\tkinter\svi ostali fajlovi za projekte\lose.png')
	tieph = tk.PhotoImage(file=r'C:\Users\Stevanovic\Desktop\tkinter\Svi ostali fajlovi za projekte\tie.png')
	icons = tk.PhotoImage(file=r'C:\Users\Stevanovic\Desktop\tkinter\Svi ostali fajlovi za projekte\rock-paper-scissors.png')
	app = App(root, "Rock, Paper, Scissors", icons)
	root.mainloop()
