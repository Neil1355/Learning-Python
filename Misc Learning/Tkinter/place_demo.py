import tkinter as tk

root = tk.Tk()

tk.Label(root, text="Name:").place(x=10, y=20)
tk.Entry(root).place(x=80, y=20)

root.mainloop()
