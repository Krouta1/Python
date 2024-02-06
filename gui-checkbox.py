from tkinter import *

def display():
    if x.get() == 1:
        print("You agreed to the terms and conditions")
    else:
        print("You did not agree to the terms and conditions")

window = Tk()

x = IntVar()

check_button = Checkbutton(
    window, 
    text="I agree to the terms and conditions", 
    font=("Arial", 20),
    variable=x, 
    onvalue=1, 
    offvalue=0,command=display, 
    height=5, 
    width=50, 
    bg="light blue", 
    fg="black",
    activeforeground="black",
    activebackground="light blue"
    )

check_button.pack()

window.mainloop()