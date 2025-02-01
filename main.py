# console

import tkinter as tk
import fush
from tkinter import ttk

__version__ = "0.1"

root = tk.Tk()
root.geometry("500x500")
root.resizable(False, False)
root.title(f"cKit {__version__}") #console
photo = tk.PhotoImage(file = 'fush.ico')
root.iconphoto(True,photo)

code = tk.Text(root, height=20, width=60)
code.pack()
tk.Label(root, text="Terminal").place(x=10, y=335)
result = tk.Text(root, height=10, width=60,state='disabled')
result.pack()

def save():
    pass

def open():
    pass

def run():
    try:
        code_str = code.get("1.0", tk.END).strip()
        result.insert('1.0', f"Output: {fush.compile_code(code_str)[1]}\n")
        result.config(state='normal')
        fush.execute(code.get("1.0", tk.END).strip())
    except RuntimeError:
        pass


def exit():
    pass

menu = tk.Menu(root)
file_menu = tk.Menu(menu, tearoff=0)
file_menu.add_command(label="Save",command=save)
file_menu.add_command(label="Open",command=open)
file_menu.add_command(label="Run code",command=run)
file_menu.add_command(label="Exit",command=exit)
menu.add_cascade(label="File", menu=file_menu)

root.bind("<Control-s>", lambda event: save())
root.bind("<Control-o>", lambda event: open())
root.bind("<F5>", lambda event: run())

root.config(menu=menu)

root.mainloop()