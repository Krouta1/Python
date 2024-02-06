from tkinter import *
from tkinter import messagebox

def click():
    #messagebox.showinfo("You clicked me!","Thanks!")
    #messagebox.showwarning("You clicked me!","Virus!" )
    #messagebox.showerror("You clicked me!","Error!" )
    if messagebox.askokcancel("You clicked me!","Do you want to continue?" ):
        print("You clicked yes!")
    else:
        print("You clicked no!")

window = Tk()

button = Button(
    window,
    text="Click me!",
    command=click
)
button.pack()

window.mainloop()