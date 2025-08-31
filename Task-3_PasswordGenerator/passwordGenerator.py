import tkinter as tk
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError
        all_chars = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(all_chars) for _ in range(length))
        result_var.set(password)
        copy_btn.config(text="Copy", bg="#2C2C2C")  # Reset copy button
    except ValueError:
        result_var.set("Enter valid length")

def copy_to_clipboard():
    password = result_var.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        copy_btn.config(text="Copied ✅", bg="#4caf50")
        root.after(1500, lambda: copy_btn.config(text="Copy", bg="#2C2C2C"))

root = tk.Tk()
root.title("🔐 Password Generator")
root.geometry("400x250")
root.configure(bg="#121212")

# Widgets
tk.Label(root, text="Enter Password Length:", font="Arial 14", bg="#121212", fg="white").pack(pady=10)
length_entry = tk.Entry(root, font="Arial 14", bg="#1E1E1E", fg="white", insertbackground="white")
length_entry.pack(pady=5)

tk.Button(root, text="Generate", command=generate_password, font="Arial 12", bg="#2C2C2C", fg="white").pack(pady=10)

result_var = tk.StringVar()
tk.Entry(root, textvariable=result_var, font="Arial 14", width=30, bg="#1E1E1E", fg="white", insertbackground="white").pack(pady=10)

copy_btn = tk.Button(root, text="Copy", command=copy_to_clipboard, font="Arial 12", bg="#2C2C2C", fg="white")
copy_btn.pack()

# Keyboard shortcut
root.bind("<Return>", lambda e: generate_password())

root.mainloop()
