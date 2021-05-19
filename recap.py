import tkinter as tk
from PIL import ImageTk, Image
import itertools

imageList = ["C:\\Users\\dyale\\OneDrive\\Documents\\Summer Projects\\Project1\\image1.png",
 "C:\\Users\\dyale\\OneDrive\\Documents\\Summer Projects\\Project1\\image2.png", 
 "C:\\Users\\dyale\\OneDrive\\Documents\\Summer Projects\\Project1\\image3.png",
 "C:\\Users\\dyale\\OneDrive\\Documents\\Summer Projects\\Project1\\image4.png",
 "C:\\Users\\dyale\\OneDrive\\Documents\\Summer Projects\\Project1\\image5.png"]

 #Changes list into an iterator
imageList = itertools.cycle(imageList)

#Creates window
master = tk.Tk()
master.geometry("600x375")

panel = tk.Label(master)



def addImage(img):
    imageList.append(img)

def changeImageF():
    try:
        img = next(imageList)
    except(StopIteration):
        return
    
    img = Image.open(img)
    img = ImageTk.PhotoImage(img)
    panel.img = img
    panel['image'] = img


back = tk.Button(master, text="Back", height = 20 , width=20)
past = tk.Button(master, text="Next", height = 20 , width=20, command = changeImageF)
back.grid(column=0, row=1)
past.grid(column=2, row=1)

label = tk.Label(master, text="Python Slideshow")
label.grid(column=1, row=0)

panel.grid(column=1,row = 1)

changeImageF()

master.mainloop()