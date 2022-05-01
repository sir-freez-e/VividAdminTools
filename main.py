import os
import sys
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.commondialog import Dialog

root= tk.Tk()

root.title('Vivid Admin Tools')
root.geometry('600x400')
root.maxsize(600, 400)
root.minsize(600, 400)
root.config(bg='#345')

def about():
  messagebox.showinfo('Vivid Admin Tools', 'a collection of readily available tools for windows OS repair')  


menubar = Menu(root, background='#ff8000', foreground='black', activebackground='white', activeforeground='black')  
file = Menu(menubar, tearoff=1, background='#ffcc99', foreground='black')  
file.add_command(label="New")  
file.add_command(label="Open")  
file.add_command(label="Save")  
file.add_command(label="Save as")    
file.add_separator()  
file.add_command(label="Exit", command=root.quit)  
menubar.add_cascade(label="File", menu=file)  

edit = Menu(menubar, tearoff=0)  
edit.add_command(label="Undo")  
edit.add_separator()     
edit.add_command(label="Cut")  
edit.add_command(label="Copy")  
edit.add_command(label="Paste")  
menubar.add_cascade(label="Edit", menu=edit)  

help = Menu(menubar, tearoff=0)  
help.add_command(label="About", command=about)  
menubar.add_cascade(label="Help", menu=help)  
    
root.config(menu=menubar)
root.mainloop()