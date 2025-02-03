# console

import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os
import fush

__version__ = "1.0"

root = tk.Tk()
root.geometry("1000x800")
root.resizable(True, True)
root.title(f"cKit {__version__}") #console
photo = tk.PhotoImage(file = 'ckit.ico')
root.iconphoto(True,photo)


code = tk.Text(root, height=20, width=60, bg='#1E1E1E', fg='#F0F0F0', insertbackground='#F0F0F0',font=('Cascadia Code', 10))
code.pack(fill=tk.BOTH, expand=True)
# tk.Label(root, text="Terminal").place(x=10, y=335)
# result = tk.Text(root, height=10, width=60,state='disabled')
# result.pack(fill=tk.BOTH, expand=True)

def update_options():
    global code, root, theme, font_size, options_label, dark_theme_check
    if theme.get() == 'light':
        bg = '#F0F0F0'
        fg = '#1E1E1E'
    elif theme.get() == 'dark':
        bg = '#1E1E1E'
        fg = '#F0F0F0'
    elif theme.get() == 'black':
        bg = '#000000'
        fg = '#FFFFFF'
    elif theme.get() == 'matrix':
        bg = '#000000'
        fg = '#00FF00'

    code.config(bg=bg, fg=fg, insertbackground=fg)
    options_root.config(bg=bg)
    options_label.config(bg=bg, fg=fg)
    dark_theme_check.config(bg=bg, fg=fg)
    options_label['bg'] = bg
    options_label['fg'] = fg

    font_size_check['bg'] = bg
    font_size_check['fg'] = fg

    light_theme_check['fg'] = fg
    light_theme_check['bg'] = bg

    dark_theme_check['fg'] = fg
    dark_theme_check['bg'] = bg

    black_theme_check['fg'] = fg
    black_theme_check['bg'] = bg

    matrix_theme_check['fg'] = fg
    matrix_theme_check['bg'] = bg

def update_font(bind):
    code["font"] = ('Cascadia Code', font_size.get())

def options():
    global options_root, code, root, theme, font_size, options_label, font_size_check, light_theme_check, dark_theme_check, black_theme_check, matrix_theme_check

    options_root = tk.Toplevel()
    options_root.geometry("500x500")
    options_root.title("Options")
    options_root.config(bg=code['bg'])

    options_label = tk.Label(options_root, text="Options", font=('TkDefaultFont', 35),bg=code['bg'],fg=code['fg'])
    options_label.place(x=10, y=10)

    font_size = tk.IntVar(value=10)

    font_size_check = tk.Scale(options_root, from_=5, to=30, orient=tk.HORIZONTAL, variable=font_size, label='Font size', 
                               bg=code['bg'], fg=code['fg'], borderwidth=0, border=0, command=update_font)
    font_size_check.place(x=10, y=70)

    theme = tk.StringVar(value='dark')

    light_theme_check = tk.Radiobutton(options_root, text="Light theme", value='light', variable=theme, bg=code['bg'], fg=code['fg'], command=update_options)
    light_theme_check.place(x=10, y=170)

    dark_theme_check = tk.Radiobutton(options_root, text="Dark theme", value='dark', variable=theme, bg=code['bg'], fg=code['fg'],command=update_options)
    dark_theme_check.place(x=10, y=200)

    black_theme_check = tk.Radiobutton(options_root, text="Black theme", value='black', variable=theme, bg=code['bg'], fg=code['fg'],command=update_options)
    black_theme_check.place(x=10, y=230)

    matrix_theme_check = tk.Radiobutton(options_root, text="Matrix", value='matrix', variable=theme, bg=code['bg'], fg=code['fg'],command=update_options)
    matrix_theme_check.place(x=10, y=260)


    options_root.mainloop()

def save():
    if " — " in root.title():
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(code.get("1.0", tk.END)[1])


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