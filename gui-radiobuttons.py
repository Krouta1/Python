from tkinter import *

food = ["Pizza", "Hamburger", "Hotdog"]
def order():
    if x.get() == 0:
        print("You ordered Pizza")
    elif x.get() == 1:
        print("You ordered Hamburger")
    elif x.get() == 2:
        print("You ordered Hotdog")
    else:
        print("You ordered nothing")

window = Tk()

x = IntVar()

for index in range(len(food)):
    radiobutton = Radiobutton(
        window, 
        text=food[index],
        variable = x,
        value=index,
        padx=20,
        font=("Arial", 16),
        #you can image it will be nice but i don't wanna
        command=order
        )
    radiobutton.pack(anchor=W)

window.mainloop()