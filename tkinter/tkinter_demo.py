import tkinter as tk
MyWindow = tk.Tk()
lbl = tk.Label(MyWindow, text = 'My Label')
lbl.pack()

txtname = tk.Entry(MyWindow)
txtname.pack()

btn = tk.Button(MyWindow, text = 'Submit')
btn.pack()

MyWindow.mainloop()


root = tk.Tk()
root.title = ('my first tkinter app')
root.geometry = ('300x200')
label = tk.Label(root, text = 'hello tkinter!')
label.pack(pady = 20)

button = tk.Button(root,text = 'click me',command = lambda: print('button clicked'))
button.pack()

root.mainloop()
