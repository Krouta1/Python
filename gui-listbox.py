from tkinter import *

def submit():
    food = []
    for index in listbox.curselection():
        food.insert(index, listbox.get(index))
    
    for index in food:
        print(index)

def add():
    listbox.insert(listbox.size(), entry_box.get())
    listbox.config(height=listbox.size())

def delete():
    for index in reversed(listbox.curselection()):
        listbox.delete(index)
    listbox.config(height=listbox.size())

window = Tk()

listbox = Listbox(
    window,
    bg="grey",
    font=("Times New Roman", 20),
    width=15,
    selectmode=MULTIPLE
    )
listbox.pack()

listbox.insert(1, "pizza")
listbox.insert(2, "hamburger")
listbox.insert(3, "hotdog")
listbox.insert(4, "spaghetti")

listbox.config(height=listbox.size())

entry_box = Entry(window)
entry_box.pack()

add_button = Button(
    window,
    text="ADD",
    command=add
)
add_button.pack()

submit_button = Button(
    window,
    text="Submit",
    command=submit
)
submit_button.pack()

delete_button = Button(
    window,
    text="Delete",
    command=delete
)
delete_button.pack()


window.mainloop()