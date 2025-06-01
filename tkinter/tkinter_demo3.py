from tkinter import *
from PIL import Image, ImageTk
ws = Tk()
ws.title('Image example with tkinter')
# Load the image using PIL
image = Image.open('images\shelby.jpeg')
img = ImageTk.PhotoImage(image)
Label(ws, image=img).pack()
# avoid garbage collection
Label.image = img
ws.mainloop()