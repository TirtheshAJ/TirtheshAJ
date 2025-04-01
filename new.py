'''
from tkinter import *
root=Tk()
def sel():
    s="you Selected option :",var.get()
    label.config(text=s)
var=IntVar()
r1=Radiobutton(root,text="option 1",var=1,command=sel)
r2=Radiobutton(root,text="option 2",var=2,command=sel)
r3=Radiobutton(root,text="option 3",var=3,command=sel)
l=Label(root)
l.pack()
root.mainloop()
print('end')
'''
'''
from tkinter import *
root=Tk()
def sel():
    print(var1.get())
    print(var2.get())
var1=IntVar()
var2=IntVar()
r1=Checkbutton(root,text="option 1",variable=var1,onvalue=1,offvalue=0,command=sel)
r1.pack()
r2=Checkbutton(root,text="option 2",variable=var2,onvalue=1,offvalue=0,command=sel)
r2.pack()
root.mainloop()
print('end')
'''
'''
from tkinter import *
root=Tk()
root.title("home")
l=Label(root,text="welcome !",font=("Arial",10))
l.pack()
l=Label(root,text="welcome !",font=("Arial",10))
'''





