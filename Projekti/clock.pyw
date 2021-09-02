#!/usr/bin/python3

# Imports
import tkinter as tk
import time
import datetime
from tkinter import ttk
from playsound import playsound

	#print("couldn't play sound")
# Buttons Class
class Buttons:
	def __init__(self, master, row, column, text, command = None,image=None):
		self.btn = tk.Button(master, text=text, command = command, padx = 5, pady=5,bg='#99a4ad', fg='white',font=('Calibri'))
		self.btn.grid(row=row, column = column, pady = 5, padx = 20)
		self.name = self
	def forget(self):
		self.btn.grid_forget()
# Comboboxes Class
class Comboboxes:
	def __init__(self, master, row, column, value, textvariable):
		self.cmbbox = ttk.Combobox(master, value=value, width=5, textvariable=textvariable, justify='center')
		self.cmbbox.current(0)
		self.cmbbox.grid(row=row, column=column, pady=5)

# Labels Class
class Labels:
	def __init__(self, master, row, column, text, bg, fg, font=("Comic Sans MS", 12), columnspan=None):
		self.lab = tk.Label(master, text=text, bg=bg, fg=fg, pady=5, padx=2, justify = 'left', font=font)
		self.lab.grid(row=row, column=column, columnspan=columnspan)
#---------------------------------------------------------------------------------------------------------
# Main Class
class App(tk.Frame):
	secondsLeft = 0
	timerOn = False
	count = 0
	hours = list(range(0,25))
	minutes = list(range(0, 60))
	seconds = list(range(0, 60))

	def __init__(self, master, title=None, geometry=None):
		tk.Frame.__init__(self, master)
		# Window
		self.master = master
		self.master.title(title)
		self.master.config(bg='#2d3a4c')
		#self.master.protocol("WM_DELETE_WINDOW", self.__callback)
		self.btnFrame = tk.Frame(self.master, bg='#2d3a4c')
		self.btnFrame.grid(row = 4, column=0, columnspan = 4)

		# Int Variables
		self.hourNum = tk.IntVar()
		self.minNum = tk.IntVar()
		self.secNum = tk.IntVar()

		# Comboboxes
		self.sethour = Comboboxes(self.master, 1, 1, self.hours, self.hourNum)
		self.setmin = Comboboxes(self.master, 1, 2, self.minutes, self.minNum)
		self.setsec = Comboboxes(self.master, 1, 3, self.seconds, self.secNum)

		# Labels
		self.Work = Labels(self.master, 1, 0, 'Work: ', '#2d3a4c', 'white')
		self.Pause = Labels(self.master, 2, 0, 'Pause: ', '#2d3a4c','white')
		#self.lab = tk.Label(self.master, 3, 0, '0:00:00', '#2d3a4c', fg='white', ("Helvetica", 48), 4) # Zasto ne moze iz klase Labels ('Labels' object does not support item assignment)
		self.lab = tk.Label(self.master, text='0:00:00', bg='#2d3a4c', fg='white', font=("Comic Sans MS", 48)) 
		self.lab.grid(row=3, column=0, columnspan=4)
		self.Hour = Labels(self.master, 0, 1, 'Hour: ', '#2d3a4c', 'white')
		self.Minute = Labels(self.master, 0, 2, 'Minute: ', '#2d3a4c','white')
		self.Second = Labels(self.master, 0, 3, 'Second: ', '#2d3a4c', 'white')

		# Buttons
		self.start = Buttons(self.btnFrame, 4, 0, 'Start', self.startclock)
		self.stop = Buttons(self.btnFrame, 4, 1, 'Stop', self.stopclock)
		self.restart = Buttons(self.btnFrame, 4, 2, 'Reset')

	# Functions
	@staticmethod
	def __callback():
		return 
	def setclock(self):
		self.lab["text"] = self.convertSec()
		if self.secondsLeft:
			self.secondsLeft -= 1
			self.timerOn = self.after(1000, self.setclock)
		else:
			self.timerOn = False
			self.popUp()

	def startclock(self):
		self.secondsLeft = int(self.secNum.get()) + int(self.minNum.get()*60) + int(self.hourNum.get()*3600)
		self.setclock()

	def stopclock(self):
		if self.timerOn:
			self.after_cancel(self.timerOn)
			self.timerOn = False
			self.count += 1
			if self.count % 2 == 1:
				self.stop.forget()
				self.stop = Buttons(self.btnFrame, 4, 1, 'Continue', self.continueClock)
			if self.count % 2 == 0:
				self.stop.forget()
				self.stop = Buttons(self.btnFrame, 4, 1, 'Stop', self.stopclock)

	def continueClock(self):
		if self.secondsLeft:
			self.secondsLeft -= 1
			self.timerOn = self.lab.after(1000, self.setclock)
		self.count += 1
		if self.count % 2 == 0:
			self.stop.forget()
			self.stop = Buttons(self.btnFrame, 4, 1, 'Stop', self.stopclock)
	
	def convertSec(self):
		return datetime.timedelta(seconds=self.secondsLeft)

	def popUp(self):
		win1 = popUps(root)
		#try:
		playsound(r"C:\Users\Stevanovic\Desktop\tkinter\Svi ostali fajlovi za projekte\ph-intro.mp3")
		#except:
		#print("couldn't play sound")
