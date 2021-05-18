from tkinter import *
from PIL import ImageTk, Image

count = 0
imageList = []

def addImage(img):
    imageList.append(img)
def chooseImage():
    count += 1

addImage("C:\\Users\\dyale\\OneDrive\\Documents\\Summer Projects\\Project1\\image1.png")
addImage("C:\\Users\\dyale\\OneDrive\\Documents\\Summer Projects\\Project1\\image2.png")
addImage("C:\\Users\\dyale\\OneDrive\\Documents\\Summer Projects\\Project1\\image3.png")
addImage("C:\\Users\\dyale\\OneDrive\\Documents\\Summer Projects\\Project1\\image4.png")
addImage("C:\\Users\\dyale\\OneDrive\\Documents\\Summer Projects\\Project1\\image5.png")

master = Tk()
master.geometry("600x375")

back = Button(master, text="Back", height = 20 , width=20)
next = Button(master, text="Next", height = 20 , width=20,command = chooseImage)
back.grid(column=0, row=1)
next.grid(column=2, row=1)

label = Label(master, text="Python Slideshow")
label.grid(column=1, row=0)

img = PhotoImage(file=imageList[count])

slideshow = Label(master, image=img,)
slideshow.grid(column=1,row = 1)
mainloop()
