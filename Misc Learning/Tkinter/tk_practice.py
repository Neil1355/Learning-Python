import tkinter as tk

root = tk.Tk()
root.title('My Info')

message = tk.Label(root,text = 'Hello, My name is Neil')
message.pack()

button = tk.Button(root, text = 'click me', command= lambda: print('Nice to meet you!'))
button.pack()

root.mainloop()