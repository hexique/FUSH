# console

import os
import fush
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from time import time

__version__ = "1.1.3"

root = tk.Tk()
root.geometry("1000x800")
root.resizable(True, True)
root.title(f"Ckit {__version__}") #console
photo = tk.PhotoImage(file = 'ckit.ico')
root.iconphoto(True,photo,photo)
root.config(bg='#1E1E1E')

path = None

code = tk.Text(root, height=20, width=60, bg='#1E1E1E', fg='#F0F0F0', insertbackground='#F0F0F0',font=('Cascadia Code', 10), wrap="none")
code.pack(fill=tk.BOTH, expand=True)

lines = ''
chars = code.get("1.0", tk.END)

data = tk.Label(root, bg=code['bg'], fg=code['fg'], justify="right",text=f"Lines: {len(lines)}\n Total characters: {len(chars)}")
data.place(x=864, y=760)

def update_data(bind):
    global lines
    chars = code.get("1.0", tk.END)
    lines = code.get("1.0",tk.END).split('\n')
    data['text'] = f"Lines: {len(lines) - 1}\n Total characters: {len(chars)}"

code.bind("<KeyRelease>", lambda event: update_data(event))

# tk.Label(root, text="Terminal").place(x=10, y=335)
# result = tk.Text(root, height=10, width=60,state='disabled')
# result.pack(fill=tk.BOTH, expand=True)

def update_options():
    global code, root, theme, font_size, options_label, dark_theme_check, show_data_check
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

    light_theme_check['fg'] = fg
    light_theme_check['bg'] = bg

    dark_theme_check['fg'] = fg
    dark_theme_check['bg'] = bg

    black_theme_check['fg'] = fg
    black_theme_check['bg'] = bg

    matrix_theme_check['fg'] = fg
    matrix_theme_check['bg'] = bg

    show_data_check['fg'] = fg
    show_data_check['bg'] = bg

    style.configure("Custom.Horizontal.TScale",
                    background=bg,
                    troughcolor=fg,
                    sliderthickness=10,
                    sliderlength=20)
    try:
        font_size_check['style'] = style
    except:
        pass

def update_font(bind):
    code["font"] = ('Cascadia Code', font_size.get())

def toggle_data():
    global data
    if show_data.get():
        data = tk.Label(root, bg=code['bg'], fg=code['fg'], justify="right",text=f"Lines: {len(lines)}\n Total characters: {len(chars)}")
        data.place(x=864, y=760)
    else:
        data.destroy() 
style = ttk.Style()

style.configure("Custom.Horizontal.TScale",
                background=code["bg"],
                troughcolor=code["fg"],
                sliderthickness=10,
                sliderlength=20)  

def options():
    global options_root, code, root, theme, font_size, options_label, font_size_check, light_theme_check, dark_theme_check
    global black_theme_check, matrix_theme_check, show_data_check, show_data

    options_root = tk.Toplevel()
    options_root.geometry("500x500")
    options_root.title(f'Ckit {__version__} — Options')
    options_root.config(bg=code['bg'])

    options_label = tk.Label(options_root, text="Options", font=('TkDefaultFont', 35),bg=code['bg'],fg=code['fg'])
    options_label.place(x=10, y=10)

    font_size = tk.IntVar(value=10)

    font_size_check = ttk.Scale(options_root, from_=5, to=50, length=100, orient=tk.HORIZONTAL, variable=font_size, 
                                command=update_font, style="Custom.Horizontal.TScale")
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
    
    show_data = tk.IntVar(value=1)
    show_data_check = tk.Checkbutton(options_root, text="Show info", variable=show_data, bg=code['bg'], fg=code['fg'], 
                                     command=toggle_data)
    show_data_check.place(x=200, y=70)
    options_root.mainloop()

def save():
    global path
    if path != None:
        with open(path, "w", encoding="utf-8") as f:
            f.write(code.get("1.0", tk.END))
        return


    file_path = filedialog.asksaveasfilename(
            initialfile="main.fush",
            defaultextension=".fush",
            # initialdir=f"{os.path.dirname(os.path.abspath(__file__))}",
            title="Save file",
            filetypes=[("FUSH file", "*.fush"), ("Python file", "*.py"), ("Text file", "*.txt"), ("All files", "*.*")]
    )
    
    path = file_path
    if file_path:
        if file_path.endswith(".py"):
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(fush.compile_code(code.get("1.0", tk.END))[1])
        else:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(code.get("1.0", tk.END))
                root.title(f'Ckit {__version__} — {os.path.basename(file_path)}')

def open_file():
    global path
    if path != None:
        messagebox.showwarning(root.title(), "Unsaved changes detected. Do you want to save?")
    file_path = filedialog.askopenfilename(

    )
    path = file_path
    if file_path:
        with open(file_path, "r", encoding="utf-8") as f:
            code.delete('1.0', tk.END)
            code.insert('1.0', f.read())
            root.title(f'Ckit {__version__} — {os.path.basename(file_path)}')

def new_file():
    if " — " in root.title():
        messagebox.showwarning(root.title(), "Unsaved changes detected. Do you want to save?")
    code.delete('1.0', tk.END)
    root.title(f"Ckit {__version__}")

def run():
    save()
    try:
        fush.execute(code.get("1.0", tk.END).strip())
    except RuntimeError:
        pass

menu = tk.Menu(root)
file_menu = tk.Menu(menu, tearoff=0)
file_menu.add_command(label="New file",command=new_file)
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