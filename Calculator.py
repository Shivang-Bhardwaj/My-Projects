from tkinter import *
w=Tk()
w.geometry('620x700')
w.title('Calculator...')
w.minsize(620,700)
w.maxsize(620,700)
# w.wm_iconbitmap('./stuff/s.ico')

def click(event):
    text=event.widget.cget('text')
    if text=='=':
        if scvalue.get().isdigit():
            value=scvalue.get()
        else:
            try:
                value=eval(scvalue.get())
            except:
                value='Error'
        scvalue.set(value)
        screen.config(textvariable=scvalue)
    elif text=='C':
        scvalue.set('')
        screen.config(textvariable=scvalue)
    else:
        scvalue.set(scvalue.get()+text)
        screen.config(textvariable=scvalue)

scvalue=StringVar()
scvalue.set('')
screen=Entry(w,textvariable=scvalue,font='lucida 35 bold',bg='cyan',fg='blue')
screen.pack(fill=X,pady=30,padx=10)


n=9
f1=Frame(w)
f=Frame(f1,bg='silver')
for i in range(3):
    for j in range(3):
        b=Button(f,text=f'{n}',padx=28,pady=5,font='lucida 20 bold',bg='black',fg='white')
        b.grid(row=i,column=j,padx=15,pady=9)
        b.bind('<ButtonPress-1>',click)

        n-=1
f.pack()

f=Frame(f1,bg='silver')
b=Button(f,text='0',padx=28,pady=5,font='lucida 20 bold',bg='black',fg='white')
b.pack(side=LEFT,padx=15,pady=9)
b.bind('<Button-1>',click)

b=Button(f,text='00',padx=22,pady=5,font='lucida 20 bold',bg='black',fg='white')
b.pack(side=LEFT,padx=15,pady=9)
b.bind('<Button-1>',click)

b=Button(f,text='.',padx=30,pady=5,font='lucida 20 bold',bg='black',fg='white')
b.pack(side=LEFT,padx=15,pady=9)
b.bind('<Button-1>',click)

f.pack()
f1.pack(side=LEFT)


f2=Frame(w,bg='silver')
b=Button(f2,text='C',padx=25,pady=5,font='lucida 20 bold',bg='yellowgreen')
b.grid(row=0,columnspan=2,padx=15,pady=9)
b.bind('<Button-1>',click)

l,k=['+','-','*','/'],0
for i in range(2):
    for j in range(2):
        b=Button(f2,text=f'{l[k]}',padx=22,pady=5,font='lucida 20 bold',bg='black',fg='white')
        b.grid(row=i+1,column=j,padx=15,pady=9)
        b.bind('<Button-1>',click)
        k+=1

b=Button(f2,text='=',padx=22,pady=5,font='lucida 20 bold',bg='black',fg='white')
b.grid(row=3,columnspan=2,padx=15,pady=9)
b.bind('<Button-1>',click)

f2.pack(side=RIGHT)


w.mainloop()