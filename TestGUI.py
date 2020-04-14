from tkinter import *
from tkinter import ttk
root =Tk()

e=Entry(root,width=50,bg="yellow",borderwidth=5)
e.pack()
def myClick():
    myLabel=ttk.Label(root,text=e.get())
    myLabel.pack()
myButton =ttk.Button(root,text="enter your name",command=myClick)
myButton.pack()

root.mainloop()