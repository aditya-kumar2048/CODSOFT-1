import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, "✅ " + task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

def delete_task():
    try:
        selected = listbox.curselection()
        listbox.delete(selected)
    except:
        messagebox.showwarning("Warning", "Please select a task to delete.")

root = tk.Tk()
root.title("✅ To-Do List")
root.geometry("320x400")
root.configure(bg="#121212")

entry = tk.Entry(root, font="Arial 14", bg="#1E1E1E", fg="white", insertbackground="white")
entry.pack(pady=10, padx=10, fill='x')

add_btn = tk.Button(root, text="Add Task", command=add_task, bg="#2C2C2C", fg="white")
add_btn.pack(pady=2)

delete_btn = tk.Button(root, text="Delete Task", command=delete_task, bg="#2C2C2C", fg="white")
delete_btn.pack(pady=2)

listbox = tk.Listbox(root, font="Arial 14", bg="#1E1E1E", fg="white", selectbackground="gray")
listbox.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Keyboard support
root.bind("<Return>", lambda e: add_task())
root.bind("<Delete>", lambda e: delete_task())

root.mainloop()
