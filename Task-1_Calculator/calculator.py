import tkinter as tk

def click(event):
    global expression
    expression += event.widget.cget("text")
    entry_var.set(expression)

def clear():
    global expression
    expression = ""
    entry_var.set("")

def evaluate():
    global expression
    try:
        result = str(eval(expression))
        entry_var.set(result)
        expression = result
    except:
        entry_var.set("Error")
        expression = ""

def key_input(event):
    global expression
    char = event.char
    if char in "0123456789+-*/.":
        expression += char
        entry_var.set(expression)
    elif event.keysym == "Return":
        evaluate()
    elif event.keysym == "BackSpace":
        expression = expression[:-1]
        entry_var.set(expression)
    elif char.upper() == 'C':
        clear()

expression = ""
root = tk.Tk()
root.title("🧮 Dark Calculator")
root.geometry("320x400")
root.configure(bg="#121212")

root.bind("<Key>", key_input)

entry_var = tk.StringVar()
entry = tk.Entry(root, textvar=entry_var, font="Arial 24", bd=0, bg="#1E1E1E", fg="white", insertbackground="white", justify="right")
entry.pack(fill='both', ipadx=8, pady=10, padx=10)

btn_frame = tk.Frame(root, bg="#121212")
btn_frame.pack()

buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['C', '0', '=', '+']
]

for row in buttons:
    row_frame = tk.Frame(btn_frame, bg="#121212")
    row_frame.pack(expand=True, fill='both')
    for btn_text in row:
        b = tk.Button(row_frame, text=btn_text, font="Arial 18", width=5, height=2,
                      bg="#2C2C2C", fg="white", activebackground="#444")
        b.pack(side='left', expand=True, fill='both', padx=2, pady=2)
        if btn_text == '=':
            b.bind("<Button-1>", lambda e: evaluate())
        elif btn_text == 'C':
            b.bind("<Button-1>", lambda e: clear())
        else:
            b.bind("<Button-1>", click)

root.mainloop()
