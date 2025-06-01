from tkinter import *
from PIL import ImageTk, Image
 
# Create the main window
ws = Tk()
ws.title('Canvas Example with Tkinter')
ws.geometry('500x500')
 
# Create a Canvas widget
canvas = Canvas(ws, width=500, height=500)
canvas.pack()
 
# Load and display the image using Pillow
img = ImageTk.PhotoImage(Image.open('images/shelby.jpeg'))
canvas.create_image(10, 10, anchor=NW, image=img)
 
# Run the application
ws.mainloop()
