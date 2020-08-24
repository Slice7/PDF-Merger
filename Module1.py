import os
from tkinter.filedialog import asksaveasfilename, askopenfilenames
from tkinter import messagebox
import PyPDF2
from tkinter import *


# Variable assignment
def title_welcome():
    title = "PDF Merger"
    return [title, "Welcome to PDFMerger!"]


def getfilename(path):
    slash = list(reversed(path)).index("/")
    return path[-slash:]


# Button functions
def add(pdf_list, filepaths):
    paths = askopenfilenames()
    if paths != "":
        for filepath in paths:
            filepaths.append(filepath)
            filename = getfilename(filepath)
            pdf_list.insert('end', filename)


def remove(pdf_list, filepaths):
    positions = pdf_list.curselection()
    if not len(positions):
        messagebox.showinfo(message='Please select a file to remove!', icon='error', title='Error!')
    else:
        for pos in sorted(positions, reverse=True):
            del filepaths[pos]
            pdf_list.delete(pos)


def merge_pdf(filepaths):
    for filepath in filepaths:
        if filepath[-4:] != ".pdf":
            messagebox.showinfo(message='You can only merge PDF files!',
                                icon='error', title='Error!')
            return
        
    if len(filepaths) < 2:
        messagebox.showinfo(message='Please select more than one file to merge!',
                            icon='error', title='Error!')
    
    else:
        try:
            while True:
                newfilepath = asksaveasfilename()
                if newfilepath == "":
                    break
                elif newfilepath[-4:] != ".pdf":
                    newfilepath += ".pdf"
                    if os.path.isfile(newfilepath):
                        confirm = messagebox.askyesno(
                            message=getfilename(newfilepath) + ' already exists.\nDo you want to replace it?',
                            icon='error', title='Confirm Save As')
                        if confirm:
                            break
                        else:
                            continue
                    else:
                        break
                else:
                    break

            if newfilepath != "":
                output = PyPDF2.PdfFileWriter()
                for filepath in filepaths:
                    pdf = PyPDF2.PdfFileReader(open(filepath, "rb"))
                    pageCount = pdf.getNumPages()
                    for page in range(0, pageCount):
                        output.addPage(pdf.getPage(page))
                newPDF = open(newfilepath, "wb")
                output.write(newPDF)
                newPDF.close()
                messagebox.showinfo(message='PDFs successfully merged!',
                                    title='Success!')

        except PyPDF2.utils.PdfReadError:
            messagebox.showinfo(
                message='Something went wrong. Press the help menu to try a workaround. Error code: 01',
                icon='error', title='Error 01')


# Messages to end user
def about():
    messagebox.showinfo(message='PDFMerger\nVersion 1.0\n2017', icon='question', title='About')


def error01():
    messagebox.showinfo(
        message='Error 01: One or more of the PDFs you tried to merge may be encrypted.\n\nTo get around this, try ' +
            'duplicating the encrypted PDF(s). To do this, open the PDF in Adobe Acrobat Reader (or your preferred ' +
            'program) as you normally would. Then print the PDF using either Ctrl+P or via the File menu. Change the ' +
            'printer/destination to Microsoft Print to PDF and then press Print. Save the new PDF and then try to ' +
            'merge it again with {}.'.format(title_welcome()[0]),
        icon='question', title='Help')


# Menu bar
def create_menu_bar(root):
    menubar = Menu(root)
    root['menu'] = menubar
    # Add menu to menu bar
    menu_help = Menu(menubar)
    menubar.add_cascade(menu=menu_help, label='Help')
    # Add item to menu
    menu_help.add_command(label='View Help', command=error01)
    menu_help.add_command(label='About', command=about)


# Resize
def resize(root, frame):
    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_rowconfigure(3, weight=1)
