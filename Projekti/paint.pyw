import tkinter as tk
from tkinter import ttk

class Buttons:
	def __init__(self, master, row, column, color, command):
		self.btn = tk.Button(master, bg=color, image=cmnImg, width=40, height=40, activebackground = color, bd=1, command=command)
		self.btn.grid(row=row, column=column, padx=1, pady=1)

class App:
	current_x = 0
	current_y = 0
	count = 0
	color = 'black'

	def __init__(self, master, fill='black', title=None, geometry=None, state='zoomed'):
		# window
		self.master = master
		self.master.title(title)
		self.master.state(state)
		self.master.geometry(geometry)
		self.master.config(bg='#474747')
		self.master.rowconfigure(0, weight=1)
		self.master.columnconfigure(0, weight=1)
		self.master.columnconfigure(1, weight=50)
		
		colorsFrame = tk.Frame(self.master, bg='#474747', highlightbackground='black', highlightthickness=3)
		colorsFrame.grid(row=0, column=0)

		'''canvFrame = tk.Frame(self.master, highlightbackground='black', highlightthickness=3)
		canvFrame.grid(row=0, column=1, rowspan=2,sticky='nsew')'''

		self.widthVal = tk.IntVar()
		# Menu
		self.menubar = tk.Menu(self.master)
		self.master.config(menu = self.menubar)
		submenu = tk.Menu(self.menubar, tearoff=0)
		self.menubar.add_cascade(label='File', menu=submenu)
		submenu.add_command(label='New Canvas', command = self.newCanvas)

		# Canvas
		self.canv = tk.Canvas(self.master, bg='white', highlightbackground='black', highlightthickness=3)
		self.canv.grid(row=0, column=1, sticky='nsew', rowspan=2)

		self.penSize = ttk.Combobox(self.master, value=list(range(0,10)), textvariable=self.widthVal, width=5)
		self.penSize.current(0)
		self.penSize.grid(row=1, column=0, pady=10)
		self.displayPallete()

		# Colors (Buttons)
		self.black = Buttons(colorsFrame, 0, 0, 'black', lambda : self.showColor('black'))
		self.gray = Buttons(colorsFrame, 0, 1, 'gray', lambda : self.showColor('gray'))
		self.brown = Buttons(colorsFrame, 1, 0, 'brown4', lambda : self.showColor('brown4'))
		self.red = Buttons(colorsFrame, 1, 1, 'red', lambda : self.showColor('red'))
		self.orange = Buttons(colorsFrame, 2, 0, 'orange', lambda : self.showColor('orange'))
		self.green = Buttons(colorsFrame, 2, 1, 'green', lambda : self.showColor('green'))
		self.blue = Buttons(colorsFrame, 3, 0, 'blue', lambda : self.showColor('blue'))
		self.purple = Buttons(colorsFrame, 3, 1, 'purple', lambda : self.showColor('purple'))

		'''self.rectBtn = Buttons(self.master, 2, 0, 'lightgreen', self.increment)
		'''
		
		self.canv.bind("<Button-1>", self.locate_xy)
		self.canv.bind("<B1-Motion>", self.addLine)
		'''else:
			self.canv.bind("<B2-Motion>", self.addRect)
		self.canv.bind('<Key>', self.newCanvas)'''

	def locate_xy(self, event):
		global current_x, current_y
		self.current_x, self.current_y = event.x, event.y

	def addLine(self, event):
		global current_x, current_y
		self.canv.create_line((self.current_x, self.current_y, event.x, event.y), fill=self.color, width=self.widthVal.get())
		self.current_x, self.current_y = event.x, event.y

	'''def addRect(self, event):
		global current_x, current_y
		self.canv.create_rectangle((self.current_x, self.current_y, event.x, event.y), fill =self.color)
		self.current_x, self.current_y = event.x, event.y
		
	def increment(self):
		self.count += 1
		print(self.count)'''

	def showColor(self, new_color):
		global color
		self.color = new_color
	
	def newCanvas(self): # Pogledaj ponovooooo
		self.canv.delete('all')
		
	def displayPallete(self):
		pass
		'''id = self.canv.create_rectangle(10, 10, 30, 30, fill='black')
		self.canv.tag_bind(id, '<Button-1>', lambda x: self.showColor('black'))
		id = self.canv.create_rectangle(10, 40, 30, 60, fill='gray')
		self.canv.tag_bind(id, '<Button-1>', lambda x: self.showColor('gray'))
		id = self.canv.create_rectangle(10, 70, 30, 90, fill='brown4')
		self.canv.tag_bind(id, '<Button-1>', lambda x: self.showColor('brown4'))
		id = self.canv.create_rectangle(10, 100, 30, 120, fill='red')
		self.canv.tag_bind(id, '<Button-1>', lambda x: self.showColor('red'))
		id = self.canv.create_rectangle(10, 130, 30, 150, fill='orange')
		self.canv.tag_bind(id, '<Button-1>', lambda x: self.showColor('orange'))
		id = self.canv.create_rectangle(10, 160, 30, 180, fill='yellow')
		self.canv.tag_bind(id, '<Button-1>', lambda x: self.showColor('yellow'))
		id = self.canv.create_rectangle(10, 190, 30, 210, fill='green')
		self.canv.tag_bind(id, '<Button-1>', lambda x: self.showColor('green'))
		id = self.canv.create_rectangle(10, 220, 30, 240, fill='blue')
		self.canv.tag_bind(id, '<Button-1>', lambda x: self.showColor('blue'))
		id = self.canv.create_rectangle(10, 250, 30, 270, fill='purple')
		self.canv.tag_bind(id, '<Button-1>', lambda x: self.showColor('purple'))'''

'''class Rectangle(App):
	def __init__(self, x1, y1, x2, y2, fill):
		super().__init__(master, title=None, geometry=None, state='zoomed')

		id = self.canv.create_rectangle(x1, y1, x2, y2, fill=fill)
		self.canv.tag_bind(id, '<Button-1>', lambda x: show_color(fill))'''

if __name__ == "__main__":
	root = tk.Tk()
	cmnImg = tk.PhotoImage(width=1, height=1)
	app = App(root, "Paint")
	root.mainloop()