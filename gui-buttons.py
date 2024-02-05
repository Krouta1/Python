from tkinter import *

window = Tk()
count = 0
def click():
    global count
    count += 1
    str_count = str(count)
    button.configure(text="Click Me: " + str_count)

button = Button(window, text="Click Me", font=("Arial Bold", 25), foreground="black", background="grey", relief="solid", pady=10, padx=10, borderwidth=5, anchor="w", activebackground="lightgrey", command=click)
button.pack()

window.mainloop()