from tkinter import ttk
import tkinter as tk

window = tk.Tk()
window.title("Check Boxes")
#logic goes here
state = tk.BooleanVar()
state.set(True)
stk = tk.Checkbutton(window,text="select")
stk.grid(column=0,row=1)
rad = tk.Radiobutton(window,text="Porn",value=1)
rad1 = tk.Radiobutton(window,text="Nigga Porn",value=2)
rad.grid(column=0,row=2)
rad1.grid(column=0,row=3)

window.mainloop()