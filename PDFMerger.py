import Module1
from tkinter import *
from tkinter import ttk

# Create file path list
filepaths = []


# Create functions
def addfile():
    Module1.add(pdf_list, filepaths)


def removefile():
    Module1.remove(pdf_list, filepaths)


def merge_button():
    Module1.merge_pdf(filepaths)


# Title
title = Module1.title_welcome()[0]
welcome_message = Module1.title_welcome()[1]

# Create root
root = Tk()
root.minsize(400, 250)
root.title(title)
root.option_add('*tearOff', FALSE)  # Prevent menus from tearing off the window

# Create menu bar
Module1.create_menu_bar(root)

# Create all widgets
frame = ttk.Frame(root, padding=(5, 5, 5, 5))
welcome = ttk.Label(frame, text=welcome_message)
pdf_list = Listbox(frame, selectmode='extended', height=5)
scroll = ttk.Scrollbar(frame, orient=VERTICAL, command=pdf_list.yview)
pdf_list['yscrollcommand'] = scroll.set  # Set scroll bar size
add = ttk.Button(frame, text='Add PDF', command=addfile)
remove = ttk.Button(frame, text='Remove', command=removefile)
merge = ttk.Button(frame, text='Merge!', command=merge_button)
cancel = ttk.Button(frame, text='Close', command=root.destroy)

# Position all widgets
frame.grid(column=0, row=0, sticky=(N, S, E, W))
welcome.grid(column=0, row=0, sticky=W, pady=(0, 10))
pdf_list.grid(column=0, row=1, rowspan=4, sticky=(N, S, E, W))
scroll.grid(column=1, row=1, rowspan=4, sticky=(N, S, W))
add.grid(column=2, row=1, padx=(5, 0), pady=(0, 5))
remove.grid(column=2, row=2, padx=(5, 0))
merge.grid(column=2, row=3, sticky=S, padx=(5, 0), pady=(0, 5))
cancel.grid(column=2, row=4, sticky=S, padx=(5, 0))

# Resize
Module1.resize(root, frame)

root.mainloop()
