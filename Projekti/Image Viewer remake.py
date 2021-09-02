import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
import os

r'''

os.chdir(r'C:\Users\Stevanovic\Desktop\Boards')

imageList = []
	for f in os.listdir():
		fName, fExt = os.path.splitext(f)
		if fExt == '.gif':
			imageList.append(tk.PhotoImage(file=f))
'''

class Buttons:
	def __init__(self, master, image, command, row, column, border=0, bg='white', padx=None, pady=None):
		self.btn = tk.Button(master, image=image, command=command, border=border, bg=bg)
		self.btn.grid(row=row, column=column)

class App(tk.Frame):
	def __init__(self, master, title=None, icon=None, geometry=None, bg='white'):
		tk.Frame.__init__(self, master)
		
		self.master = master
		self.master.title(title)
		self.master.geometry(geometry)
		self.master.state("zoomed")
		self.master.config(bg=bg)
		self.master.iconphoto(False, icon)

		# Menu Dodati edit
		self.menubar = tk.Menu(self.master)
		self.master.config(menu=self.menubar)
		self.submenu = tk.Menu(self.menubar, tearoff=0)
		self.menubar.add_cascade(label='File', menu=self.submenu)
		self.submenu.add_command(label="Add Photo", command=self.browse_file)
		self.submenu.add_command(label="File edit")
		
		# Frames
		topframe = tk.Frame(master, bg=bg)
		topframe.pack()
		bottomframe = tk.Frame(master, bg='blue')
		bottomframe.pack()
	
		# Bottom Frame
		self.deleteBtn = Buttons(bottomframe, deletePhoto, self.dltPhoto, 0, 0)
		self.rotateBtn = Buttons(bottomframe, rotatePhoto, self.rttPhoto, 0, 1)

		# Top Frame
		self.preBtn = Buttons(topframe, prePhoto, self.showPrePhoto, 0, 0)
		self.imgLabel = tk.Label(topframe, image=pixel, width=1600, height=900, bg=bg)
		self.imgLabel.grid(row=0, column=1, pady=20, padx = 40)
		self.nextBtn = Buttons(topframe, nextPhoto, self.showNextPhoto, 0, 2)

		mFile = open(r'C:\Users\Stevanovic\Desktop\tkinter\Svi ostali fajlovi za projekte\myImgList.txt', 'r')
		myPathList = mFile.read().splitlines()
		mFile.close()
		for item in myPathList:
			if item != "":
				imgList.append(item)

		self.resizeImg(index)

		self.master.bind('<Left>', self.keyBind)
		self.master.bind('<Right>', self.keyBind)
		
	def browse_file(self):
		global imgList, index
		filename_path = filedialog.askopenfilename()
		imgList.append(filename_path)

		mFile = open(r'C:\Users\Stevanovic\Desktop\tkinter\Svi ostali fajlovi za projekte\myImgList.txt', 'w+')

		for i in range(0, len(imgList)):
			mFile.write(imgList[i] + '\n')
		mFile.close()
		self.showNextPhoto()

	def resizeImg(self,index):
		global imgList
		try:
			path = imgList[index]
			original = Image.open(path)
			original.thumbnail(maxsize, Image.ANTIALIAS)
			resized = ImageTk.PhotoImage(original)
			self.imgLabel.configure(image=resized)
			self.imgLabel.ImageTK = resized
		except IndexError:
			pass
		except Exception:
			pass

	def showPrePhoto(self):
		global index
		try:
			index -= 1
			if index < 0:
				index = len(imgList)-1
			self.resizeImg(index)
		except:
			pass

	def showNextPhoto(self):
		global index
		try:
			index += 1
			if index > len(imgList)-1:
				index=0
			self.resizeImg(index)
		except:
			pass

	def dltPhoto(self):
		global imgList, index
		try:
			imgList.pop(index)
			index-=1
			mFile = open(r'C:\Users\Stevanovic\Desktop\tkinter\Svi ostali fajlovi za projekte\myImgList.txt', 'w')
			for i in range(0, len(imgList)):
				mFile.write(imgList[i] + '\n')
			mFile.close()
			self.showNextPhoto()
		except IndexError:
			index-=1
			mFile = open(r'C:\Users\Stevanovic\Desktop\tkinter\Svi ostali fajlovi za projekte\myImgList.txt', 'w')
			for i in range(0, len(imgList)):
				mFile.write(imgList[i] + '\n')
			mFile.close()

	def rttPhoto(self):
		global imgList, degree
		try:
			degree += 90

			path = imgList[index]
			original = Image.open(path)
			original.thumbnail(maxsize, Image.ANTIALIAS)
			original = original.rotate(degree)
			resized = ImageTk.PhotoImage(original)

			self.imgLabel.configure(image=resized)
			self.imgLabel.ImageTK = resized

			if degree == 360:
				degree = 0
		except:
			pass

	def keyBind(self, event):
		if event.keysym == 'Left':
			self.showPrePhoto()
		elif event.keysym == 'Right':
			self.showNextPhoto()


if __name__ == "__main__":
	root = tk.Tk()
	pixel = tk.PhotoImage(width=1, height=1)
	maxsize = (1600, 900)
	degree = 0
	iconf = tk.PhotoImage(file=r'C:\Users\Stevanovic\Desktop\slike za programe\camera.png')
	prePhoto = tk.PhotoImage(file=r'C:\Users\Stevanovic\Desktop\slike za programe\previous.png')
	nextPhoto = tk.PhotoImage(file=r'C:\Users\Stevanovic\Desktop\slike za programe\next.png')
	deletePhoto = tk.PhotoImage(file=r'C:\Users\Stevanovic\Desktop\slike za programe\trash.png')
	rotatePhoto = tk.PhotoImage(file=r'C:\Users\Stevanovic\Desktop\slike za programe\refresh.png')
	imgList = []
	index = 0
	app = App(root, "Image Viewer", iconf)
	root.mainloop()
