########################################################################################################
# Projet : Content Folder                                                                              #
# Auteur : Soradev                                                                                     #
# Version : 1.0.0                                                                                      #
########################################################################################################
# Description :                                                                                        #
#   Generates the file tree of a selected folder                                                       #
########################################################################################################
# For any questions or contributions, please contact the author at sora.dev.pro@gmail.com              #
########################################################################################################

import os
import tkinter as tk
from tkinter import filedialog, scrolledtext, messagebox

def generate_tree(path, prefix=""):
    tree = ""
    items = os.listdir(path)
    items.sort()
    pointers = ['├── '] * (len(items) - 1) + ['└── ']
    
    for pointer, item in zip(pointers, items):
        item_path = os.path.join(path, item)
        tree += prefix + pointer + item + "\n"
        if os.path.isdir(item_path):
            extension = '│   ' if pointer == '├── ' else '    '
            tree += generate_tree(item_path, prefix + extension)
    
    return tree

def choose_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        tree = os.path.basename(folder_selected) + "/\n" + generate_tree(folder_selected)
        text_area.delete(1.0, tk.END)
        text_area.insert(tk.END, tree)
        btn_copy.config(state=tk.NORMAL)

def copy_to_clipboard():
    app.clipboard_clear()
    app.clipboard_append(text_area.get(1.0, tk.END))
    messagebox.showinfo("Succès", "Arborescence copiée dans le presse-papiers.")

def center_window(root, width=800, height=600):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = int((screen_width / 2) - (width / 2))
    y = int((screen_height / 2) - (height / 2))
    root.geometry(f'{width}x{height}+{x}+{y}')

app = tk.Tk()
app.title("ContentFolder")

center_window(app)

btn_choose_folder = tk.Button(app, text="Choisir Dossier", command=choose_folder)
btn_choose_folder.pack(pady=10)

text_area = scrolledtext.ScrolledText(app, width=90, height=30)
text_area.pack(pady=10, padx=10)

btn_copy = tk.Button(app, text="Copier", state=tk.DISABLED, command=copy_to_clipboard)
btn_copy.pack(pady=5)

app.mainloop()
