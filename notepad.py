from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os 

def newfile():
    global file
    root.title("Untitled -Notepad")
    file = None
    TextArea.delete(1.0,END)

def openfile():
    global file
    file = askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
    if file=="":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        TextArea.delete(1.0,END)
        f =open(file,"r")
        TextArea.insert(1.0,f.read())
        f.close()
    
def savefile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile="Untiteled.txt",defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
        if file =="":
            file = None
        else:
            f = open(file,"w")
            f.write(TextArea.get(1.0,END))
            f.close
            root.title(os.path.basename(file) + ' - Notepad')
    else:
        f = open(file,"w")
        f.write(TextArea.get(1.0,END))
        f.close

def saveas():
    pass

def cut():
    TextArea.event_generate(("<<Cut>>"))

def copy():
    TextArea.event_generate(("<<Copy>>"))

def paste():
    TextArea.event_generate(("<<Paste>>"))

def statusbar():
    showinfo("Notepad","This notepad is created by Devang.")




if __name__ =='__main__':
    root = Tk()
    root.geometry("555x444")
    root.title("My Notepad")
    
    
    TextArea = Text(root,font="lucida 25 bold")
    file = None
    TextArea.pack(expand=True,fill=BOTH)
    
    mainmenu = Menu(root)
    m1=Menu(mainmenu,tearoff=0)
    m1.add_command(label="New",command=newfile)
    m1.add_command(label="Open",command=openfile)
    m1.add_separator()
    m1.add_command(label="Save",command=savefile)
    m1.add_command(label="Save As",command=saveas)
    m1.add_separator()
    m1.add_command(label="Print",command=print)
    m1.add_command(label="Exit",command=quit)
    root.config(menu=mainmenu)

    mainmenu.add_cascade(label="File",menu=m1)

    m2=Menu(mainmenu,tearoff=0)
    m2.add_command(label="Undo",command=open)
    m2.add_separator()
    m2.add_command(label="Cut",command=cut)
    m2.add_command(label="Copy",command=copy)
    m2.add_command(label="Paste",command=paste)
    m2.add_command(label="Delete",command=print)
    
    root.config(menu=mainmenu)

    mainmenu.add_cascade(label="Edit",menu=m2)

    m3=Menu(mainmenu,tearoff=0)
    m3.add_command(label="Zoom",command=open)
    m3.add_command(label="Status Bar",command=statusbar)
    root.config(menu=mainmenu)
    mainmenu.add_cascade(label="View",menu=m3)

    # Addinh the scrollbar
    Scroll = Scrollbar(TextArea)
    Scroll.pack(side=RIGHT,fill=Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)
    
    root.mainloop()