import tkinter as tk

# Create main window
root = tk.Tk()
root.title("To-Do List")

# List to store tasks and checkbox states
tasks = []

def add_task():
    task_text = entry.get()
    if task_text:
        var = tk.BooleanVar()
        cb = tk.Checkbutton(frame, text=task_text, variable=var)
        cb.pack(anchor="w")
        tasks.append((cb, var))
        entry.delete(0, tk.END)

def delete_completed():
    for cb, var in tasks[:]:
        if var.get():
            cb.destroy()
            tasks.remove((cb, var))

# Input field and Add button
entry = tk.Entry(root, width=30)
entry.pack(pady=5)

add_btn = tk.Button(root, text="Add Task", command=add_task)
add_btn.pack()

# Frame to hold checkboxes
frame = tk.Frame(root)
frame.pack(pady=10)

# Delete button
del_btn = tk.Button(root, text="Delete Completed", command=delete_completed)
del_btn.pack(pady=5)

# Start GUI
root.mainloop()
