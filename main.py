# console

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import os
import fush

__version__ = "0.2"

root = tk.Tk()
root.geometry("1000x500")
root.resizable(True, True)
root.title(f"cKit {__version__}") #console
photo = tk.PhotoImage(file = 'fush.ico')
root.iconphoto(True,photo)

code = tk.Text(root, height=20, width=60)
code.pack(fill=tk.BOTH, expand=True)
# tk.Label(root, text="Terminal").place(x=10, y=335)
# result = tk.Text(root, height=10, width=60,state='disabled')
# result.pack(fill=tk.BOTH, expand=True)

def save():
    file_path = filedialog.asksaveasfilename(
            initialfile="main.fush",
            defaultextension=".fush",
            initialdir=f"{os.path.dirname(os.path.abspath(__file__))}",
            title="Save FUSH file",
            filetypes=[("FUSH file", "*.fush"), ("Python file", "*.py"), ("Text file", "*.txt"), ("All files", "*.*")]
    )
    
    if file_path:
        with open(file_path, "w") as f:
            f.write(code.get("1.0", tk.END))

def open_file():
    file_path = filedialog.askopenfilename(

    )
    
    if file_path:
        with open(file_path, "r") as f:
            code.insert('1.0', f.read())
            root.title(f'cKit {__version__} — {os.path.basename(file_path)}')

def run():
    try:
        code_str = code.get("1.0", tk.END).strip()
        # result.insert('1.0', f"Output: {fush.compile_code(code_str)[1]}\n")
        # result.config(state='normal')
        fush.execute(code.get("1.0", tk.END).strip())
    except RuntimeError:
        pass


def exit():
    pass

menu = tk.Menu(root)
file_menu = tk.Menu(menu, tearoff=0)
file_menu.add_command(label="Save",command=save)
file_menu.add_command(label="Open",command=open_file)
file_menu.add_command(label="Run code",command=run)
file_menu.add_command(label="Exit",command=exit)
menu.add_cascade(label="File", menu=file_menu)

root.bind("<Control-s>", lambda event: save())
root.bind("<Control-o>", lambda event: open_file())
root.bind("<F5>", lambda event: run())

root.config(menu=menu)

root.mainloop()