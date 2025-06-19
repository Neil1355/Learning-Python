#import statement - step - 1
import tkinter as tk
from tkinter import messagebox

#the white screen on which other content would come
window = tk.Tk()

# A title is the main heading on the frame/window
window.title("My first app")

# we could also set the length and width of a window using geometry.
window.geometry('300x200')

#A Label is used to display text on the window. You usually use it 
# to describe what to enter in a field, give titles, or show information.
label = tk.Label(window, text = "enter your name") #window is the  name of the frame here.

#we would also have to pack it. 
# pack() Tells Tkinter to put it on the window. Without it, it won’t show.
label.pack()

# To add textbox, we use Entry().
# we could store the value entered in the text box using stringvar.
name_var = tk.StringVar()
pass_var = tk.StringVar()
check_var = tk.IntVar()
#now, lets add the entry textbox.
# *we would add .pack() in the end so we dont have to do it again like above
entry = tk.Entry(window, textvariable = name_var).pack() #textvariable is a keyword here. not reserved but important.

#we could swap text in passwords with '*' too like this.
password = tk.Label(window, text = 'enter your password').pack()
pass_entry = tk.Entry(window, textvariable=pass_var, show= '*').pack()

#Let's add a checkbox now!
checkbox = tk.Checkbutton(window, text = 'remember me', variable = check_var).pack()
#function for command used in button below, followed with messagebox.
# a messagebox shows 3 kinds of pop-ups, 
#✅ Success: “Registration Complete!”

#⚠️ Warning: “Please fill all fields!”

#❌ Error: “Passwords do not match!”
#the 3 kinds are:
#messagebox.showinfo("Title", "Your message here")
#messagebox.showwarning("Title", "This is a warning")
#messagebox.showerror("Title", "Something went wrong!")
def show_name():
    name = name_var.get()
    print('Hello, ',name)
    if name:
        messagebox.showinfo("Welcome", f"Hello, {name}!")
    else:
        messagebox.showwarning("Missing Input", "Please enter your name.")
    
#Buttons could be added in the (window,text, command) format,
# where command does stuff like open another window, launch a popup, etc.
button = tk.Button(window, text = 'Enter', command = show_name).pack()

#adding an exit button using grid (to close the app)
# grid(row, column) tells tkinter where to place it on a virtual table
#can't use grid coz we could use either grid, or pack. no together in one window.
#exit_button = tk.Button(window, text = 'Exit', command = window.destroy)
#exit_button.grid(row=2, column=0, pady=10)
exit_button = tk.Button(window, text = 'Exit', command = window.destroy).pack()

#in the end, we gotta call the window with mainloop() to keep it running.
window.mainloop()