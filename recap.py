from tkinter import Button, Label, Tk, mainloop

imageList = []

def addImage(img):
    imageList.append(img)

addImage("image1.png")
addImage("image2.jpg")
addImage("image3.jpg")
addImage("image4.jpg")
addImage("image5.jpg")

master = Tk()
master.geometry("800x600")


back = Button(master, text="Back", height = 20 , width=20).pack(side="left")
next = Button(master, text="Next", height = 20 , width=20).pack(side="right")


label = Label(master, text="Python Slideshow").pack()

mainloop()

fart = 1