from tkinter import*
import tkinter.scrolledtext as st
top = Tk()
top.title("tk")
l1=Label(top,text="Contact List").place(x=45,y=0)
listbox= Listbox(top,height=10,width=20,bg='white')
listbox.place(x=20,y=20)
b2 = Button(top,text="Display Contact").place(x=30,y=190)
lastn = Label(top,text="Last Name:").place(x=0,y=230)
e1 = Entry(top).place(x=65,y=232)
til=Label(top,text="New Contact")
til.place(x=200,y=10)
Cl = Label(top,text="First Name:")
Cl.place(x=200,y=40)
LastName = Label(top,text="Last Name:")
LastName.place(x=200,y=70)
phone = Label(top,text="Phone #:")
phone.place(x=200,y=100)
but=Checkbutton(top,text="Friend")
but.place(x=280,y=130)
email=Label(top,text="Email:")
email.place(x=200,y=160)
Birthday=Label(top,text="Birthday:")
Birthday.place(x=200,y=190)

e1 = Entry(top).place(x=280,y=40)
e1 = Entry(top).place(x=280,y=70)
e1 = Entry(top).place(x=280,y=100)
e1 = Entry(top).place(x=280,y=160)
e1 = Entry(top).place(x=280,y=190)
b1 = Button(top,text="Add Contact").place(x=270,y=220)
b2 = Button(top,text="Search").place(x=50,y=270)

top.mainloop()