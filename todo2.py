import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def remove_task():
    selected_index = listbox.curselection()
    if selected_index:
        listbox.delete(selected_index)
    else:
        messagebox.showwarning("Warning", "Please select a task to remove.")

def clear_tasks():
    listbox.delete(0, tk.END)

root = tk.Tk()
root.title("Bhumika's to do list")

entry = tk.Entry(root, width=30)
entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()

remove_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_button.pack()

clear_button = tk.Button(root, text="Clear All", command=clear_tasks)
clear_button.pack()

listbox = tk.Listbox(root, selectmode=tk.SINGLE)
listbox.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

root.mainloop()
