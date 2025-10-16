from tkinter import *
root =Tk()
root.title("My Calculator")
root.geometry("644x900")

def click(event):
    global scvalue
    text = event.widget.cget("text")
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(scvalue.get())

            except Exception as e:
                print(e)
                value = "Error"


        scvalue.set(value)
        screen.update()

    elif text == "C":
        scvalue.set("")
        screen.update()

    else:
        scvalue.set(scvalue.get() + text)
        screen.update()


scvalue = StringVar()
scvalue.set("")

screen = Entry(root,textvar=scvalue,font="lucida 40 bold")
screen.pack(fill=X,pady=10,ipady=5,ipadx=5)



f=Frame(root,bg="grey")

b=Button(f,text="9",font="lucida 35 bold",padx=20,pady=18)
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)


b=Button(f,text="8",font="lucida 35 bold",padx=20,pady=18)
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="7",font="lucida 35 bold",padx=20,pady=18)
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="+",font="lucida 35 bold",padx=20,pady=18)
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)

f.pack()


f=Frame(root,bg="grey")

b=Button(f,text="6",font="lucida 35 bold",padx=20,pady=18)
b.pack(side=LEFT,padx=19,pady=5)
b.bind("<Button-1>",click)


b=Button(f,text="5",font="lucida 35 bold",padx=20,pady=18)
b.pack(side=LEFT,padx=19,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="4",font="lucida 35 bold",padx=20,pady=18)
b.pack(side=LEFT,padx=19,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="-",font="lucida 35 bold",padx=20,pady=18)
b.pack(side=LEFT,padx=19,pady=5)
b.bind("<Button-1>",click)

f.pack()


f=Frame(root,bg="grey")

b=Button(f,text="3",font="lucida 35 bold",padx=20,pady=18)
b.pack(side=LEFT,padx=19,pady=5)
b.bind("<Button-1>",click)


b=Button(f,text="2",font="lucida 35 bold",padx=20,pady=18)
b.pack(side=LEFT,padx=19,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="1",font="lucida 35 bold",padx=20,pady=18)
b.pack(side=LEFT,padx=19,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="*",font="lucida 35 bold",padx=20,pady=18)
b.pack(side=LEFT,padx=19,pady=5)
b.bind("<Button-1>",click)

f.pack()

f=Frame(root,bg="grey")

b=Button(f,text="%",font="lucida 35 bold",padx=20,pady=18)
b.pack(side=LEFT,padx=16,pady=5)
b.bind("<Button-1>",click)


b=Button(f,text="0",font="lucida 35 bold",padx=20,pady=18)
b.pack(side=LEFT,padx=16,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="C",font="lucida 35 bold",padx=20,pady=18)
b.pack(side=LEFT,padx=16,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="=",font="lucida 35 bold",padx=20,pady=18)
b.pack(side=LEFT,padx=16,pady=5)
b.bind("<Button-1>",click)

f.pack()


root.mainloop()