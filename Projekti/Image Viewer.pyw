from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Image Viewer')
root.resizable(0,0)

myImg1 = ImageTk.PhotoImage(Image.open(r'C:\Users\Stevanovic\Desktop\Boards\board 1.gif'))
myImg2 = ImageTk.PhotoImage(Image.open(r'C:\Users\Stevanovic\Desktop\Boards\board 2.gif'))
myImg3 = ImageTk.PhotoImage(Image.open(r'C:\Users\Stevanovic\Desktop\Boards\board 3.gif'))
myImg4 = ImageTk.PhotoImage(Image.open(r'C:\Users\Stevanovic\Desktop\Boards\board 4.gif'))
myImg5 = ImageTk.PhotoImage(Image.open(r'C:\Users\Stevanovic\Desktop\Boards\board 5.gif'))
myImg6 = ImageTk.PhotoImage(Image.open(r'C:\Users\Stevanovic\Desktop\Boards\board 6.gif'))
myImg7 = ImageTk.PhotoImage(Image.open(r'C:\Users\Stevanovic\Desktop\Boards\board 7.gif'))
myImg8 = ImageTk.PhotoImage(Image.open(r'C:\Users\Stevanovic\Desktop\Boards\board 8.gif'))


imageList = [myImg1, myImg2, myImg3, myImg4, myImg5, myImg6, myImg7, myImg8]

status = Label(root, text='Image 1 of {}'.format(len(imageList)), bd=1, relief=SUNKEN, anchor=E, bg='#e7e4e4')

myLabel = Label(image=myImg1)
myLabel.grid(row=0, column=0, columnspan=3)

def forward(imageNumber):
	global myLabel
	global btnForward
	global btnBack

	myLabel.grid_forget()
	myLabel = Label(image=imageList[imageNumber-1])
	btnForward = Button(root, text='>>', command=lambda: forward(imageNumber+1))
	btnBack = Button(root, text='<<', command=lambda: forward(imageNumber-1))
	
	if imageNumber == len(imageList):
		btnForward = Button(root, text='>>', state=DISABLED)
	if imageNumber == 1:
		btnBack = Button(root, text='<<', state=DISABLED)
	
	myLabel.grid(row=0, column=0, columnspan=3)
	btnBack.grid(row=1, column=0)
	btnForward.grid(row=1, column=2)

	# Update Status Bar
	status = Label(root, text='Image {} of {}'.format(imageNumber, len(imageList)), bd=1, relief=SUNKEN, anchor=E, bg='#e7e4e4')
	status.grid(row=3, column=0, columnspan=3, sticky=W+E)


def back(imageNumber):
	global myLabel
	global btnForward
	global btnBack

	myLabel.grid_forget()
	myLabel = Label(image= imageList[imageNumber-1])
	btnForward = Button(root, text='>>', command=lambda: forward(imageNumber+1))
	btnBack = Button(root, text='<<', command=lambda: forward(imageNumber-1))

	myLabel.grid(row=0, column=0, columnspan=3)
	btnBack.grid(row=1, column=0)
	btnForward.grid(row=1, column=2)


btnBack = Button(root, text='<<', command = back, state=DISABLED)
btnExit = Button(root, text='Exit Program', command = root.destroy)
btnForward = Button(root, text='>>', command = lambda: forward(2))

btnBack.grid(row=1, column=0)
btnExit.grid(row=1, column=1)
btnForward.grid(row=1, column=2, pady = 10)
status.grid(row=3, column=0, columnspan=3, sticky=W+E)


root.mainloop()
