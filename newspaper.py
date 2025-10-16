from tkinter import *
from PIL import Image,ImageTk
root=Tk()
root.geometry("1000x750")
root.title("News-Paper")

def every_100(text):
    final_text=""
    for i in range(0,len(text)):
        final_text +=text[i]
        if i%100==0 and i!=0:
            final_text +="\n" 
    return final_text

texts=[]
photos=[]
for i in range(0,3):
    with open(f"{i+1}.txt") as f:
        text = f.read()
        texts.append(every_100(text))
        
    image = Image.open(f"{i+1}.png")
    photos.append(ImageTk.PhotoImage(image))



f0 = Frame(root,width=800,height=70)
Label(f0,text="My NewsPaper",font="Lucida 33 bold").pack()

Label(f0,text="13 Augest,2024",font="Lucida 13 bold").pack()
f0.pack()

f1= Frame(root,width=900,height=200,pady=34)
Label(f1,text=texts[0],padx=22,pady=22).pack(side=LEFT)
Label(f1,image=photos[0]).pack(side=RIGHT)
f1.pack(anchor="w")


f2= Frame(root,width=900,height=200,pady=34,padx=22)
Label(f2,text=texts[1],padx=22,pady=22).pack(side=RIGHT)
Label(f2,image=photos[1]).pack(side=RIGHT)
f2.pack(anchor="w")


f3= Frame(root,width=900,height=200,pady=34)
Label(f3,text=texts[2],padx=22,pady=22).pack(side=LEFT)
Label(f3,image=photos[2]).pack(side=RIGHT)
f3.pack(anchor="w")

root.mainloop()