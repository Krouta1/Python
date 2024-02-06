from tkinter import *
from tkinter import colorchooser

def click():
    window.configure(bg=colorchooser.askcolor()[1])


window = Tk()
window.geometry("500x500")

button = Button(window, text="Choose color", command=click)
button.pack()

window.mainloop()