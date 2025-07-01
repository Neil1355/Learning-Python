import tkinter
root = tkinter.Tk()

frame = tkinter.Frame(root, height = 200, width=200,bg='navy')
frame.place(x=50,y=50)

tkinter.Label(frame, text = 'relx=0 , rely = 0').place(relx=0 , rely = 0)
tkinter.Label(frame, text = 'relx=0.4 , rely = 0.6').place(relx=0.4 , rely = 0.6)
tkinter.Label(frame, text = 'relx=1 , rely = 1').place(relx=1 , rely = 1)

root.mainloop()

import tkinter as tk

window = tk.Tk()

frame = tk.Frame(master=window, width=150, height=150)
frame.pack()

label1 = tk.Label(master=frame, text="I'm at (0, 0)", bg="red")
label1.place(x=0, y=0)

label2 = tk.Label(master=frame, text="I'm at (75, 75)", bg="yellow")
label2.place(x=75, y=75)

window.mainloop()