import tkinter as tk
from PIL import ImageTk, Image
import itertools
import time


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

stop = False
timer = time.time()


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

def slideshow():
    while True:
        print("test")
        changeImageF()
        time.sleep(1.0 - ((time.time() - timer) % 1.0))
        if stop == True:
            break

def stopPressed():
    stop = True
    return stop

past = tk.Button(master, text="Next", height = 2, width=20, command = changeImageF)
slideshow = tk.Button(master, text="Slideshow", height=2, width = 20, command = slideshow)
stop = tk.Button(master, text="Stop", height = 2, width = 20, command = stopPressed)
past.grid(column=1, row=2)
slideshow.grid(column = 2, row = 2)
stop.grid(column = 3, row = 2)

label = tk.Label(master, text="Python Slideshow")
label.grid(column=2, row=0)

panel.grid(column=2,row = 1)

changeImageF()

master.mainloop()