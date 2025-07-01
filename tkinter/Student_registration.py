import tkinter as tk

root = tk.Tk()
root.title("Student Registration")

tk.Label(root, text="Name:").pack()
tk.Entry(root).pack()

tk.Label(root, text="Student ID:").pack()
tk.Entry(root).pack()

tk.Label(root, text="Class:").pack()
tk.Entry(root).pack()

root.mainloop()