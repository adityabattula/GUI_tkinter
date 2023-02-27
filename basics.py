import tkinter as tk 
from tkinter import ttk

window = tk.Tk()
window.title("CALCULATOR")
def clicked():
    temp = "Welcome to "+txt.get()
    label.configure(text=temp)

label = tk.Label(window, text = "Name",font=("Arial Bold",10))
bt = tk.Button(window,text = "submit",bg='red',fg='white',command=clicked)
txt = tk.Entry(window,text = "type here",width=30)
combo = ttk.Combobox(window)
combo['values']=(1,2,3,4,5)
combo.current(3)
combo.grid(column=0,row=4)


label.grid(column=0,row=1)
bt.grid(column=2,row=1)
txt.grid(column=1,row=1)

window.mainloop()