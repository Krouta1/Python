from tkinter import *

food = ["Pizza", "Hamburger", "Hotdog"]

window = Tk()

x = IntVar()

for index in range(len(food)):
    radiobutton = Radiobutton(
        window, 
        text=food[index],
        variable = x,
        value=index,
        padx=20,
        font=("Arial", 16)
        #you can image it will be nice but i don't wanna
        )
    radiobutton.pack(anchor=W)

window.mainloop()