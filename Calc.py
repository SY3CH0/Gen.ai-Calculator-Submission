import tkinter as tk
from math import sin, cos, tan, log, sqrt

def button_click(value):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_text + str(value))

def evaluate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def clear():
    entry.delete(0, tk.END)

memory = 0

def memory_clear():
    global memory
    memory = 0

def memory_recall():
    entry.delete(0, tk.END)
    entry.insert(tk.END, str(memory))

def memory_add():
    global memory
    try:
        memory += eval(entry.get())
    except:
        pass

def memory_subtract():
    global memory
    try:
        memory -= eval(entry.get())
    except:
        pass

root = tk.Tk()
root.title("CalcMate")
root.geometry("400x600")
root.config(bg="#0d0d0d")  # Dark background for neon effect

button_color = "#1f1f1f"
button_text_color = "white"
hover_color = "#00ccff"
font = ('Arial', 18)
glow_color = "#00ff99"

entry = tk.Entry(root, width=18, font=('Arial', 28), borderwidth=0, relief="solid", bg="#161616", fg="white", justify='right')
entry.grid(row=0, column=0, columnspan=4, pady=20, padx=10)
entry.config(insertbackground='white')  # Cursor color

entry.config(highlightbackground=glow_color, highlightthickness=2, relief="solid")

def create_button(text, command, row, col, w=5, h=2):
    btn = tk.Button(root, text=text, width=w, height=h, font=font, bg=button_color, fg=button_text_color, 
                    border=0, activebackground=hover_color, activeforeground="white", command=command)
    btn.grid(row=row, column=col, padx=10, pady=10)
    btn.config(relief="flat", overrelief="flat")
    btn.bind("<Enter>", lambda e: btn.config(bg=hover_color))
    btn.bind("<Leave>", lambda e: btn.config(bg=button_color))
    return btn

def percentage():
    try:
        result = eval(entry.get()) / 100
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

buttons = [
    ('MC', memory_clear), ('MR', memory_recall), ('M+', memory_add), ('M-', memory_subtract),
    ('7', lambda: button_click('7')), ('8', lambda: button_click('8')), ('9', lambda: button_click('9')), ('/', lambda: button_click('/')),
    ('4', lambda: button_click('4')), ('5', lambda: button_click('5')), ('6', lambda: button_click('6')), ('*', lambda: button_click('*')),
    ('1', lambda: button_click('1')), ('2', lambda: button_click('2')), ('3', lambda: button_click('3')), ('-', lambda: button_click('-')),
    ('0', lambda: button_click('0')), ('.', lambda: button_click('.')), ('%', percentage), ('+', lambda: button_click('+')),
]

row = 1
col = 0
for text, command in buttons:
    create_button(text, command, row, col)
    col += 1
    if col > 3:
        col = 0
        row += 1

create_button('C', clear, row, 0)
create_button('√', lambda: button_click('sqrt('), row, 1)
create_button('log', lambda: button_click('log('), row, 2)
create_button('=', evaluate, row, 3)

root.mainloop()