#--------------------------------------------------------------------------------------------------------------------------
# Popups Class
class popUps:
	secondsLeft = 300
	timerOn = False
	count = 0
	def __init__(self, master):
		#App.__init__(self, master)
		# Top Level
		self.popWin = tk.Toplevel(master)
		self.popWin.config(bg='lightgreen')
		self.popWin.resizable(False, False)
		self.popWin.title("ZZzzzzzzzz...")
		self.popWin.lift()
		self.popWin.state('zoomed')
		self.popWin.protocol("WM_DELETE_WINDOW", self.__callback)

		'''
		self.hourNum1 = tk.IntVar()
		self.minNum1 = tk.IntVar()
		self.secNum1 = tk.IntVar()
		self.sethour1 = Comboboxes(self.master, 2, 1, self.hours, self.hourNum1)
		self.setmin1 = Comboboxes(self.master, 2, 2, self.minutes, self.minNum1)
		self.setsec1 = Comboboxes(self.master, 2, 3, self.seconds, self.secNum1)'''
		# Label
		self.lab = tk.Label(self.popWin, bd=30, bg='lightgreen', text="0:00:00", font=("Helvetica", 100), fg='white')
		self.lab.pack(anchor=tk.CENTER, pady = 400)
		self.setclock()

	# Functions

	@staticmethod
	def __callback():
		return 
	def setclock(self):
		try:
			self.lab["text"] = self.convertSec() # Zaaasto bacaa error
		except:
			pass
		if self.secondsLeft:
			self.secondsLeft -= 1
			self.timerOn = self.lab.after(1000, self.setclock)
		else:
			playsound(r"C:\Users\Stevanovic\Desktop\tkinter\Svi ostali fajlovi za projekte\ph-intro.mp3")
			self.popWin.destroy()
			#print("couldn't play sound")
			
			self.timerOn = False
	def convertSec(self):
		return datetime.timedelta(seconds=self.secondsLeft)

	def stopclock(self):
		if self.timerOn:
			self.after_cancel(self.timerOn)
			self.timerOn = False


	r'''
	def startclock(self):
		self.secondsLeft1 = int(self.secNum1.get()) + int(self.minNum1.get()*60) + int(self.hourNum1.get()*3600)
		self.setclock()	# root, treba vrv self.master, samo da ga napravim...
		#playsound(r"C:\Users\Stevanovic\Desktop\tkinter\ph-intro\Svi ostali fajlovi za projekte\ph-intro.mp3")
	'''

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root, "Pomodoro", "400x200")
    root.mainloop()

		#self.lab2 = tk.Label(self.master, text="", font=("Helvetica", 14), fg='green')
		#self.lab2.grid(row=0, column=0)
'''
		self.sethour = ttk.Combobox(self.master, value=hours, width=5, textvariable=self.hourNum)
		self.sethour.current(0)
		self.sethour.grid(row=0, column=0,pady=5)
		self.setmin = ttk.Combobox(self.master, value=minutes, width=5, textvariable=self.minNum)
		self.setmin.current(0)
		self.setmin.grid(row=0, column=1)
		self.setsec = ttk.Combobox(self.master, value=seconds, width=5, textvariable=self.secNum)
		self.setsec.current(0)
		self.setsec.grid(row=0, column=2)'''
'''self.current = f"{self.hourNum.get()}:{self.minNum.get()}:{self.secNum.get()}"
		self.lab.after(200, self.setclock)'''

