import tkinter as tk
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",       
    password="",        
    database="test"    
)
cursor = conn.cursor()

def show_message(text):
    status_label.config(text=text)

def create_user():
    name = name_entry.get()
    email = email_entry.get()
    if name and email:
        cursor.execute("INSERT INTO student (name, email) VALUES (%s, %s)", (name, email))
        conn.commit()
        show_message("User created!")
        read_users()
        clear_entries()
    else:
        show_message("Please fill all fields.")

def read_users():
    user_list.delete(0, tk.END)  
    cursor.execute("SELECT id, name, email FROM student")
    global user_data
    user_data = cursor.fetchall()
    for uid, name, email in user_data:
        user_list.insert(tk.END, f"ID: {uid} | {name} | {email}")


def delete_user():
    index = user_list.curselection()
    if index:
        user_id = user_data[index[0]][0]  
        cursor.execute("DELETE FROM student WHERE id = %s", (user_id,))
        conn.commit()
        show_message("User deleted.")
        read_users()
        clear_entries()

def update_user():
    index = user_list.curselection()
    if index:
        user_id = user_data[index[0]][0]
        name = name_entry.get()
        email = email_entry.get()
        if name and email:
            cursor.execute("UPDATE student SET name = %s, email = %s WHERE id = %s", (name, email, user_id))
            conn.commit()
            show_message("User updated.")
            read_users()
            clear_entries()
        else:
            show_message("Fill all fields before updating.", "red")

def on_select(event):
    index = user_list.curselection()
    if index:
        id_entry.delete(0, tk.END)
        name_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        uid, name, email = user_data[index[0]]
        id_entry.insert(0, str(uid))
        name_entry.insert(0, name)
        email_entry.insert(0, email)

def clear_entries():
    id_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Student CRUD App")
root.geometry("450x350")


tk.Label(root, text="ID").grid(row=0, column=0, padx=5, pady=5)
tk.Label(root, text="Name").grid(row=1, column=0, padx=5)
tk.Label(root, text="Email").grid(row=2, column=0, padx=5)

id_entry = tk.Entry(root, width=30)
id_entry.grid(row=0, column=1, padx=10, pady=5)

name_entry = tk.Entry(root, width=30)
name_entry.grid(row=1, column=1, padx=10, pady=5)

email_entry = tk.Entry(root, width=30)
email_entry.grid(row=2, column=1, padx=10)

tk.Button(root, text="Create", width=10, command=create_user).grid(row=0, column=2)
tk.Button(root, text="Update", width=10, command=update_user).grid(row=1, column=2)
tk.Button(root, text="Delete", width=10, command=delete_user).grid(row=2, column=2)

user_list = tk.Listbox(root, width=55)
user_list.grid(row=4, column=0, columnspan=3, padx=10, pady=10)
user_list.bind("<<ListboxSelect>>", on_select)

status_label = tk.Label(root, text="", fg="green")
status_label.grid(row=5, column=0, columnspan=3)

read_users()

root.mainloop()

cursor.close()
conn.close()
