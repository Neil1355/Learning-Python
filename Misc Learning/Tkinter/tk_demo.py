import tkinter as tk

root = tk.Tk()  # Create the main window
root.title('My Window')
message = tk.Label(root, text='hello world')
message.pack()

root.geometry('300x200')

#Button
button=tk.Button(root,text = 'click me', command= lambda: print('button clicked!'))
button.pack()
root.mainloop()  # Start the GUI event loop
