import tkinter
import tkinter.scrolledtext as st
window = tkinter.Tk()
window.geometry("420x210")
window.title('CSV Contact List')
frame1 = tkinter.Frame(window, highlightbackground="gray", highlightthickness=1)

l1=tkinter.Label(frame1,text="Last Name")
txt1 = tkinter.Text(frame1,width=15,height=1)
l2=tkinter.Label(frame1,text="First Name")
txt2 = tkinter.Text(frame1,width=15,height=1)
l3=tkinter.Label(frame1,text="Email")
txt3 = tkinter.Text(frame1,width=15,height=1)
l4=tkinter.Label(frame1,text="Phone")
txt4 = tkinter.Text(frame1,width=15,height=1)
listbox= tkinter.Listbox(window,height=10,width=20,bg='white')
frame1.grid(column=0,row=0)

listbox.insert(1, 'Gauford, Albertine')
listbox.insert(2, 'Greger, Bryce')
listbox.insert(3, 'Wetherald,Rickey')
listbox.insert(4, 'Onthank, Giustina')
listbox.insert(5, 'Clever, Ulric')
listbox.insert(6, 'Guthrum, Amble')
listbox.insert(7, 'Guppey, Austine')
listbox.insert(8, 'Farndale, Gerhardt')
listbox.insert(9, 'Wolfenden, Caressa')
listbox.insert(10, 'Holliar, Robbyn')
listbox.insert(11, 'MacAllaster, Lisabeth')

l1.grid(column=3,row=0,padx=5,pady=5)
txt1.grid(column=5,row=0,padx=5,pady=5)
l2.grid(column=3,row=1,padx=5,pady=5)
txt2.grid(column=5,row=1,padx=5,pady=5)
l3.grid(column=3,row=2,padx=5,pady=5)
txt3.grid(column=5,row=2,padx=5,pady=5)
l4.grid(column=3,row=3,padx=5,pady=5)
txt4.grid(column=5,row=3,padx=5,pady=5)
listbox.grid(column=1,row=0,padx=10)
frame1.grid(column=10, row=0,padx=40)



window.mainloop()