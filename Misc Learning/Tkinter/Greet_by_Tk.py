import tkinter as tk

root = tk.Tk()
root.geometry('300x200')
message = tk.Label(root, text= ' Enter your name: ')
message.pack()

entry = tk.Entry(root)
entry.pack()

def show_input():
    user_name = entry.get()
    print('Hello,',user_name)
    
button = tk.Button(root, text= 'Greet me!', command=show_input)
button.pack()

root.mainloop()