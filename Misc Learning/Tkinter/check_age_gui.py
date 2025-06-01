import tkinter as tk

root = tk.Tk()
root.geometry('300x200')
message = tk.Label(root, text= 'Enter your age: ')
message.pack()

entry = tk.Entry(root)
entry.pack()

def show_age():
    user_age = entry.get()
    print(f'you are {user_age} Years old.')
    
button = tk.Button(root, text= 'check age', command= show_age)
button.pack()

root.mainloop()