# console

import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os
import fush

__version__ = "0.3.1"

root = tk.Tk()
root.geometry("1000x800")
root.resizable(True, True)
root.title(f"cKit {__version__}") #console
photo = tk.PhotoImage(file = 'ckit.ico')
root.iconphoto(True,photo)

code = tk.Text(root, height=20, width=60, bg='#1E1E1E', fg='#F0F0F0', font=("Cascadia Code", 12))
code.pack(fill=tk.BOTH, expand=True)
# tk.Label(root, text="Terminal").place(x=10, y=335)
# result = tk.Text(root, height=10, width=60,state='disabled')
# result.pack(fill=tk.BOTH, expand=True)

def update_options():
    global code, root, dark_theme, font_size
    if dark_theme.get():
        code.config(bg='#1E1E1E', fg='#F0F0F0')
        root.config(bg='#1E1E1E')
    else:
        code.config(bg='#F0F0F0', fg='#1E1E1E')
        root.config(bg='#F0F0F0')

def update_font(bind):
    code["font"] = ("Cascadia Code", font_size.get())


def options():
    global options_root, code, root, dark_theme, font_size

    if 'root' not in globals():
        root = tk.Tk()
        root.geometry("500x500")
        root.title("Main Window")
        code = tk.Text(root, bg='#1E1E1E', fg='#F0F0F0')
        code.pack(fill=tk.BOTH, expand=True)

    options_root = tk.Toplevel()
    options_root.geometry("500x500")
    options_root.title("Options")
    options_root.config(bg=code['bg'])

    tk.Label(options_root, text="Options", font=('TkDefaultFont', 35)).place(x=10, y=10)

    font_size = tk.IntVar(value=10)
    ttk.Scale(options_root, from_=5, to=30, orient=tk.HORIZONTAL, variable=font_size, command=update_font).place(x=10, y=70)

    dark_theme = tk.IntVar(value=1)
    ttk.Checkbutton(options_root, text="Dark theme", variable=dark_theme, command=update_options).place(x=10, y=150)


    options_root.mainloop()

def save():
    file_path = filedialog.asksaveasfilename(
            initialfile="main.fush",
            defaultextension=".fush",
            # initialdir=f"{os.path.dirname(os.path.abspath(__file__))}",
            title="Save file",
            filetypes=[("FUSH file", "*.fush"), ("Python file", "*.py"), ("Text file", "*.txt"), ("All files", "*.*")]
    )
    
    if file_path:
        if file_path.endswith(".py"):
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(fush.compile_code(code.get("1.0", tk.END))[1])
        else:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(code.get("1.0", tk.END))
                root.title(f'cKit {__version__} — {os.path.basename(file_path)}')

def open_file():
    file_path = filedialog.askopenfilename(

    )
    
    if file_path:
        with open(file_path, "r", encoding="utf-8") as f:
            code.delete('1.0', tk.END)
            code.insert('1.0', f.read())
            root.title(f'cKit {__version__} — {os.path.basename(file_path)}')

def run():
    try:
        # code_str = code.get("1.0", tk.END).strip()
        # result.insert('1.0', f"Output: {fush.compile_code(code_str)[1]}\n")
        # result.config(state='normal')
        # fush.exit_code()
        fush.execute(code.get("1.0", tk.END).strip())
    except RuntimeError:
        pass

menu = tk.Menu(root)
file_menu = tk.Menu(menu, tearoff=0)
file_menu.add_command(label="Save",command=save)
file_menu.add_command(label="Open",command=open_file)
file_menu.add_command(label="Run code",command=run)
file_menu.add_command(label="Options",command=options)
file_menu.add_command(label="Exit",command=quit)
menu.add_cascade(label="File", menu=file_menu)

root.bind("<Control-s>", lambda event: save())
root.bind("<Control-o>", lambda event: open_file())
root.bind("<Control-i>", lambda event: options())

root.bind("<F5>", lambda event: run())

root.config(menu=menu)

root.mainloop()