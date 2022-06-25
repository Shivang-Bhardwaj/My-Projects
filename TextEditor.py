from tkinter import *
from tkinter import messagebox as mb
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os

def newFile():
    global file
    w.title('Untitled-Notepad')
    file=None
    TextArea.delete(1.0,END)


def openFile():
    global file
    file=askopenfilename(defaultextension='.txt',filetypes=[('All Files','*.*'),('Text Documents','*.txt')])
    if file=='':
        file=None
    else:
        w.title(os.path.basename(file)+'-Notepad')
        TextArea.delete(1.0,END)
        f=open(file,'r')
        TextArea.insert(1.0,f.read())
        f.close()

def saveFile():
    global file 
    if file==None:
        file=asksaveasfilename(initialfile='Untitled.txt',defaultextension='.txt',filetypes=[('All Files','*.*'),('Text Documents','*.txt')])
        if file=='':
            file=None
        else:
            f=open(file,'w')
            f.write(TextArea.get(1.0,END))
            f.close()
            w.title(os.path.basename(file+'-Notepad'))
            print('filesaved')
    else:
        f=open(file,'w')
        f.write(TextArea.get(1.0,END))
        f.close()


def quitApp():
    w.destroy()
def cut():
    TextArea.event_generate('<<Cut>>')                 # new thing
def copy():
    TextArea.event_generate('<<Copy>>')
def paste():
    TextArea.event_generate('<<Paste>>')
def about():
    mb.showinfo('Notepad','Notepad by shiva...')

if __name__=='__main__':
    w=Tk()
    w.title('Untitled - Notepad')
    # w.wm_iconbitmap('./stuff/s.ico')
    w.geometry('644x688')


    TextArea=Text(w,font='lucida 13')
    TextArea.pack(fill=BOTH,expand=True)
    file=None


    MenuBar=Menu(w)

    FileMenu=Menu(MenuBar,tearoff=0)
    FileMenu.add_command(label='New',command=newFile)
    FileMenu.add_command(label='Open',command=openFile)
    FileMenu.add_command(label='Save',command=saveFile)
    FileMenu.add_separator()
    FileMenu.add_command(label='Exit',command=quitApp)
    MenuBar.add_cascade(label='File',menu=FileMenu)

    EditMenu=Menu(MenuBar,tearoff=0)
    EditMenu.add_command(label='Cut',command=cut)
    EditMenu.add_command(label='Copy',command=copy)
    EditMenu.add_command(label='Paste',command=paste)
    MenuBar.add_cascade(label='Edit',menu=EditMenu)

    HelpMenu=Menu(MenuBar,tearoff=0)
    HelpMenu.add_command(label='About Notepad',command=about)
    MenuBar.add_cascade(label='Help',menu=HelpMenu)

    w.config(menu=MenuBar)


    Scroll=Scrollbar(TextArea)
    Scroll.pack(side=RIGHT,fill=Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)


    w.mainloop()