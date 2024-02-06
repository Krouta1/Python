from tkinter import *

window = Tk()

entry =  Entry(window, width=20, bg="light blue", fg="black", font=("Arial", 20))
entry.insert(0, "Enter your name")
entry.pack(side=LEFT)

#submit button
sumbit_btn = Button(window, text="Submit", width=15, bg="black", fg="white", font=("Arial", 20), command=lambda: print(entry.get()))    
sumbit_btn.pack(side=RIGHT)

#delete button
delete_btn = Button(window, text="Delete", width=15, bg="black", fg="white", font=("Arial", 20), command=lambda: entry.delete(0, END))
delete_btn.pack(side=RIGHT)

#backspace button
backspace_btn = Button(window, text="Backspace", width=15, bg="black", fg="white", font=("Arial", 20), command=lambda: entry.delete(len(entry.get())-1, END))
backspace_btn.pack()

window.mainloop()